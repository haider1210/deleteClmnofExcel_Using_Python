import pandas as pd

# Load the Excel file
file_path = 'path_to_your_file.xlsx'
sheet_name = 'Sheet1'  # Specify the sheet name if necessary

# Read the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Specify the columns to keep
columns_to_keep = ['Vmname', 'Status']

# Retain only the specified columns
df_filtered = df[columns_to_keep]

# Save the resulting DataFrame back to an Excel file
output_file_path = 'filtered_output.xlsx'
df_filtered.to_excel(output_file_path, index=False)

print(f"Filtered Excel file saved to {output_file_path}")
