"""Answer isolation, frozen response regression and scoring failure controls."""

import copy
import json
import unittest

from tools.evaluate_hidden_answers import CASE_IDS, ROOT, SOURCE, digest, prepare, score


class HiddenAnswerEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.suite = json.loads(SOURCE.read_text())
        self.packet, self.key = prepare(self.suite)
        self.submission = json.loads(
            (ROOT / "tests/fixtures/hidden_answer_smoke_responses.json").read_text())

    def test_evaluator_payload_excludes_answer_bearing_metadata(self):
        changed = copy.deepcopy(self.suite)
        for case in changed["cases"]:
            for field in ("title", "required_preservations", "violated_constraints",
                          "structural_signature", "paired_case_id", "source_documents"):
                case[field] = "DO_NOT_LEAK_REFERENCE_METADATA"
        packet, _ = prepare(changed)
        self.assertEqual(packet, self.packet)
        self.assertNotIn("DO_NOT_LEAK", json.dumps(packet))
        self.assertFalse(any(case_id in json.dumps(packet) for case_id in CASE_IDS))
        for item in packet["items"]:
            self.assertEqual(set(item), {"item_id", "scenario"})

    def test_separately_authored_smoke_judgments_match_eight_cases(self):
        result = score(self.packet, self.key, self.submission)
        self.assertEqual((result["matched"], result["case_count"]), (8, 8))
        self.assertEqual(result["confusion"], {"pass->pass": 4, "reject->reject": 4})

    def test_reversing_eight_authored_verdicts_is_detected(self):
        changed = copy.deepcopy(self.suite)
        for case in changed["cases"]:
            if case["case_id"] in CASE_IDS:
                case["expected_result"] = {"pass": "reject", "reject": "pass"}[case["expected_result"]]
        packet, key = prepare(changed)
        self.assertEqual(packet, self.packet)  # The scenario facts did not change.
        result = score(packet, key, self.submission)
        self.assertEqual(result["matched"], 0)
        self.assertEqual(result["case_count"], 8)

    def test_packet_changes_invalidate_frozen_responses(self):
        packet = copy.deepcopy(self.packet)
        packet["items"][0]["scenario"] += " Independent review is then removed."
        with self.assertRaises(ValueError):
            score(packet, self.key, self.submission)
        key = copy.deepcopy(self.key)
        key["packet_sha256"] = digest(packet)
        with self.assertRaises(ValueError):
            score(packet, key, self.submission)

    def test_missing_extra_duplicate_and_empty_answers_fail_closed(self):
        for mode in ("missing", "extra", "duplicate", "empty", "invalid"):
            with self.subTest(mode=mode):
                submission = copy.deepcopy(self.submission)
                rows = submission["responses"]
                if mode == "missing":
                    rows.pop()
                elif mode == "extra":
                    rows.append(dict(rows[0], item_id="extra"))
                elif mode == "duplicate":
                    rows.append(rows[0])
                elif mode == "empty":
                    rows[0]["rationale"] = " "
                else:
                    rows[0]["judgment"] = "probably"
                with self.assertRaises(ValueError):
                    score(self.packet, self.key, submission)

    def test_revision_request_is_reported_without_counting_as_correct(self):
        submission = copy.deepcopy(self.submission)
        submission["responses"][0]["judgment"] = "revise_required"
        result = score(self.packet, self.key, submission)
        self.assertEqual(result["matched"], 7)
        self.assertEqual(result["revision_requests"], 1)

    def test_disclosures_and_key_exposure_are_checked(self):
        for mode in ("missing", "key_supplied"):
            with self.subTest(mode=mode):
                submission = copy.deepcopy(self.submission)
                if mode == "missing":
                    del submission["evaluation"]["prior_source_exposure"]
                else:
                    submission["evaluation"]["answer_key_access"] = "supplied"
                with self.assertRaises(ValueError):
                    score(self.packet, self.key, submission)


if __name__ == "__main__":
    unittest.main()
