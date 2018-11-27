import sys
from sys import version_info


py3  =  version_info[0] > 2 #creates boolean value for test that Python major version > 2
qs = True
end = False

def madLib(loc1, noun1, uot1, verb1, verb2, verb3, verb4, noun2, noun3, noun4, noun5, noun6, verb5, adj1, verb6, loc2):								
	full="\n\nIn "+loc1+" born and raised. \nOn the "+noun1+" was where I spent most of my "+uot1+"\n"+verb1+", "+verb2+", and "+verb3+" all cool \nAnd "+verb4+" some "+noun2+" outside of the "+noun3+"\nWhen a couple of " + noun4+" who were up to no good \nStarted making "+noun5+" in my "+noun6+"\nI got in one little "+verb5+" and my mom got "+adj1+"\nShe said you're " + verb6 + " with your auntie and uncle in "+loc2
	return full


while qs:
	if py3:
		loc1 = input("Tell me a location (proper noun): ")
		noun1 = input("Tell me a noun: ")
		uot1 = input("Tell me a plural unit of time: ")
		verb1 = input("Tell me a verb ending in -ing: ")
		verb2 = input("Tell me another verb ending in -ing: ")
		verb3 = input("another -ing verb: ")
		verb4 = input("guess what? now any verb: ")
		noun2 = input("Tell me a noun: ")
		noun3 = input("and another noun: ")
		noun4 = input("and a plural noun: ")
		noun5 = input("and a regular noun: ")
		noun6 = input("and one more noun: ")
		verb5 = input("and another verb: ")
		adj1 = input("adjective: ")
		verb6 = input("one last verb: ")
		loc2 = input("annnnd one more location (proper noun): ")	
				
		while True:
			try:
				inp = input("please enter a number or q to quit: ")
				if inp=='q':
					sys.exit(0)
				else:
					num=int(inp)
			except ValueError:
				print("Sorry, I didn't get that.")
				continue
			else:
				end=True
				break
					
	else:
		loc1 = raw_input("Tell me a location (proper noun): ")
		noun1 = raw_input("Tell me a noun: ")
		uot1 = raw_input("Tell me a plural unit of time: ")
		verb1 = raw_input("Tell me a verb ending in -ing: ")
		verb2 = raw_input("Tell me another verb ending in -ing: ")
		verb3 = raw_input("another -ing verb: ")
		verb4 = raw_input("guess what? now any verb: ")
		noun2 = raw_input("Tell me a noun: ")
		noun3 = raw_input("and another noun: ")
		noun4 = raw_input("and a plural noun: ")
		noun5 = raw_input("and a regular noun: ")
		noun6 = raw_input("and one more noun: ")
		verb5 = raw_input("and another verb: ")
		adj1 = raw_input("adjective: ")
		verb6 = raw_input("one last verb: ")
		loc2 = raw_input("annnnd one more location (proper noun): ")
				
		while True:
			try:
				inp = raw_input("please enter a number or q to quit: ")
				if inp=='q':
					sys.exit(0)
				else:
					num=int(inp)
			except ValueError:
				print("Sorry, I didn't get that.")
				continue
			else:
				end=True
				break
		
			#doesn't work:
			#num = raw_input("now please input a number or q to quit: ")
			#if num.isdigit()==False:
			#	print("sorry, try again. \n" + num + " isn't an integer")
			#elif num=='q':
			#	print ("goodbye")
			#	sys.exit(0)
			#else:
			#	break
	
	while end:
		print(madLib(loc1, noun1, uot1, verb1, verb2, verb3, verb4, noun2, noun3, noun4, noun5, noun6, verb5, adj1, verb6, loc2))
		if py3:
			choice = input("\nAgain? y/n: ")	
			if choice in ['y','n']:
				if choice == 'n':
					sys.exit(1)
				else:
					break
			else:
				continue
		else:
			choice = raw_input("\nAgain? y/n: ")	
			if choice in ['y','n']:
				if choice == 'n':
					sys.exit(1)
				else:
					break
			else:
				continue				