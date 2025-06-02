import pygame
from src.utils.constants import FONT_NAME, SCREEN_WIDTH, SCREEN_HEIGHT, UI_BG_COLOR

class GameUI:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.SysFont(FONT_NAME, 22)
        self.selected_tower = None

        # 升級按鈕區域
        self.upgrade_btn_rect = pygame.Rect(SCREEN_WIDTH-150, 45, 130, 40)

    def update(self, dt):
        # 偵測滑鼠是否選中塔
        mouse_pos = pygame.mouse.get_pos()
        self.selected_tower = None
        for tower in self.game_manager.towers:
            if tower.rect.collidepoint(mouse_pos):
                self.selected_tower = tower
                break

    def draw(self, surface):
        # 畫UI背景
        pygame.draw.rect(surface, UI_BG_COLOR, (0, 0, SCREEN_WIDTH, 40))
        money_txt = self.font.render(f"金錢: {self.game_manager.money}", True, (0, 80, 0))
        life_txt = self.font.render(f"生命: {self.game_manager.life}", True, (180, 0, 0))
        score_txt = self.font.render(f"分數: {self.game_manager.score}", True, (0, 0, 180))
        surface.blit(money_txt, (10, 7))
        surface.blit(life_txt, (150, 7))
        surface.blit(score_txt, (280, 7))

        # 畫升級按鈕（當滑鼠在塔上時）
        if self.selected_tower is not None:
            tower = self.selected_tower
            if tower.level < tower.max_level:
                pygame.draw.rect(surface, (240, 210, 80), self.upgrade_btn_rect)
                upgrade_cost = tower.get_upgrade_cost()
                txt = self.font.render(f"升級({tower.level}->{tower.level+1}) ${upgrade_cost}", True, (60,30,0))
                surface.blit(txt, (self.upgrade_btn_rect.x+10, self.upgrade_btn_rect.y+7))
            else:
                pygame.draw.rect(surface, (200, 200, 200), self.upgrade_btn_rect)
                txt = self.font.render("已達最大等級", True, (120,120,120))
                surface.blit(txt, (self.upgrade_btn_rect.x+10, self.upgrade_btn_rect.y+7))

            # 顯示塔等級
            level_txt = self.font.render(f"Lv.{tower.level}", True, (50, 20, 200))
            surface.blit(level_txt, (tower.rect.x, tower.rect.y-25))

    def handle_event(self, event):
        # 點擊升級按鈕
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.selected_tower and self.selected_tower.level < self.selected_tower.max_level:
                if self.upgrade_btn_rect.collidepoint(event.pos):
                    cost = self.selected_tower.get_upgrade_cost()
                    if self.game_manager.money >= cost:
                        self.game_manager.money -= cost
                        self.selected_tower.upgrade()
                    return True
        return False

    def handle_click(self, pos):
        # UI操作點擊
        pass
