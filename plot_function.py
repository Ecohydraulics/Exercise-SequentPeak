def plot_storage_curve(array_1d, min_indices, max_indices, min_values, max_values):
    """
    Plots SD_line (1d-numpy array) and markers of local maxima and minima
    :param array_1d: np.array (1xn) of the SD line
    :param min_indices: np.array (1xi) of indices (positions in SD line array) of local maxima
    :param max_indices: np.array (1xj) of indices (positions in SD line array) of local minima
    :param min_values: np.array (1xi) of values (of SD line array) of local maxima
    :param max_values: np.array (1xj) of values (of SD line array) of local maxima
    :return: show and save plot in script directory as SD_curve.png
    """
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as font_manager
    # set font properties
    hfont = {'family': 'normal',
             'weight': 'normal',
             'size': 10,
             'style': 'normal',
             'fontname': 'Arial'}
    font = font_manager.FontProperties(family=hfont['fontname'],
                                       weight=hfont['weight'],
                                       style=hfont['style'],
                                       size=hfont['size'])
    # create plot
    x_values = list(range(1, array_1d.size + 1))
    fig = plt.figure(figsize=(6, 3), dpi=150, facecolor='w', edgecolor='k')
    axe = fig.add_subplot(1, 1, 1)
    axe.plot(x_values, array_1d, linestyle='-', color="slategrey", label='storage line')

    # plot extrema
    axe.plot(min_indices, min_values, linestyle="None", color="darkred",
             marker="v", markersize=4, label='Local minima')
    axe.plot(max_indices, max_values, linestyle="None", color="limegreen",
             marker="^", markersize=4, label='Local maxima')

    # Define axis labels and legend
    axe.set_xlabel("time (months)", **hfont)
    axe.set_ylabel("storage volume (million m³)", **hfont)
    axe.legend(loc='upper left', prop=font, facecolor='w', edgecolor='gray', framealpha=1, fancybox=0)

    # Set grid
    axe.grid(color='gray', linestyle='-', linewidth=0.2)
    axe.set_ylim((0, int(np.nanmax(array_1d) * 1.1)))
    axe.set_xlim((0, array_1d.size + 1))

    # Output plot
    plt.savefig("storage_curve.png", bbox_inches='tight')
    plt.show()