# COSMOS Eye (CE-001)

COSMOS Eye is a local-first, modular environmental observation subsystem for COSMOS. Its first milestone is a **simulation-only software core** that normalizes sensor-like events into a common event model.

## Current status

- Phase I scaffold: simulation only.
- No camera, microphone, Bluetooth, Wi-Fi, SDR, GPS, or other physical sensor is activated.
- No network listener, remote upload, device control, or automatic transfer is implemented.
- Sensor adapters are interfaces planned for later phases, not working hardware drivers.

## Architecture

```text
COSMOS_EYE/
  cosmos_eye/
    models.py       # normalized event and sensor types
    simulator.py    # deterministic synthetic event source
    main.py         # local CLI demonstration
  tests/
    test_simulator.py
  config.example.json
  SECURITY.md
```

## Run

Requires Python 3.10+ and uses only the standard library.

```bash
python -m cosmos_eye.main --count 5 --interval 0.5
python -m unittest discover -s tests -v
```

Run these commands from the `COSMOS_EYE` directory.

## Event model

Every event includes a UTC timestamp, node identifier, sensor category, measurement name, numeric value, unit, and a `simulated` provenance flag. The flag must remain false only for a future adapter that has been explicitly implemented and validated against a real device.

## COSMOS integration contract

COSMOS Eye is an independent module. Integration with COSMOS OS should initially be through a documented local event interface and explicit configuration. It must not assume privileged access to the phone, host, camera, microphone, or network. A future integration adapter must be opt-in, least-privilege, and independently testable.

## Roadmap

1. **CE-001:** normalized event model, simulator, CLI, tests.
2. **CE-002:** dashboard and local event bus.
3. **CE-003:** opt-in physical sensor adapters with capability checks.
4. **CE-004:** multi-node transport, authentication, and signed event provenance.
5. **CE-005:** analytics, alerting, and retention controls.

See [SECURITY.md](SECURITY.md) before adding a real sensor or network component.
