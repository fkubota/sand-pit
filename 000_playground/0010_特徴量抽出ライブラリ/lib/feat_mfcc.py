import pandas as pd
import librosa


class FeatMFCC:
    def __init__(self, sampling_rate, window_size_sec, window_stride_sec):
        self.sampling_rate = sampling_rate
        self.window_size_sec = window_size_sec
        self.window_stride_sec = window_stride_sec
        self.name = 'MFCC'
        self.default_option = {'n_mfcc': 20, 'dct_type': 2}

    def feature_extraction(self, signal, **kwargs):
        n_mfcc = kwargs.get('n_mfcc', 20)
        dct_type = kwargs.get('dct_type', 2)

        df_feat = pd.DataFrame()
        n_fft = int(self.sampling_rate * self.window_size_sec)
        hop_length = int(self.sampling_rate * self.window_stride_sec)

        # feat
        feat = librosa.feature.mfcc(signal,
                                    sr=self.sampling_rate,
                                    n_fft=n_fft,
                                    hop_length=hop_length,
                                    n_mfcc=n_mfcc,
                                    dct_type=dct_type)

        for n in range(len(feat)):
            df_feat[f'mfcc_{str(n).zfill(2)}'] = feat[n]
        return df_feat
