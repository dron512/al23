#include <stdio.h>
#include <wiringPi.h>

void main(){
    /*
        주파수...
        19.2MHZ 기본 주파수 대역..
        클럭수..
        1초마다 Hz
    */   
    //pin 번호 초기화
    wiringPiSetup();
    const int pinNum1 = 0;
    const int pinNum2 = 1;
    pinMode(pinNum1,OUTPUT);
    pinMode(pinNum2,OUTPUT);

    /*
       int 형으로 n의 값을 입력받아 
       1 입력 받으면 LED 1번 켜고
       2 입력 받으면 LED 1번 끄고
       3 입력 받으면 LED 2번 켜고
       4 입력 받으면 LED 2번 끄도록 합시다.
    */
    while(1){
        int a=0;
        printf("a 값입력\n");
        scanf("%d",&a);
        printf("a = %d\n",a);
        if (a ==1){
            digitalWrite(pinNum1,HIGH);
        }
        else if(a ==2){
            digitalWrite(pinNum1,LOW);
        }
        else if(a ==3){
            digitalWrite(pinNum2,HIGH);
        }
        else if(a ==4){
            digitalWrite(pinNum2,LOW);
        }
    }
}
