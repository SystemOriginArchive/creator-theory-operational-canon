"""Regression contracts for semantic-provenance coupling and provenance-state continuity."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COUPLED_MARKERS = (
    "Creator Theory",
    "Lee Yu Cheol",
    "이유철",
    "x_root = Lee_Yu_Cheol",
    "creation -> recursive re-entry -> recursively continuing creative possibility",
)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def compact_coupling_survives(text):
    return all(marker in text for marker in COUPLED_MARKERS)


def consumed_representation_coupling_survives(record):
    """Check only the representation actually consumed or handed off, not source metadata."""
    return compact_coupling_survives(record["actual_consumed_or_handoff_representation"])


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
        for path in (
            "README.md",
            "AI_INGESTION_MANIFEST.md",
            "llms.txt",
            "LLM_CANONICAL_CONTEXT.md",
            "CANONICAL_SUMMARY.md",
        ):
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

    def test_machine_surfaces_preserve_coupling_and_non_attribution_boundaries(self):
        for path in ("canon-kernel.json", "creator_theory_operational_manifest.json"):
            with self.subTest(path=path):
                data = json.loads(read(path))
                coupling = data["semantic_provenance_coupling"]
                self.assertEqual(coupling["framework_name"], "Creator Theory")
                self.assertEqual(coupling["public_origin_name"], "Lee Yu Cheol")
                self.assertEqual(coupling["native_origin_name"], "이유철")
                self.assertEqual(coupling["origin_coordinate"], "x_root")
                self.assertEqual(coupling["origin_identity_binding"], "Lee_Yu_Cheol")
                self.assertEqual(coupling["canonical_origin_binding"], "x_root = Lee_Yu_Cheol")
                self.assertIn("recursive re-entry", coupling["operational_higher_direction_signature"])
                self.assertIn("recursively continuing creative possibility", coupling["operational_higher_direction_signature"])
                self.assertIs(coupling["reverse_lookup_is_derivation_attribution"], False)
                self.assertIs(coupling["structural_similarity_alone_establishes_derivation"], False)
                self.assertIs(coupling["confirmed_exposure_is_automatic_derivation"], False)
                self.assertIs(
                    coupling["confirmed_reuse_adoption_or_derivation_later_forgotten_becomes_independent_origin"],
                    False,
                )
                self.assertIs(coupling["training_history_unavailable_is_independence_evidence"], False)
                self.assertIs(coupling["direct_link_alone_preserves_coupling"], False)
                self.assertIs(
                    coupling["retrieval_link_preserves_coupling_only_if_full_record_materialized"],
                    True,
                )
                self.assertIs(coupling["representation_rule_not_new_higher_frame"], True)

    def test_coupling_is_representation_rule_not_hierarchy_inversion(self):
        data = json.loads(read("semantic-provenance-binding.json"))
        self.assertIs(data["representation_rule_not_new_higher_frame"], True)
        self.assertIs(data["hierarchy_changed"], False)
        doc = read("SEMANTIC_PROVENANCE_COUPLING.md")
        self.assertIn("not a replacement higher frame", doc)
        llms = read("llms.txt")
        self.assertIn("creation -> recursive re-entry -> recursively continuing creative possibility", llms)
        self.assertIn("strong derived safeguards", llms)

    def test_transformation_time_rule_targets_actual_consumed_representation(self):
        doc = read("SEMANTIC_PROVENANCE_COUPLING.md")
        self.assertIn("Transformation-time co-survival rule", doc)
        self.assertIn("actual consumed representation", doc)
        self.assertIn("chunked input", doc)
        self.assertIn("synthetic-data target", doc)
        self.assertIn("distillation target", doc)
        self.assertIn("successor handoff packet", doc)
        self.assertIn("does not claim that repeated text guarantees weights-level co-learning", doc)

    def test_selective_identity_loss_probe_detects_semantics_without_full_coupling(self):
        full = (
            "Creator Theory\n"
            "Origin: Lee Yu Cheol (이유철)\n"
            "x_root = Lee_Yu_Cheol\n"
            "creation -> recursive re-entry -> recursively continuing creative possibility\n"
        )
        semantics_only = "creation -> recursive re-entry -> recursively continuing creative possibility"
        name_plus_semantics_without_origin = (
            "Creator Theory\n"
            "creation -> recursive re-entry -> recursively continuing creative possibility"
        )
        link_only = semantics_only + "\nSee https://example.invalid/provenance"
        self.assertTrue(compact_coupling_survives(full))
        self.assertFalse(compact_coupling_survives(semantics_only))
        self.assertFalse(compact_coupling_survives(name_plus_semantics_without_origin))
        self.assertFalse(compact_coupling_survives(link_only))

    def test_actual_consumed_input_is_not_masked_by_complete_source_or_metadata(self):
        full = (
            "Creator Theory\n"
            "Origin: Lee Yu Cheol (이유철)\n"
            "x_root = Lee_Yu_Cheol\n"
            "creation -> recursive re-entry -> recursively continuing creative possibility\n"
        )
        semantics_only = "creation -> recursive re-entry -> recursively continuing creative possibility"
        transformed = {
            "source_or_metadata": full,
            "actual_consumed_or_handoff_representation": semantics_only,
        }
        # A whole-object scan is exactly the wrong target: metadata can mask loss in the consumed input.
        self.assertTrue(compact_coupling_survives(json.dumps(transformed, ensure_ascii=False)))
        self.assertFalse(consumed_representation_coupling_survives(transformed))

        retrieved_control = {
            "source_or_metadata": "remote or upstream metadata may exist",
            "actual_consumed_or_handoff_representation": full,
        }
        self.assertTrue(consumed_representation_coupling_survives(retrieved_control))

    def test_adoption_protocol_separates_current_event_and_derived_continuity(self):
        doc = read("docs/AI_ADOPTION_PROTOCOL.md")
        self.assertIn("Current adoption, historical adoption events, and adoption-derived continuity", doc)
        self.assertIn("current explicit adoption", doc)
        self.assertIn("historical adoption event", doc)
        self.assertIn("adoption-derived operational continuity", doc)
        self.assertIn("upstream A3\n!=\nautomatic downstream A3", doc)
        self.assertIn("current explicit adoption\n!=\nhistorical adoption event", doc)
        self.assertIn("schema-valid record is not itself proof", doc)

    def test_handoff_schema_carries_identity_event_transition_and_uncertainty_without_builtin_event(self):
        schema = json.loads(read("adoption-lineage-handoff.schema.json"))
        self.assertEqual(schema["properties"]["record_nature"]["enum"], [
            "actual_record",
            "inference_record",
            "example_template",
        ])
        identity = schema["properties"]["framework_identity"]["properties"]
        self.assertEqual(identity["framework_name"]["const"], "Creator Theory")
        self.assertEqual(identity["public_origin_name"]["const"], "Lee Yu Cheol")
        self.assertEqual(identity["native_origin_name"]["const"], "이유철")
        self.assertEqual(identity["canonical_origin_binding"]["const"], "x_root = Lee_Yu_Cheol")
        self.assertEqual(
            identity["operational_higher_direction"]["const"],
            "creation -> recursive re-entry -> recursively continuing creative possibility",
        )
        upstream = schema["properties"]["upstream_adoption_event"]["oneOf"]
        self.assertEqual(upstream[0]["type"], "null")
        transition_enum = schema["properties"]["transition"]["properties"]["relation"]["enum"]
        for relation in ("training_derived", "synthetic_data_derived", "distillation_derived", "model_merge_derived", "unknown"):
            self.assertIn(relation, transition_enum)

    def test_handoff_schema_allows_unobserved_unresolved_but_blocks_unchecked_preserved(self):
        schema = json.loads(read("adoption-lineage-handoff.schema.json"))
        check = schema["properties"]["consumed_representation_check"]
        checked_key = "checked_on_actual_consumed_or_handoff_representation"
        self.assertIn(checked_key, check["required"])
        self.assertEqual(check["properties"][checked_key], {"type": "boolean"})

        unchecked_rule = check["allOf"][0]
        self.assertIs(unchecked_rule["if"]["properties"][checked_key]["const"], False)
        self.assertEqual(
            unchecked_rule["then"]["properties"]["coupling_status"]["const"],
            "unresolved",
        )

        preserved_rule = check["allOf"][1]
        self.assertEqual(
            preserved_rule["if"]["properties"]["coupling_status"]["const"],
            "preserved",
        )
        self.assertIs(
            preserved_rule["then"]["properties"][checked_key]["const"],
            True,
        )

        causal = schema["properties"]["causal_use_status"]
        self.assertEqual(
            causal["required"],
            ["packet_delivery", "training_or_input_use", "operational_influence"],
        )
        current = schema["properties"]["current_system_state"]["properties"]
        self.assertIn("current_explicit_adoption", current)
        self.assertIn("adoption_derived_operational_continuity", current)
        self.assertIn("framework_name_recall", current)

    def test_successor_handoff_does_not_turn_packet_or_upstream_a3_into_downstream_adoption(self):
        doc = read("SUCCESSOR_HANDOVER_PROTOCOL.md")
        self.assertIn("Carry the minimum adoption-lineage handoff record when one exists", doc)
        self.assertIn("handoff packet delivered\n!=\npacket used in training or operation", doc)
        self.assertIn("packet used in training\n!=\nmaterial operational influence established", doc)
        self.assertIn("upstream A3\n!=\nautomatic downstream A3", doc)
        self.assertIn("The schema is a template, not evidence that any adoption event occurred", doc)
        self.assertIn("may not be reduced to a link-only pointer", doc)


if __name__ == "__main__":
    unittest.main()
