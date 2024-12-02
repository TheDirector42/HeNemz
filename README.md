FFT Light Analysis Tool
Overview
This Python script processes power meter data from CSV files and performs a Fast Fourier Transform (FFT) analysis on the power readings. It visualizes the frequency spectrum of the data to analyze patterns or detect anomalies.

Features
CSV Data Processing: Reads and processes power data from a specified CSV file.
FFT Analysis: Computes the FFT of power data to analyze frequency components.
Visualization: Generates a frequency spectrum plot in decibels (dB).
Custom Parameters:
Sample Rate: Specify the data sample rate (in Hz).
Output Directory: Define where to save results and plots (if implemented).
Prerequisites
Python 3.7 or later
Virtual environment (recommended)
Dependencies
The following Python libraries are required:

numpy
pandas
matplotlib
scipy
Setup Instructions
Clone or Download the Repository

bash
Copy code
git clone https://github.com/YourUsername/fft_light_analysis.git
cd fft_light_analysis
Set Up a Virtual Environment

bash
Copy code
python -m venv env
source env/bin/activate      # macOS/Linux
env\Scripts\activate         # Windows
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Prepare Data Place your CSV data files in a directory (e.g., PowerMeter/). Ensure the files have the following format:

Columns: Samples, Date, Time, Power (W)
Rows: Data rows with numeric values in the "Power (W)" column.
Run the Script

bash
Copy code
python fft_light_analysis.py "path/to/datafile.csv" --sample_rate <sample_rate_in_hz> --output_dir <output_directory>
Example:

bash
Copy code
python fft_light_analysis.py "PowerMeter/2024-11-28_Arm2.csv" --sample_rate 100 --output_dir Results/
How It Works
File Processing:

Reads the CSV file and cleans the "Power (W)" column.
Handles missing or invalid values.
FFT Analysis:

Computes the FFT of the power data.
Outputs a frequency spectrum plot (magnitude in dB vs. frequency).
Visualization:

Displays the frequency spectrum using Matplotlib.
Future Enhancements
Save plots and analysis results to the specified output directory.
Add error handling for incorrect file formats.
Support for batch processing of multiple CSV files.
Dynamic configuration for plot customization.
