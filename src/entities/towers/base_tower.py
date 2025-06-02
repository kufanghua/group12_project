import pygame
from src.entities.base_entity import BaseEntity

class BaseTower(BaseEntity):
    """
    所有塔的基底類別，包含共通屬性與方法
    """
    def __init__(self, x, y, game_manager):
        super().__init__(x, y)
        self.game_manager = game_manager
        self.range = 100
        self.damage = 10
        self.fire_rate = 1.0  # 每秒射擊次數
        self.last_shot = 0
        self.level = 1
        self.upgrade_cost = 100

    def update(self, dt):
        # 自動尋找最近敵人並攻擊
        enemy = self.find_target()
        if enemy:
            self.last_shot += dt
            if self.last_shot >= 1.0 / self.fire_rate:
                self.shoot(enemy)
                self.last_shot = 0

    def find_target(self):
        # 找最近的敵人
        min_dist = float('inf')
        target = None
        for enemy in self.game_manager.enemies:
            if not hasattr(enemy, "rect"):
                continue
            dist = ((self.x - enemy.rect.centerx) ** 2 + (self.y - enemy.rect.centery) ** 2) ** 0.5
            if dist <= self.range and dist < min_dist and enemy.is_alive():
                min_dist = dist
                target = enemy
        return target

    def shoot(self, target):
        # 子類別實作
        pass

    def upgrade(self):
        # 子類別實作
        pass

    def draw(self, surface):
        # 畫出塔
        surface.blit(self.image, self.rect.topleft)
        # 畫攻擊範圍（僅選中時可加，預設不畫）
        # pygame.draw.circle(surface, (150,150,255,100), (self.x, self.y), self.range, 1)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
