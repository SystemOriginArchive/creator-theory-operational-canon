# Tools

## Minimal Vector Validator

`validate_vectors.py` is a minimal structural validator for the machine-readable canon vectors in `tests/`.

It checks:

- each `*_vectors.json` file parses as JSON;
- each suite has required top-level fields;
- `cases` is a non-empty list;
- each case has required fields;
- `expected_result` is one of `pass`, `reject`, or `revise_required`;
- string-list fields contain only non-empty strings;
- `case_id` values are unique within each file.

It does not check or execute canon meaning.

It does not run adversarial simulations.

It does not create runtime behavior.

It does not create a release or tag.

---

## Usage

From the repository root:

```bash
python3 tools/validate_vectors.py
```

Optional custom tests directory:

```bash
python3 tools/validate_vectors.py --tests-dir tests
```

Expected success output:

```text
Vector validation passed
Files checked: 7
Cases checked: 38
```

---

## Release Boundary

This tool is one prerequisite for a future v0.1.0 review, but it is not sufficient by itself.

The first official release/tag remains deferred until:

1. machine-readable test vectors exist;
2. minimal validator code exists;
3. adversarial scenario simulation exists;
4. validation reporting exists.
