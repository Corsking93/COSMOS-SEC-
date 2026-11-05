"""Normalized event types shared by COSMOS Eye sensor adapters."""

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any


SENSOR_CATEGORIES = (
    "visual",
    "optical",
    "acoustic",
    "magnetic",
    "radio_frequency",
    "environmental",
    "spatial",
)


@dataclass(frozen=True)
class SensorEvent:
    timestamp: str
    node_id: str
    category: str
    measurement: str
    value: float
    unit: str
    simulated: bool
    source: str

    @classmethod
    def create(
        cls,
        *,
        node_id: str,
        category: str,
        measurement: str,
        value: float,
        unit: str,
        simulated: bool,
        source: str,
    ) -> "SensorEvent":
        if category not in SENSOR_CATEGORIES:
            raise ValueError(f"Unsupported sensor category: {category}")
        if not node_id or not measurement or not unit or not source:
            raise ValueError("node_id, measurement, unit, and source are required")
        return cls(
            timestamp=datetime.now(timezone.utc).isoformat(),
            node_id=node_id,
            category=category,
            measurement=measurement,
            value=float(value),
            unit=unit,
            simulated=bool(simulated),
            source=source,
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
