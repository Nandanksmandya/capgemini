import xlrd
from Tools.scripts.var_access_benchmark import C

from Library.configure import Configuration


class ReadExcel:
    def chage_theme_locators(self):
        path = Configuration.LOCATORS_PATH
        wb = xlrd.open_workbook(path)
        ws = wb.sheet_by_name(Configuration.SHEETNAME_LOCATORS)
        rows = ws.get_rows()
        header = next(rows)
        data = {}
        for row in rows:
            data[row[0].value] = (row[1].value, row[2].value)
        return data

    def login_details(self):
        path = Configuration.LOCATORS_PATH
        wb = xlrd.open_workbook(path)
        ws = wb.sheet_by_name(Configuration.SHEETNAME_DATA)
        rows = ws.get_rows()
        header = next(rows)
        l_ = []
        for row in rows:
            l_.append((row[0].value, row[1].value, row[2].value, row[3].value, row[4].value))

        return l_

    def mute_login_details(self):
        path = Configuration.LOCATORS_PATH
        wb = xlrd.open_workbook(path)
        ws = wb.sheet_by_name(Configuration.MUTE_LOGIN_DATA)
        rows = ws.get_rows()
        header = next(rows)
        l_ = []
        for row in rows:
            l_.append((row[0].value, row[1].value))

        return l_


# //div[text()='Doctor Strange']/..

# r = ReadExcel()
# data = r.mute_login_details()
# print(data)
# loc_name, loc_value = data["select_theme"]
#
# print(loc_value.format("Doctor strange"))
