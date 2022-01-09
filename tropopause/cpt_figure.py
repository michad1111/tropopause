import matplotlib.pyplot as plt


def cpt_fig(data_ecmwf, data_metop):
    ecmwf_alt = data_ecmwf.attrs["cpt_alt"].values
    ecmwf_temp = data_ecmwf.attrs["cpt_temp"].values

    metop_alt = data_metop.attrs["cpt_alt"].values
    metop_temp = data_metop.attrs["cpt_temp"].values

    fig, axs = plt.subplots(2, constrained_layout=True)

    axs[0].plot(data_ecmwf.altitude, data_ecmwf.temperature, label="ECMWF", color="red")
    axs[0].annotate(
        f"CPT: \n ({ecmwf_alt:.0f}, {ecmwf_temp:.2f})",
        xy=(ecmwf_alt, ecmwf_temp),
        xytext=(ecmwf_alt, ecmwf_temp + 15),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
        horizontalalignment="center",
    )
    axs[0].set_title(
        f"latitude {data_ecmwf.attrs['lat_limit']}, time {data_ecmwf.time.values.astype('datetime64[M]')}"
    )

    axs[1].plot(data_metop.altitude, data_metop.temperature, label="METOP")
    axs[1].annotate(
        f"CPT: \n ({metop_alt:.0f}, {metop_temp:.2f})",
        xy=(metop_alt, metop_temp),
        xytext=(metop_alt, metop_temp + 15),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
        horizontalalignment="center",
    )
    axs[1].set_title(
        f"latitude {data_metop.attrs['lat_limit']}, time {data_metop.attrs['time_limit'][0]}"
    )
    axs[0].set_ylabel("temperature / K")
    axs[1].set_ylabel("temperature / K")
    axs[1].set_xlabel("altitude / m")
    axs[0].legend()
    axs[1].legend()

    fig.savefig("CPT.png")
