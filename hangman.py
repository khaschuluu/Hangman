#import random
#import os
#
#hided = random.choice([
#	'bmw',
#	'kia',
#	'lamborgini',
#	'mercedes-benz',
#	'lincoln',
#	'ford',
#	'honda',
#	'mazda',
#	'land rover',
#	'rover',
#	'audi',
#	'cadillac',
#	'infiniti',
#	'hummer',
#	'hyundai',
#	'toyota',
#	'jeep',
#	'ferrari',
#	'nissan',
#	'mitsubishi',
#	'bentley',
#	'jaguar',
#	'suzuci',
#	'lotus',
#	'lexus',
#	'volvo',
#	'daewoo',
#	'isuzu'])
#
#missed = ''
#finded = ''
#
#os.system('clear')
#
#print 'GO! man. Good luck for U ;)'
#print 'Finded characters: ' + finded
#print 'Missed characters: ' + missed
#print
#
#for ch in hided:
#	if ch == ' ':
#		print ' ',
#	else:
#		print '_',
#
#while len(missed) < 5:
#	inserted = raw_input("\nYour choie: ")
#	
#	os.system('clear')	
#	
#        if inserted in missed:
#		print inserted + ' is missed character!'
#	elif inserted in finded:
#		print inserted + ' is finded character!'
#	elif inserted not in hided:
#		missed += inserted
#		print inserted + ' missed!'
#	else:
#		finded += inserted
#		print inserted + ' finded!'	
#	
#	print 'Finded characters: ' + finded
#	print 'Missed characters: ' + missed
#
#        notend = 'false'
#	
#        for ch in hided:
#		if ch in finded:
#			print ch,
#		elif ch == ' ':
#			print ' ',
#		else:
#			print '_',
#			notend = 'true'
#			
#        print
#	if len(missed) <> 0:
#		if len(missed) > 0: print ' O  '
#		if len(missed) > 1: print '/|\\'
#		if len(missed) > 2: print ' |  '
#		if len(missed) > 3: print ' ^  '
#		if len(missed) > 4: print '/ \\'
#		
#        if notend == 'false':
#		break
#
#if len(missed) > 3:
#	print '\nYou are HANGMAN!!! True word is ' + hided + '\nBye bye!'
#else:
#	print '\nCongratulation ' + hided + ' is TRUE!!! You can ;)'
#=======
import random, os

class Hangman:	
	def __init__(self):
		os.system('clear')
		
		animals=[
				'lion',
				'camel',
				'orangutan',
				'giraffe',
				'bear',
				]
		colors=[
				'black',
				'orange',
				'brown',
				]
				
		car_models=[
				'bmw',
				'kia',
				'lamborgini',
				'mercedes-benz',
				'lincoln',
				'ford',
				]

		dict={
			'amitan':animals,
			'ungu':colors,
			'mashinii zagwar':car_models,
		}

		self.type_of_word=random.choice(dict.keys())
		self.secret_word=random.choice(dict[self.type_of_word])
		
		self.missed = ''
		self.found = ''
		self.possible_tries=4
		self.remaining=self.possible_tries
		self.game_over = False
		self.is_dead = False
		
		self.hangman_begin="""
		_________
		|       |
		|		
		|     
		|		
		|		
		|     
		|
		"""
		self.hangman_1="""
		_________
		|	|
		|	0 --don't get me killed man!
		|     
		|		
		|		
		|     
		|
		"""
		
		self.hangman_2="""
		_________
		|	|
		|	0 --r u stupid?
		|      /|\\
		|		
		|		
		|     
		|
		"""
		self.hangman_3="""
		_________
		|	|
		|	0 --oh shit!
		|      /|\\
		|	|
		|	^
		|     
		|
		"""
		
		self.hangman_dead= """
		_________
		|	|
		|	0 --~!@#$%^-aaaaah!
		|      /|\\
		|	|
		|	^
		|      / \\
		|
		"""
		
		self.hangman_alive= """
		
		
			0 -- you saved my ass, man! thx!
		       /|\\
			|
			^
		       / \\
		
		"""
		
	def play(self):		
		while self.game_over==False:
			self.draw_board()
			self.draw_hangman()	
			self.get_input()
			self.draw_hangman()
			if self.is_game_over():
				break
		self.end_game()
					
	def get_input(self):
		input = str.lower(raw_input("\nUsgee oruulna uu:"))
		if len(input)==1:
			if input in self.missed:
				print input + ' useg alga!'
			elif input in self.found:
				print input + ' useg baina!'
			elif input not in self.secret_word:
				self.missed += input
				print input + ' useg alga!'	
			elif input in self.secret_word:
				self.found += input
				print input + ' useg baina!'	
		else:
			self.play()
					
	def draw_board(self):
		os.system('clear')
		print 'Odoo tand taah '+str(self.possible_tries-len(self.missed))+' bolomj baina.\n'
		print 'Ene bol negen '+self.type_of_word+' (angliar) :'
		if len(self.missed)>0:
			print 'Baihgui usegnuud: ' + self.missed + '\n'
		else:
			print '\n'
		for ch in self.secret_word:
			if ch in self.found:
				print ch,
			elif ch == ' ':
				print ' ',
			else:
				print '_',
		print '\n'

	def is_game_over(self):
		if (self.possible_tries-len(self.missed))==0:
			return True
			self.is_dead=True
		elif len(self.secret_word)==len(self.found):
			return True
			self.is_dead=False
		else:
			return False

	def end_game(self):
		os.system('clear')
		if (self.possible_tries-len(self.missed))==0:
			print '\nYOU KILLED THE POOR BASTARD. GAME OVER, DUDE.'
		elif len(self.secret_word)==len(self.found):
			print '\nCONGRATS! Ta \'' + self.secret_word + '\' hemeeh '+self.type_of_word+'-g zow taalaa!! ;)\n'
		self.play_again()
	
	def play_again(self):
		input=raw_input('\nPlay again? (y/n):')
		if len(input)==1:
			if input=='y':
				self.__init__()
				self.play()
			elif input=='n':
				os.system('clear')
				print '\nYOU KILLED THE POOR BASTARD. GAME OVER, DUDE.'
				print '\nSEE YOU IN HELL!\n'
			else:
				self.end_game()
		
	def draw_hangman(self):
		if len(self.missed)==0:
			print self.hangman_begin
		elif len(self.missed)==1:
			print self.hangman_1
		elif len(self.missed)==2:
			print self.hangman_2
		elif len(self.missed)==3:
			print self.hangman_3
		elif len(self.missed)==4:
			print self.hangman_dead
	
def main():
	hangman=Hangman()
	hangman.play()

if __name__ == '__main__': main()
