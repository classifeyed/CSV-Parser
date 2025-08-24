# CSV-Parser

Project was intended to use as a CSV parser for security events. In particular identity based activity. 
- Tested against 345 x 75 CSV file.
- Column names = Field Names, build output query 

Currently has 
- Auto-removal of columns with no data.
- Menu based selection for columns that have data.
  - Selected field names appended to list.
  - Script will show the first 5 and last 5 time stamp entries that contains the data.
  
Need to implment the following
- Better field selection
- Adding time range to data.
- Output to CSV?
