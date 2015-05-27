# PiCubesPython

These are Python examples how to access PiCubes I/O Modules from Raspberry Pi using Python.

These are next the functions in picubes class that are used to communicate with I/O modules:

	# ===========================================================================
	# writeDO(module,output,value) - Control Pi-Cube DO Board
	# module - Module address (1-6)
	# output - Output number (1-4)
	# value  - Digital output value : 
	#            0=Off
	#            1=On
	# ===========================================================================
	
	# ===========================================================================
	# writeUO(module,output,type,value) - Control Pi-Cube UO Board
	# module - Module address (1-6)
	# output - Output number (1-4)
	# type   - Universal output type:
	#	     0 = Digital Output (0/12VDC)
	#            1 = Modulation (0-10VDC)
	#            2-255 = Digital otput PWM with this period in sec.
 	# value  - Universal output value:
 	#	     0/1 = For digital type 
 	#            0-100% = for Modulation/PWM
	# ===========================================================================
	
	# ===========================================================================
	# readUI(module,input,type) - Control and Read Pi-Cube UI Board
	# module - Module address (1-6)
	# input  - Input number (1-4)
	# type   - Input type
	#            0 = Resistance (Return value 0-350000)
	#            1 = Digital (Return value 0-1)
	#            2 = Voltage/Current (Return value 0-100%,represent 0-10V/0-20mA) 
	#            3 = 10K Type II Thermistor (Return value -4000 to 14000, scale 0.01)
	#            4 = Pulse Input (Return value is counter value)  
	# ===========================================================================	
	

