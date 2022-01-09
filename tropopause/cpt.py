import os
from pkg_resources import resource_filename
import xarray as xr
import numpy as np

file_path_ECMWF = resource_filename(
    __name__,
    os.path.join(
        "data",
        "ECMWF_IFS-ea-0051_an_F32-T42_yggdrasil-0.5.0_altitude_10x10_temperature.nc",
    ),
)

data = xr.open_dataset(file_path_ECMWF)


def calc_cpt(lat, time):
    try:
        t = np.datetime64(time, "M")
    except ValueError:
        t = data.time.max()
        print(t)
    data_sel = (
        data.sel(latitude=slice(lat[0], lat[1]))
        .sel(time=t, method="nearest")
        .mean(dim="longitude")
    )
    lat_limit = (
        data_sel.latitude_bounds.values.min(),
        data_sel.latitude_bounds.values.max(),
    )
    data_sel = data_sel.mean(dim="latitude")
    data_sel.attrs["lat_limit"] = lat_limit

    cpt_temp = data_sel.temperature.min()
    cpt_alt = data_sel.temperature.idxmin()

    return data_sel, cpt_alt, cpt_temp
