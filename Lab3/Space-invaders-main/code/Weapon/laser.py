import pygame

class Laser(pygame.sprite.Sprite):
	def __init__(self,pos,speed,screen_height):
		super().__init__()
		self.image = pygame.Surface((4,20))
		self.image.fill('white')
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed
		self.height_y_constraint = screen_height

	def destroy(self):
		if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
			self.kill()

	def collision_with_blocks(self, blocks_group):
		# Возвращает список блоков, с которыми лазер столкнулся
		collided_blocks = pygame.sprite.spritecollide(self, blocks_group, True)
		# Если есть столкновения, уничтожаем лазер
		if collided_blocks:
			self.kill()