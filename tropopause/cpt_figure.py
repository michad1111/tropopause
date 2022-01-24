import matplotlib.pyplot as plt


def cpt_fig(data):
    fig, ax = plt.subplots(len(data), constrained_layout=True)
    for idx, (label, ds) in enumerate(data.items()):
        print(f"Plotting {label}")
        ax[idx].plot(ds.altitude, ds.temperature, label=label)
        alt = ds.cpt_alt.values
        temp = ds.cpt_temp.values
        temp_delta = ds.temperature.max() - ds.temperature.min()
        ax[idx].annotate(
            f"CPT: \n ({alt:.0f}, {temp:.2f})",
            xy=(alt, temp),
            xytext=(alt, temp + temp_delta * 0.25),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"),
            horizontalalignment="center",
        )
        try:
            ax[idx].set_title(
                f"latitude {ds.lat_limit.values}, time {ds.time.values.astype('datetime64[M]')}"
            )
        except AttributeError:
            ax[idx].set_title(
                f"latitude {ds.lat_limit.values}, time {ds.time_limit.values[0]}"
            )
        ax[idx].set_ylabel("temperature / K")
        ax[idx].legend()
    ax[-1].set_xlabel("altitude / m")
    fig.savefig("CPT.png")
