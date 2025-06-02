import pygame
from src.game.map_manager import MapManager
from src.game.wave_manager import WaveManager
from src.ui.game_ui import GameUI
from src.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class GameManager:
    def __init__(self):
        # 遊戲狀態
        self.money = 300
        self.life = 20
        self.score = 0

        # Sprite Groups
        self.towers = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

        # 遊戲模組
        self.map_manager = MapManager(self)
        self.wave_manager = WaveManager(self)
        self.ui = GameUI(self)

        self.selected_tower_type = None  # 準備建造的塔型
        self.running = True

    def update(self, dt):
        self.wave_manager.update(dt)
        self.enemies.update(dt)
        self.towers.update(dt)
        self.projectiles.update(dt)
        self.ui.update(dt)

    def draw(self, surface):
        self.map_manager.draw(surface)
        self.towers.draw(surface)
        self.enemies.draw(surface)
        self.projectiles.draw(surface)
        self.ui.draw(surface)

    def handle_event(self, event):
        if self.ui.handle_event(event):
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左鍵
                pos = pygame.mouse.get_pos()
                if self.selected_tower_type:
                    placed = self.map_manager.place_tower(pos, self.selected_tower_type)
                    if placed:
                        self.money -= self.selected_tower_type.cost
                        self.selected_tower_type = None
                else:
                    self.ui.handle_click(pos)
            elif event.button == 3:  # 右鍵
                self.selected_tower_type = None
                self.ui.selected_tower = None

    def add_tower(self, tower):
        self.towers.add(tower)

    def add_enemy(self, enemy):
        self.enemies.add(enemy)

    def add_projectile(self, projectile):
        self.projectiles.add(projectile)

    def lose_life(self, amount=1):
        self.life -= amount
        if self.life <= 0:
            self.running = False

    def get_tower_at(self, pos):
        for tower in self.towers:
            if tower.rect.collidepoint(pos):
                return tower
        return None
