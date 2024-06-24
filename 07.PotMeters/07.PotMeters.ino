void setup() 
{
    Serial.begin(9600);
}

void loop() 
{
    int pot1Val = analogRead(A0);
    int pot2Val = analogRead(A1);
    while (!Serial){};
    Serial.print(pot1Val); Serial.print(",");
    Serial.print(pot2Val); Serial.println();
    delay(200);
}
