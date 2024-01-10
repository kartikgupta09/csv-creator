# csv-creator
Python script to convert JSON data to CSV.

The script uses a singleton design pattern to ensure only one instance of the converter is created. The converter takes a dictionary of data and a list of columns to keep, flattens the JSON data, and writes the specified columns to a CSV file. The script includes error handling for invalid data types and issues with file writing.
