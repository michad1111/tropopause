import argparse

from . import tropopause


def temp_anomalies_graz():
    """Entry point for the tropopause"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start",
        required=True,
        type=int,
        help="Start year of the reference timeframe.",
    )

    args = parser.parse_args()
