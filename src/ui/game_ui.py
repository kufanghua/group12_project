import pygame
from src.utils.constants import FONT_NAME, SCREEN_WIDTH, SCREEN_HEIGHT, UI_BG_COLOR
from src.entities.towers.cannon_tower import CannonTower
from src.entities.towers.machine_tower import MachineTower
from src.entities.towers.freeze_tower import FreezeTower

TOWER_CLASSES = [
    (CannonTower, "加農砲塔"),
    (MachineTower, "機槍塔"),
    (FreezeTower, "冰凍塔")
]

class GameUI:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.SysFont(FONT_NAME, 22)
        self.tower_buttons = []
        self.selected_idx = None
        self._init_tower_buttons()

    def _init_tower_buttons(self):
        # 設定塔按鈕區域(畫面左上)
        for i, (tower_cls, label) in enumerate(TOWER_CLASSES):
            rect = pygame.Rect(20 + i * 80, 45, 70, 70)
            self.tower_buttons.append((rect, tower_cls, label))

    def update(self, dt):
        pass

    def draw(self, surface):
        # 畫UI背景
        pygame.draw.rect(surface, UI_BG_COLOR, (0, 0, SCREEN_WIDTH, 40))
        money_txt = self.font.render(f"金錢: {self.game_manager.money}", True, (0, 80, 0))
        life_txt = self.font.render(f"生命: {self.game_manager.life}", True, (180, 0, 0))
        score_txt = self.font.render(f"分數: {self.game_manager.score}", True, (0, 0, 180))
        surface.blit(money_txt, (10, 7))
        surface.blit(life_txt, (150, 7))
        surface.blit(score_txt, (280, 7))

        # 畫塔選擇按鈕區
        for i, (rect, tower_cls, label) in enumerate(self.tower_buttons):
            # 選取效果
            if self.game_manager.selected_tower_type == tower_cls:
                pygame.draw.rect(surface, (170, 200, 255), rect)
            else:
                pygame.draw.rect(surface, (220, 220, 220), rect)
            pygame.draw.rect(surface, (60, 60, 90), rect, 2)
            # 塔名
            txt = pygame.font.SysFont(FONT_NAME, 18).render(label, True, (30, 30, 80))
            surface.blit(txt, (rect.x + 3, rect.y + 8))
            # 價格
            price = getattr(tower_cls, "cost", 100)
            price_txt = pygame.font.SysFont(FONT_NAME, 16).render(f"${price}", True, (80, 90, 20))
            surface.blit(price_txt, (rect.x + 6, rect.y + 40))
        
        # 若未選塔，提示
        if not self.game_manager.selected_tower_type:
            tip = self.font.render("請先點選上方塔種再蓋塔", True, (200, 40, 40))
            surface.blit(tip, (SCREEN_WIDTH//2 - tip.get_width()//2, 9))

    def handle_event(self, event):
        # 處理塔按鈕區的點擊
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for rect, tower_cls, _ in self.tower_buttons:
                if rect.collidepoint(pos):
                    self.game_manager.selected_tower_type = tower_cls
                    return True  # 事件被UI處理
        return False

    def handle_click(self, pos):
        # 非塔按鈕區的左鍵點擊（如需擴充UI可用）
        pass
