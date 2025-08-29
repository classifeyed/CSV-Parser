import pandas as pd
print("="*100)
print("="*100)
try:
    import openpyxl
except ImportError:
    print("openpyxl is not installed. Installing now...")
import subprocess, sys
import importlib

print("Checking for openpyxl package...")
print("If not installed, it will be installed now.")
print("="*100)
print("="*100)

print("Importing openpyxl package...")
openpyxl = importlib.import_module("openpyxl")

# Function to install packages
subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"]) 

# === Load in Data ===
df = pd.read_csv("UPDATE_ME")
print("="*100)

print("First 5 and Last 5 rows of file: ")
print("Data Loaded successfully from file", "\n", df.tail(), df.head())

print("="*100)

# === Global lists to track selected and valid columns ===

empty_columns = []
selected_columns = []
event_id_search = [4634, 4624, 4672, 4616, 4662, 4769, 4768, 4799, 4648, 4776, 4771]

print("Cleaning columns...")
print("Removing empty columns...")

print("="*100)
print("="*100)

# === Function to clean NaN columns and standardize column names ===
def columns():
    empty_cols = [col for col in df.columns if df[col].isna().all()] # Identify completely empty columns
    cleaned = df.drop(columns=empty_cols) # Drop completely empty columns
    print("Columns cleaned: ", len(empty_cols))
    print("Dropped empty columns: ", empty_cols) # Print the names of dropped columns
    print("="*100)
    print("="*100)
    return cleaned


# === Function to pull out data ===
def rows():
    df_clean = columns()  # Drop rows where all elements are NaN
    for index, row in df_clean.iterrows():
        non_empty = row.dropna(how='all')  # Drop NaN values in the row
        print(f"Row {index} non-empty values:\n{non_empty}\n")
        print(non_empty.to_dict())  # Print as dictionary for clarity
        print("="*50)

# === For loop it iteraite through event_id_search to create individual sheets ===
def event_id_sheets(event_id_search):
    df_clean = columns()  # clean inside the function
    print("Creating Excel file with Event ID sheets...")
    with pd.ExcelWriter("Event_IDs.xlsx", engine="openpyxl") as writer:
        for event_id in event_id_search:
            df_event = df_clean[df_clean['Event ID'] == event_id]
            print(f"Dropping empty columns inside sheets for Event ID: {event_id}")
            df_event = df_event.dropna(axis=1, how='all')
            df_event = df_event.apply(
                lambda col: col.str.replace('-', '') if col.dtype == 'object' else col
            )
            if not df_event.empty:
                df_event.to_excel(writer, sheet_name=f"Event_{event_id}", index=False)
                print("="*50)
                print(f"Added sheet: Event_{event_id} with {len(df_event)} records.")
            else:
                print(f"No records found for Event ID: {event_id}")
event_id_sheets(event_id_search)
print("="*100)


