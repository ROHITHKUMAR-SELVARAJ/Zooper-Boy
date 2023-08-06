import wiringpi as wiringpi
import pyttsx3
from time import sleep
engine=pyttsx3.init()
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(8, 0)
count=0
while(count<100):
 my_input=wiringpi.digitalRead(8)
 if(my_input):
  print("Not Detected !")
  engine.say("Enjoy your food")
  engine.runAndWait()
 #  break
 else:
  print("Alcohol Detected")
  engine.say("Food is contaminated")
  engine.runAndWait()
 count=count+1
sleep(1)
