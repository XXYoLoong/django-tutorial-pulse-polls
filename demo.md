# Django项目实践：基于官方Tutorial构建双语投票网站 Pulse Polls

## 一、项目概述

### 1. 项目名称

Django项目实践：基于官方Tutorial构建双语投票网站 Pulse Polls

### 2. 作者信息

- 姓名：倪家诚
- 英文名：Ni Jiacheng
- 日期：2026-03-31
- GitHub：`https://github.com/XXYoLoong/django-tutorial-pulse-polls`

### 3. 项目背景

本项目以 Django 官方中文文档 `https://docs.djangoproject.com/zh-hans/6.0/intro/` 为实践主线，在完成官网 Tutorial 基础功能的前提下，进一步将原始示例扩展为一个适合作业展示和演示汇报的双语投票网站。

项目不仅完成了官方教程中的模型、视图、模板、路由、后台管理、测试等基础内容，还进行了以下扩展：

- 支持中英双语界面切换
- 重构首页、详情页、结果页 UI
- 增加更丰富、更安全、更适合作业展示的投票主题
- 提供一键生成演示数据的管理命令
- 补全文档、许可证、Git 仓库和 GitHub 发布流程

## 二、项目目标

本项目的目标包括：

- 按照 Django 官网 Tutorial 完成完整项目实践
- 理解 Django 的 MTV 架构和核心开发流程
- 掌握模型设计、模板渲染、视图逻辑、URL 分发、后台管理和测试方法
- 在官方示例基础上进行工程化和展示型升级
- 形成可运行、可演示、可复现、可发布的完整作品

## 三、开发环境

### 1. 本地环境

- 操作系统：Windows
- 工作目录：`f:\YL-Workspace\Z-1`
- Python：`3.14.3`
- pip：`25.3`

### 2. 核心依赖

- Django：`6.0.3`
- django-debug-toolbar：`6.2.0`

### 3. 项目地址

- GitHub 仓库：`https://github.com/XXYoLoong/django-tutorial-pulse-polls`

## 四、项目实施过程

### 1. 环境检查与准备

首先检查工作目录状态以及 Python、pip 和 Django 可用版本，确认本机具备创建 Django 6.0 项目的条件。

执行的关键操作：

- 检查当前目录内容
- 检查 Python 版本
- 检查 pip 版本
- 查询 Django 可安装版本
- 查阅 Django 官方中文文档

结论：

- 当前目录可直接作为项目工作区
- Django 6.0.3 可正常安装

### 2. 创建虚拟环境并安装依赖

为了避免污染系统 Python 环境，在项目根目录下创建虚拟环境 `.venv`，然后安装 Django。

关键命令：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install Django==6.0.3
.\.venv\Scripts\python.exe -m django --version
```

结果：

- 成功创建 `.venv`
- 成功安装 Django 6.0.3

### 3. 初始化 Django 项目

在当前目录中执行官方命令创建 Django 项目 `mysite`。

关键命令：

```powershell
.\.venv\Scripts\django-admin.exe startproject mysite .
```

生成核心文件：

- `manage.py`
- `mysite/settings.py`
- `mysite/urls.py`
- `mysite/asgi.py`
- `mysite/wsgi.py`

### 4. 创建 polls 应用并完成 Tutorial 主体功能

按照官网教程创建 `polls` 应用，并逐步补充模型、视图、模板和路由。

关键命令：

```powershell
.\.venv\Scripts\python.exe manage.py startapp polls
```

主要工作：

- 在 `models.py` 中创建 `Question` 和 `Choice`
- 在 `views.py` 中实现 `IndexView`、`DetailView`、`ResultsView` 和 `vote()`
- 在 `urls.py` 中配置投票相关路由
- 在模板中实现首页、详情页、结果页
- 将 `polls` 注册到 `INSTALLED_APPS`

### 5. 配置后台管理与静态资源

为了满足教程要求并提升项目完整性，对后台管理和静态文件进行了配置。

主要工作：

- 在 `admin.py` 中注册 `Question` 和 `Choice`
- 配置后台列表显示、筛选和搜索
- 添加样式文件和背景资源

### 6. 接入 django-debug-toolbar

根据 Django Tutorial 第 8 部分，接入 `django-debug-toolbar` 作为第三方开发辅助工具。

主要工作：

- 在 `requirements.txt` 中加入依赖
- 在 `settings.py` 中配置 `INSTALLED_APPS`、`MIDDLEWARE` 和 `INTERNAL_IPS`
- 在 `urls.py` 中挂载调试路由

说明：

- 为避免影响测试，调试工具栏只在非测试模式下启用

### 7. 生成迁移并初始化数据库

模型完成后，执行迁移命令生成数据库结构。

关键命令：

```powershell
.\.venv\Scripts\python.exe manage.py makemigrations polls
.\.venv\Scripts\python.exe manage.py migrate
```

结果：

- 成功生成 `0001_initial.py`
- 成功创建并初始化 `db.sqlite3`

### 8. 创建管理员账户与初始演示数据

为了方便后台演示，创建了超级用户，并通过 shell 写入了一组初始示例数据。

后台账号：

- 用户名：`admin`
- 密码：`Admin123456!`

### 9. 修复首页和详情页访问问题

在项目运行过程中，先后发现两个常见问题：

- 访问根路径 `/` 出现 404
- 访问 `/polls/1` 时因为缺少尾部斜杠而显示 `Not Found`

处理方法：

- 在 `mysite/urls.py` 中为根路径添加跳转逻辑
- 在 `polls/urls.py` 中兼容带斜杠与不带斜杠的访问

### 10. 清理重复数据并补全测试

在手工插入示例数据时，出现了重复问题目。后续进行了清理，并同步修正了测试文案与页面内容，使测试结果与页面表现保持一致。

### 11. 项目升级为双语投票站

在完成官网 Tutorial 基础功能后，对项目进行了展示型升级。

升级内容包括：

- 为 `Question` 和 `Choice` 增加英文标题字段
- 为 `Question` 增加中英文描述字段
- 新增统一布局模板 `base.html`
- 重构首页、详情页、结果页
- 增加中英双语切换按钮
- 新增前端脚本 `app.js`
- 将页面样式升级为卡片化展示风格
- 在结果页中增加投票比例可视化

### 12. 丰富投票内容

为了使项目更适合作业展示，不再使用官方 Tutorial 原始那种单一示例问题，而是设计了 6 组轻松、有趣、无争议的投票内容。

选题方向参考了中文社区中常见的日常讨论氛围，但避免了争议性、价值观冲突和道德风险题目，方向包括：

- 理想周末方式
- 饮品选择偏好
- 多出一小时如何使用
- 旅行前优先准备什么
- 学习时喜欢的环境
- 最能点亮一天的小确幸

### 13. 新增一键生成演示数据命令

为了让项目更工程化，也为了方便后续演示和复用，新增了 Django 自定义管理命令：

```powershell
.\.venv\Scripts\python.exe manage.py seed_polls
```

该命令会：

- 清空现有投票题目
- 重建 6 组双语投票
- 自动生成 24 个选项

### 14. 完成最终检查与测试

最终使用以下命令验证项目可运行性：

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py test
.\.venv\Scripts\python.exe manage.py runserver
```

验证结果：

- `check` 通过
- `test` 10 项全部通过
- 首页、详情页、结果页均返回 `200`
- 双语切换按钮可正常显示

### 15. 补全文档、许可证与 GitHub 发布

为方便作业提交和项目公开展示，新增并完善了以下文件：

- `README.md`
- `README.en.md`
- `LICENSE`
- `demo.md`

许可证采用：

- Apache License 2.0

随后完成 Git 初始化、提交和 GitHub 仓库发布：

- 本地仓库分支：`main`
- GitHub 仓库：`https://github.com/XXYoLoong/django-tutorial-pulse-polls`

## 五、项目核心成果

### 1. 功能成果

- 完成 Django 官网 Tutorial 核心功能
- 支持投票列表页、详情页、结果页和后台管理
- 支持提交投票并统计票数
- 支持结果可视化展示
- 支持中英双语切换

### 2. 工程成果

- 提供 `seed_polls` 数据生成命令
- 提供中英文 README
- 提供 Apache License 2.0 许可证
- 完成 GitHub 仓库发布

### 3. 展示成果

- 页面风格比官网原始示例更适合作业汇报
- 投票内容更加丰富，演示性更强
- 文档记录完整，便于提交和答辩说明

## 六、项目文件说明

主要文件结构如下：

```text
Z-1/
├─ mysite/
├─ polls/
│  ├─ management/commands/seed_polls.py
│  ├─ migrations/
│  ├─ static/polls/
│  └─ templates/polls/
├─ demo.md
├─ README.md
├─ README.en.md
├─ LICENSE
├─ manage.py
└─ requirements.txt
```

## 七、当前可用账号

- 后台用户名：`admin`
- 后台密码：`Admin123456!`

## 八、项目运行方式

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_polls
.\.venv\Scripts\python.exe manage.py runserver
```

运行后可访问：

- 首页：`http://127.0.0.1:8000/`
- 投票页：`http://127.0.0.1:8000/polls/`
- 后台：`http://127.0.0.1:8000/admin/`

## 九、总结

本项目从 Django 官方 Tutorial 出发，完整实践了 Django Web 开发的基本流程，并在教程基础上进行了较大幅度的展示型升级。整个实践过程涵盖了从环境准备、项目初始化、应用开发、数据库迁移、后台管理、测试验证，到前端美化、双语支持、数据填充、文档整理、GitHub 发布等多个环节。

通过本次项目实践，不仅完成了官方示例，也进一步提升了项目的完整性、可展示性和工程化程度。对于课程作业、项目答辩和技术总结而言，这样的结果更具有说服力和展示价值。
