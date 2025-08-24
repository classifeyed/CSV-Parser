import pandas as pd

df = pd.read_csv("Attack_Scenario.csv")
print("="*100)
print("="*100)
print("First 5 and last 5 rows of file:")
print("Data loaded successfully from file", df.head())
print("="*100)
print("="*100)
# print(df.head())
# print(df.columns)

selected_columns = []
valid_columns = []

def columns():
    empty_cols = [col for col in df.columns if df[col].isna().all()] # Identify completely empty columns
    # num_dropped = len(empty_cols) # Count of empty columns
    cleaned = df.drop(columns=empty_cols) # Drop completely empty columns
    cleaned_count = len(cleaned)
    # print("Removed NaN Column Count: ", num_dropped) # Print the count of removed columns
    # print("Dropped empty columns: ", empty_cols) # Print the names of dropped columns
    # print("Column headers count:", cleaned_count) # Print the count of remaining columns
    # print("Columns in the DataFrame: ", cleaned.columns.tolist()) # Print remaining columns
    cleaned.columns = [col.lower().replace(" ", ".") for col in cleaned.columns]
    return cleaned
columns()
print("="*100)

# Function to count occurrences in a specified column
def count():
    df_clean = columns()

    while True:
        print("You can count occurrences in any column of the file")
        print("="*100)
        print("Available columns are: ", df_clean.columns.tolist())
        print("="*100)

        column_to_count = input("Which column would you like to count? (seperate with commas)")
        column_list = [col.strip() for col in column_to_count.split(",")]
        for col in column_list:
            if col in df_clean.columns:
                valid_columns.append(col)
            else:
                print(f"Column '{col}' does not exist, this will be ignored.")
        print("Valid columns to count: ", valid_columns)
        if column_to_count not in selected_columns:
            selected_columns.append(column_to_count)
            print("Selected Columns: ", selected_columns)
        elif column_to_count in df_clean.columns:
            counts = df_clean[column_to_count].value_counts()
            print(f"Count for column: '{column_to_count}':\n", counts)
            print("="*100)
        else:
            print(f"Column '{column_to_count}' does not exist in the DataFrame. Please choose from the available columns.")
            break
        choice = input("Would you like to count another column? (yes/no): ").strip().lower()
        if choice in ['no' or "n"]:
            print("Exiting the column counting tool.")
            break

        
        
count()


print("="*100)


# Function to analyze the 'date.and.time' column
def time():
    df_clean = columns()
    # print(df_clean["date.and.time"].head())
    df_clean["date.and.time"] = pd.to_datetime(df_clean["date.and.time"]) # Convert to datetime
    earliest_event = df_clean["date.and.time"].min()
    print("Earliest Event Timestamp: ", earliest_event)
    latest_event = df_clean["date.and.time"].max()
    print("Latest Event Timestamp: ", latest_event)
    duration = df_clean["date.and.time"].max() - df_clean["date.and.time"].min()
    print("Duration Between Earliest and Latest Event: ", duration)
    df_clean_sorted = df_clean.sort_values("date.and.time")
    # print("Sorted DataFrame by 'date.and.time':\n", df_clean_sorted[["date.and.time"]].head())
time()

# Function to create a timeline of events
def timeline():
    df_clean = columns()
    df_sorted = df_clean.sort_values("date.and.time")
    df_story = df_sorted[["date.and.time"] + selected_columns]
    print(df_story.head(20))
timeline()
print("="*100)