import pygame
from src.entities.towers.base_tower import BaseTower
from src.entities.projectiles.cannon_ball import CannonBall

class CannonTower(BaseTower):
    name = "Cannon"
    cost = 100

    def __init__(self, x, y, game_manager):
        super().__init__(x, y, game_manager)
        self.image = pygame.Surface((38, 38), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (120, 120, 120), (6, 6, 26, 26))
        pygame.draw.circle(self.image, (90, 90, 90), (19, 19), 16, 4)
        self.range = 110
        self.damage = 50
        self.fire_rate = 1.2
        self.level = 1
        self.upgrade_cost = 80

    def shoot(self, target):
        bullet = CannonBall(self.x, self.y, target, self.damage, self.game_manager)
        self.game_manager.projectiles.add(bullet)

    def upgrade(self):
        if self.level == 1:
            self.level = 2
            self.damage += 30
            self.range += 20
            self.fire_rate *= 1.15
            self.upgrade_cost = 130
            pygame.draw.circle(self.image, (170, 150, 90), (19, 19), 16, 4)
        elif self.level == 2:
            self.level = 3
            self.damage += 50
            self.range += 20
            self.fire_rate *= 1.15
            self.upgrade_cost = 200
            pygame.draw.rect(self.image, (210, 170, 90), (12, 12, 14, 14))
        # 可依需求增加更多等級
