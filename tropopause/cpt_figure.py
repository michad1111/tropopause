import matplotlib.pyplot as plt


def cpt_fig(data_sel, cpt_alt, cpt_temp, data_METOP):
    fig, axs = plt.subplots(2, constrained_layout=True)

    axs[0].plot(data_sel.altitude, data_sel.temperature, label="ECMWF")
    axs[0].annotate(
        f"CPT: \n ({cpt_alt.values:.0f}, {cpt_temp.values:.2f})",
        xy=(cpt_alt, cpt_temp),
        xytext=(cpt_alt, cpt_temp + 15),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
        horizontalalignment="center",
    )
    axs[0].set_title(
        f"latitude {data_sel.attrs['lat_limit']}, time {data_sel.time.values.astype('datetime64[M]')}"
    )

    axs[1].plot(data_METOP.altitude, data_METOP.temperature, label="METOP")
    axs[1].annotate(
        f"CPT: \n ({data_METOP.attrs['cpt_alt']:.0f}, {data_METOP.attrs['cpt_temp']:.2f})",
        xy=(data_METOP.attrs["cpt_alt"], data_METOP.attrs["cpt_temp"]),
        xytext=(data_METOP.attrs["cpt_alt"], data_METOP.attrs["cpt_temp"] + 15),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
        horizontalalignment="center",
    )
    axs[1].set_title(
        f"latitude {data_METOP.attrs['lat_limit']}, time {data_METOP.attrs['time_limit']}"
    )
    axs[0].set_ylabel("temperature")
    axs[1].set_ylabel("temperature")
    axs[1].set_xlabel("altitude")

    fig.savefig("CPT.png")
