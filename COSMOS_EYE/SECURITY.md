# Security and activation boundaries

## Safe defaults

- Simulation mode is the only implemented operating mode.
- Physical sensors, network transport, remote upload, and device control are disabled.
- No credentials, tokens, personal recordings, or private sensor data belong in this repository.
- Do not commit real location traces, audio, video, MAC addresses, or other identifying telemetry.

## Future hardware adapters

Every adapter must require explicit configuration, expose its permissions, identify the physical source, and fail closed when permissions or hardware are unavailable. Camera and microphone access must have visible activation indicators and user-controlled stop controls.

## Radio-frequency observations

Future RF features must be limited to lawful, passive measurements and metadata from authorized equipment. Do not add packet interception, credential capture, decryption, or surveillance of private communications.

## Multi-node design

Before enabling transport, define node identity, mutual authentication, replay protection, event signing, key rotation, retention, and owner-controlled enrollment. No node may grant itself privileged authority.

## Integrity

Git commit signature verification establishes that GitHub accepted the commit's cryptographic signature. It does not establish the correctness, safety, ownership of all included assets, or physical-device integrity of the software. Release artifacts should later include reproducible build instructions and SHA-256 manifests.
