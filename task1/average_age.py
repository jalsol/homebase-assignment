import csv

INPUT_CSV_FILE = 'data.csv'
DELIMITER = ','

def calculate_average_age():
    with open(INPUT_CSV_FILE, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=DELIMITER)
        ages = []

        for index, row in enumerate(reader):
            # +1 to account for header row
            # +1 to account for 0-indexing
            row_index = index + 2

            try:
                age_str = row['Age']
                ages.append(int(age_str))
            except KeyError:
                print(f'Cannot access key from row (row {row_index}): Age="{row}"')
                print('Stopping...')
                return
            except ValueError:
                print(f'Invalid age (row {row_index}): Age="{age_str}", skipping...')
                continue

    if not ages:
        print('No valid ages found')
    else:
        average_age = sum(ages) / len(ages)
        print(f'Average age: {average_age}')

if __name__ == '__main__':
    calculate_average_age()