import argparse

from . import tropopause


def temp_anomalies_graz():
    """Latitude boundaries for CPT calculation"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--lat",
        required=True,
        nargs="+",
        type=int,
        help="two integers for the boundaries of the latitude range",
    )

    args = parser.parse_args()

    data_sel, cpt_alt, cpt_temp = tropopause.calc_cpt(args.lat)
    tropopause.cpt_fig(args.lat, data_sel, cpt_alt, cpt_temp)