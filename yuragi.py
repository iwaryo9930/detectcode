import RPi.GPIO as GPIO
import time
from time import sleep


INTERVAL=3
SLEEPTIME=0.5

GPIO_sensor=4
GPIO_led=17

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_sensor,GPIO.IN)
GPIO.setup(GPIO_led,GPIO.OUT)


try:
    print("CTRL+C=stop")
    cnt=0 # to count GPIO_sensor==GPIO.HIGH
    misscnt=0 # to count GPIO_sensor==GPIO.LOW
    while True:
        if(GPIO.input(GPIO_sensor)==GPIO.HIGH):
            cnt=cnt+1
            if 0<cnt<=50:
                misssnt=0
                print("YURAGI MAX level flashing")
                # coding here to send INT like"1" to Topic by MQTT
            elif 50<cnt<=100:
                misscnt=0
                print("YURAGI NORMAL level flashing")
                # coding here to send INT like"2" to Topic by MQTT
            else:
                misscnt=0
                print("YURAGI MINIMUM level flashing")
                # coding here to send INT like"3" to Topic by MQTT
            time.sleep(SLEEPTIME)
        else:
            misscnt=misscnt+1
            if misscnt>200:  # undetected mode continues ==>>This means your partner gets busy
                cnt=0
            if misscnt>1000:
                print("turn off YURAGI.")
                # coding here to send INT like"4" to Topic by MQTT
            time.sleep(INTERVAL)
            GPIO.output(GPIO_led,GPIO.LOW)
            
except KeyboardInterrupt:
    print("finishing...")
finally:
    GPIO.cleanup()
    print("GPIO cleanup finished")
                