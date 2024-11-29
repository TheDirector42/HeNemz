import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# FFT function (same as before)
def fft(x):
    N = len(x)
    if N == 1:
        return x
    twiddle_factors = np.exp(-2j * np.pi * np.arange(N // 2) / N)
    x_even = fft(x[::2])  # Recursion
    x_odd = fft(x[1::2])
    return np.concatenate([x_even + twiddle_factors * x_odd,
                           x_even - twiddle_factors * x_odd])

# Process the specific file (PowerMeter\2024-11-28 Both Arms.csv)
def process_file(file_path):
    try:
        # Read the CSV file with comma delimiter (standard CSV format)
        data = pd.read_csv(file_path, delimiter=',', skiprows=1, engine='python')  # Skip the first row if metadata
        
        # Debugging output: check the first few rows to inspect the data
        print("Data preview:\n", data.head())
        print("Data columns:", data.columns)

        # Rename columns to match the data structure
        data.columns = ["Samples", "Date", "Time", "Power (W)"]

        # Convert "Power (W)" to numeric (float), and handle any errors (e.g., NaN values)
        data["Power (W)"] = pd.to_numeric(data["Power (W)"], errors='coerce')
        data = data.dropna(subset=["Power (W)"])  # Drop rows where "Power (W)" is NaN

        return data
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

# Function to perform FFT on the power data
def perform_fft_on_power_data(power_data, sample_rate=1):
    N = len(power_data)
    t = np.arange(N) / sample_rate  # Time array

    # Use the FFT function on the power data
    X = np.fft.fft(power_data)  # Using np.fft.fft for performance
    X_shifted = np.roll(X, N // 2)  # Shift zero frequency to center
    X_mag = 10 * np.log10(np.abs(X_shifted) ** 2)  # Magnitude in dB

    return X_mag, t

# Main function to process the specific file and perform FFT
def process_and_fft_specific_file(file_path):
    # Process the file
    data = process_file(file_path)  # Process the CSV file
    if data is None:
        print("Failed to process the file.")
        return
    
    power_data = data["Power (W)"].values  # Extract power data
    
    # Perform FFT on the power data
    X_mag, t = perform_fft_on_power_data(power_data)
    
    # Plot the results
    sample_rate = 1  # Define sample rate (in Hz, adjust as needed)
    f = np.linspace(-sample_rate / 2, sample_rate / 2, len(X_mag))  # Frequency (in Hz)
    plt.plot(f, X_mag)
    plt.title(f"FFT of Power Data from {file_path}")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude [dB]")
    plt.grid(True)
    plt.show()

# Example usage
file_path = r'PowerMeter/2024-11-28 Arm 2 Attempt 2.csv'  # Update with the path to your file
process_and_fft_specific_file(file_path)
