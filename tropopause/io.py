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

file_path_example_gridded = resource_filename(
    __name__,
    os.path.join("../tests/data", "example_gridded.nc"),
)

def read_gridded(filepath=file_path_ECMWF):
    """Opens data file with gridded data and stores the data in xarray dataset"""
    match filepath:
        case "ecwmf":
            filepath = file_path_ECMWF
            print("Read ECMWF")
        case "example_gridded":
            filepath = file_path_example_gridded
            print("Read exmaple_gridded")
    ds = xr.open_dataset(filepath)
    return ds


def read_metop():
    """Opens METOP file and stores the data in xarray dataset"""
    print("Read METOP")
    ds = xr.open_dataset(file_path_METOP)
    return ds
