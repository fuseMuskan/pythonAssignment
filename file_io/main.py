import csv
import json
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


def add_to_json(filename: str, new_player: dict) -> None:
    """This function takes in a JSON filename and new player name
    and updates the JSON with new player name

    Args:
        filename (str): filepath of the JSON file
        new_player (dict): key, value pair of the new player, {"name": age}
    """
    try:
        with open(filename, "r") as fp:
            datas = json.load(fp)
            for name, age in new_player.items():
                temp_dict = {"name":name, "age":age}
                datas.append(temp_dict)
            with open(filename, "w") as fp1:
                json.dump(datas, fp1)
    except:
        return "File Not Found"


