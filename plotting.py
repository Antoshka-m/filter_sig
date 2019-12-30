import matplotlib.pyplot as plt
import seaborn as sns

def plot_filtered(ax, t, x_filt, f_low, f_high, tlims=None):
    ax.plot(t, x_filt)
    
    ax.set_title('After %s Hz to %s Hz band-pass filter' % (f_low, f_high))
    ax.set_xlabel('Time, s')
    if tlims is not None:
        ax.set_xlim(tlims[0], tlims[1])
    plt.grid()
        
def plot_flattened(ax, t, x_flat, window_l, tlims=None):
    t=t.iloc[:len(x_flat)]
    ax.plot(t, x_flat)
    # sns.lineplot(x=t, y=x_flat, ax=ax)
    ax.set_title('After flattening using %s s window' % window_l)
    ax.set_xlabel('Time, s')
    if tlims is not None:
        ax.set_xlim(tlims[0], tlims[1])
    plt.grid()
        
        
def plot_raw(ax, t, x, tlims=None):
    ax.plot(t, x)
    # sns.lineplot(x=t, y=x, ax=ax)
    ax.set_title('Raw timeseries signal')
    ax.set_xlabel('Time, s')
    if tlims is not None:
        ax.set_xlim(tlims[0], tlims[1])
    plt.grid()

def plot_compare_raw_w_bandpass(t,
                                x,
                                x_flat,
                                x_filt,
                                tlims,
                                window_l,
                                f_low,
                                f_high):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10, 10))
    plot_raw(ax=ax1, t=t, x=x, tlims=tlims)
    plot_flattened(ax=ax2,
                   t=t,
                   x_flat=x_flat,
                   window_l=window_l,
                   tlims=tlims)
    plot_filtered(ax=ax3,
                  t=t,
                  x_filt=x_filt,
                  f_low=f_low,
                  f_high=f_high,
                  tlims=tlims)
    plt.tight_layout()
    plt.show()
    