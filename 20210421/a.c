#include <stdio.h>
#include <wiringPi.h>

int main(){
    int buzpin = 1;

    wiringPiSetup();
    // 1번 pin을 pwm output 설정
    pinMode(buzpin,PWM_OUTPUT);
    int arr[] = {262, 294, 330, 349, 392, 440, 494, 523};

    // 19.2MHz 19로 나누어서 1000000Mhz 설정
    pwmSetClock(19);
    pwmSetMode(PWM_MODE_MS);
    for ( int i =0; i< sizeof(arr)/sizeof(int); i++){
        // 1초에 262 번 262Hz 설정
        pwmSetRange(1000000/arr[i]);
        // 262Hz 중에 50% High 설정
        pwmWrite(buzpin,1000000/arr[i]/2);
        delay(1000);
    }
    pwmWrite(buzpin,0);

    return 0;
}
