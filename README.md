# Django Tutorial Pulse Polls

基于 Django 官方 Tutorial 6.0 完成，并在原始教程基础上扩展为更适合作业展示的双语投票站。

## 作者信息

- 姓名：倪家诚
- English Name: Ni Jiacheng
- GitHub：XXYoLoong / 游龙
- 日期：2026-03-31

## CSDN 文章

- 文章标题：`Django项目实战：手把手实现一个双语投票网站并发布到 GitHub，附完整代码与部署说明`
- CSDN 链接：`待发布后补充`

## 项目亮点

- 完成 Django 官方 tutorial 的核心流程
- 支持投票列表、详情、投票提交、结果页、管理后台
- 支持中英双语切换
- 首页、详情页、结果页进行了展示型 UI 升级
- 内置 6 组轻松、安全、无争议的双语投票题目
- 提供 `seed_polls` 命令，可一键重建演示数据

## 项目截图

### 网站主页

![网站主页](./assets/screenshot-home-zh.png)

### 投票详情页

![投票详情页](./assets/screenshot-detail-zh.png)

### Django 后台界面

![后台界面](./assets/screenshot-admin-zh.png)

## 环境要求

- Python 3.14.3
- Django 6.0.3
- django-debug-toolbar 6.2.0

## 安装与启动

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_polls
.\.venv\Scripts\python.exe manage.py runserver
```

启动后访问：

- 首页：`http://127.0.0.1:8000/`
- 投票页：`http://127.0.0.1:8000/polls/`
- 后台：`http://127.0.0.1:8000/admin/`

## 后台账号

- 用户名：`admin`
- 密码：`Admin123456!`

## 常用命令

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
.\.venv\Scripts\python.exe manage.py seed_polls
```

## 项目结构

```text
Z-1/
├─ assets/
├─ mysite/
├─ polls/
├─ demo.md
├─ manage.py
├─ README.md
├─ README.en.md
├─ LICENSE
└─ requirements.txt
```

## 过程记录

完整开发与排错过程见 [demo.md](./demo.md)。

## 许可证

本项目采用 Apache License 2.0，详见 [LICENSE](./LICENSE)。
