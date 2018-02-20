from sht_sensor import Sht
from time import sleep

def main(sht):
	while True:
		temp = round(sht.read_t(), 2)
		hum = round(sht.read_rh(), 2)
		print(temp, hum)
		sleep(10)

if __name__ == '__main__':
	sht = Sht(24, 23)
	main(sht)