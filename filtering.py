from scipy.signal import butter, sosfilt


def butter_bandpass(f_low, f_high, fs, order=5):
    """Design digital Butterworth filter for bandpass filtering"""
    fnyq = 0.5 * fs
    low = f_low/fnyq
    high = f_high/fnyq
    # use of second-order sections 'sos' is preferable!
    sos = butter(order, [low, high], btype='band', output='sos')
    return sos


def butter_bandpass_filtering(data, f_low, f_high, fs, order=5):
   sos = butter_bandpass(f_low, f_high, fs, order=order)
   y = sosfilt(sos, data)
   return y
    