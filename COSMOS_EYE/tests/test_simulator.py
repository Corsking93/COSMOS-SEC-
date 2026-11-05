import unittest

from cosmos_eye.models import SensorEvent
from cosmos_eye.simulator import SensorSimulator


class SensorEventTests(unittest.TestCase):
    def test_event_has_simulated_provenance(self):
        event = SensorEvent.create(
            node_id="test-node",
            category="optical",
            measurement="ambient_light",
            value=100,
            unit="lux",
            simulated=True,
            source="test://fixture",
        )
        self.assertTrue(event.simulated)
        self.assertEqual(event.category, "optical")

    def test_unknown_category_rejected(self):
        with self.assertRaises(ValueError):
            SensorEvent.create(
                node_id="test-node",
                category="unknown",
                measurement="x",
                value=1,
                unit="u",
                simulated=True,
                source="test://fixture",
            )


class SimulatorTests(unittest.TestCase):
    def test_emits_requested_number_of_events(self):
        events = list(SensorSimulator(seed=1).events(count=9))
        self.assertEqual(len(events), 9)
        self.assertTrue(all(event.simulated for event in events))

    def test_invalid_count_rejected(self):
        with self.assertRaises(ValueError):
            list(SensorSimulator().events(count=0))


if __name__ == "__main__":
    unittest.main()
