#!/usr/bin/env python3

from matplotlib import pyplot as plt

import numpy as np

with plt.xkcd():
    # Based on "Stove Ownership" from XKCD by Randall Munroe
    # https://xkcd.com/418/

    fig = plt.figure(figsize=(6,4))
    ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.set_ylim([-30, 10])

    def f_sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def f_foo(x):
        if x < -1.0:
            return -1.0
        if x > 1.0:
            return 1.0

        return x


    f = f_sigmoid
    x = np.arange(-10, 10, step=0.1)
    y = [f(xp) for xp in x]

    ax.annotate(
        "absolutelty worth it",
        xy=(-1, f(-1)),
        arrowprops=dict(arrowstyle="->"),
        xytext=(-10, f(3)  - 0.5),
    )

    ax.annotate(
        "absolutelty not worth it",
        xy=(5, f(5)),
        arrowprops=dict(arrowstyle="->"),
        xytext=(1, f(5) - 0.5),
    )

    ax.plot(x, y)

    ax.set_xlabel("effort put into visualizations")
    ax.set_ylabel("number of people \nunderstanding my visualizations")
    # fig.text(0.5, 0.05, '"Stove Ownership" from xkcd by Randall Munroe', ha="center")

    plt.savefig("featured.png",dpi=240)
    plt.savefig("featured.svg",dpi=240)
