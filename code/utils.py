def set_mpl_defaults(mpl):
    mpl.rc('figure', figsize=(10, 6))
    mpl.rc('axes', color_cycle='k')
    mpl.rc('lines', linewidth=2)
    mpl.rc('axes', facecolor='white', edgecolor='black')
    mpl.rc('patch', facecolor='white', edgecolor='none')
    mpl.rc('lines', markeredgewidth=0)
    mpl.rc('font', size=18, family='Helvetica Neue')
    mpl.rc('legend', fontsize=14, frameon=False)
    mpl.rc('xtick.major', pad=8)
    mpl.rc('ytick.major', pad=8)
    mpl.rc('svg', fonttype='none') # 'path' saves it as a path, not as a text object

def remove_spines(axes=None, top=False, right=False, left=True, bottom=True):
    """ Minimize chartjunk by stripping out unnecessary plot borders and axis ticks
    The top/right/left/bottom keywords toggle whether the corresponding plot border is drawn
    """
    import matplotlib.pyplot as plt

    ax = axes or plt.gca()
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
    
    # turn off all ticks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')
    
    # now re-enable visibles
    if top:
        ax.xaxis.tick_top()
    if bottom:
        ax.xaxis.tick_bottom()
    if left:
        ax.yaxis.tick_left()
    if right:
        ax.yaxis.tick_right()

def save_figure(fig, filename, folder='../figures', exts=['pdf']):
    import os
    import matplotlib.pyplot as plt
    for ext in exts:
        i = 0
        while True:
            path = '{}/{}-{:d}.{}'.format(folder, filename, i, ext)
            if not os.path.exists(path):
                break
            i += 1
        plt.savefig(path)