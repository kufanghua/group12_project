import pygame
from src.entities.towers.base_tower import BaseTower
from src.entities.projectiles.bullet import Bullet

class MachineTower(BaseTower):
    name = "Machine"
    cost = 90

    def __init__(self, x, y, game_manager):
        super().__init__(x, y, game_manager)
        self.image = pygame.Surface((38, 38), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (100, 200, 120), (6, 6, 26, 26))
        pygame.draw.circle(self.image, (70, 160, 70), (19, 19), 16, 4)
        self.range = 90
        self.damage = 18
        self.fire_rate = 2.3
        self.level = 1
        self.upgrade_cost = 60

    def shoot(self, target):
        bullet = Bullet(self.x, self.y, target, self.damage, self.game_manager)
        self.game_manager.projectiles.add(bullet)

    def upgrade(self):
        if self.level == 1:
            self.level = 2
            self.damage += 10
            self.range += 10
            self.fire_rate *= 1.10
            self.upgrade_cost = 110
            pygame.draw.circle(self.image, (120, 230, 170), (19, 19), 10, 2)
        elif self.level == 2:
            self.level = 3
            self.damage += 20
            self.range += 10
            self.fire_rate *= 1.10
            self.upgrade_cost = 160
            pygame.draw.rect(self.image, (120, 240, 170), (12, 12, 14, 14))
