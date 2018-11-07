from matplotlib import colors as mcolors, cm


# The name of the colormap.
_colormap_name = "nifty"
# The colormap data, as a list of RGB tuples.
_colormap_data = [
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.5),
    (0.0, 0.5, 0.5),
    (0.5, 0.5, 0.5),
    (0.5, 0.5, 1.0),
    (1.0, 1.0, 1.0),
]


cmap = mcolors.ListedColormap(_colormap_data, _colormap_name)


def register_cmap():
    cm.register_cmap(cmap=cmap)


if __name__ == "__main__":

    from matplotlib import pyplot as plt

    fig = plt.figure()
    sm = cm.ScalarMappable(cmap=cmap)
    sm.set_array([])
    fig.colorbar(sm)
    plt.show()
