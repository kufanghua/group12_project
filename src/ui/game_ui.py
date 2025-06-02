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
        self.selected_tower = None  # 新增：選中的地圖上塔
        self._init_tower_buttons()

    def _init_tower_buttons(self):
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

        # 畫塔選擇按鈕
        for i, (rect, tower_cls, label) in enumerate(self.tower_buttons):
            if self.game_manager.selected_tower_type == tower_cls:
                pygame.draw.rect(surface, (170, 200, 255), rect)
            else:
                pygame.draw.rect(surface, (220, 220, 220), rect)
            pygame.draw.rect(surface, (60, 60, 90), rect, 2)
            txt = pygame.font.SysFont(FONT_NAME, 18).render(label, True, (30, 30, 80))
            surface.blit(txt, (rect.x + 3, rect.y + 8))
            price = getattr(tower_cls, "cost", 100)
            price_txt = pygame.font.SysFont(FONT_NAME, 16).render(f"${price}", True, (80, 90, 20))
            surface.blit(price_txt, (rect.x + 6, rect.y + 40))
        
        # 若未選塔，提示
        if not self.game_manager.selected_tower_type:
            tip = self.font.render("請先點選上方塔種再蓋塔，或點現有塔升級", True, (200, 40, 40))
            surface.blit(tip, (SCREEN_WIDTH//2 - tip.get_width()//2, 9))

        # ----------- 升級UI -----------
        if self.selected_tower:
            tower = self.selected_tower
            info_bg = pygame.Rect(SCREEN_WIDTH-220, 45, 200, 110)
            pygame.draw.rect(surface, (240, 240, 255), info_bg)
            pygame.draw.rect(surface, (60, 60, 90), info_bg, 2)
            title = self.font.render("塔資訊/升級", True, (20, 20, 90))
            surface.blit(title, (info_bg.x + 10, info_bg.y + 6))
            # 塔等級
            lv_txt = self.font.render(f"LV: {getattr(tower, 'level', 1)}", True, (30, 30, 60))
            surface.blit(lv_txt, (info_bg.x + 10, info_bg.y + 36))
            # 攻擊力/射程/攻速
            atk = getattr(tower, "damage", 0)
            rg = getattr(tower, "range", 0)
            spd = getattr(tower, "fire_rate", 0)
            surface.blit(self.font.render(f"ATK:{atk}  Range:{rg}", True, (60, 30, 30)), (info_bg.x+10, info_bg.y+66))
            surface.blit(self.font.render(f"FireRate:{spd}", True, (60, 30, 30)), (info_bg.x+10, info_bg.y+92))
            # 升級按鈕
            up_rect = pygame.Rect(info_bg.x+110, info_bg.y+30, 80, 35)
            pygame.draw.rect(surface, (200, 220, 200), up_rect)
            pygame.draw.rect(surface, (60, 90, 60), up_rect, 2)
            upgrade_cost = getattr(tower, "upgrade_cost", 100)
            up_txt = pygame.font.SysFont(FONT_NAME, 18).render(f"升級 ${upgrade_cost}", True, (20, 90, 20))
            surface.blit(up_txt, (up_rect.x+4, up_rect.y+7))
            # 若錢不夠，顯示不能升級
            if self.game_manager.money < upgrade_cost:
                warn = pygame.font.SysFont(FONT_NAME, 16).render("金錢不足", True, (200, 40, 40))
                surface.blit(warn, (up_rect.x-18, up_rect.y+38))

            # 存下升級按鈕位置
            self._upgrade_btn_rect = up_rect
        else:
            self._upgrade_btn_rect = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            # 點選塔選擇按鈕
            for rect, tower_cls, _ in self.tower_buttons:
                if rect.collidepoint(pos):
                    self.game_manager.selected_tower_type = tower_cls
                    self.selected_tower = None  # 取消選中地圖塔
                    return True
            # 點升級按鈕
            if self.selected_tower and self._upgrade_btn_rect and self._upgrade_btn_rect.collidepoint(pos):
                tower = self.selected_tower
                if self.game_manager.money >= getattr(tower, "upgrade_cost", 100):
                    self.game_manager.money -= tower.upgrade_cost
                    tower.upgrade()
                return True
        return False

    def handle_click(self, pos):
        # 點擊地圖上的塔，選中進行升級
        for tower in self.game_manager.towers:
            if tower.rect.collidepoint(pos):
                self.selected_tower = tower
                self.game_manager.selected_tower_type = None
                return
        # 沒有點到塔則清除
        self.selected_tower = None
