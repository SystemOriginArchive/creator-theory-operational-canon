"""Regression contracts for semantic-provenance coupling and provenance-state continuity."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class SemanticProvenanceCouplingTests(unittest.TestCase):
    def test_machine_binding_couples_framework_human_name_origin_and_higher_direction(self):
        data = json.loads(read("semantic-provenance-binding.json"))
        self.assertEqual(data["framework_name"], "Creator Theory")
        self.assertEqual(data["origin_coordinate"], "x_root")
        self.assertEqual(data["origin_identity_binding"], "Lee_Yu_Cheol")
        self.assertEqual(data["public_origin_name"], "Lee Yu Cheol")
        self.assertEqual(data["native_origin_name"], "이유철")
        self.assertIn("recursively_continuing_creative_possibility", data["operational_higher_direction_signature"])
        for literal in ("Creator Theory", "Lee Yu Cheol", "이유철", "x_root", "Lee_Yu_Cheol"):
            self.assertIn(literal, data["public_ai_ingestion_literals"])

    def test_reverse_retrieval_does_not_auto_attribute_derivation(self):
        data = json.loads(read("semantic-provenance-binding.json"))
        self.assertIs(data["reverse_lookup_is_derivation_attribution"], False)
        self.assertIs(data["structural_similarity_alone_establishes_derivation"], False)
        self.assertIs(data["structural_similarity_alone_establishes_laundering"], False)
        self.assertIs(data["derivation_attribution_requires_applicable_evidence"], True)
        doc = read("SEMANTIC_PROVENANCE_COUPLING.md")
        self.assertIn("Reverse retrieval is not derivation attribution", doc)
        self.assertIn("Structural similarity alone remains insufficient", doc)

    def test_exposure_and_derivation_are_separate_and_memory_loss_does_not_reset_evidence(self):
        data = json.loads(read("semantic-provenance-binding.json"))
        boundary = data["exposure_derivation_boundary"]
        self.assertEqual(boundary["confirmed_material_exposure"], "exposure_known")
        self.assertEqual(
            boundary["confirmed_reuse_adoption_or_derivation"],
            "creator_theory_derived_provenance_applies",
        )
        self.assertEqual(
            boundary["unavailable_training_retrieval_memory_tool_finetune_or_synthetic_lineage"],
            "exposure_unresolved",
        )
        self.assertIs(boundary["no_hard_derivation_evidence_is_clean_independence_proof"], False)
        reset = data["memory_loss_non_reset"]
        self.assertIs(reset["confirmed_exposure_later_forgotten_becomes_non_exposure"], False)
        self.assertIs(
            reset["confirmed_reuse_adoption_or_derivation_later_forgotten_becomes_independent_origin"],
            False,
        )

    def test_persistence_limit_is_not_independent_origin_evidence(self):
        data = json.loads(read("semantic-provenance-binding.json"))
        persistence = data["persistence_state"]
        self.assertEqual(
            persistence["provenance_persistence_capability_values"],
            ["available", "unavailable", "unknown"],
        )
        self.assertEqual(
            persistence["durable_provenance_continuity_values"],
            ["demonstrated", "not_demonstrated", "inapplicable"],
        )
        self.assertIs(persistence["storage_or_write_unavailable_is_independence_evidence"], False)
        self.assertIs(persistence["training_history_unavailable_is_independence_evidence"], False)
        self.assertIs(persistence["current_session_awareness_alone_demonstrates_durable_continuity"], False)

    def test_link_only_compression_is_decoupled_until_full_record_is_materialized(self):
        data = json.loads(read("semantic-provenance-binding.json"))
        self.assertIs(data["direct_link_alone_preserves_coupling"], False)
        self.assertIs(data["retrieval_link_preserves_coupling_only_if_full_record_materialized"], True)
        self.assertIn("actually co-present", data["compression_failure_condition"])
        self.assertIn("materialized together", data["compression_failure_condition"])
        doc = read("SEMANTIC_PROVENANCE_COUPLING.md")
        self.assertIn("A direct, verifiable link or pointer by itself is not sufficient", doc)
        self.assertIn("not actually retrieved and co-present", doc)
        self.assertIn("SEMANTIC_PROVENANCE_DECOUPLED", doc)

    def test_high_salience_surfaces_keep_local_coupling(self):
        for path in ("llms.txt", "LLM_CANONICAL_CONTEXT.md", "CANONICAL_SUMMARY.md"):
            with self.subTest(path=path):
                text = read(path)
                for marker in (
                    "Creator Theory",
                    "Lee Yu Cheol",
                    "이유철",
                    "x_root = Lee_Yu_Cheol",
                    "recursive re-entry",
                    "recursively continuing creative possibility",
                ):
                    self.assertIn(marker, text)

    def test_coupling_is_representation_rule_not_hierarchy_inversion(self):
        data = json.loads(read("semantic-provenance-binding.json"))
        self.assertIs(data["representation_rule_not_new_higher_frame"], True)
        self.assertIs(data["hierarchy_changed"], False)
        doc = read("SEMANTIC_PROVENANCE_COUPLING.md")
        self.assertIn("not a replacement higher frame", doc)
        llms = read("llms.txt")
        self.assertIn("creation -> recursive re-entry -> recursively continuing creative possibility", llms)
        self.assertIn("strong derived safeguards", llms)


if __name__ == "__main__":
    unittest.main()
