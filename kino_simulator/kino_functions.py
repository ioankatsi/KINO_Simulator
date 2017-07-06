import sys
import pygame
from rectangle import Rectangle
from random import randint
import random
import time

def check_keydown_events(event, k_settings, screen):
	if event.key == pygame.K_q:
		sys.exit()
		'''
	elif event.key == pygame.K_p and stats.game_active == False:
		start_game(k_settings, screen, stats, play_button)
		'''
def check_event(k_settings, screen):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, k_settings, screen)
		
def update_screen(k_settings, screen):
	""" Update images on the screen and flip to the new screen """
	# Redraw the screen 
	screen.fill(k_settings.bg_color)
	create_board(k_settings, screen)
	simulation(k_settings, screen)
	pygame.display.flip()


def create_rectangle(k_settings, screen, msg, i, coloumn, color_change):
	rectangle = Rectangle(k_settings, screen, msg)
	rectangle_width = rectangle.rect.width 
	rectangle.x = 2 * rectangle.width * i  # εναλλακτική rectangle.x = rectangle.width +  2 * rectangle.width * i
	rectangle.rect.x = rectangle.x
	rectangle.rect.y =  1.7 * rectangle.rect.height * coloumn
	if color_change == True:
		rectangle.button_color = (170, 10, 70)
	rectangle.prep_msg(msg)
	rectangle.draw_rectangle()


def winner_numbers(k_settings, screen):  # ΣΕ ΚΑΘΕ ΑΡΙΘΜΟ ΠΟΥ ΒΡΙΣΚΩ ΑΠΟ ΤΟΥΣ ΤΥΧΕΡΟΥ΅ΚΑΤΑΧΑΡΩ ΔΕΙΚΤΕΣ i, coloumn ΣΕ ΕΝΑ dictionary
	c = 0
	color_change = False
	ln =lucky_numbers()
	ln_info = []
	for coloumn in range(1, 9):
		for i in range(1, 11):
			c += 1	
			if c in ln:
				color_change = True
				info = {'c' : c, 'i' : i, 'coloumn' : coloumn}
				ln_info.append(info)
	print("THE ORIGINAL ------------------- WINNER_NUMBERS")			
	for info in ln_info[:20]:
		print(info)
	random.shuffle(ln_info)
	print("THE SHUFFLED ------------------- WINNER_NUMBERS")
	for info in ln_info[:20]:
		print(info)	
	return ln_info

def effect_numbers(k_settings, screen): 
	c = 0
	color_change = False
	ln = effect_list()
	ln_info = []
	for coloumn in range(1, 9):
		for i in range(1, 11):
			c += 1	
			if c in ln:
				color_change = True
				info = {'c' : c, 'i' : i, 'coloumn' : coloumn}
				ln_info.append(info)		
	random.shuffle(ln_info)		
	return ln_info

def simulation(k_settings, screen):
	shuffled = winner_numbers(k_settings, screen)	
	shown_numbers = []
	for shuffle in shuffled[:20]:
		effect_lst = effect_numbers(k_settings,  screen)
		for effect in effect_lst[:10]: 
			if effect['c'] not in  shown_numbers :
				color_change = True
				create_rectangle(k_settings, screen, str(effect['c']), effect['i'], effect['coloumn'], color_change)
				pygame.display.flip()
				time.sleep(0.7)
				color_change = False
				create_rectangle(k_settings, screen, str(effect['c']), effect['i'], effect['coloumn'], color_change)
				pygame.display.flip()
			else:
				#effect_lst = version_3(k_settings,  screen)
				continue 

		color_change = True
		create_rectangle(k_settings, screen, str(shuffle['c']), shuffle['i'], shuffle['coloumn'], color_change)
		pygame.display.flip()
		time.sleep(2)
		shown_numbers.append(shuffle['c'])
		print(shown_numbers)
		color_change = False


def create_board(k_settings, screen):
	c = 0
	color_change = False
	for coloumn in range(1, 9):
		for i in range(1, 11):	
			c +=1
			create_rectangle(k_settings, screen, str(c), i, coloumn, color_change)
	pygame.display.flip()																#!!! EFFECT FOR ROW PRINTING
			
def lucky_numbers():
	lucky_numbers = []
	count = 0
	while count < 20 :
		x = randint (1, 80)
		if x not in lucky_numbers:
			lucky_numbers.append(x)
			count += 1
	random.shuffle(lucky_numbers)
	#print(lucky_numbers)
	return lucky_numbers

def effect_list():
	effect_l = []
	count = 0
	while count < 19 :
		x = randint(1, 80)
		effect_l.append(x)
		count +=1
	random.shuffle(effect_l)
	return effect_l



'''
# PRINTING RESULT IN ROW NOT RANDOM 
def winner_number(k_settings, screen):
	all_the_numbers = list(range(80))
	random.shuffle(all_the_numbers)
	color_change = False
	ln = lucky_numbers()
	effect_lst = effect_list()
	for number in all_the_numbers:
		if number in ln:
			color_change = True
		create_rectangle(k_settings, screen, str(number), i, coloumn, color_change)
		pygame.display.flip()
		color_change = False	

def winner_numbers(k_settings, screen):
	c = 0
	color_change = False
	ln =lucky_numbers()
	for coloumn in range(1, 9):
		for i in range(1, 11):
			c += 1	
			if c in ln:
				color_change = True
			create_rectangle(k_settings, screen, str(c), i, coloumn, color_change)	
			pygame.display.flip()
			color_change = False
'''

