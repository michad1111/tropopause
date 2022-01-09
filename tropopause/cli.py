import argparse

from . import cpt_ecmwf
from . import cpt_metop
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

    data_ecmwf = cpt_ecmwf.calc_cpt(args.lat, args.time)
    data_metop = cpt_metop.calc_cpt(args.lat)
    cpt_figure.cpt_fig(data_ecmwf, data_metop)
