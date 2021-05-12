from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws
ws["A1"].value = "test"
wb.save("a.xlsx")