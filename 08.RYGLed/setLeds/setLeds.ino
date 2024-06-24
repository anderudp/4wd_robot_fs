int redPin = 3;
int yellowPin = 5;
int greenPin = 6;

int r = 0;
int y = 0;
int g = 0;

void setup() 
{
    Serial.begin(9600);
    pinMode(redPin, OUTPUT);
    pinMode(yellowPin, OUTPUT);
    pinMode(greenPin, OUTPUT);
}

void loop() 
{
    while(!Serial){};
    if(Serial.available() > 0)
    {
        r = Serial.parseInt();
        y = Serial.parseInt();
        g = Serial.parseInt();
    }
    Serial.print(r);Serial.print(","); Serial.print(y);Serial.print(","); Serial.print(g);Serial.println(); 
    analogWrite(redPin, r);
    analogWrite(yellowPin, y);
    analogWrite(greenPin, g);
}
