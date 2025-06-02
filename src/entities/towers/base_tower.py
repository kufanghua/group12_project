import pygame
from src.entities.base_entity import BaseEntity
from src.utils.constants import TILE_SIZE

class BaseTower(BaseEntity):
    name = "BaseTower"
    cost = 50
    range = 100
    attack_speed = 1.0  # seconds
    damage = 10

    def __init__(self, x, y, game_manager):
        image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(image, (120, 120, 120), (TILE_SIZE//2, TILE_SIZE//2), TILE_SIZE//2)
        super().__init__(x, y, image)
        self.game_manager = game_manager
        self.attack_cooldown = 0

    def update(self, dt):
        self.attack_cooldown -= dt
        if self.attack_cooldown <= 0:
            target = self.find_target()
            if target:
                self.shoot(target)
                self.attack_cooldown = self.attack_speed

    def find_target(self):
        # 找到第一個在射程內的敵人
        for enemy in self.game_manager.enemies:
            if self.distance_to(enemy) <= self.range:
                return enemy
        return None

    def shoot(self, target):
        pass  # 子類覆寫

    def distance_to(self, entity):
        dx = self.x - entity.x
        dy = self.y - entity.y
        return (dx*dx + dy*dy) ** 0.5
