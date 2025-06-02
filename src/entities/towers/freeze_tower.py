import pygame
from src.entities.towers.base_tower import BaseTower
from src.entities.projectiles.ice_ball import IceBall

class FreezeTower(BaseTower):
    name = "Freeze"
    cost = 120

    def __init__(self, x, y, game_manager):
        super().__init__(x, y, game_manager)
        self.image = pygame.Surface((38, 38), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (140, 140, 255), (6, 6, 26, 26))
        pygame.draw.circle(self.image, (100, 200, 255), (19, 19), 16, 4)
        self.range = 95
        self.damage = 12
        self.fire_rate = 1.8
        self.level = 1
        self.upgrade_cost = 90
        self.slow_effect = 0.4
        self.slow_time = 2.2

    def shoot(self, target):
        bullet = IceBall(self.x, self.y, target, self.damage, self.game_manager)
        self.game_manager.projectiles.add(bullet)

    def upgrade(self):
        if self.level == 1:
            self.level = 2
            self.damage += 8
            self.range += 10
            self.fire_rate *= 1.10
            self.slow_effect += 0.1
            self.upgrade_cost = 140
            pygame.draw.circle(self.image, (180, 220, 255), (19, 19), 10, 2)
        elif self.level == 2:
            self.level = 3
            self.damage += 15
            self.range += 10
            self.fire_rate *= 1.10
            self.slow_effect += 0.1
            self.upgrade_cost = 180
            pygame.draw.rect(self.image, (180, 220, 255), (12, 12, 14, 14))
