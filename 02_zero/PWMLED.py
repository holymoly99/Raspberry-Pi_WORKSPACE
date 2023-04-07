from gpiozero import PWMLED
from time import sleep
from signal import pause

led = PWMLED(13)

# while True:
#     led.value = 0 # off
#     sleep(1)
#     led.value = 0.5 # 50%의 밝기
#     sleep(1)
#     led.value = 1 # 100%의 밝기
#     sleep(1)
int a = (parse.int(input('종료를 원하면 엔터를 눌러라'))
led.pulse() # 메인 스레드가 종료하면 같이 종료됨
#pause()

input('종료를 원하면 엔터를 눌러라')