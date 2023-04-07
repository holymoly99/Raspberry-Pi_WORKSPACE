from gpiozero import Button
from gpiozero import LED
from time import sleep 
from signal import pause 

button = Button(26)
led1 = LED(13)
led2 = LED(19)
# while True:
#     if button.is_pressed:
#         print("pressed")
#     else:
#         print("not pressed")
    
#     sleep(1)

def say_hello():
    print("hi! bro")
    
def say_bye():
    print("bye! bro")

# button.when_pressed = led.on
# button.when_released = led.off
# pause()

button.when_pressed = led1.on
button.when_released = led2.on

led1.off
led2.off



pause()