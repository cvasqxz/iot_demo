from sht_sensor import Sht
from time import sleep, time
from struct import pack

def main(sht):
	# buffers
	msg = ''
	i = 0

	while True:
		temp = pack('f', round(sht.read_t(), 2))
		hum = pack('f', round(sht.read_rh(), 2))
		timestamp = pack('L', int(time()))

		msg =+ timestamp + temp + hum
		i += 1

		if i == 6:
			print(msg, len(msg))
			msg = ''
			i = 0

		sleep(1)

if __name__ == '__main__':
	sht = Sht(24, 23)
	main(sht)