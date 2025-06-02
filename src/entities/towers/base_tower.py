import pygame
from src.entities.base_entity import BaseEntity
from src.utils.constants import TILE_SIZE

class BaseTower(BaseEntity):
    name = "BaseTower"
    cost = 50
    range = 100
    attack_speed = 1.0  # seconds
    damage = 10

    upgrade_cost_factor = 1.5  # 每級升級費用倍率
    max_level = 3

    def __init__(self, x, y, game_manager):
        image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(image, (120, 120, 120), (TILE_SIZE//2, TILE_SIZE//2), TILE_SIZE//2)
        super().__init__(x, y, image)
        self.game_manager = game_manager
        self.attack_cooldown = 0
        self.level = 1

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

    def get_upgrade_cost(self):
        # 第1級升2級: cost*upgrade_cost_factor，第2級升3級: cost*upgrade_cost_factor^2
        if self.level < self.max_level:
            return int(self.cost * (self.upgrade_cost_factor ** self.level))
        return None

    def upgrade(self):
        if self.level < self.max_level:
            self.level += 1
            self.damage = int(self.damage * 1.5)
            self.range = int(self.range * 1.1)
            self.attack_speed = max(0.1, self.attack_speed * 0.85)
            # 可在這裡根據level調整外觀
            return True
        return False
