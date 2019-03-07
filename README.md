# Bateau-RC
Le but de ce projet est la fabrication d'un bateau radiocommandé avec un Arduino et Raspberry Pi

# Prerequis
Un Raspberry Pi 3 (emeteur)

Une Manette Usb ou bluetooth (ici un Dualshock 4)

Un arduino nano (recepteur)

Une coque de bateau

Des modules radio HC-12

Un servo moteur standart avec un gouvernaille et une tige metallique

Des moteurs brushed, arbres de transmission, helices, une lipo

Un ESC Newrain 480A pour moteur brushed

Pas male de fils pour les connections


# Le Montage Bateau
Partit la plus complexe du projet, amenagement de la coque.
![bateau](https://github.com/Arnaud-Della/Bateau-RC/blob/master/Images/20190306_182206.jpg)
![bateau2](https://github.com/Arnaud-Della/Bateau-RC/blob/master/Images/20190306_182149.jpg)
![bateau3](https://github.com/Arnaud-Della/Bateau-RC/blob/master/Images/20190306_182157.jpg)
Cette partie est propre a votre propre amenagement du bateau neanmoins elle necessite plusieurs essaie avant de trouver les bons emplacements.
Si tout c'est bien passer, que le gouvernaille tourne bien et que la transimission moteur/arbre fonctionne, on peut passer à la partie suivante ! :)

# Code
Regler le raspberry pour qu'il puisse communquer avec le module HC-12 par Rx Tx :

sudo raspi-config > interphaces > serial > no > yes

Installation librairies:

sudo pip2 install pygame

sudo apt-get install serial


# Branchement
Pour Module HC12-12:
HC-12 -> Raspberry

VCC -> 5v

Gnd -> Gnd

Rx -> Tx

Tx -> Rx

(le dernier pin n'est pas utiliser)

HC-12 -> Arduino

VCC -> 5v

Gnd -> Gnd

Rx -> Tx

Tx -> Rx

(le dernier pin n'est pas utiliser)


Pour ESC NewRain:

Signal (blanc)-> pin 4 arduino

+5V (rouge) -> vin arduino

Gnd (noir) -> Gnd arduino


Pour Servo:

Signal (blanc)-> pin 9 arduino

Vcc (rouge) -> +5V arduino

Gnd (noir) -> Gnd arduino


