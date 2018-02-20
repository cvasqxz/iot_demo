from sht_sensor import Sht
from time import sleep, time
from struct import pack
from OP_RETURN import OP_RETURN_send

def main(sht):
	# buffers
	msg = ''
	i = 0

	while True:
		temp = pack('f', round(sht.read_t(), 2))
		hum = pack('f', round(sht.read_rh(), 2))
		timestamp = pack('L', int(time()))

		msg += timestamp + temp + hum
		i += 1
		print('medicion %i: %s, %s' % (i, temp.encode('hex'), hum.encode('hex')))

		if i == 6:
			result = OP_RETURN_send('cZJXM2yPqjbinTZ48fV8tjGqjxAePJeWuQ', 0.001, msg, False)
			if 'error' in result:
				print('Error: ' + result['error'])
			else:
				print('TxID: ' + result['txid'])

			msg = ''
			i = 0

		sleep(100)

if __name__ == '__main__':
	sht = Sht(24, 23)
	main(sht)