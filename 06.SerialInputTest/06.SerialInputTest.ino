int val;
void setup() 
{
    Serial.begin(9600);
    Serial.println("Double it! (Input format: a,b,c,d,...)");
}

void loop() 
{
    while (Serial.available() > 0)
    {
        val = Serial.parseInt();
        Serial.println(val*2);
    }
    
}
