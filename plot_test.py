import mne

edf_file = "data/chb01/chb01_01.edf"
raw = mne.io.read_raw_edf(edf_file, preload=True)
raw.plot(n_channels=10, duration=5, scalings='auto', block=True)
