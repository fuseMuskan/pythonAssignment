import csv
def create_csv_file():
    """This files read a file named "data.csv" and
    filters out name of the people having age greater than or equal
    to 18 and creates a new file names "adults.csv"
    """
    try:
        with open("./dataset/data.csv", "r") as fp1:
            csvFile = csv.reader(fp1)   # reading the csv file
            next(csvFile, None)         # Skip the headers
            with open("./dataset/adults.csv", "a") as fp2:
                fp2.writelines("Name, Age\n")
                for name, age in csvFile:
                    if int(age) >= 18:
                        fp2.writelines(f"{name}, {age}\n")
        print("File Created Successfully")
    except FileNotFoundError:
        print("File Not Found")

create_csv_file()

