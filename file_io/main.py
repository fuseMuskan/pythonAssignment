"""This module consist of three functions one to create a 
csv file, to update a json file and to search keyword from a log file"""
import csv
import json
def create_csv_file():
    """This files read a file named "data.csv" and
    filters out name of the people having age greater than or equal
    to 18 and creates a new file names "adults.csv"
    """
    try:
        with open("./dataset/data.csv", "r", encoding="utf-8") as file_pointer_one:
            csv_file = csv.reader(file_pointer_one)   # reading the csv file
            next(csv_file, None)         # Skip the headers
            with open("./dataset/adults.csv", "a", encoding="utf-8") as file_pointer_two:
                file_pointer_two.writelines("Name, Age\n")
                for name, age in csv_file:
                    if int(age) >= 18:
                        file_pointer_two.writelines(f"{name}, {age}\n")
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
        with open(filename, "r", encoding="utf-8") as file_pointer:
            datas = json.load(file_pointer)
            for name, age in new_player.items():
                temp_dict = {"name":name, "age":age}
                datas.append(temp_dict)
            with open(filename, "w", encoding="utf-8") as file_pointer_one:
                json.dump(datas, file_pointer_one)
    except FileNotFoundError:
        print("File Not Found")

def search_log(log_file_path: str, search_keyword: str):
    """Searches for lines containing the search keyword in the log file.

    Args:
        LOG_FILE_PATH (str): The path to the log file.
        SEARCH_KEYWORD (str): The keyword to search for in the log.

    Returns:
        None
    """

    try:
        with open(log_file_path, 'r', encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                if search_keyword in line:
                    print(f"Line {line_number}: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: The log file '{LOG_FILE_PATH}' was not found.")

LOG_FILE_PATH = "./dataset/sample_log.log"
SEARCH_KEYWORD = "INFO"
search_log(LOG_FILE_PATH, SEARCH_KEYWORD)
