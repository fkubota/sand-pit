from scipy import signal
import numpy as np
import pyqtgraph

# Create the data
fs = 10e3
N = 1e5
amp = 2 * np.sqrt(2)
# noise_power = 0.01 * fs / 2
time = np.arange(N) / float(fs)
mod = 500*np.cos(2*np.pi*0.25*time)
carrier = amp * np.sin(2*np.pi*3e3*time + mod)
# noise = np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
# noise *= np.exp(-time/5)
# x = carrier + noise

# filename = librosa.util.example_audio_file()
# data, sr = librosa.load(filename, sr=None)
f, t, Sxx = signal.spectrogram(carrier, fs)

# Interpret image data as row-major instead of col-major
pyqtgraph.setConfigOptions(imageAxisOrder='row-major')

# window and plot
pyqtgraph.mkQApp()
win = pyqtgraph.GraphicsLayoutWidget()
p1 = win.addPlot()

# Item for displaying image data
img = pyqtgraph.ImageItem()
img.setImage(Sxx)
img.scale(t[-1]/np.size(Sxx, axis=1),
          f[-1]/np.size(Sxx, axis=0))
p1.addItem(img)

# color
hist = pyqtgraph.HistogramLUTItem()
hist.setImageItem(img)
hist.setLevels(np.min(Sxx), np.max(Sxx))
hist.gradient.restoreState(
        {'mode': 'rgb',
         'ticks': [(0.5, (0, 182, 188, 255)),
                   (1.0, (246, 111, 0, 255)),
                   (0.0, (75, 0, 113, 255))]})

# show
win.show()
pyqtgraph.Qt.QtGui.QApplication.instance().exec_()
