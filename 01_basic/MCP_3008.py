import spidev
import time

# 딜레이 시간 (센서 측정 간격)
delay = 0.5
# MCP3008 채널 중 센서에 연결한 채널 설정
pot_channel = 0

# SPI 인스턴스 spi 생성
spi = spidev.SpiDev()

# SPI 통신 시작하기 /dev/spidev0.0 파일을 열겠다.
spi.open(0, 0)

# spi 통신 속도 설정 100KHz
spi.max_speed_hz = 100000

# 0~7 까지 8개 채널에서 SPI 데이터 읽기
def readadc(adcnum):
    if adcnum < 0 or adcnum > 7:
        return -1
    
    # 요청 및 값 리턴 MOSI(Master out Slave in)
    # 리스트에서 r[0]은 스타트 비트 1, 8+adcnum을 왼쪽으로 4비트 움직이고, 0은 don't care로 신경 쓸 필요 없음
    r = spi.xfer2([1, 8+adcnum <<4, 0])  # 왼쪽으로 4bit 움직여라(비트 연산자) 
    ## 비트 연산자
    # & 마스크는 0이면 무조건 0으로 만들고 1이면 유지
    # or 마스크는 1이면 무조건 1로 만들고, 0이면 유지
    # r[1] & 3(00000011) 이므로 두자리는 유지하고 나머지는 0으로 만들겟다는 의미
    # 10비트 해석

    # MISO
    data = ((r[1] & 3) << 8) + r[2]

    return data

while True:
    #readadc 함수로 pot_channel의 SPI 데이터를 읽기
    pot_value = readadc(pot_channel)
    print("--------------")
    print("LDR value:", pot_value)
    time.sleep(delay)