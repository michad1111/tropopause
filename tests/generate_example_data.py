import numpy as np
import xarray as xr


t1 = np.array([[280.1, 275.5, 268.5], [290.2, 291.1, 288.7]])
t2 = t1 - 5
t = np.array([[t1, t2]])
print(t.shape)
da = xr.DataArray(
    t,
    dims=("time", "altitude", "longitude", "latitude"),
    coords={
        "time": [np.datetime64("2020-12")],
        "altitude": [500, 1000],
        "latitude": [45.0, 50.0, 55.0],
        "longitude": [100.0, 110.0],
    },
)
ds = xr.Dataset(data_vars={"temperature": da})
ds["temperature"].attrs["units"] = "K"
print(ds)

ds.to_netcdf(
    path="../tests/data/example_gridded.nc", mode="w", format="NETCDF3_CLASSIC"
)
