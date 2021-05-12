#include <stdio.h>
#include <wiringPi.h>

int main(){

    wiringPiSetup();
    const int servo_pin = 1;

    pinMode(servo_pin, PWM_OUTPUT);

    pwmSetClock(19);    // 기본 클럭이 32인데 19로 설정
    pwmSetMode(PWM_MODE_MS);
    pwmSetRange(20000); // 50Hz 설정

    // 0도로 이동합니다.
    pwmWrite(servo_pin,600);
    delay(1);

    // 0 도에서 180도로 이동하면서 딜레이를 0.02초로 설정합니다.
    while(1){
        for (int i =600; i<=2500;i++){
            pwmWrite(servo_pin,i);
            delay(2);
        }
        for (int i =2500; i>=600;i--){
            pwmWrite(servo_pin,i);
            delay(2);
        }
    }

    pwmWrite(servo_pin,600);
    delay(1);

    pwmWrite(servo_pin,0);
    return 0;
}