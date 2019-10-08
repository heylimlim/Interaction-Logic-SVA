int speakerPin = 10;
const int fsrPin = A0;
int fsrReading;
void setup(void) {
 Serial.begin(9600);
 pinMode(speakerPin, OUTPUT);
}
void loop(void) {
 fsrReading = analogRead(fsrPin);
 Serial.println(fsrReading);
 delay(10); if (fsrReading >=834) {
   long frequency = 300;
   tone(speakerPin, frequency );
   //delay(200);
   noTone(speakerPin);
//delay(100);
}}