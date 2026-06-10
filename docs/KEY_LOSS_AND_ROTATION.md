# Key Loss and Rotation

## Scope

This document describes user-side key loss and rotation states for PROV-K.

It does not create keys, recover keys, or sign releases.

## Key Loss Scenarios

If the private key is lost but not suspected compromised, no new releases should be signed with that key.

If the private key may have been copied, photographed, uploaded, pasted, or stored in a synced folder, treat it as compromised.

If the public key is lost but the private key remains safe, derive or export the public key again using the user's offline tooling.

If both private and public key references are uncertain, stop release signing until an auditor reviews the situation.

## Normal Rotation

Normal rotation requires:

1. a current public-key fingerprint;
2. a new public-key fingerprint;
3. a previous manifest hash;
4. a rotation record signed by the previous private key;
5. human review before any signed release uses the new key.

Unsigned rotation records remain `UNSIGNED_DRAFT`.

A valid previous-key signature may promote the rotation record to `ROTATED_KEY_RELEASE`.

## DISPUTED

Use `DISPUTED` when provenance continuity, key custody, or signature validity is under unresolved challenge.

`DISPUTED` does not erase the origin chain and does not authorize a replacement throne.

## EMERGENCY_REASSERTED

Use `EMERGENCY_REASSERTED` only after human owner review when continuity must be restated after a key incident.

It is a documented state, not automatic proof.

## Non-Replacement Boundary

Key rotation changes verification keys. It does not change AAOS Genesis priority, `x_root` continuity, origin attribution, the Creator Theory high frame, or the non-throne constraint.
