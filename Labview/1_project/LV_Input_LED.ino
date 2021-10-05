#define Re_I1 5
#define Re_I2 4
#define Re_U1 3
#define Re_U2 2
#define Re_1 9
#define Re_2 8
#define Re_3 7
#define Re_4 6

int cmd=0;
void setup() {
   pinMode(Re_I1, OUTPUT);
   pinMode(Re_I2, OUTPUT);
   pinMode(Re_U1, OUTPUT);
   pinMode(Re_U2, OUTPUT);
   pinMode(Re_1, OUTPUT);
   pinMode(Re_2, OUTPUT);
   pinMode(Re_3, OUTPUT);
   pinMode(Re_4, OUTPUT);

   Serial.begin(9600);
}

void loop() {
   if (Serial.available() > 0)
  {
    cmd=Serial.read();
    if(cmd==49){ //dec=49-56 chr=1-8
      digitalWrite(Re_I1, HIGH);
      digitalWrite(Re_I2, HIGH);
      digitalWrite(Re_U1, HIGH);
      digitalWrite(Re_U2, HIGH);
      digitalWrite(Re_1, LOW);
      digitalWrite(Re_2, LOW);
      digitalWrite(Re_3, LOW);
      digitalWrite(Re_4, LOW);
    }
    
    if(cmd==50){
      digitalWrite(Re_I1, HIGH);
      digitalWrite(Re_I2, HIGH);
      digitalWrite(Re_U1, HIGH);
      digitalWrite(Re_U2, HIGH);
      digitalWrite(Re_1, HIGH);
      digitalWrite(Re_2, LOW);
      digitalWrite(Re_3, LOW);
      digitalWrite(Re_4, HIGH);
    }
    
    if(cmd==51){
      digitalWrite(Re_I1, HIGH);
      digitalWrite(Re_I2, HIGH);
      digitalWrite(Re_U1, HIGH);
      digitalWrite(Re_U2, HIGH);
      digitalWrite(Re_1, HIGH);
      digitalWrite(Re_2, HIGH);
      digitalWrite(Re_3, HIGH);
      digitalWrite(Re_4, HIGH);
    }
    
     if(cmd==52){
      digitalWrite(Re_I1, HIGH);
      digitalWrite(Re_I2, HIGH);
      digitalWrite(Re_U1, HIGH);
      digitalWrite(Re_U2, HIGH);
      digitalWrite(Re_1, LOW);
      digitalWrite(Re_2, HIGH);
      digitalWrite(Re_3, HIGH);
      digitalWrite(Re_4, LOW);
    }
     if(cmd==53){
      digitalWrite(Re_I1, LOW);
      digitalWrite(Re_I2, LOW);
      digitalWrite(Re_U1, LOW);
      digitalWrite(Re_U2, LOW);
      digitalWrite(Re_1, LOW);
      digitalWrite(Re_2, LOW);
      digitalWrite(Re_3, LOW);
      digitalWrite(Re_4, LOW);
    }
     if(cmd==54){
      digitalWrite(Re_I1, LOW);
      digitalWrite(Re_I2, LOW);
      digitalWrite(Re_U1, LOW);
      digitalWrite(Re_U2, LOW);
      digitalWrite(Re_1, HIGH);
      digitalWrite(Re_2, LOW);
      digitalWrite(Re_3, LOW);
      digitalWrite(Re_4, HIGH);
    }
     if(cmd==55){
      digitalWrite(Re_I1, LOW);
      digitalWrite(Re_I2, LOW);
      digitalWrite(Re_U1, LOW);
      digitalWrite(Re_U2, LOW);
      digitalWrite(Re_1, HIGH);
      digitalWrite(Re_2, HIGH);
      digitalWrite(Re_3, HIGH);
      digitalWrite(Re_4, HIGH);
    }
     if(cmd==56){
      digitalWrite(Re_I1, LOW);
      digitalWrite(Re_I2, LOW);
      digitalWrite(Re_U1, LOW);
      digitalWrite(Re_U2, LOW);
      digitalWrite(Re_1, LOW);
      digitalWrite(Re_2, HIGH);
      digitalWrite(Re_3, HIGH);
      digitalWrite(Re_4, LOW);
    }
  }
}
