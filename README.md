# Tower Defense OOP Project

本專案是一個以 Python 物件導向設計（OOP）為核心的塔防遊戲專案範例，適合用於教學、學習及程式設計練習。遊戲特色包括多樣化的塔與敵人類型、波數挑戰、基礎動畫與音效、易於擴充的模組化架構。

## 目錄結構

```
tower-defense-oop/
├── README.md
├── requirements.txt
├── .gitignore
├── main.py
├── docs/
├── src/
├── assets/
├── tests/
└── screenshots/
```

- `main.py`：主程式入口
- `docs/`：玩法、設計與說明文件
- `src/`：遊戲所有原始碼，依功能模組劃分
- `assets/`：圖片、音效等資源
- `tests/`：單元測試
- `screenshots/`：遊戲截圖與示範動畫

## 遊戲玩法

- 建造不同種類的防禦塔，阻止敵人通過地圖終點
- 每種塔有不同射程、攻擊方式及特殊效果
- 敵人有基本型、快速型、坦克型等
- 支援多波敵人進攻
- 金錢與升級系統

更多玩法請見 [docs/gameplay.md](docs/gameplay.md)。

## OOP 設計原則

- 採用物件導向設計，模組化拆分
- 不同塔、敵人、投射物皆為獨立類別，便於擴充
- 遊戲管理、波數管理、地圖管理等皆抽象為管理器
- 具備良好繼承與多型設計

詳細設計請見 [docs/oop_design.md](docs/oop_design.md)。

## 安裝與執行

### 1. 安裝需求套件

建議使用 Python 3.9+，於專案根目錄執行：

```bash
pip install -r requirements.txt
```

### 2. 執行遊戲

```bash
python main.py
```

## 主要依賴

- pygame
- 其他詳見 `requirements.txt`

## 測試

```bash
python -m unittest discover tests
```

## 截圖與動畫

- ![遊戲畫面1](screenshots/gameplay1.png)
- ![遊戲畫面2](screenshots/gameplay2.png)
- ![遊戲demo](screenshots/demo.gif)

## 專案貢獻

歡迎 PR、issue 討論設計與功能擴充。

## 授權

MIT License

https://github.com/copilot/share/82414088-4264-8c21-9003-f04244b549aa
