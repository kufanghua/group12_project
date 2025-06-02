import pygame
from src.entities.base_entity import BaseEntity

class BaseTower(BaseEntity):
    def __init__(self, x, y, game_manager):
        super().__init__(x, y)
        self.game_manager = game_manager
        self.last_shot = 0

    def upgrade(self):
        pass  # 由子類別覆寫
