int moistPin = 0;
int moistVal = 0;
#define lightSensor A2
int incomingByte;
bool redFlag = false;

void setup()
{
  Serial.begin(115200);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}
void loop()
{
  {
    
    moistVal = analogRead(moistPin);
    int percent = 2.718282 * 2.718282 * (.008985 * moistVal + 0.207762); 
    Serial.print(percent);
    Serial.println("% Moisture ");

    int Light = analogRead(lightSensor);
    Serial.print(Light);
    Serial.println("% Light Absorbed ");
    
    delay(1000);

    incomingByte = Serial.read();
    if (incomingByte = 84){
      digitalWrite(12, LOW);
      digitalWrite(13, HIGH);
      }

     if (incomingByte != 84){
      digitalWrite(12, HIGH);
      digitalWrite(13, LOW);
      }

    
    }
    
    
   }
  
  



  
