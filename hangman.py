import random
import os

hided = random.choice([
	'bmw',
	'kia',
	'lamborgini',
	'mercedes-benz',
	'lincoln',
	'ford',
	'honda',
	'mazda',
	'land rover',
	'rover',
	'audi',
	'cadillac',
	'infiniti',
	'hummer',
	'hyundai',
	'toyota',
	'jeep',
	'ferrari',
	'nissan',
	'mitsubishi',
	'bentley',
	'jaguar',
	'suzuci',
	'lotus',
	'lexus',
	'volvo',
	'daewoo',
	'isuzu'])

missed = ''
finded = ''

os.system('clear')

print 'GO! man. Good luck for U ;)'
print 'Finded characters: ' + finded
print 'Missed characters: ' + missed
print

for ch in hided:
	if ch == ' ':
		print ' ',
	else:
		print '_',

while len(missed) < 5:
	inserted = raw_input("\nYour choie: ")
	
	os.system('clear')	
	
        if inserted in missed:
		print inserted + ' is missed character!'
	elif inserted in finded:
		print inserted + ' is finded character!'
	elif inserted not in hided:
		missed += inserted
		print inserted + ' missed!'
	else:
		finded += inserted
		print inserted + ' finded!'	
	
	print 'Finded characters: ' + finded
	print 'Missed characters: ' + missed

        notend = 'false'
	
        for ch in hided:
		if ch in finded:
			print ch,
		elif ch == ' ':
			print ' ',
		else:
			print '_',
			notend = 'true'
			
        print
	if len(missed) <> 0:
		if len(missed) > 0: print ' O  '
		if len(missed) > 1: print '/|\\'
		if len(missed) > 2: print ' |  '
		if len(missed) > 3: print ' ^  '
		if len(missed) > 4: print '/ \\'
		
        if notend == 'false':
		break

if len(missed) == 5:
	print '\nYou are HANGMAN!!! True word is ' + hided + '\nBye bye!'
else:
	print '\nCongratulation ' + hided + ' is TRUE!!! You can ;)'