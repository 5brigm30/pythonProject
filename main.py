import csv

file_path = "titanic.csv"

records = []

print("Loading data...", end="")

try:
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)

    print("Done!")
    print(f"Successfully loaded {len(records)} records.")

except IOError:
    print("Could not read the file.")
