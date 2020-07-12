import sys
import librosa
import numpy as np
import pyqtgraph as pg
import PyQt5.QtWidgets as QW
import PyQt5.QtMultimedia as QM
from PyQt5.QtCore import QUrl


class MainWindow(QW.QMainWindow):
    def __init__(self):
        super().__init__()

        self.w = QW.QWidget()
        self.player = QM.QMediaPlayer()
        self.lbl_file = QW.QLabel('No File')
        self.btn_open = QW.QPushButton('Open')
        self.btn_play = QW.QPushButton('Play')
        self.btn_pause = QW.QPushButton('Pause')

        # graph
        self.w_pg_signal = pg.GraphicsWindow()
        self.p_pg0 = self.w_pg_signal.addPlot()
        self.pg_signal0 = self.p_pg0.plot(pen=('#0F8EBB50'))
        self.pg_bar = pg.InfiniteLine(
                                pen='FF000055',
                                hoverPen='0000FF55',
                                movable=True
                                )

        # init method
        self.init_ui()
        self.init_event()

    def init_ui(self):
        self.setCentralWidget(self.w)
        self.player.setNotifyInterval(100)

        # graph
        self.w_pg_signal.setBackground('FFFFFF00')
        self.p_pg0.addItem(self.pg_bar)

        # layout
        hbox0 = QW.QHBoxLayout()
        hbox0.addWidget(self.lbl_file)
        hbox0.addWidget(self.btn_open)
        hbox1 = QW.QHBoxLayout()
        hbox1.addWidget(self.btn_play)
        hbox1.addWidget(self.btn_pause)
        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.w_pg_signal)
        vbox0.addLayout(hbox0)
        vbox0.addLayout(hbox1)
        self.w.setLayout(vbox0)

    def init_event(self):
        # btn
        self.btn_open.clicked.connect(self.clicked_open)
        self.btn_play.clicked.connect(self.play_handler)
        self.btn_pause.clicked.connect(self.pause_handler)

        # player
        self.player.positionChanged.connect(self.player_position_changed)

    def play_handler(self):
        print('-- play_handler')
        self.player.play()

    def pause_handler(self):
        print('-- pause_handler')
        self.player.pause()

    def player_position_changed(self, posi, senderType=False):
        posi_sec = posi/1000
        print(posi, posi_sec)
        self.pg_bar.setPos(posi_sec)

    def clicked_open(self):
        print('-- clicked_open')
        filename, _ = QW.QFileDialog.getOpenFileName(self, 'Open Music File')
        self.lbl_file.setText(filename)
        if filename == '':
            return
        else:
            self.player.setMedia(
                QM.QMediaContent(QUrl.fromLocalFile(filename))
                )

        # graph update
        signal, sr = librosa.load(filename, sr=None)
        x = np.arange(0, len(signal))/sr
        x = x[::100]
        signal = signal[::100]
        self.pg_signal0.setData(x, signal)


def main():
    app = QW.QApplication(sys.argv)

    w = MainWindow()
    w.resize(700, 300)
    w.move(500, 600)
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
