#include <stdio.h>
#include <wiringPi.h>

void main(){
    
    const int led_pin = 0;

    wiringPiSetup();

    pinMode(led_pin,OUTPUT);

    digitalWrite(led_pin,HIGH);

}
