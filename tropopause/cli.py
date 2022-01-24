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
    parser.add_argument(
        "--source",
        required=False,
        type=str,
        nargs="+",
        default=("ecmwf", "metop"),
        help="specify data source; options: ecmwf, metop, example_gridded; default: ecmwf, metop"
    )

    args = parser.parse_args()
    if args.lat[0] >= args.lat[1]:
        parser.error("Second latitude value must be larger than first latitude value.")

    if (args.lat[0] < -90) or (args.lat[1] > 90):
        parser.error("latitude values need to be within [-90, 90].")

    data = {}

    if len(args.source) < 2:
        raise AttributeError("A minimum of two sources is required")

    if "ecmwf" in args.source:
        data["ecmwf"] = cpt.calc_from_gridded(io.read_gridded("ecwmf"), args.lat, args.time)

    if "metop" in args.source:
        data["metop"] = cpt.calc_from_index_based(io.read_index_based("metop"), args.lat)

    if "example_gridded" in args.source:
        data["example_gridded"] = cpt.calc_from_gridded(io.read_gridded("example_gridded"), args.lat, args.time)

    if len(data) < 2:
        raise AttributeError("A minimum of two valid sources is required")
    cpt_figure.cpt_fig(data)
