// State change detection program

// pins definition:
const int  pirOutputPin = 2;    // PIR output pin

// state variables:
int detectionCounter = 0;    // counter for the number of move detection
int pirOutputState = 0;      // current state of PIR output
int lastPirState = 0;        // previous state of PIR output

void setup() {
  pinMode(pirOutputPin, INPUT);
  Serial.begin(9600);
}


void loop() {
  // read the PIR signal input pin:
  pirOutputState = digitalRead(pirOutputPin);

  if (pirOutputState != lastPirState) {
    if (pirOutputState == HIGH) {
      detectionCounter++;
      Serial.println(detectionCounter);
    }
    delay(100);
  }
  lastPirState = pirOutputState;
}
