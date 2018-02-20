from sht_sensor import Sht
from time import sleep
from struct import pack

def main(sht):
	buff_temp = buff_hum = ''
	i = 0

	while True:
		buff_temp += pack('f', round(sht.read_t(), 2))
		buff_hum += pack('f', round(sht.read_rh(), 2))
		i += 1

		if i == 10:
			msg = buff_hum + buff_temp
			print(msg, len(msg))
			i = 0
			buff_hum = buff_temp = ''

		sleep(10)

if __name__ == '__main__':
	sht = Sht(24, 23)
	main(sht)