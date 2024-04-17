import gspread
from gspread import Client, Worksheet, Spreadsheet

SPREADSHEET_URL = 'https://docs.google.com/spreadsheets/d/1N0HdxzTdMTKxDAV_8EFgIVBESw5qB6Kzx7gzf4JnYq8/edit#gid=0'


def get_names(ws: Worksheet):
    list_of_lists = ws.get_all_values()
    names = []
    for name in list_of_lists:
        names.append(name[0])
    return names


gc: Client = gspread.service_account("ПУТЬ К JSON ФАЙЛУ")
sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)
ws = sh.get_worksheet(0)
names = get_names(ws)
marks = [[[] for _ in range(20)] for _ in range(12)]
for i in range(12):
    ws = sh.get_worksheet(i)
    list_of_lists = ws.get_all_values()
    for k in range(len(list_of_lists)):
        for j in range(1, len(list_of_lists[k])):
            if list_of_lists[k][j] != '':
                marks[i][k].append(int(list_of_lists[k][j]))
