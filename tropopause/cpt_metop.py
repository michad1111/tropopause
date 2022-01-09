import os
from pkg_resources import resource_filename
import xarray as xr
import numpy as np

file_path_METOP = resource_filename(
    __name__,
    os.path.join("data", "METOP-A_GPS_2020-01-01_OPSv5.6.2_UCAR-2016.0120_L2.nc"),
)

data_METOP = xr.open_dataset(file_path_METOP)


def calc_cpt(lat):
    data_sel = data_METOP.where(data_METOP.latitude >= lat[0], drop=True)
    data_sel = data_sel.where(data_sel.latitude <= lat[1], drop=True)
    lat_limit = (
        np.round(data_sel.latitude.values.min(), 2),
        np.round(data_sel.latitude.values.max(), 2),
    )
    time_limit = [
        data_sel.time.values.min().astype("datetime64[m]").astype("str"),
        data_sel.time.values.max().astype("datetime64[m]").astype("str"),
    ]
    data_sel = data_sel.mean("n_event")
    data_sel.attrs["lat_limit"] = lat_limit
    data_sel.attrs["time_limit"] = time_limit

    data_sel.attrs["cpt_temp"] = data_sel.temperature.min().values
    data_sel.attrs["cpt_alt"] = data_sel.temperature.idxmin().values

    return data_sel
