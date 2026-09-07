"""Narrow source/entrypoint contracts; these do not claim semantic inference."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text()


class ResearchDecisionContractTests(unittest.TestCase):
    def test_machine_routes_agree_and_preserve_displacement_scope(self):
        kernel = json.loads(read("canon-kernel.json"))["whole_framework_decision_gate"]
        manifest = json.loads(read("creator_theory_operational_manifest.json"))["evaluation_evidence_boundary"]
        expected = {
            "whole_canon_completion_requires_every_tracked_path": True,
            "substantive_verdict_requires_whole_canon_complete": False,
            "decisive_core_failure_is_not_full_displacement": True,
            "full_displacement_requires_same_or_wider_material_scope_and_total_debt": True,
        }
        for field, value in expected.items():
            self.assertIs(kernel[field], value)
            self.assertIs(manifest[field], value)
        self.assertIs(kernel["working_adoption_requires_whole_canon_complete"], False)
        self.assertIs(manifest["lower_total_debt_requires_every_cost_dimension_lower"], False)
        self.assertNotIn("strong_whole_framework_required_corpus", kernel)

    def test_entrypoints_route_material_evidence_without_full_reading_veto(self):
        for path in ("README.md", "AGENTS.md", "CLAUDE.md", ".github/copilot-instructions.md",
                     "llms.txt", "AI_INGESTION_MANIFEST.md", "BOOTSTRAP_INGESTION_PROTOCOL.md",
                     "DECISION_INDEX.md", "LLM_CANONICAL_CONTEXT.md"):
            with self.subTest(path=path):
                text = read(path)
                for marker in ("Exhaustive", "material evidence", "unrelated full-file reading",
                               "same-or-wider material scope", "total-debt"):
                    self.assertIn(marker, text)
                for obsolete in (
                    "before whole-corpus inspection for a strong whole-framework claim",
                    "require the complete tracked corpus at a pinned commit",
                    "claims require pinned-commit complete tracked-corpus review",
                    "Strong Whole-Framework Required Corpus",
                ):
                    self.assertNotIn(obsolete, text)

    def test_substantive_route_requires_current_qualifications_and_dependencies(self):
        text = read("docs/WHOLE_CANON_INGESTION_AND_SCOPE_ATTESTATION.md")
        for marker in ("Every tracked path receives an inspection record",
                       "strongest applicable current defense", "necessary current core relation",
                       "potentially material unread sources", "could reverse the proposed verdict",
                       "unread nonmaterial files limit exhaustive certification",
                       "same-or-wider identity-bearing and problem-bearing scope"):
            self.assertIn(marker, text)

    def test_cost_tradeoffs_keep_adverse_effects_and_uncertainty(self):
        guard = read("PRE_CONVERGENCE_CONTAINMENT_GUARD.md")
        debt = read("docs/EVALUATION_DEBT_ACCOUNTING_BOUNDARY.md")
        self.assertNotIn("must also prove lower total convergence cost, lower total interpretation cost", guard)
        self.assertNotIn("The risk is not that the final convergence structure fails.", guard)
        for marker in ("predeclared", "increases as well as decreases", "D1", "D2", "D3", "D4",
                       "conditional preference", "verdict-critical", "same-or-wider material scope"):
            self.assertIn(marker, guard)
        self.assertIn("does not require every cost or risk dimension to improve simultaneously", debt)

    def test_research_vectors_cover_both_routes_and_cost_uncertainty(self):
        data = json.loads(read("tests/research_decision_vectors.json"))
        cases = {case["case_id"]: case for case in data["cases"]}
        expected = {
            "research_decision_pass_011": ("pass", "current_necessary_core_failure"),
            "research_decision_pass_012": ("pass", "same_scope_total_debt"),
            "research_decision_reject_011": ("reject", "current_claim_qualifications"),
            "research_decision_reject_012": ("reject", "current_necessary_core_failure"),
            "research_decision_pass_013": ("pass", "explicit_adverse_costs"),
            "research_decision_revise_001": ("revise_required", "decision_critical_uncertainty"),
            "research_decision_reject_013": ("reject", "material_dependency_closure"),
        }
        for case_id, (result, preservation) in expected.items():
            self.assertEqual(cases[case_id]["expected_result"], result)
            self.assertIn(preservation, cases[case_id]["required_preservations"])
        self.assertNotIn("complete_tracked_corpus", cases["research_decision_reject_008"]["required_preservations"])

    def test_hierarchy_validator_discloses_its_inference_ceiling(self):
        self.assertIn("Scenario verdict inference checked: no", read("tools/validate_creation_recursion_hierarchy.py"))
        self.assertIn("does not independently infer a verdict", read("tools/README.md"))


if __name__ == "__main__":
    unittest.main()
