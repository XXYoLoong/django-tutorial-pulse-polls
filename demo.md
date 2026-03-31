# Django Tutorial 实践记录

## 项目说明

- 工作区：`f:\YL-Workspace\Z-1`
- 作者：倪家诚 / Ni Jiacheng
- 日期：2026-03-31
- 目标：按照 Django 官方教程 `https://docs.djangoproject.com/zh-hans/6.0/intro/` 完成示例项目，并尽量执行到最后一步。
- 记录原则：每完成一个阶段，就在本文件追加实际操作、生成文件和验证结果。

## 步骤 1：初始环境检查

- 检查当前工作区内容，结果显示目录当前基本为空。
- 检查 Python 版本：`Python 3.14.3`
- 检查 `py` 版本：`Python 3.14.3`
- 检查 `pip` 版本：`pip 25.3`
- 查询可安装 Django 版本，确认官方源可获取 `Django 6.0.3`
- 查阅 Django 官方文档首页，确认本次以 `Django 6.0` 中文教程为主线实现。

## 当前结论

- 可以继续在当前目录中直接构建项目。
- 下一步将创建虚拟环境、安装 Django，并开始按 tutorial 搭建项目。

## 步骤 2：创建虚拟环境并安装依赖

- 在项目根目录执行：`python -m venv .venv`
- 确认生成目录：`.venv/Include`、`.venv/Lib`、`.venv/Scripts`
- 在虚拟环境中安装 Django：`.\.venv\Scripts\python.exe -m pip install Django==6.0.3`
- 安装完成后验证版本：`.\.venv\Scripts\python.exe -m django --version`
- 验证结果：`6.0.3`

### 本阶段生成文件

- `.venv/`
- `demo.md`

## 步骤 3：初始化 Django 项目

- 使用官方命令在当前目录创建项目：`.\.venv\Scripts\django-admin.exe startproject mysite .`
- 生成核心入口文件：`manage.py`
- 生成项目配置目录：`mysite/`
- 检查生成的初始配置文件：
  - `mysite/settings.py`
  - `mysite/urls.py`
  - `mysite/asgi.py`
  - `mysite/wsgi.py`

### 本阶段新增文件

- `manage.py`
- `mysite/__init__.py`
- `mysite/asgi.py`
- `mysite/settings.py`
- `mysite/urls.py`
- `mysite/wsgi.py`

## 步骤 4：创建 polls 应用并补全教程主体代码

- 创建应用：`.\.venv\Scripts\python.exe manage.py startapp polls`
- 修改 `mysite/settings.py`
  - 将 `polls.apps.PollsConfig` 加入 `INSTALLED_APPS`
  - 设置 `LANGUAGE_CODE = "zh-hans"`
  - 设置 `TIME_ZONE = "Asia/Shanghai"`
- 修改 `mysite/urls.py`
  - 挂载 `polls/` 路由
- 编写 `polls/models.py`
  - 创建 `Question`
  - 创建 `Choice`
  - 实现 `__str__()`
  - 实现 `was_published_recently()`
- 编写 `polls/views.py`
  - 使用泛型视图实现 `IndexView`
  - 使用泛型视图实现 `DetailView`
  - 使用泛型视图实现 `ResultsView`
  - 实现 `vote()` 提交逻辑
- 新增 `polls/urls.py`
  - 配置 `index`
  - 配置 `detail`
  - 配置 `results`
  - 配置 `vote`
- 编写模板
  - `polls/templates/polls/index.html`
  - `polls/templates/polls/detail.html`
  - `polls/templates/polls/results.html`
- 编写后台管理
  - `polls/admin.py`
  - 配置 `ChoiceInline`
  - 配置 `QuestionAdmin`
  - 配置 `fieldsets`、`list_display`、`list_filter`、`search_fields`
- 编写测试
  - `polls/tests.py`
  - 覆盖模型测试、列表页测试、详情页测试
- 编写静态文件
  - `polls/static/polls/style.css`
  - `polls/static/polls/images/background.gif`
- 新增工程辅助文件
  - `.gitignore`
  - `requirements.txt`

### 本阶段新增或修改文件

- `.gitignore`
- `requirements.txt`
- `mysite/settings.py`
- `mysite/urls.py`
- `polls/__init__.py`
- `polls/admin.py`
- `polls/apps.py`
- `polls/models.py`
- `polls/tests.py`
- `polls/views.py`
- `polls/urls.py`
- `polls/templates/polls/index.html`
- `polls/templates/polls/detail.html`
- `polls/templates/polls/results.html`
- `polls/static/polls/style.css`
- `polls/static/polls/images/background.gif`
- `polls/migrations/__init__.py`

## 步骤 5：接入第 8 部分第三方包 django-debug-toolbar

- 根据 Django Tutorial 第 8 部分与官方安装文档，安装第三方调试工具栏。
- 在 `requirements.txt` 中加入：`django-debug-toolbar==6.2.0`
- 执行安装：`.\.venv\Scripts\python.exe -m pip install -r requirements.txt`
- 修改 `mysite/settings.py`
  - 新增 `TESTING = "test" in sys.argv`
  - 非测试环境下自动将 `debug_toolbar` 加入 `INSTALLED_APPS`
  - 非测试环境下自动将 `debug_toolbar.middleware.DebugToolbarMiddleware` 加入 `MIDDLEWARE`
  - 新增 `INTERNAL_IPS = ["127.0.0.1"]`
  - 针对 Windows 静态资源 MIME 类型问题，增加：
    - `import mimetypes`
    - `mimetypes.add_type("application/javascript", ".js", True)`
- 修改 `mysite/urls.py`
  - 非测试环境下通过 `debug_toolbar_urls()` 注入 `__debug__/` 调试路由

### 本阶段修改文件

- `requirements.txt`
- `mysite/settings.py`
- `mysite/urls.py`

## 步骤 6：生成迁移并初始化数据库

- 生成应用迁移：`.\.venv\Scripts\python.exe manage.py makemigrations polls`
- 成功生成：
  - `polls/migrations/0001_initial.py`
- 执行数据库迁移：`.\.venv\Scripts\python.exe manage.py migrate`
- 成功应用内置应用与 `polls` 的所有迁移
- 生成 SQLite 数据库文件：`db.sqlite3`

### 本阶段新增文件

- `polls/migrations/0001_initial.py`
- `db.sqlite3`

## 步骤 7：执行自动化测试

- 执行命令：`.\.venv\Scripts\python.exe manage.py test`
- 测试结果：
  - 发现测试数：`10`
  - 结果：`OK`
- 说明：
  - `Question.was_published_recently()` 的未来时间、过旧时间、最近时间逻辑均通过
  - `index` 页面只展示已发布投票的逻辑通过
  - `detail` 页面对未来投票返回 404 的逻辑通过

## 步骤 8：创建后台账户与示例数据

- 创建后台超级用户
  - 用户名：`admin`
  - 邮箱：`admin@example.com`
  - 密码：`Admin123456!`
- 使用 `manage.py shell -c` 写入示例问题与选项
  - 问题：`What's new in Django 6.0?`
  - 选项 1：`Async support improvements`
  - 选项 2：`Better admin experience`
  - 选项 3：`Cleaner tutorial flow`
- 示例问题创建结果：`question_id=2`

## 步骤 9：运行服务并进行页面联通性验证

- 启动本地开发服务器：
  - `.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000 --noreload`
- 使用 PowerShell 请求页面进行验证
- 验证结果：
  - `http://127.0.0.1:8000/polls/` 返回 `200`
  - `http://127.0.0.1:8000/admin/login/` 返回 `200`
- 说明：
  - 项目已可正常启动
  - 投票页与后台登录页已可访问

## 步骤 10：过程中的异常与处理

- 异常 1：
  - 初次使用 `manage.py shell` 通过标准输入传入脚本时，当前环境进入了交互控制台，导致脚本没有按预期一次性执行。
- 处理方式：
  - 改为使用 `manage.py shell -c "..."` 重新执行。
- 影响评估：
  - 不影响后续步骤，问题已解决。

- 异常 2：
  - 当前目录不是 Git 仓库，执行 `git status --short` 时提示 `fatal: not a git repository`
- 处理方式：
  - 未强行初始化 Git，因为这不是完成 tutorial 的必要条件。
- 影响评估：
  - 不影响项目运行、测试和作业交付。

## 当前项目文件清单

- `.gitignore`
- `demo.md`
- `requirements.txt`
- `manage.py`
- `db.sqlite3`
- `mysite/__init__.py`
- `mysite/asgi.py`
- `mysite/settings.py`
- `mysite/urls.py`
- `mysite/wsgi.py`
- `polls/__init__.py`
- `polls/admin.py`
- `polls/apps.py`
- `polls/models.py`
- `polls/tests.py`
- `polls/views.py`
- `polls/urls.py`
- `polls/migrations/__init__.py`
- `polls/migrations/0001_initial.py`
- `polls/templates/polls/index.html`
- `polls/templates/polls/detail.html`
- `polls/templates/polls/results.html`
- `polls/static/polls/style.css`
- `polls/static/polls/images/background.gif`

## 最终状态

- Django 官方 tutorial 主体项目已完成。
- 第 1 到第 7 部分所需的 `polls` 项目结构、模型、视图、模板、后台、测试、静态文件均已完成。
- 第 8 部分第三方包 `django-debug-toolbar` 已安装并接入项目。
- 数据库迁移已完成。
- 自动化测试已全部通过。
- 本地开发服务器已验证可以启动。

## 步骤 11：修复根路径 404

- 问题现象：
  - 访问 `http://127.0.0.1:8000/` 时出现 404
- 问题原因：
  - 项目只配置了 `polls/`、`admin/` 和 `__debug__/` 路由，根路径 `/` 没有匹配规则
- 处理方式：
  - 修改 `mysite/urls.py`
  - 为根路径 `""` 增加跳转逻辑，自动重定向到 `polls:index`
- 修复结果：
  - 访问根路径 `/` 会自动跳转到 `/polls/`

## 步骤 12：清理重复示例数据

- 问题现象：
  - `polls/` 页面出现两条几乎相同的投票问题
- 排查结果：
  - 数据库中存在两条记录：
    - `id=1`：`What's new in Django 6.0?`
    - `id=2`：`Whats new in Django 6.0?`
- 问题原因：
  - 之前通过命令行写入示例数据时执行过两次，且其中一次题目文本缺少撇号，导致生成了重复记录
- 处理方式：
  - 保留 `id=1` 的正确记录
  - 删除 `id=2` 的重复记录
- 修复结果：
  - 投票列表页只保留一条规范的示例问题

## 步骤 13：修复详情页访问与优化首页展示

- 问题现象：
  - 用户访问 `http://127.0.0.1:8000/polls/1` 时显示 `Not Found`
  - 首页列表页展示过于简陋，只有一行链接，不利于作业展示
- 排查结果：
  - 路由主规则使用的是带斜杠形式：`/polls/1/`
  - 用户访问的是不带末尾斜杠的地址：`/polls/1`
- 处理方式：
  - 在 `polls/urls.py` 中增加不带末尾斜杠的兼容路由
  - 优化 `polls/templates/polls/index.html`，增加标题、说明文案和更完整的页面结构
  - 优化 `polls/templates/polls/detail.html` 与 `polls/templates/polls/results.html`
  - 优化 `polls/static/polls/style.css`，让首页更适合作业展示
- 修复结果：
  - `polls/1` 和 `polls/1/` 都可以访问
  - 首页从教程极简样式调整为更完整的展示页

## 步骤 14：同步测试文案并补全示例选项

- 问题现象：
  - 页面文案改成中文后，自动化测试仍在检查英文提示语
  - 当前示例问题缺少可投票选项，详情页功能展示不完整
- 处理方式：
  - 修改 `polls/tests.py`，将空状态断言更新为中文文案
  - 给现有示例问题补充 3 个选项
- 修复结果：
  - 测试与页面展示保持一致
  - 详情页可正常显示并提交投票

## 步骤 15：升级为双语投票站并重构页面结构

- 目标：
  - 让页面更适合作业展示，而不是保留 tutorial 的最简页面
  - 支持中英双语切换
  - 丰富投票内容，提升互动性
- 处理方式：
  - 扩展 `Question` 和 `Choice` 模型，增加英文标题与描述字段
  - 新增 `polls/templates/polls/base.html` 作为统一布局模板
  - 重写首页、详情页、结果页模板
  - 新增 `polls/static/polls/app.js`，通过 `localStorage` 保存中英切换状态
  - 重写 `polls/static/polls/style.css`，升级为卡片化、玻璃拟态风格界面
  - 在结果页加入投票比例条形图
- 本阶段新增或修改文件：
  - `polls/models.py`
  - `polls/admin.py`
  - `polls/views.py`
  - `polls/templates/polls/base.html`
  - `polls/templates/polls/index.html`
  - `polls/templates/polls/detail.html`
  - `polls/templates/polls/results.html`
  - `polls/static/polls/style.css`
  - `polls/static/polls/app.js`

## 步骤 16：新增可重复执行的示例数据命令

- 目标：
  - 批量生成多组安全、轻松、适合展示的投票内容
- 处理方式：
  - 新增 Django 自定义命令：`python manage.py seed_polls`
  - 命令会清空现有投票题目并重建一组新的双语示例投票
- 题目方向：
  - 周末方式
  - 饮品选择
  - 额外一小时如何使用
  - 旅行准备
  - 学习陪伴方式
  - 日常小确幸
- 参考原则：
  - 只采用轻松、日常、无争议方向
  - 适配知乎社区常见的学习、生活、兴趣类讨论氛围
- 新增文件：
  - `polls/management/__init__.py`
  - `polls/management/commands/__init__.py`
  - `polls/management/commands/seed_polls.py`

## 步骤 17：执行双语字段迁移并写入新投票数据

- 执行迁移：
  - `python manage.py makemigrations polls`
  - `python manage.py migrate`
- 新生成迁移文件：
  - `polls/migrations/0002_choice_choice_text_en_question_description_and_more.py`
- 执行示例数据命令：
  - `python manage.py seed_polls`
- 写入结果：
  - 共生成 `6` 组双语投票
  - 共生成 `24` 个投票选项

## 步骤 18：最终校验

- 执行检查：
  - `python manage.py check`
  - `python manage.py test`
- 验证结果：
  - 系统检查通过
  - 自动化测试 `10` 项全部通过
- 页面联通性验证：
  - `/polls/` 返回 `200`
  - 首页渲染 `6` 个投票卡片
  - `/polls/2/` 返回 `200`
  - `/polls/2/results/` 返回 `200`
  - 首页检测到语言切换按钮 `lang-toggle`

## 本轮升级后的作业亮点

- 保留 Django 官方 tutorial 的核心结构和功能
- 将前端从教程极简页面升级为更完整的展示型界面
- 支持中英双语切换
- 投票内容扩展为多组轻松、日常、无争议话题
- 通过 `seed_polls` 命令可以重复生成演示数据，便于作业展示和验收

## 步骤 19：补全文档、许可证与作者信息

- 新增或更新文档：
  - `README.md`
  - `README.en.md`
  - `LICENSE`
  - `demo.md`
- 文档中补充的信息：
  - 作者姓名：倪家诚 / Ni Jiacheng
  - 日期：2026-03-31
  - 项目启动方式
  - 管理后台账号信息
  - Apache License 2.0 许可证说明

## 当前后台账号

- 用户名：`admin`
- 密码：`Admin123456!`

## 步骤 20：初始化 Git 并上传到 GitHub

- 初始化本地 Git 仓库：
  - `git init -b main`
- 检查本机 Git 配置：
  - 用户名：`Ni`
  - 邮箱：`2561889884@qq.com`
- 创建首个提交：
  - `git add .`
  - `git commit -m "Initial Django tutorial bilingual polls project"`
- 通过 GitHub API 新建远端仓库：
  - 仓库名：`django-tutorial-pulse-polls`
  - GitHub 用户：`XXYoLoong`
  - 仓库地址：`https://github.com/XXYoLoong/django-tutorial-pulse-polls`
- 配置远端并推送：
  - `git remote add origin https://github.com/XXYoLoong/django-tutorial-pulse-polls.git`
  - `git push -u origin main`
- 结果：
  - 本地 `main` 分支已成功推送到 GitHub
  - `origin/main` 已建立追踪关系

## 当前交付状态

- 项目代码已整理为 Git 仓库
- GitHub 远端仓库已创建并推送完成
- `README.md`、`README.en.md`、`demo.md`、`LICENSE` 已补齐
- 作者和日期信息已写入文档
