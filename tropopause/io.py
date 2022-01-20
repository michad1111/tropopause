import xarray as xr
import os
from pkg_resources import resource_filename

file_path_ECMWF = resource_filename(
    __name__,
    os.path.join(
        "data",
        "ECMWF_IFS-ea-0051_an_F32-T42_yggdrasil-0.5.0_altitude_10x10_temperature.nc",
    ),
)

file_path_METOP = resource_filename(
    __name__,
    os.path.join("data", "METOP-A_GPS_2020-01-01_OPSv5.6.2_UCAR-2016.0120_L2.nc"),
)


def read_ecmwf():
    """Opens ECMWF file and stores the data in xarray dataset"""
    print("Read ECMWF")
    ds = xr.open_dataset(file_path_ECMWF)
    return ds


def read_metop():
    """Opens METOP file and stores the data in xarray dataset"""
    print("Read METOP")
    ds = xr.open_dataset(file_path_ECMWF)
    return ds
