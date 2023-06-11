import ltaudio as lta

# specify where ltspice project is
filepath = 'D:/Users/emast/Python/PyCharm Community Edition 2021.1.1/Projects/LTSpice Audio Gen/examples/distortion 00/LTSpice/distortion 00.raw'
lt_example = lta.ltaudio(filepath)

# specify file path for output file
output_path = "D:/Users/emast/Python/PyCharm Community Edition 2021.1.1/Projects/LTSpice Audio Gen/examples/distortion 00/LTAudio Outputs/"
clean_file_name = "example_clean.wav"
distorted_file_name = "example_dist.wav"

lt_example.make_wav('V(n006)',output_path+clean_file_name, 300)    # Pass in the LTSpice Variable you want, the output path, and the volume of your file
lt_example.make_wav('V(n005)',output_path+distorted_file_name, 200)    # Pass in the LTSpice Variable you want, the output path, and the volume of your file

