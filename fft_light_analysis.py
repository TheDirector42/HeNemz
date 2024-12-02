import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import windows, spectrogram
from matplotlib.colors import LogNorm
import os
import argparse

# FFT function with windowing
def perform_fft_on_power_data(power_data, sample_rate=1):
    N = len(power_data)
    t = np.arange(N) / sample_rate  # Time array
    
    # Apply a Hanning window
    window = windows.hann(N)
    power_data_windowed = power_data * window
    
    # Perform FFT
    X = np.fft.fft(power_data_windowed)
    X_shifted = np.roll(X, N // 2)  # Shift zero frequency to center
    X_mag = 10 * np.log10(np.abs(X_shifted) ** 2)  # Magnitude in dB
    
    frequencies = np.linspace(-sample_rate / 2, sample_rate / 2, len(X_mag))
    return frequencies, X_mag

# Spectrogram plotting
def plot_spectrogram(power_data, sample_rate=1):
    f, t, Sxx = spectrogram(power_data, fs=sample_rate, nperseg=256)
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud', norm=LogNorm())
    plt.title('Spectrogram of Power Data')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.colorbar(label='Intensity [dB]')
    plt.show()

# Process a single CSV file
def process_file(file_path):
    try:
        data = pd.read_csv(file_path, delimiter=',', engine='python')
        
        # Debugging output
        print(f"Processing file: {file_path}")
        print("Data preview:\n", data.head())
        
        # Dynamic column renaming
        expected_columns = ["Samples", "Date", "Time", "Power (W)"]
        data.columns = expected_columns[:len(data.columns)]  # Adjust based on column count
        
        # Convert "Power (W)" to numeric
        if "Power (W)" in data.columns:
            data["Power (W)"] = pd.to_numeric(data["Power (W)"], errors='coerce')
            data = data.dropna(subset=["Power (W)"])  # Drop rows with NaN in "Power (W)"
        else:
            raise ValueError("Missing 'Power (W)' column.")
        
        return data
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

# Batch process files in a directory
def process_files_in_directory(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if file_path.endswith('.csv'):
            process_and_fft_specific_file(file_path)

# Save FFT results to CSV
def save_fft_results_to_csv(frequencies, magnitudes, output_path):
    try:
        df = pd.DataFrame({'Frequency (Hz)': frequencies, 'Magnitude (dB)': magnitudes})
        df.to_csv(output_path, index=False)
        print(f"FFT results saved to {output_path}")
    except Exception as e:
        print(f"Error saving FFT results: {e}")

# Main processing function
def process_and_fft_specific_file(file_path, output_dir=None, sample_rate=1):
    data = process_file(file_path)
    if data is None:
        return
    
    power_data = data["Power (W)"].values
    frequencies, magnitudes = perform_fft_on_power_data(power_data, sample_rate)
    
    # Plot FFT
    plt.plot(frequencies, magnitudes)
    plt.title(f"FFT of Power Data from {file_path}")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude [dB]")
    plt.grid(True)
    plt.show()
    
    # Plot Spectrogram
    plot_spectrogram(power_data, sample_rate)
    
    # Save results
    if output_dir:
        output_path = os.path.join(output_dir, f"{os.path.basename(file_path).split('.')[0]}_fft_results.csv")
        save_fft_results_to_csv(frequencies, magnitudes, output_path)

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description="Process and analyze power meter CSV files.")
    parser.add_argument("file_path", help="Path to the CSV file or directory of CSV files.")
    parser.add_argument("--output_dir", help="Directory to save FFT results.", default=None)
    parser.add_argument("--sample_rate", type=float, help="Sampling rate in Hz.", default=1)
    args = parser.parse_args()
    
    if os.path.isdir(args.file_path):
        process_files_in_directory(args.file_path)
    elif os.path.isfile(args.file_path):
        process_and_fft_specific_file(args.file_path, args.output_dir, args.sample_rate)
    else:
        print(f"Invalid path: {args.file_path}")

# Run the program
if __name__ == "__main__":
    main()
