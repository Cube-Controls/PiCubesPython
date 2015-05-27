
import time
from picubes import picubes

picubes = picubes()

while True:
	# Test picubes.readUI Function
	print 'Module 1 Input 1 Resistance: ',picubes.readUI(1,1,0)
	print 'Module 1 Input 2 Digital: ',picubes.readUI(1,2,1)
	print 'Module 1 Input 3 Voltage: ',picubes.readUI(1,3,2)*0.1
	print 'Module 1 Input 4 Temperature: ',picubes.readUI(1,4,3) * 0.01
  
	print 'Module 2 Input 1 Counter: ',picubes.readUI(2,1,4)
  
	# Test picubes.readDO Function
	print 'Output 1, Module 5 Off '
	picubes.writeDO(5,1,0) # Output 1 on Module 5 Off
	time.sleep(2)          # wait two seconds
	print 'Output 1, Module 5 On '
	picubes.writeDO(5,1,1) # Output 1 on Module 5 On
	time.sleep(2)          # wait two seconds
	print 'Output 1, Module 5 Off '
	picubes.writeDO(5,1,0) # Output 1 on Module 5 Off


    `   # Test picubes.readUO Function
	print 'Output 1, Module 3 Off '
	picubes.writeUO(3,1,0,0) # Universal Output 1 on Module 3 is Digital Off
	time.sleep(2)            # wait two seconds	
	print 'Output 1, Module 3 On '
	picubes.writeUO(3,1,0,1) # Universal Output 1 on Module 3 is Digital On
	time.sleep(2)            # wait two seconds	
	print 'Output 1, Module 3 On '
	picubes.writeUO(3,1,0,0) # Universal Output 1 on Module 3 is Digital Off

	print 'Output 2, Module 3 5V '
	picubes.writeUO(3,2,1,50)  # Universal Output 2 on Module 3 is Modulation 50% Output
	print 'Output 3, Module 3 10sec PWM 50% Duty '
	picubes.writeUO(3,3,10,50) # Universal Output 3 on Module 3 is PWM Modulation Output with period 10 seconds and 50% Duty Cycle
	
