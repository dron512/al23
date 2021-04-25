#include <stdio.h>
#include <wiringPi.h>

int main(){

    wiringPiSetup();

    pinMode(1,PWM_OUTPUT);

    while(1){
        // 0 ~ 1024 100만HIGH 101~1024까찌 LOW
        pwmWrite(1,1024);
    }

    return -1;
}
