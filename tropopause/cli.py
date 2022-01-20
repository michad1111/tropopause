import argparse

from . import cpt
from . import io
from . import cpt_figure


def tropopause():
    """Latitude boundaries for CPT calculation"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lat",
        required=True,
        nargs="+",
        type=int,
        help="two integers for the boundaries of the latitude range",
    )
    parser.add_argument(
        "--time",
        required=False,
        type=str,
        default="2020-12",
        help="time for tropopause analysis format YYYY-MM (default: 2020-12)",
    )

    args = parser.parse_args()
    if args.lat[0] >= args.lat[1]:
        parser.error("Second latitude value must be larger than first latitude value.")

    if (args.lat[0] < -90) or (args.lat[1] > 90):
        parser.error("latitude values need to be within [-90, 90].")

    data = {}
    data["ecmwf"] = cpt.calc_from_gridded(io.read_ecmwf(), args.lat, args.time)
    data["metop"] = cpt.calc_from_index_based(io.read_metop(), args.lat)
    cpt_figure.cpt_fig(data)
