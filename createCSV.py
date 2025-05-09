import csv

# Data that we want to write into the CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"],
    ["David", 28, "Miami"]
]

# Specify the file name
file_name = "people_data.csv"

# Writing the data to the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write each row from the data list
    for row in data:
        writer.writerow(row)

print(f"CSV file '{file_name}' has been created and populated.")