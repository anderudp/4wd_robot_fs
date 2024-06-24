int LedPwmPin = 11;
int LedDelay = 5;
int intensity = 0;
void setup()
{
    pinMode(LedPwmPin, OUTPUT);
}

void loop() 
{
    while(intensity < 255) 
    {
        analogWrite(LedPwmPin, intensity);
        intensity++;
        delay(LedDelay);
    }
    while (intensity > 0)
    {
        analogWrite(LedPwmPin, intensity);
        intensity--;
        delay(LedDelay);
    }
}
