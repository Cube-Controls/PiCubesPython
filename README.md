# PiCubesPython

These are Python examples how to access PiCubes I/O Modules from Raspberry Pi using Python.

These are next the functions in picubes class that are used to communicate with I/O modules:

	# ===========================================================================
	# writeDO(module,output,value) - Control Pi-Cube DO Board
	# module - Module address (1-6)
	# output - Output number (1-4)
	# value  - Digital output value 0-Off,1-On
	# ===========================================================================
	
	# ===========================================================================
	# writeUO(module,output,type,value) - Control Pi-Cube UO Board
	# module - Module address (1-6)
	# output - Output number (1-4)
	# type   - 0 = Digital , 1 = Modulation , 2-255 = PWM with this period in sec.
 	# value  -  0/1 For digital type , 0-100% for Modulation/PWM
	# ===========================================================================
	
	# ===========================================================================
	# readUI(module,input,type) - Control and Read Pi-Cube UI Board
	# module - Module address (1-6)
	# input  - Input number (1-4)
	# type   - 0 = Resistance , 1 = Digital, 2 = Voltage/Current , 
	#          3 = 10K Type II Thermistor, 4 - Pulse Input
	# ===========================================================================	
	

