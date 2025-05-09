import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the tkinter root window
Tk().withdraw()

# Open file dialog to select CSV file
file_path = askopenfilename(title="Select CSV file", filetypes=[("CSV Files", "*.csv")])
if not file_path:
    print("No file selected.")
    exit()

# Load the CSV
df = pd.read_csv(file_path)

# Clean column names
df.columns = [col.strip() for col in df.columns]

# Ask user for category
category = input("Enter the Sector (e.g., IT, Pharma, Motor): ").strip()

# Match column name case-insensitively
matched_column = next((col for col in df.columns if col.lower() == category.lower()), None)

if matched_column:
    print(f"\nCompanies under '{matched_column}':")
    # Show non-empty values in the selected column
    print(df[matched_column].dropna().astype(str).str.strip().to_string(index=False))
else:
    print(f"\nInvalid category '{category}'. Available options are: {', '.join(df.columns)}")
