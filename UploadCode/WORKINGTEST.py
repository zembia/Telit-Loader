import time
import USB0
import SER
import SER2

SER.set_speed('115200','8N1')
SER2.set_speed('115200','8N1')

i = 0
print('HOLA\n');
while i < 3:
	time.sleep(1)
	a = USB0.send('TEST\r\n')	
	print('HOLA\n');
	b = SER.send('PAULO\n')
	c = SER2.send('BENITO\n')
	i = i + 1

SER.send('END of script\n')
SER2.send('END OF END\n')

