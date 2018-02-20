from sht_sensor import Sht
from time import sleep
from struct import pack

def main(sht):
	while True:
		temp = pack('f', round(sht.read_t(), 2))
		hum = pack('f', round(sht.read_rh(), 2))
		print(temp, hum)
		sleep(10)

if __name__ == '__main__':
	sht = Sht(24, 23)
	main(sht)