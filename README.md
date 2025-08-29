---

# CSV Event Log Parser

This project parses Windows Event Log CSV exports and organizes them into individual Excel sheets by **Event ID**. The script also cleans the data by removing completely empty columns and replacing dashes (`-`) with spaces in text fields.

---

## Features

* ✅ Removes fully empty columns from the dataset
* ✅ Creates a **multi-sheet Excel file** (`Event_IDs.xlsx`) with one sheet per Event ID
* ✅ Supports custom **Event ID lists** for targeted parsing
* ✅ Cleans text by replacing `-` with spaces for readability
* ✅ Auto-installs required dependencies (`openpyxl`) if not already installed

---

## Requirements

* Python **3.10+**
* [pandas](https://pandas.pydata.org/)
* [openpyxl](https://openpyxl.readthedocs.io/) (automatically installed if missing)

---

## Installation

Clone the repo:

```bash
git clone https://github.com/classifeyed/csv-event-parser.git
cd csv-event-parser
```

Install dependencies manually (if needed):

```bash
pip install pandas openpyxl
```

Or just run the script — it will install `openpyxl` automatically if it’s missing.

---

## Usage

1. Place your exported CSV file (e.g., `your_csv_file.csv`) in the project folder.
2. Update the script with your list of **Event IDs**:

```python
event_id_search = [4634, 4624, 4672, 4616, 4662, 4769, 4768, 4799, 4648, 4776, 4771]
```

3. Run the script:

```bash
python csv_parser.py
```

4. Output:

* A single Excel file: **`Event_IDs.xlsx`**
* Each sheet corresponds to an Event ID (e.g., `Event_4624`, `Event_4634`, etc.)
* Cleaned columns (empty ones removed, dashes replaced with spaces)

---

## Example Output

```
Creating Excel file with Event ID sheets...
Dropping empty columns inside sheets for Event ID: 4624
==================================================
Added sheet: Event_4624 with 120 records.
Dropping empty columns inside sheets for Event ID: 4634
==================================================
Added sheet: Event_4634 with 45 records.
...
```
