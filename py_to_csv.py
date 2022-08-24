import csv


def open_csv(file):
    """Выгружает данные из csv"""
    with open(file, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def write_csv(contacts_list, file):
    """Записывает отформатированные данные в новый csv"""
    with open(file, "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',', lineterminator='\n')
        datawriter.writerows(contacts_list)
