import re

from py_to_csv import open_csv, write_csv
import patterns


class CorrectCSV:
    """Класс для исправления файла .csv"""
    def __init__(self):
        self.pattern_phone = patterns.phone
        self.pattern_common = patterns.common

    def _get_contact_str(self, contact_l=list):
        """Принимает на вход список контактов и передаёт на выход в виде строки"""
        cont_str = ""
        for q in contact_l:
            cont_str += ",".join(q) + "\n"
        return cont_str

    def _format_list_contact(self, list_com, h_row):
        """Принимает на вход список список и строку заголовок
         и передаёт на выход отформатированный"""
        list_corr = [h_row]

        while len(list_com) > 0:
            row_check = list_com.pop(0)
            row_res = ['', '', '', '', '', '', '']

            for n, row in enumerate(list_com):
                if row_check[0] == row[0] and row_check[1] == row[1]:
                    row_ = list_com.pop(n)
                    row_res = self._unite_rows(row_, row_res)

            row_result = self._unite_rows(row_res, row_check)
            row_result[5] = self._format_number_phone(row_result[5])

            list_corr.append(row_result)

        return list_corr

    def _format_number_phone(self, number_phone=str):
        """Принимает на строку номера телефона и передаёт на выход отформатированную"""
        num_match = re.match(patterns.phone, number_phone)
        if not num_match.group(2):
            return
        num_str = num_match.group(2) + num_match.group(3) + num_match.group(4) + num_match.group(5)
        num_res = f'+7({num_str[:3]}){num_str[3:6]}-{num_str[6:8]}-{num_str[8:]}'
        if num_match.group(6):
            num_res += f' доб.{num_match.group(6)}'
        return num_res

    def _unite_rows(self, row1=list or tuple, row2=list or tuple):
        """Получает на вход два кортежа, сравнивает и передаёт объединённый список на выход"""
        row_united = [
            row1[0] or row2[0],
            row1[1] or row2[1],
            row1[2] or row2[2],
            row1[3] or row2[3],
            row1[4] or row2[4],
            row1[5] or row2[5],
            row1[6] or row2[6]
        ]
        return row_united

    def formate_csv(self, wrong_csv=".csv", correct_csv=".csv"):
        """Принимает на вход некоррестный файл csv и файл csv для записи,
        в который записывает исправленный"""
        wrong_csv = wrong_csv
        correct_csv = correct_csv

        contact_list = open_csv(wrong_csv)

        head_row = contact_list.pop(0)
        contact_str = self._get_contact_str(contact_list)

        list_contacts_re = re.findall(patterns.common, contact_str)
        list_corrected = self._format_list_contact(list_contacts_re, head_row)

        write_csv(list_corrected, correct_csv)
