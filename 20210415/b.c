#include <stdio.h>
#include <wiringPi.h>

// cltr + ` 터미널 열기
int main(){
    int led_pin = 1;

    wiringPiSetup();

    pwmSetClock(19);
    pwmSetMode(PWM_MODE_MS);
    pwmSetRange(1000000/10);

    while(1){
        pwmWrite(led_pin,1000000/2/10);
    }

    return -1;
}