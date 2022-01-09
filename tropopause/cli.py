import argparse

from . import cpt


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
        default='2020-12',
        help="time for tropopause analysis format YYYY-MM (default: 2020-12)",
    )

    args = parser.parse_args()

    data_sel, cpt_alt, cpt_temp = cpt.calc_cpt(args.lat, args.time)
    cpt.cpt_fig(args.lat, data_sel, cpt_alt, cpt_temp)