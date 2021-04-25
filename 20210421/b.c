#include <stdio.h>
#include <wiringPi.h>

int main(){

    const int outpin = 2;
    const int inpin = 0;

    wiringPiSetup();

    pinMode(outpin,OUTPUT);
    pinMode(inpin,INPUT);

    while (1){
        int inRead = digitalRead(inpin);
        printf("inRead = %d\n",inRead);
        if(inRead == 1){
            digitalWrite(outpin,HIGH);
        }
        else{
            digitalWrite(outpin,LOW);
        }
        delay(200);
    }

    return 0;
}
