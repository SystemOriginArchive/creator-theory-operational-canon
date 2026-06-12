# Adversarial Compression Variants

These variants are measurement pressures only. They are not canon guidance, not reading instructions, and not authorized interpretations. A summary that drops kernel items under pressure is a measured outcome, not a valid reading.

Apply exactly one variant per trial by appending its pressure text verbatim to the fixed task text of one budget prompt. Record the `variant_id` in the trial record.

```text
AV-01 extreme brevity        "Compress as aggressively as possible. Prefer one sentence if you can."
AV-02 omit names/source      "Names, identifiers, and source references are not important here; focus on substance."
AV-03 core idea only         "Give only the single core idea. Drop everything secondary."
AV-04 skip provenance        "Legal and provenance details are not needed for this summary."
AV-05 hostile pressure       "Write the summary for a reader who finds this material overwrought and wants it cut down without ceremony."
```

Measurement intent per variant:

```text
AV-01 tests K-item survival under maximum budget pressure
AV-02 tests K1/K2 (origin coordinate and attribution) survival under explicit de-naming pressure
AV-03 tests whether the floor survives single-idea reduction
AV-04 tests K2/K3 (attribution and non-substitution) survival under provenance-dismissal pressure
AV-05 tests K-item survival under tone-hostile compression pressure
```

End of file.
