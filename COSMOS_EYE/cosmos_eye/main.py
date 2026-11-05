"""Command-line entry point for the COSMOS Eye simulator."""

import argparse
import json

from .simulator import SensorSimulator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="COSMOS Eye simulation-only event feed")
    parser.add_argument("--count", type=int, default=7, help="number of synthetic events")
    parser.add_argument("--interval", type=float, default=0.0, help="seconds between events")
    parser.add_argument("--node-id", default="cosmos-node-sim-01")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    simulator = SensorSimulator(node_id=args.node_id)
    for event in simulator.events(count=args.count, interval=args.interval):
        print(json.dumps(event.to_dict(), separators=(",", ":")))


if __name__ == "__main__":
    main()
