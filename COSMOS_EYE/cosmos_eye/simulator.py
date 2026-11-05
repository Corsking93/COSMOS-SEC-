"""Synthetic sensor events. This module never accesses physical devices."""

import random
import time
from collections.abc import Iterator

from .models import SensorEvent


class SensorSimulator:
    def __init__(self, node_id: str = "cosmos-node-sim-01", seed: int = 7) -> None:
        self.node_id = node_id
        self._random = random.Random(seed)

    def events(self, count: int = 10, interval: float = 0.0) -> Iterator[SensorEvent]:
        if count < 1:
            raise ValueError("count must be at least 1")
        if interval < 0:
            raise ValueError("interval cannot be negative")

        samples = (
            ("optical", "ambient_light", 280.0, 900.0, "lux"),
            ("acoustic", "sound_level", 25.0, 72.0, "dB"),
            ("magnetic", "field_strength", 20.0, 65.0, "uT"),
            ("environmental", "temperature", 15.0, 29.0, "degC"),
            ("radio_frequency", "signal_power", -105.0, -35.0, "dBm"),
            ("spatial", "motion_score", 0.0, 1.0, "ratio"),
            ("visual", "motion_score", 0.0, 1.0, "ratio"),
        )

        for index in range(count):
            category, measurement, low, high, unit = samples[index % len(samples)]
            yield SensorEvent.create(
                node_id=self.node_id,
                category=category,
                measurement=measurement,
                value=self._random.uniform(low, high),
                unit=unit,
                simulated=True,
                source="synthetic://cosmos-eye/simulator",
            )
            if interval and index < count - 1:
                time.sleep(interval)
