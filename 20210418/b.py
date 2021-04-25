import RPi.GPIO as GPIO
from openpyxl import Workbook
import datetime
wb = Workbook()
ws = wb.active

ws.append(['a','buttonPressed',datetime.datetime.now()]);

wb.save("a.xlsx")
