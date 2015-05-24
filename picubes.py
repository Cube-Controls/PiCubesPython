#!/usr/bin/python
import smbus
import re

# ===========================================================================
# Cube Control PiCubes_I2C Class
# ===========================================================================

class picubes(object):

	def __init__(self):
		self.bus = smbus.SMBus(1)
		
	def errMsg(self):
		print "Error accessing PiCubes I2C !" 
		return -1

	def getSignedNumber(self, number, bitLength):
		mask = (2 ** bitLength) - 1
		if number & (1 << (bitLength - 1)):
			return number | ~mask
		else:
			return number & mask

	# ===========================================================================
	# writeDO(module,output,value) - Control Pi-Cube DO Board
	# module - Module address (1-6)
	# output - Output number (1-4)
	# value  - Digital output value 0-Off,1-On
	# ===========================================================================
	def writeDO(self,module,output,value):
		if module < 1 or module > 6:
			return
		if output < 1 or output > 4:
			return
		try:
			out_values = [0x00,0x00]
			out_values[0] = value
			address = (module-1)*8+(output-1)*2
			self.bus.write_i2c_block_data(0x1C ,address,out_values)
			return
		except IOError, err:
			return self.errMsg()

	# ===========================================================================
	# writeUO(module,output,type,value) - Control Pi-Cube UO Board
	# module - Module address (1-6)
	# output - Output number (1-4)
	# type   - 0 = Digital , 1 = Modulation , 2-255 = PWM with this period in sec.
 	# value  -  0/1 For digital type , 0-100% for Modulation/PWM
	# ===========================================================================			

	def writeUO(self,module,output,type,value):
		if module < 1 or module > 6:
			return
		if output < 1 or output > 4:
			return
		try:
			out_values = [0x00,0x00]
			out_values[0] = type
			out_values[1] = value
			address = (module-1)*8 +(output-1)*2
			self.bus.write_i2c_block_data(0x1C ,address,out_values)
			return
		except IOError, err:
			return self.errMsg()
			
	# ===========================================================================
	# readUI(module,input,type) - Control and Read Pi-Cube UI Board
	# module - Module address (1-6)
	# input  - Input number (1-4)
	# type   - 0 = Resistance , 1 = Digital, 2 = Voltage/Current , 
	#          3 = 10K Type II Thermistor, 4 - Pulse Input
	# ===========================================================================				
			
	def readUI(self,module,inputn,type):
		if module < 1 or module > 6:
			return
		if inputn < 1 or inputn > 4:
			return
		try:			
			out_values = [0x00,0x00]
			out_values[0] = type
			# write type first
			address = (module-1)*8 +(inputn-1)*2
			self.bus.write_i2c_block_data(0x1C ,address,out_values)
			# read value
			reg = 48 + (module-1)*16 + (inputn-1)*4
			result = self.bus.read_i2c_block_data(0x1C, reg, 4)
			if type == 4:
				calc = result[0] | result[1]<<8 | result[2]<<16 | result[3]<<24
			else:
				calc = self.getSignedNumber(result[0] | result[1]<<8 | result[2]<<16 | result[3]<<24,32)
			return calc
		except IOError, err:
			return self.errMsg()

if __name__ == '__main__':
  try:
    bus = picubes()
    print "PiCubes I2C bus is accessible"
  except:
    print "Error accessing PiCubes I2C bus"

