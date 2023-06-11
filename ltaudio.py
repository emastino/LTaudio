from scipy.io.wavfile import write
import numpy as np
import ltspice


class ltaudio:

    def __init__(self, file_path):
        self.lt = None
        self.sample_rate = 44100  # Hz
        self.sample_time = 1/self.sample_rate
        self.time = []  # Sec, numpy array
        self.init(file_path)

    def init(self, ltspice_file_path):

        self.lt = ltspice.Ltspice(ltspice_file_path)
        self.lt.parse()  # Data loading sequence. It may take few minutes for huge file.

        self.time = self.lt.get_time()

    def interpolate_for_me(self, tf, tr_1, tr, yr_1, yr):
        m = (yr - yr_1) / (tr - tr_1)
        yf = m * (tf - tr_1) + yr_1
        return yf




    def make_wav(self, input_variable_name, output_file_path, volume=100):

        ltspice_data = self.lt.get_data(input_variable_name)
        output = []

        # Pseudo Sampled Time Array
        time_f = np.linspace(0, self.time[-1], int(self.time[-1] / self.sample_time))

        # Initial Value
        output.append(volume * ltspice_data[0])

        i_f = 1
        i = 1

        while i_f < len(time_f) - 1:

            if self.time[i - 1] < time_f[i_f] < self.time[i]:
                # Slope form and interpolate
                clean_interp_temp = volume * self.interpolate_for_me(time_f[i_f], self.time[i - 1], self.time[i],
                                                                     ltspice_data[i - 1], ltspice_data[i])

                output.append(clean_interp_temp)

                i_f += 1

            if time_f[i_f] > self.time[i]:
                i += 1

        sampled_data = np.array(output)


        write(output_file_path, self.sample_rate, sampled_data.astype(np.int16))

