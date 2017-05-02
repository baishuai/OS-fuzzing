import matplotlib.patches as patches
import matplotlib.pyplot as plt


def plt_speedup(tv, pv, height=5, width=15, fontsize=18):
    fig = plt.figure(figsize=(width, height))

    ax = fig.add_subplot(1, 1, 1)
    ax.axis('off')

    stv = sum(tv)
    spv = sum(pv)
    rectangles = {
        'robust ' + format(tv[0] / stv, '0.1%'): patches.Rectangle(
            (0, 0.5),
            tv[0] / stv, 0.28,
            fill=True, facecolor='grey',
            linewidth=3
        ),
        'buggy ' + format(tv[1] / stv, '0.1%'): patches.Rectangle(
            (tv[0] / stv, 0.5),
            tv[1] / stv, 0.28,
            fill=True, facecolor='r',
            linewidth=3
        ),
        format(pv[0] / spv, '0.1%'): patches.Rectangle(
            (0, 0.2),
            pv[0] / spv, 0.28,
            fill=True, facecolor='grey',
            linewidth=3
        ),
        format(pv[1] / spv, '0.1%'): patches.Rectangle(
            (pv[0] / spv, 0.2),
            pv[1] / spv, 0.28,
            fill=True, facecolor='r',
            linewidth=3,
            edgecolor='black',
            hatch='/',
            linestyle='dashed'
        ),
        format(pv[2] / spv, '0.1%'): patches.Rectangle(
            ((pv[0] + pv[1]) / spv, 0.2),
            pv[2] / spv, 0.28,
            fill=True, facecolor='r',
            linewidth=3,
            edgecolor='black',
            hatch='\\',
            linestyle='dashed'
        ),
        format(pv[3] / spv, '0.1%'): patches.Rectangle(
            ((pv[0] + pv[1] + pv[2]) / spv, 0.2),
            pv[3] / spv, 0.28,
            fill=True, facecolor='y',
            linewidth=3
        )
    }

    for r in rectangles:
        ax.add_artist(rectangles[r])
        rx, ry = rectangles[r].get_xy()
        cx = rx + rectangles[r].get_width() / 2.0
        cy = ry + rectangles[r].get_height() / 2.0
        ax.annotate(r, (cx, cy), color='black', weight='bold',
                    fontsize=18, ha='center', va='center')

    speedup = (pv[2] / tv[1]) / ((pv[1] + pv[2]) / sum(pv))
    speedup_str = "speedup: ({:.1%}/{:.1%}) / ({:.1%}+{:.1%}) = {:.1%}".format(pv[2] / spv, tv[1] / stv,
                                                                               pv[1] / spv, pv[2] / spv,
                                                                               speedup)
    ax.annotate(speedup_str, xy=(0.5, 0.9), fontsize=22, ha='center', va='center')
    # plt.show()


if __name__ == '__main__':
    tv = [99, 83]
    pv = [78, 21, 15, 68]

    plt_speedup(tv, pv)
