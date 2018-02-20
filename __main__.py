from sht_sensor import Sht
from time import sleep

def main(sht):
	while True:
		temp = sht.read_t()
		hum = sht.read_rh()
		print(temp, hum)
		sleep(10)

if __name__ == '__main__':
	sht = Sht(24, 23)
	main(sht)