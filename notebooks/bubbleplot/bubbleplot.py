import pylab
from collections import defaultdict
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

name = lambda x: x.display.replace("  ", "")
font0 = FontProperties()
font0.set_weight('bold')


def bubble_plot(script, binary, rows, columns, process, rate=320, label_y=-3.5, rotation="horizontal", show_lower_label=True,
                axis_y="Provenance Applications", axis_x="← Provenance Types →", xticksize=12, yticksize=14,
                pointsize=12, axissize=14):
    xs_map = {
        name: i + 2 for i, name in enumerate(rows)
    }
    ys_map = {
        name: 2*i for i, name in enumerate(columns)
    }

    xs, ys, ss = [], [], []
    gs = {}
    for j, mode in enumerate((script, binary)):
        gs["binary" if j else "script"] = groups = defaultdict(set)

        def add(goal, category, approach):
            groups[(goal, category)].add(name(approach))
            #groups[("Overall", category)].add(name(approach))
            
        for a, m in mode:
            process(a, m, add)

        for group, elements in groups.items():
            if group[1] not in xs_map:
                print(group[1], 'not in rows')
                continue
            if group[0] not in ys_map:
                print(group[0], 'not in columns')
                continue
            xs.append((-1 if j else 1) * xs_map[group[1]])
            ys.append(ys_map[group[0]])
            ss.append(rate * len(elements))

    
    fig, ax = plt.subplots()

    sc = ax.scatter(xs, ys, s=ss, c=(0.95, 0.95, 0.95), edgecolors=(0, 0, 0))

    for x, y, s in zip(xs, ys, ss):
        pylab.text(x, y, str(int(s/rate)), color="black", fontsize=pointsize,
                   horizontalalignment="center",
                   verticalalignment="center")

    ax.grid()

    names = [x for x in rows]
    
    labels = list(reversed(names)) + [""] * 3 + names
    plt.xticks(range(-len(names) - 1, len(names) + 2), labels, rotation=rotation)
    plt.tick_params(axis='both', which='major', labelsize=xticksize)
    plt.yticks(range(0, len(columns) * 2 + 2, 2), [""]*(len(columns) + 1))
    
    if names[-1] == "Overall":
        iterticks = iter(ax.xaxis.get_major_ticks())
        first_tick = next(iterticks)
        for last_tick in iterticks:
            pass
        first_tick.label1.set_fontweight('bold')
        last_tick.label1.set_fontweight('bold')
    
    
    for i, column in enumerate(columns):
        font0.set_size(yticksize)
        kwargs = {'fontsize':yticksize} if i != len(columns) -1 else {'fontproperties':font0, 'fontsize':yticksize}
        pylab.text(0, i * 2 , column, color="black",
                   horizontalalignment="center",
                   verticalalignment="center", **kwargs)

    if show_lower_label:
        pylab.text(-(len(labels) + 3) / 4, label_y , "Binary", color="black", fontsize=12,
                   horizontalalignment="center",
                   verticalalignment="center")
        pylab.text((len(labels) + 3) / 4, label_y , "Script", color="black", fontsize=12,
                   horizontalalignment="center",
                   verticalalignment="center")
    
   
    ax.set_xlabel(axis_x, fontsize=axissize)
    ax.set_ylabel(axis_y, fontsize=axissize)
   
    return plt, gs


def script_bubble_plot(script, rows, columns, process, rate=320, label_y=-3.5, rotation="horizontal",
                       axis_y="Provenance Applications", axis_x="Provenance Types", xticksize=14, yticksize=14,
                       pointsize=12, axissize=14, show_lower_label=False):
    plt, groups = bubble_plot(script, [], rows, columns, process, rate=rate, label_y=label_y, rotation=rotation,
                              show_lower_label=show_lower_label, axis_y=axis_y, axis_x=axis_x, xticksize=xticksize, yticksize=yticksize, pointsize=pointsize, axissize=axissize)
    plt.xlim(-1, len(rows) + 2)

    return plt, groups