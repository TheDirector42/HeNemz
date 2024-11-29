import numpy as np
import matplotlib.pyplot as plt
import os

# Step 1: Load and parse the dataset
def load_dataset(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Skip metadata and locate the header
    for i, line in enumerate(lines):
        if line.startswith("Measurement"):
            header_index = i
            break

    # Extract data from the lines below the header
    data_lines = lines[header_index + 1:]
    data = []
    for line in data_lines:
        values = line.strip().split('\t')
        try:
            # Keep only the 'TotalPower[dBm]' column (index 10)
            data.append([float(values[10])])  # Column 10 corresponds to TotalPower[dBm]
        except ValueError:
            continue

    data = np.array(data)

    return data  # Return data without padding

# Step 2: Clean and analyze data using numpy.fft
def clean_and_analyze(filename):
    data = load_dataset(filename)
    
    # Remove NaN or invalid values
    data = data[np.isfinite(data)]
    
    # Normalize data (optional)
    data -= np.mean(data)
    data /= np.std(data)
    
    # Perform FFT using numpy's fft
    X = np.fft.fft(data.flatten())  # Flatten to 1D for FFT
    X_shifted = np.fft.fftshift(X)  # Shift for centered spectrum
    X_mag = 10 * np.log10(np.abs(X_shifted)**2)

    # Plot the results
    N = len(data)
    f = np.linspace(-0.5, 0.5, N)  # Frequency axis normalized
    plt.figure(figsize=(10, 6))
    plt.plot(f, X_mag, label="FFT Magnitude")
    plt.xlabel('Frequency (normalized)')
    plt.ylabel('Magnitude [dB]')
    plt.title('FFT of Total Power')
    plt.grid()
    plt.legend()
    plt.show()

# Step 3: Execute the function with the correct path
filename = os.path.join('Data Set', 'Beam Data_2024-11-29_11.48.54_#003.txt')
clean_and_analyze(filename)
