import RPi.GPIO as GPIO
import time

def põleb(pin,aeg): #LED põlema
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(aeg)
    return
def kustub(pin,aeg): #LED kustu
    GPIO.output(pin,GPIO.LOW)
    time.sleep(aeg)
    return
def roheline(pin): #rohelise tule vilkumine
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return
    
def katkestus(pin): #sinine tuli põlema
    põleb(16,1)
    return
    
GPIO.setmode(GPIO.BOARD)  #Selleks, et kasutada Rasberry Pi "board pin numbers"
GPIO.setwarnings(False)

GPIO.setup(32, GPIO.OUT) #roheline, autod
GPIO.setup(36, GPIO.OUT) #kollane, autod
GPIO.setup(37, GPIO.OUT) #punane, autod
GPIO.setup(18, GPIO.OUT) #roheline, jälakäijad
GPIO.setup(22, GPIO.OUT) #punane, jalakäijad
GPIO.setup(16, GPIO.OUT) #sinine
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #nupp

GPIO.add_event_detect(12, GPIO.FALLING, callback = katkestus, bouncetime = 10) #katkestus

for i in range(4):
    põleb(22,.05) #punane, jalakäija
    põleb(37,3) #punane, auto
    põleb(36,2) #kollane, auto
    kustub(37,.05) #punane, auto
    kustub(36,.05) #kollane, auto
    põleb(32,3) #roheline, auto
    kustub(32,1) #roheline, auto
    for i in range(4):
        roheline(32)
    põleb(36,3) #kollane, auto
    kustub(36,.05) #kollane, auto
    if GPIO.event_detected(12):
        põleb(37,1) #punane, auto
        põleb(22,1) #punane, jalakäija
        kustub(22,.05) #punane, jalakäija
        kustub(16,.05) #sinine
        põleb (18,4) #roheline, jalakäija
        kustub(18,.05) #roheline, jalakäija


print("Valmis!")
GPIO.cleanup()
