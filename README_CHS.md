# AgenticSeek：私有、本地的 Manus 替代方案

<p align="center">
<img align="center" src="./media/agentic_seek_logo.png" width="300" height="300" alt="Agentic Seek Logo">
<p>

    [English](./README.md) | 中文 | [繁體中文](./README_CHT.md) | [Français](./README_FR.md) | [日本語](./README_JP.md) | [Português (Brasil)](./README_PTBR.md)

*一个**100%本地运行的 Manus AI 替代品**，支持语音的 AI 助手，可自主浏览网页、编写代码、规划任务，所有数据仅保存在你的设备上。专为本地推理模型设计，完全在你的硬件上运行，确保隐私无忧，无需云端依赖。*

[![访问 AgenticSeek](https://img.shields.io/static/v1?label=Website&message=AgenticSeek&color=blue&style=flat-square)](https://fosowl.github.io/agenticSeek.html) ![License](https://img.shields.io/badge/license-GPL--3.0-green) [![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.gg/8hGDaME3TC) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/fosowl.svg?style=social&label=Update%20%40Fosowl)](https://x.com/Martin993886460) [![GitHub stars](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=social)](https://github.com/Fosowl/agenticSeek/stargazers)

### 为什么选择 AgenticSeek？

* 🔒 完全本地 & 私有 —— 所有内容都在你的电脑上运行，无云端、无数据共享。你的文件、对话和搜索都保持私密。

* 🌐 智能网页浏览 —— AgenticSeek 可自主浏览互联网：搜索、阅读、提取信息、填写网页表单，全程免手动。

* 💻 自动化编程助手 —— 需要代码？它能编写、调试并运行 Python、C、Go、Java 等程序，无需监督。

* 🧠 智能代理选择 —— 你提问，它自动判断最合适的代理来完成任务。就像有一支专家团队随时待命。

* 📋 规划并执行复杂任务 —— 从旅行规划到复杂项目，可将大任务拆分为步骤，调用多个 AI 代理协作完成。

* 🎙️ 语音支持 —— 干净、快速、未来感的语音与语音转文本功能，让你像科幻电影中的 AI 一样与它对话。（开发中）

### **演示**

> *你能搜索 agenticSeek 项目，了解需要哪些技能，然后打开 CV_candidates.zip 并告诉我哪些最匹配该项目吗？*

https://github.com/user-attachments/assets/b8ca60e9-7b3b-4533-840e-08f9ac426316

免责声明：本演示及出现的所有文件（如 CV_candidates.zip）均为虚构。我们不是公司，只寻求开源贡献者而非候选人。

> 🛠⚠️️ **项目正在积极开发中**

> 🙏 本项目起初只是一个副业，没有路线图也没有资金支持。它意外地登上了 GitHub Trending。非常感谢大家的贡献、反馈与耐心。

## 前置条件

请确保已安装 chrome driver、docker 和 python3.10。

如遇 chrome driver 相关问题，请参见 **Chromedriver** 部分。

### 1. **克隆仓库并初始化**

```sh
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

### 2. 修改 .env 文件内容

```sh
SEARXNG_BASE_URL="http://127.0.0.1:8080"
REDIS_BASE_URL="redis://redis:6379/0"
WORK_DIR="/Users/mlg/Documents/workspace_for_ai"
OLLAMA_PORT="11434"
LM_STUDIO_PORT="1234"
CUSTOM_ADDITIONAL_LLM_PORT="11435"
OPENAI_API_KEY='optional'
DEEPSEEK_API_KEY='optional'
OPENROUTER_API_KEY='optional'
TOGETHER_API_KEY='optional'
GOOGLE_API_KEY='optional'
ANTHROPIC_API_KEY='optional'
```

**API Key 完全可选，若你选择本地运行 LLM（本项目主要目的），可留空，只要硬件足够。**

以下环境变量用于配置应用的连接和 API 密钥。

根据需要更新 `.env` 文件：

- **SEARXNG_BASE_URL**：保持不变
- **REDIS_BASE_URL**：保持不变
- **WORK_DIR**：本地工作目录路径，AgenticSeek 可读取和操作这些文件
- **OLLAMA_PORT**：Ollama 服务端口
- **LM_STUDIO_PORT**：LM Studio 服务端口
- **CUSTOM_ADDITIONAL_LLM_PORT**：自定义 LLM 服务端口

下方所有 API 密钥环境变量均为**可选**，仅在你打算使用外部 API 而非本地 LLM 时填写。

### 3. **启动 Docker**

确保已安装并运行 Docker。可通过以下命令启动：

- **Linux/macOS：**  
        打开终端运行：
        ```sh
        sudo systemctl start docker
        ```
        或在应用菜单启动 Docker Desktop。

- **Windows：**  
        在开始菜单启动 Docker Desktop。

验证 Docker 是否运行：

```sh
docker info
```
如能看到 Docker 信息，则运行正常。

---

## 本地运行 LLM 的设置

**硬件要求：**

本地运行 LLM 需有足够硬件。至少需支持 Qwen/Deepseek 14B 的 GPU。详细模型/性能建议见 FAQ。

**启动本地 provider**  

以 ollama 为例，启动本地 provider：

```sh
ollama serve
```

下方有本地支持的 provider 列表。

**修改 config.ini**

将 config.ini 文件中的 provider_name 设置为支持的 provider，provider_model 设置为 provider 支持的 LLM。推荐推理模型如 *Qwen* 或 *Deepseek*。

详细硬件要求见 README 末尾 FAQ。

```sh
[MAIN]
is_local = True # 是否本地运行
provider_name = ollama # 或 lm-studio、openai 等
provider_model = deepseek-r1:14b # 选择适合硬件的模型
provider_server_address = 127.0.0.1:11434
agent_name = Jarvis # AI 名称
recover_last_session = True # 是否恢复上次会话
save_session = True # 是否保存当前会话
speak = False # 语音输出
listen = False # 语音输入，仅 CLI，实验性
jarvis_personality = False # 是否使用 Jarvis 风格（实验性）
languages = en zh # 语言列表，语音默认第一个
[BROWSER]
headless_browser = True # 除非 CLI，否则保持不变
stealth_mode = True # 使用 undetected selenium 降低被检测概率
```

**警告：**

- `config.ini` 不支持注释。不要直接复制示例配置，否则注释会导致错误。请手动修改 config.ini，去除注释。

- 若用 LM-studio 运行 LLM，provider_name 不要设为 `openai`，应设为 `lm-studio`。

- 某些 provider（如 lm-studio）要求 IP 前加 `http://`，如 `http://127.0.0.1:1234`

**本地 provider 列表**

| Provider  | 本地？ | 说明                                               |
|-----------|--------|----------------------------------------------------|
| ollama    | 是     | 使用 ollama 本地运行 LLM                           |
| lm-studio | 是     | 使用 LM studio 本地运行 LLM（provider_name 设为 lm-studio）|
| openai    | 是     | 使用 openai 兼容 API（如 llama.cpp server）        |

下一步：[启动服务并运行 AgenticSeek](#Start-services-and-Run)  

*如遇问题见**已知问题**部分*

*硬件无法本地运行 deepseek 时见**API 运行**部分*

*详细配置说明见**Config**部分*

---

## 使用 API 运行设置

**API 运行为可选，见上方本地运行方法。**

在 `config.ini` 设置所需 provider。API provider 列表如下。

```sh
[MAIN]
is_local = False
provider_name = google
provider_model = gemini-2.0-flash
provider_server_address = 127.0.0.1:5000 # 无关紧要
```
警告：确保 config 中无多余空格。

导出 API key：`export <<PROVIDER>>_API_KEY="xxx"`

示例：`export TOGETHER_API_KEY="xxxxx"`

**API provider 列表**
    
| Provider  | 本地？ | 说明                                               |
|-----------|--------|----------------------------------------------------|
| openai    | 视情况 | 使用 ChatGPT API  |
| deepseek  | 否     | Deepseek API（非私有）                            |
| huggingface| 否    | Hugging-Face API（非私有）                        |
| togetherAI | 否    | 使用 together AI API（非私有）                    |
| google | 否    | 使用 google gemini API（非私有）                    |

注意：使用 gemini 时代码/bash 可能失败，模型对格式提示不敏感，优化针对 deepseek r1。gpt-4o 在本项目 prompt 下表现也较差。

下一步：[启动服务并运行 AgenticSeek](#Start-services-and-Run)

*如遇问题见**已知问题**部分*

*详细配置说明见**Config**部分*

---

## 启动服务并运行

启动所需服务。此操作会启动 docker-compose.yml 中的所有服务，包括：
        - searxng
        - redis（searxng 依赖）
        - frontend
        - backend（如用 `full`）

```sh
./start_services.sh full # MacOS
start ./start_services.cmd full # Windows
```

**警告：** 此步骤会下载并加载所有 Docker 镜像，可能需 30 分钟。启动后请等待 backend 服务完全运行（日志中出现 backend: <info>），再发送消息。backend 启动比其他服务慢。

访问 `http://localhost:3000/`，即可看到网页界面。

**可选：使用 CLI 界面运行：**

如需 CLI 界面，需在主机安装依赖：

```sh
./install.sh
./install.bat # windows
```

启动服务：

```sh
./start_services.sh # MacOS
start ./start_services.cmd # Windows
```

然后运行：`python3 cli.py`

---

## 使用方法

确保服务已通过 `./start_services.sh full` 启动，并访问 `localhost:3000` 使用网页界面。

CLI 模式下可通过设置 `listen = True` 启用语音转文本。

退出时，只需说/输入 `goodbye`。

以下为示例用法：

> *用 python 写一个贪吃蛇游戏！*

> *搜索法国雷恩的最佳咖啡馆，并将三家及其地址保存到 rennes_cafes.txt。*

> *写一个 Go 程序计算阶乘，保存为 factorial.go 到你的工作区*

> *在 summer_pictures 文件夹中查找所有 JPG 文件，用今天日期重命名，并将重命名文件列表保存到 photos_list.txt*

> *在线搜索 2024 年热门科幻电影，挑选三部今晚观看，保存到 movie_night.txt。*

> *搜索 2025 年最新 AI 新闻文章，选三篇，写 Python 脚本抓取标题和摘要，脚本保存为 news_scraper.py，摘要保存到 ai_news.txt（/home/projects）*

> *周五，搜索免费股票价格 API，用 supersuper7434567@gmail.com 注册，然后写 Python 脚本每日获取特斯拉股价，结果保存到 stock_prices.csv*

*表单填写功能仍为实验性，可能失败。*

输入查询后，AgenticSeek 会自动分配最佳代理执行任务。

由于目前为早期原型，代理路由系统可能无法总是正确分配代理。

因此，建议明确表达需求及 AI 执行方式。例如需网页搜索时，不要说：

`你知道哪些适合独自旅行的国家吗？`

而应说：

`请进行网页搜索，找出最适合独自旅行的国家`

---

## **在自有服务器运行 LLM 的设置**  

如有高性能电脑或服务器，可用自定义 llm server 远程运行 LLM。

在运行 AI 模型的“服务器”上获取 IP 地址：

```sh
ip a | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 # 本地 IP
curl https://ipinfo.io/ip # 公网 IP
```

注：Windows/macOS 可用 ipconfig 或 ifconfig 查询 IP。

克隆仓库并进入 `server/` 文件夹：

```sh
git clone --depth 1 https://github.com/Fosowl/agenticSeek.git
cd agenticSeek/llm_server/
```

安装服务器依赖：

```sh
pip3 install -r requirements.txt
```

运行服务器脚本：

```sh
python3 app.py --provider ollama --port 3333
```

可选择 `ollama` 或 `llamacpp` 作为 LLM 服务。

在你的个人电脑上：

修改 `config.ini`，将 `provider_name` 设为 `server`，`provider_model` 设为 `deepseek-r1:xxb`。
`provider_server_address` 设为运行模型机器的 IP。

```sh
[MAIN]
is_local = False
provider_name = server
provider_model = deepseek-r1:70b
provider_server_address = x.x.x.x:3333
```

下一步：[启动服务并运行 AgenticSeek](#Start-services-and-Run)  

---

## 语音转文本

警告：目前仅 CLI 模式支持语音转文本。

目前仅支持英文语音转文本。

默认关闭语音转文本。启用方法：在 config.ini 设置 listen 为 True：

```
listen = True
```

启用后，语音转文本会监听触发词（即 agent 名称），再开始处理输入。可通过修改 *config.ini* 的 `agent_name` 自定义：

```
agent_name = Friday
```

建议使用常见英文名如 "John" 或 "Emma" 作为 agent 名称。

看到转录开始出现后，呼叫 agent 名称唤醒（如“Friday”）。

清晰说出你的请求。

以确认短语结尾，表示系统可继续处理。例如：
```
"do it", "go ahead", "execute", "run", "start", "thanks", "would ya", "please", "okay?", "proceed", "continue", "go on", "do that", "go it", "do you understand?"
```

## 配置说明

配置示例：
```
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:32b
provider_server_address = 127.0.0.1:11434
agent_name = Friday
recover_last_session = False
save_session = False
speak = False
listen = False
jarvis_personality = False
languages = en zh
[BROWSER]
headless_browser = False
stealth_mode = False
```

**说明：**

- is_local -> 本地运行（True）或远程服务器（False）

- provider_name -> 使用的 provider（如：`ollama`、`server`、`lm-studio`、`deepseek-api`）

- provider_model -> 使用的模型，如 deepseek-r1:32b

- provider_server_address -> 服务器地址，如 127.0.0.1:11434（本地），API 可随意

- agent_name -> 代理名称，如 Friday，语音唤醒词

- recover_last_session -> 是否恢复上次会话（True/False）

- save_session -> 是否保存会话数据（True/False）

- speak -> 是否启用语音输出（True/False）

- listen -> 是否启用语音输入（True/False）

- jarvis_personality -> 是否使用 JARVIS 风格（True/False），仅更换 prompt

- languages -> 支持语言列表，供 LLM 路由使用，建议不要太多或太相似

- headless_browser -> 是否无头浏览器（True/False）

- stealth_mode -> 是否降低被检测概率，需手动安装 anticaptcha 扩展

- languages -> 支持语言列表，代理路由系统需用，列表越长下载模型越多

## Provider 列表

下表为可用 provider：

| Provider  | 本地？ | 说明                                               |
|-----------|--------|----------------------------------------------------|
| ollama    | 是     | 使用 ollama 本地运行 LLM                           |
| server    | 是     | 在其他机器托管模型，本机调用                       |
| lm-studio | 是     | 使用 LM studio 本地运行 LLM（provider_name 设为 lm-studio）|
| openai    | 视情况 | 使用 ChatGPT API（非私有）或 openai 兼容 API       |
| deepseek-api  | 否     | Deepseek API（非私有）                            |
| huggingface| 否    | Hugging-Face API（非私有）                        |
| togetherAI | 否    | 使用 together AI API（非私有）                    |
| google | 否    | 使用 google gemini API（非私有）                    |

选择 provider 时修改 config.ini：

```
is_local = True
provider_name = ollama
provider_model = deepseek-r1:32b
provider_server_address = 127.0.0.1:5000
```
`is_local`：本地 LLM 设为 True，否则 False。

`provider_name`：选择 provider 名称，见上表。

`provider_model`：设置代理使用的模型。

`provider_server_address`：如非 server provider，可随意。

# 已知问题

## Chromedriver 问题

**已知错误 #1：** *chromedriver 不匹配*

`Exception: Failed to initialize browser: Message: session not created: This version of ChromeDriver only supports Chrome version 113
Current browser version is 134.0.6998.89 with binary path`

出现此问题是浏览器与 chromedriver 版本不匹配。

需下载最新版本：

https://developer.chrome.com/docs/chromedriver/downloads

如用 Chrome 115 及以上，访问：

https://googlechromelabs.github.io/chrome-for-testing/

下载与你操作系统匹配的 chromedriver。

![alt text](./media/chromedriver_readme.png)

如本节不全请提交 issue。

## 连接适配器问题

```
Exception: Provider lm-studio failed: HTTP request failed: No connection adapters were found for '127.0.0.1:11434/v1/chat/completions'
```

请确保 provider IP 前加 `http://`：

`provider_server_address = http://127.0.0.1:11434`

## SearxNG base URL 必须提供

```
raise ValueError("SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.")
ValueError: SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.
```

可能未将 `.env.example` 重命名为 `.env`？也可导出 SEARXNG_BASE_URL：

`export  SEARXNG_BASE_URL="http://127.0.0.1:8080"`

## FAQ

**Q: 需要什么硬件？**  

| 模型规模  | GPU  | 说明                                               |
|-----------|--------|----------------------------------------------------|
| 7B        | 8GB 显存 | ⚠️ 不推荐。性能差，易幻觉，规划代理易失败。         |
| 14B        | 12GB 显存（如 RTX 3060） | ✅ 简单任务可用，网页浏览和规划任务可能吃力。|
| 32B        | 24GB+ 显存（如 RTX 4090） | 🚀 大多数任务成功，复杂规划仍有难度。        |
| 70B+        | 48GB+ 显存（如 mac studio） | 💪 推荐，高级用例表现优异。                |

**Q: 为什么选 Deepseek R1？**  

Deepseek R1 在推理和工具调用方面表现优异。我们认为它非常适合本项目，其他模型也可用，但 Deepseek 是首选。

**Q: 运行 `cli.py` 报错怎么办？**  

确保本地服务（`ollama serve`）已启动，`config.ini` 配置正确，依赖已安装。如仍有问题欢迎提交 issue。

**Q: 真能 100% 本地运行吗？**  

是的，使用 Ollama、lm-studio 或 server provider 时，语音、LLM、语音转文本均本地运行。非本地（OpenAI 等 API）为可选。

**Q: 有 Manus 为什么还要用 AgenticSeek？**

本项目起初只是兴趣驱动的副业。特别之处在于主打本地模型，避免 API。
灵感来自 Jarvis 和 Friday（钢铁侠），功能上更接近 Manus，因为大家最想要的是本地 manus 替代品。
与 Manus 不同，AgenticSeek 更注重独立性、隐私和避免 API 成本。

## 贡献

我们欢迎开发者改进 AgenticSeek！请查看 open issues 或讨论区。

[贡献指南](./docs/CONTRIBUTING.md)

[![Star History Chart](https://api.star-history.com/svg?repos=Fosowl/agenticSeek&type=Date)](https://www.star-history.com/#Fosowl/agenticSeek&Date)

## 维护者：

 > [Fosowl](https://github.com/Fosowl) | 巴黎时间 

 > [antoineVIVIES](https://github.com/antoineVIVIES) | 台北时间 

 > [steveh8758](https://github.com/steveh8758) | 台北时间 

## 特别感谢：

 > [tcsenpai](https://github.com/tcsenpai) 和 [plitc](https://github.com/plitc) 协助后端 docker 化

