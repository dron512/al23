import RPi.GPIO as GPIO     # GPIO 라이브러리 가져오기
import time     # 시간 라이브러리 가져오기
from openpyxl import Workbook   #엑셀 라이브러리 가져오기
import datetime  # 날짜 시간 출력 라이브러리 가져오기
from flask import Flask  # flask 라이브러리 가져오기

app = Flask(__name__)   

wb = Workbook()  #엑셀 파일 생성
ws = wb.active  #엑셀 시트 활성화
# wb.create_sheet()

lpinnum = 27
bpinnum = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(lpinnum,GPIO.OUT)
GPIO.setup(bpinnum,GPIO.IN)

try:
    @app.route('/')
    def home():
        return 'Hello, World!'

    @app.route('/26/high')
    def high26():
        GPIO.output(lpinnum,1)
        return '26 high'

    @app.route('/26/low')
    def low26():
        GPIO.output(lpinnum,0)
        return '26 low'

    if __name__ == '__main__':
        app.run(debug=True)

#    while True:
#        i_value = GPIO.input(bpinnum)
#        print('button value = ',i_value)
#        time.sleep(0.2)
#        # openpyxl flask lib
#        if i_value == 1 :
#            ws.append(['buttonclicked','nowtime=',datetime.datetime.now()])

except KeyboardInterrupt:
    pass

wb.save('a.xlsx')  #엑셀에 저장
GPIO.cleanup()
