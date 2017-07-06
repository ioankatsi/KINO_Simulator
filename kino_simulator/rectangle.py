import pygame.font

class Rectangle():
	def  __init__(self, k_settings, screen, msg):
		""" Initialize button attributes. """
		self.screen = screen
		self.screen_rect = screen.get_rect()

		# Set the dimensiosn of the button
		self.width, self.height = 50 ,50
		self.button_color = (250, 250, 250)
		self.text_color = (1, 1, 1)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.x = self.screen_rect.left 
		self.rect.top = self.screen_rect.top + 10

		# The button message needs to be prepped only once.
		self.prep_msg(msg)

	def prep_msg(self, msg):
		"Render the msg"
		self.msg_image = self.font.render(msg, True, self.text_color,
			self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_rectangle(self):
		# Draw blank button and then draw message.
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)



		