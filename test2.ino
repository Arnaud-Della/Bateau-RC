#include <Time.h>
#include <TimeLib.h>
#include <Servo.h>
#include <SoftwareSerial.h>



#define MIN_PULSE_LENGTH 1000 // Minimum pulse length in µs
#define MAX_PULSE_LENGTH 2000 // Maximum pulse length in µs

Servo motA;
Servo servo;
SoftwareSerial HC12(10, 11);
int long t=0;
int long nombreEnCours = 0;

void setup() {
    Serial.begin(9600);
    servo.attach(9);
    motA.attach(4, MIN_PULSE_LENGTH, MAX_PULSE_LENGTH);
    motA.writeMicroseconds(1500);
    servo.write(90);
    while(!Serial.available()){
    }
}


void loop() {
 
    // Si un caractère est disponible
    if ( Serial.available() ) {
     
        // On lit ce caractère
        char c = Serial.read();
         
        // Si c'est un chiffre, on l'ajoute au nombre
        if ( ( c >= '0' ) && ( c <= '9' ) ) {
            nombreEnCours = ( ( nombreEnCours * 10 ) + ( c - '0' ) );
        }
         
        // Si c'est une lettre majuscule, alors on fait une action
        if ( ( c >= 'A' ) && ( c <= 'Z' ) ) {
             
            // Pour un 'A', on affiche un texte
            if ( c == 'A' ) {
                /*Serial.print("Le nombre ");
                Serial.print(nombreEnCours);
                Serial.println(" vient d'etre envoyer.");*/
                motA.writeMicroseconds(nombreEnCours);
                delay(50);
            }
            if ( c == 'B' ) {
                /*Serial.print("Le nombre ");
                Serial.print(nombreEnCours);
                Serial.println(" vient d'etre envoyer.");*/
                servo.write(nombreEnCours);
                delay(50);
            }

            nombreEnCours = 0;
         
        }
     
    }
    else{
      t=now()+2;
      while(!Serial.available()){
        if (now()>t){
          motA.writeMicroseconds(1500);
          servo.write(0);
        }
      }
    }
          
        
     
}
