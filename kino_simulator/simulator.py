import pygame
from settings import Settings
import kino_functions as kf



def run_game():
	# Initialize pygame, settings and create screen object
	pygame.init()
	k_settings = Settings()
	screen = pygame.display.set_mode(
		(k_settings.screen_width, k_settings.screen_height))
	pygame.display.set_caption("ΚΙΝΟ")

	while True:
		kf.check_event(k_settings, screen)
		kf.update_screen(k_settings, screen)

run_game()
