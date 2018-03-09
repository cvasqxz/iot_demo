from sht_sensor import Sht
from time import sleep, time
from struct import pack
from OP_RETURN import OP_RETURN_send
from random import random

def main(sht):
	# buffers
	mov = 0.001
	msg = ''
	i = 0

	while True:
		# mediciones empaquetadas
		temp = pack('f', round(sht.read_t(), 2))
		hum = pack('f', round(sht.read_rh(), 2))
		timestamp = pack('L', int(time()))

		# agregar mediciones al buffer
		msg += timestamp + temp + hum
		i += 1

		# debug
		print('medicion %i: %s, %s' % (i, temp.encode('hex'), hum.encode('hex')))

		# envio de tx
		if i == 6:
			result = OP_RETURN_send('cijgisFYuwYiqwhjZnbowrQYXsUq9G3GmA', mov, msg, False)

			if 'error' in result:
				print('Error: ' + result['error'])
			else:
				print('TxID: ' + result['txid'])

			# reset
			msg = ''
			i = 0

		sleep(100)

if __name__ == '__main__':
	# lector de sensor sht15
	sht = Sht(24, 23)

	# funcion principal
	main(sht)