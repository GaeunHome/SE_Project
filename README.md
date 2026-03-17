# 營運儀表板

[![Python](https://img.shields.io/badge/Python-3-3776AB)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Framework-092E20)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3)](https://getbootstrap.com/)

以一個按摩椅公司為案例進行需求分析，設計營運儀表板，涵蓋庫存管理、員工績效、銷售數據等。

## 團隊成員

| 角色 | 成員 |
|------|------|
| **前端設計** | 侯文家、謝佩芸、李玟霓、劉建昱、趙子嘉 |
| **後端開發** | 侯文家、謝佩芸、李玟霓 |

## 技術堆疊

| 類別 | 技術 |
|------|------|
| **前端** | HTML, CSS, Bootstrap |
| **後端** | Python, Django |

## 專案目的

讓專案成員深入理解軟體開發過程中的各個具體步驟，並透過實際的專案經驗學習如何進行專案管理。實現一個可供企業營運者使用的儀表板，通過該系統可以即時了解企業內部的運營狀況，從而幫助管理層做出數據驅動的決策。

## 完成度

目前專案的雛形已經完成，系統能夠實現基本的數據輸入與存儲功能：
- 用戶可以通過表單提交數據，並且這些數據能夠被成功存儲到資料庫中。
- 系統基本具備了查看和管理資料的功能，為後續擴展其他功能打下了基礎。

## 未來展望

### 介面優化
- 優化頁面的排版和元素間距
- 增加更多響應式設計
- 增強交互設計

### 資料庫優化
- 增加資料表間的外鍵關聯
- 對資料庫進行正規化
- 深化對 Django ORM 的掌握

## 專案結構

```
SE_Project/
├── manage.py               # Django 管理指令
├── final/                  # Django 專案設定
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── finalapp/               # 主要 App
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── static/                 # 靜態資源
│   ├── css/
│   ├── js/
│   └── images/
├── templates/              # 模板
├── .gitignore
└── README.md
```

## 快速開始

```bash
pip install django
python manage.py migrate
python manage.py runserver
```
