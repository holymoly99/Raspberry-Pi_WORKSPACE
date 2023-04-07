from gpiozero import LED
from time import sleep
from signal import pause

red =LED(13)

# 1초 on 1초 off 1초 on 1초 off 1초 on 1초 off 1초 on 1초 off 1초 on 1초 off 
# while True:
#     red.on()
#     sleep(1)
#     red.off()
#     sleep(1)

# red.blink() # 스레드로 동작(기본) --> 데몬스레드
# sleep(3)
# #pause() # 스레드가 다르기 때문에 pause를 해도 blink()는 여전히 진행된다.
# red.blink(on_time=0.5, off_time=0.5)
# sleep(5)

# red.blink(on_time=0.2, off_time=2)
# sleep(10)

print(red.value)

# @property
# def month(self):   # getter
#     return self.__month

# @month.setter
# def month(self, month):
#     if 1<=month <=12:
#         self.__month = month

#

# led 켜짐 ㄷㄷ; because 변수가 아닌 -property- 이기 때문
# *변수*처럼 사용하지만 실제론 *함수*임!!
red.value = 1  # setter 호출   
print(red.value) # getter 호출
sleep(5)

red.value = 0
print(red.value)