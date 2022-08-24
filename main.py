from correction_csv import CorrectCSV


if __name__ == "__main__":
    corr_csv = CorrectCSV()
    corr_csv.formate_csv("phonebook_raw.csv", "phonebook.csv")
