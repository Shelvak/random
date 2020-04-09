//Sensores
int ArribaTrigger = A0;
int ArribaEcho = A1;
int AbajoTrigger = A0;
int AbajoEcho = A1;

long ArribaDistance, AbajoDistance;

int delaymili = 500;
int maximumRangeCm = 100;
int minimumRangeCm = 0;


//Leds
int led0=0;
int led1=1;
int led2=2;
int led3=3;
int led4=4;
int led5=5;
int led6=6;
int led7=7;
int led8=8;
int led9=9;
int led10=10;
int led11=11;
int led12=12;
int led13=13;
int leds[14] = {
  led0, led1, led2, led3, led4, led5,
  led6, led7, led8, led9, led10, led11,
  led12, led13
};

//Configs
int serialBSP = 9600;
int ledQuantityOn=4;

//sound functions
void initTrigger() {
	digitalWrite(ArribaTrigger, LOW);
	digitalWrite(AbajoTrigger, LOW);
	delayMicroseconds(2);
	digitalWrite(ArribaTrigger, HIGH);
	digitalWrite(AbajoTrigger, HIGH);
	delayMicroseconds(10);
	digitalWrite(ArribaTrigger, LOW);
	digitalWrite(AbajoTrigger, LOW);
}
long microsecCm(long microsecond) {
	return microsecond / 58;
}

//Configuramos los led como salida en bajo.
void initLedsInLowMode() {
  for (int i=0; i <= 13; i += 1) {
    pinMode(leds[i],OUTPUT);
  }
}

void turnOffAllLeds() {
  for (int i=0; i <= 13; i += 1) {
    digitalWrite(leds[i],LOW);
  }
}

void turnOnLed(int ledNumber) {
  digitalWrite(leds[ledNumber], HIGH);
  Serial.print("Poniendo en alto ");
  Serial.print(ledNumber);
  Serial.print("\n");
}

void turnOffLed(int ledNumber) {
  digitalWrite(leds[ledNumber], LOW);
  Serial.print("Poniendo en bajo ");
  Serial.print(ledNumber);
  Serial.print("\n");
}



void turnOnFromLedIncreasing(int ledNumber) {
  int x = ledNumber;
  for (x; x < (ledNumber + ledQuantityOn); x=x+1) {
    Serial.print("iterando en ");
    Serial.print(x);
    Serial.print("\n");
    if (x <= 13) {
      turnOnLed(x);
    }

    if (x-4 >= 0) {
      turnOffLed(x-4);
    }
  }
}

void turnOnFromLedDecrementing(int ledNumber) {
  for (int x=ledNumber; x > (ledNumber - ledQuantityOn); x=x-1) {
    if (x > 0) {
      turnOnLed(x);
    }

    if (x+4 <= 13) {
      turnOffLed(x+4);
    }
  }
}


void setup() {
  Serial.begin(serialBSP);

  pinMode(ArribaTrigger,OUTPUT);
  pinMode(ArribaEcho,INPUT);
  pinMode(AbajoTrigger,OUTPUT);
  pinMode(AbajoEcho,INPUT);

  initLedsInLowMode();
  turnOffAllLeds();
}


void loop() {
  turnOffAllLeds();
	initTrigger();

	ArribaDistance = microsecCm(pulseIn(ArribaEcho, HIGH));
	AbajoDistance = microsecCm(pulseIn(AbajoEcho, HIGH));

  Serial.print("Arriva y abajo ");
  Serial.print(ArribaDistance);
  Serial.print("cm ");
  Serial.print(AbajoDistance);
  Serial.print("cm \n");

  for (int x = 0 ; x <= 13 ; x=x+1) {
    if (ArribaDistance <= maximumRangeCm || minimumRangeCm < ArribaDistance) {
      Serial.print("Recorriendo globalmente ");
      Serial.print(x);
      Serial.print("\n");
      turnOnFromLedIncreasing(x);
      delay(1000);
    } else {
      break;
    }
  }

  turnOffAllLeds();

	for (int x = 13 ; x >= 0 ; x=x-1) {
    if (AbajoDistance <= maximumRangeCm || minimumRangeCm < AbajoDistance) {
      Serial.print("Recorriendo globalmente ");
      Serial.print(x);
      Serial.print("\n");
      turnOnFromLedDecrementing(x);
      delay(1000);
    } else {
      break;
    }
  }

  delay(500);
}
