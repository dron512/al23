from flask import Flask
from openpyxl import load_workbook
import RPi.GPIO

app = Flask(__name__)

@app.route('/')
def home():
    wb = load_workbook('a.xlsx')
    ws = wb.active
    ws.append(['url','called'])

    wb.save('modifieda.xlsx')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host="192.168.137.84", debug=True)
