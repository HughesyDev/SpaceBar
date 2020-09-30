import csv

ETL_CSV_FILEPATH = 'dbtesting/Import_User_Sample_en.csv'

testdata = []

def load_csv():
    global testdata
    try:
        with open(ETL_CSV_FILEPATH, "r") as test_csv: 
            testdata = test_csv.read().splitlines()
    
    except Exception as e:
        print(f"Exception raised with the following error:\n {e}")

print(testdata)