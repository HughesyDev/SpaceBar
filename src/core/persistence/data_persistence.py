import csv 

def save_data(filepath, data):
    try:
        with open(filepath, 'w', newline="") as csvfile:
            target_file = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
            for item in data:
                target_file.writerow([item])
    except Exception as err:
        print(f"Unable to save, error occurred displaying:\n>>> {err}")