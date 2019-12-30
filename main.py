from flattening import flattening
from plotting import (plot_filtered, plot_flattened, plot_raw,
                      plot_compare_raw_w_bandpass)
from filtering import butter_bandpass, butter_bandpass_filtering
from get_filenames import get_filenames, get_fps_from_fname
from os.path import basename
import pandas as pd

print('Choose one file')
file = get_filenames()[0]
df=pd.read_csv(file)
fs = get_fps_from_fname(file)
print('Read %s file recorded with fs=%sHz' %(basename(file), fs))
y = df['Iz norm']
x = df['Il norm']
t = df['t']
f_low = 80
f_high = 140
tlims=(120.0, 120.3)
flat_window=30
fit, x_flat = flattening(data=x, dt=t[1]-t[0], chunk_l=flat_window)
x_filt =  butter_bandpass_filtering(data=x,
                                    f_low=f_low,
                                    f_high=f_high,
                                    fs=fs)
plot_compare_raw_w_bandpass(t,
                            x,
                            x_flat,
                            x_filt,
                            None,
                            flat_window,
                            f_low,
                            f_high)
plot_compare_raw_w_bandpass(t,
                            x,
                            x_flat,
                            x_filt,
                            tlims,
                            flat_window,
                            f_low,
                            f_high)
