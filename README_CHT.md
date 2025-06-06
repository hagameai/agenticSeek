# AgenticSeek：私有、本地的 Manus 替代方案

[English](./README.md) | 中文 | [繁體中文](./README_CHT.md) | [Français](./README_FR.md) | [日本語](./README_JP.md) | [Português (Brasil)](./README_PTBR.md)

*一個**100%本地運行的 Manus AI 替代品**，支持語音的 AI 助手，可自主瀏覽網頁、編寫代碼、規劃任務，所有數據僅保存在你的設備上。專為本地推理模型設計，完全在你的硬件上運行，確保隱私無憂，無需雲端依賴。*

[![訪問 AgenticSeek](https://img.shields.io/static/v1?label=Website&message=AgenticSeek&color=blue&style=flat-square)](https://fosowl.github.io/agenticSeek.html) ![License](https://img.shields.io/badge/license-GPL--3.0-green) [![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.gg/8hGDaME3TC) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/fosowl.svg?style=social&label=Update%20%40Fosowl)](https://x.com/Martin993886460) [![GitHub stars](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=social)](https://github.com/Fosowl/agenticSeek/stargazers)

### 為什麼選擇 AgenticSeek？

* 🔒 完全本地 & 私有 —— 所有內容都在你的電腦上運行，無雲端、無數據共享。你的文件、對話和搜索都保持私密。

* 🌐 智能網頁瀏覽 —— AgenticSeek 可自主瀏覽互聯網：搜索、閱讀、提取信息、填寫網頁表單，全程免手動。

* 💻 自動化編程助手 —— 需要代碼？它能編寫、調試並運行 Python、C、Go、Java 等程序，無需監督。

* 🧠 智能代理選擇 —— 你提問，它自動判斷最合適的代理來完成任務。就像有一支專家團隊隨時待命。

* 📋 規劃並執行複雜任務 —— 從旅行規劃到複雜項目，可將大任務拆分為步驟，調用多個 AI 代理協作完成。

* 🎙️ 語音支持 —— 乾淨、快速、未來感的語音與語音轉文本功能，讓你像科幻電影中的 AI 一樣與它對話。（開發中）

### **演示**

> *你能搜索 agenticSeek 項目，了解需要哪些技能，然後打開 CV_candidates.zip 並告訴我哪些最匹配該項目嗎？*

https://github.com/user-attachments/assets/b8ca60e9-7b3b-4533-840e-08f9ac426316

免責聲明：本演示及出現的所有文件（如 CV_candidates.zip）均為虛構。我們不是公司，只尋求開源貢獻者而非候選人。

> 🛠⚠️️ **項目正在積極開發中**

> 🙏 本項目起初只是一個副業，沒有路線圖也沒有資金支持。它意外地登上了 GitHub Trending。非常感謝大家的貢獻、反饋與耐心。

## 前置條件

請確保已安裝 chrome driver、docker 和 python3.10。

如遇 chrome driver 相關問題，請參見 **Chromedriver** 部分。

### 1. **克隆倉庫並初始化**

```sh
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

### 2. 修改 .env 文件內容

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

**API Key 完全可選，若你選擇本地運行 LLM（本項目主要目的），可留空，只要硬件足夠。**

以下環境變量用於配置應用的連接和 API 密鑰。

根據需要更新 `.env` 文件：

- **SEARXNG_BASE_URL**：保持不變
- **REDIS_BASE_URL**：保持不變
- **WORK_DIR**：本地工作目錄路徑，AgenticSeek 可讀取和操作這些文件
- **OLLAMA_PORT**：Ollama 服務端口
- **LM_STUDIO_PORT**：LM Studio 服務端口
- **CUSTOM_ADDITIONAL_LLM_PORT**：自定義 LLM 服務端口

下方所有 API 密鑰環境變量均為**可選**，僅在你打算使用外部 API 而非本地 LLM 時填寫。

### 3. **啟動 Docker**

確保已安裝並運行 Docker。可通過以下命令啟動：

- **Linux/macOS：**
打開終端運行：
```sh
sudo systemctl start docker
```
或在應用菜單啟動 Docker Desktop。

- **Windows：**
在開始菜單啟動 Docker Desktop。

驗證 Docker 是否運行：

```sh
docker info
```
如能看到 Docker 信息，則運行正常。

---

## 本地運行 LLM 的設置

**硬件要求：**

本地運行 LLM 需有足夠硬件。至少需支持 Qwen/Deepseek 14B 的 GPU。詳細模型/性能建議見 FAQ。

**啟動本地 provider**

以 ollama 為例，啟動本地 provider：

```sh
ollama serve
```

下方有本地支持的 provider 列表。

**修改 config.ini**

將 config.ini 文件中的 provider_name 設置為支持的 provider，provider_model 設置為 provider 支持的 LLM。推薦推理模型如 *Qwen* 或 *Deepseek*。

詳細硬件要求見 README 末尾 FAQ。

```sh
[MAIN]
is_local = True # 是否本地運行
provider_name = ollama # 或 lm-studio、openai 等
provider_model = deepseek-r1:14b # 選擇適合硬件的模型
provider_server_address = 127.0.0.1:11434
agent_name = Jarvis # AI 名稱
recover_last_session = True # 是否恢復上次會話
save_session = True # 是否保存當前會話
speak = False # 語音輸出
listen = False # 語音輸入，僅 CLI，實驗性
jarvis_personality = False # 是否使用 Jarvis 風格（實驗性）
languages = en zh # 語言列表，語音默認第一個
[BROWSER]
headless_browser = True # 除非 CLI，否則保持不變
stealth_mode = True # 使用 undetected selenium 降低被檢測概率
```

**警告：**

- `config.ini` 不支持註釋。不要直接複製示例配置，否則註釋會導致錯誤。請手動修改 config.ini，去除註釋。

- 若用 LM-studio 運行 LLM，provider_name 不要設為 `openai`，應設為 `lm-studio`。

- 某些 provider（如 lm-studio）要求 IP 前加 `http://`，如 `http://127.0.0.1:1234`

**本地 provider 列表**

| Provider | 本地？ | 說明 |
|-----------|--------|----------------------------------------------------|
| ollama | 是 | 使用 ollama 本地運行 LLM |
| lm-studio | 是 | 使用 LM studio 本地運行 LLM（provider_name 設為 lm-studio）|
| openai | 是 | 使用 openai 兼容 API（如 llama.cpp server） |

下一步：[啟動服務並運行 AgenticSeek](#Start-services-and-Run)

*如遇問題見**已知問題**部分*

*硬件無法本地運行 deepseek 時見**API 運行**部分*

*詳細配置說明見**Config**部分*

---

## 使用 API 運行設置

**API 運行為可選，見上方本地運行方法。**

在 `config.ini` 設置所需 provider。API provider 列表如下。

```sh
[MAIN]
is_local = False
provider_name = google
provider_model = gemini-2.0-flash
provider_server_address = 127.0.0.1:5000 # 無關緊要
```
警告：確保 config 中無多餘空格。

導出 API key：`export <>_API_KEY="xxx"`

示例：`export TOGETHER_API_KEY="xxxxx"`

**API provider 列表**

| Provider | 本地？ | 說明 |
|-----------|--------|----------------------------------------------------|
| openai | 視情況 | 使用 ChatGPT API |
| deepseek | 否 | Deepseek API（非私有） |
| huggingface| 否 | Hugging-Face API（非私有） |
| togetherAI | 否 | 使用 together AI API（非私有） |
| google | 否 | 使用 google gemini API（非私有） |

注意：使用 gemini 時代碼/bash 可能失敗，模型對格式提示不敏感，優化針對 deepseek r1。gpt-4o 在本項目 prompt 下表現也較差。

下一步：[啟動服務並運行 AgenticSeek](#Start-services-and-Run)

*如遇問題見**已知問題**部分*

*詳細配置說明見**Config**部分*

---

## 啟動服務並運行

啟動所需服務。此操作會啟動 docker-compose.yml 中的所有服務，包括：
- searxng
- redis（searxng 依賴）
- frontend
- backend（如用 `full`）

```sh
./start_services.sh full # MacOS
start ./start_services.cmd full # Windows
```

**警告：** 此步驟會下載並加載所有 Docker 鏡像，可能需 30 分鐘。啟動后請等待 backend 服務完全運行（日誌中出現 backend: ），再發送消息。backend 啟動比其他服務慢。

訪問 `http://localhost:3000/`，即可看到網頁界面。

**可選：使用 CLI 界面運行：**

如需 CLI 界面，需在主機安裝依賴：

```sh
./install.sh
./install.bat # windows
```

啟動服務：

```sh
./start_services.sh # MacOS
start ./start_services.cmd # Windows
```

然後運行：`python3 cli.py`

---

## 使用方法

確保服務已通過 `./start_services.sh full` 啟動，並訪問 `localhost:3000` 使用網頁界面。

CLI 模式下可通過設置 `listen = True` 啟用語音轉文本。

退出時，只需說/輸入 `goodbye`。

以下為示例用法：

> *用 python 寫一個貪吃蛇遊戲！*

> *搜索法國雷恩的最佳咖啡館，並將三家及其地址保存到 rennes_cafes.txt。*

> *寫一個 Go 程序計算階乘，保存為 factorial.go 到你的工作區*

> *在 summer_pictures 文件夾中查找所有 JPG 文件，用今天日期重命名，並將重命名文件列表保存到 photos_list.txt*

> *在線搜索 2024 年熱門科幻電影，挑選三部今晚觀看，保存到 movie_night.txt。*

> *搜索 2025 年最新 AI 新聞文章，選三篇，寫 Python 腳本抓取標題和摘要，腳本保存為 news_scraper.py，摘要保存到 ai_news.txt（/home/projects）*

> *周五，搜索免費股票價格 API，用 supersuper7434567@gmail.com 註冊，然後寫 Python 腳本每日獲取特斯拉股價，結果保存到 stock_prices.csv*

*表單填寫功能仍為實驗性，可能失敗。*

輸入查詢后，AgenticSeek 會自動分配最佳代理執行任務。

由於目前為早期原型，代理路由系統可能無法總是正確分配代理。

因此，建議明確表達需求及 AI 執行方式。例如需網頁搜索時，不要說：

`你知道哪些適合獨自旅行的國家嗎？`

而應說：

`請進行網頁搜索，找出最適合獨自旅行的國家`

---

## **在自有服務器運行 LLM 的設置**

如有高性能電腦或服務器，可用自定義 llm server 遠程運行 LLM。

在運行 AI 模型的“服務器”上獲取 IP 地址：

```sh
ip a | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 # 本地 IP
curl https://ipinfo.io/ip # 公網 IP
```

註：Windows/macOS 可用 ipconfig 或 ifconfig 查詢 IP。

克隆倉庫並進入 `server/` 文件夾：

```sh
git clone --depth 1 https://github.com/Fosowl/agenticSeek.git
cd agenticSeek/llm_server/
```

安裝服務器依賴：

```sh
pip3 install -r requirements.txt
```

運行服務器腳本：

```sh
python3 app.py --provider ollama --port 3333
```

可選擇 `ollama` 或 `llamacpp` 作為 LLM 服務。

在你的個人電腦上：

修改 `config.ini`，將 `provider_name` 設為 `server`，`provider_model` 設為 `deepseek-r1:xxb`。
`provider_server_address` 設為運行模型機器的 IP。

```sh
[MAIN]
is_local = False
provider_name = server
provider_model = deepseek-r1:70b
provider_server_address = x.x.x.x:3333
```

下一步：[啟動服務並運行 AgenticSeek](#Start-services-and-Run)

---

## 語音轉文本

警告：目前僅 CLI 模式支持語音轉文本。

目前僅支持英文語音轉文本。

默認關閉語音轉文本。啟用方法：在 config.ini 設置 listen 為 True：

```
listen = True
```

啟用后，語音轉文本會監聽觸發詞（即 agent 名稱），再開始處理輸入。可通過修改 *config.ini* 的 `agent_name` 自定義：

```
agent_name = Friday
```

建議使用常見英文名如 "John" 或 "Emma" 作為 agent 名稱。

看到轉錄開始出現后，呼叫 agent 名稱喚醒（如“Friday”）。

清晰說出你的請求。

以確認短語結尾，表示系統可繼續處理。例如：
```
"do it", "go ahead", "execute", "run", "start", "thanks", "would ya", "please", "okay?", "proceed", "continue", "go on", "do that", "go it", "do you understand?"
```

## 配置說明

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

**說明：**

- is_local -> 本地運行（True）或遠程服務器（False）

- provider_name -> 使用的 provider（如：`ollama`、`server`、`lm-studio`、`deepseek-api`）

- provider_model -> 使用的模型，如 deepseek-r1:32b

- provider_server_address -> 服務器地址，如 127.0.0.1:11434（本地），API 可隨意

- agent_name -> 代理名稱，如 Friday，語音喚醒詞

- recover_last_session -> 是否恢復上次會話（True/False）

- save_session -> 是否保存會話數據（True/False）

- speak -> 是否啟用語音輸出（True/False）

- listen -> 是否啟用語音輸入（True/False）

- jarvis_personality -> 是否使用 JARVIS 風格（True/False），僅更換 prompt

- languages -> 支持語言列表，供 LLM 路由使用，建議不要太多或太相似

- headless_browser -> 是否無頭瀏覽器（True/False）

- stealth_mode -> 是否降低被檢測概率，需手動安裝 anticaptcha 擴展

- languages -> 支持語言列表，代理路由系統需用，列表越長下載模型越多

## Provider 列表

下表為可用 provider：

| Provider | 本地？ | 說明 |
|-----------|--------|----------------------------------------------------|
| ollama | 是 | 使用 ollama 本地運行 LLM |
| server | 是 | 在其他機器託管模型，本機調用 |
| lm-studio | 是 | 使用 LM studio 本地運行 LLM（provider_name 設為 lm-studio）|
| openai | 視情況 | 使用 ChatGPT API（非私有）或 openai 兼容 API |
| deepseek-api | 否 | Deepseek API（非私有） |
| huggingface| 否 | Hugging-Face API（非私有） |
| togetherAI | 否 | 使用 together AI API（非私有） |
| google | 否 | 使用 google gemini API（非私有） |

選擇 provider 時修改 config.ini：

```
is_local = True
provider_name = ollama
provider_model = deepseek-r1:32b
provider_server_address = 127.0.0.1:5000
```
`is_local`：本地 LLM 設為 True，否則 False。

`provider_name`：選擇 provider 名稱，見上表。

`provider_model`：設置代理使用的模型。

`provider_server_address`：如非 server provider，可隨意。

# 已知問題

## Chromedriver 問題

**已知錯誤 #1：** *chromedriver 不匹配*

`Exception: Failed to initialize browser: Message: session not created: This version of ChromeDriver only supports Chrome version 113
Current browser version is 134.0.6998.89 with binary path`

出現此問題是瀏覽器與 chromedriver 版本不匹配。

需下載最新版本：

https://developer.chrome.com/docs/chromedriver/downloads

如用 Chrome 115 及以上，訪問：

https://googlechromelabs.github.io/chrome-for-testing/

下載與你操作系統匹配的 chromedriver。

![alt text](./media/chromedriver_readme.png)

如本節不全請提交 issue。

## 連接適配器問題

```
Exception: Provider lm-studio failed: HTTP request failed: No connection adapters were found for '127.0.0.1:11434/v1/chat/completions'
```

請確保 provider IP 前加 `http://`：

`provider_server_address = http://127.0.0.1:11434`

## SearxNG base URL 必須提供

```
raise ValueError("SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.")
ValueError: SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.
```

可能未將 `.env.example` 重命名為 `.env`？也可導出 SEARXNG_BASE_URL：

`export SEARXNG_BASE_URL="http://127.0.0.1:8080"`

## FAQ

**Q: 需要什麼硬件？**

| 模型規模 | GPU | 說明 |
|-----------|--------|----------------------------------------------------|
| 7B | 8GB 顯存 | ⚠️ 不推薦。性能差，易幻覺，規劃代理易失敗。 |
| 14B | 12GB 顯存（如 RTX 3060） | ✅ 簡單任務可用，網頁瀏覽和規劃任務可能吃力。|
| 32B | 24GB+ 顯存（如 RTX 4090） | 🚀 大多數任務成功，複雜規劃仍有難度。 |
| 70B+ | 48GB+ 顯存（如 mac studio） | 💪 推薦，高級用例表現優異。 |

**Q: 為什麼選 Deepseek R1？**

Deepseek R1 在推理和工具調用方面表現優異。我們認為它非常適合本項目，其他模型也可用，但 Deepseek 是首選。

**Q: 運行 `cli.py` 報錯怎麼辦？**

確保本地服務（`ollama serve`）已啟動，`config.ini` 配置正確，依賴已安裝。如仍有問題歡迎提交 issue。

**Q: 真能 100% 本地運行嗎？**

是的，使用 Ollama、lm-studio 或 server provider 時，語音、LLM、語音轉文本均本地運行。非本地（OpenAI 等 API）為可選。

**Q: 有 Manus 為什麼還要用 AgenticSeek？**

本項目起初只是興趣驅動的副業。特別之處在於主打本地模型，避免 API。
靈感來自 Jarvis 和 Friday（鋼鐵俠），功能上更接近 Manus，因為大家最想要的是本地 manus 替代品。
與 Manus 不同，AgenticSeek 更注重獨立性、隱私和避免 API 成本。

## 貢獻

我們歡迎開發者改進 AgenticSeek！請查看 open issues 或討論區。

[貢獻指南](./docs/CONTRIBUTING.md)

[![Star History Chart](https://api.star-history.com/svg?repos=Fosowl/agenticSeek&type=Date)](https://www.star-history.com/#Fosowl/agenticSeek&Date)

## 維護者：

> [Fosowl](https://github.com/Fosowl) | 巴黎時間

> [antoineVIVIES](https://github.com/antoineVIVIES) | 台北時間

> [steveh8758](https://github.com/steveh8758) | 台北時間

## 特別感謝：

> [tcsenpai](https://github.com/tcsenpai) 和 [plitc](https://github.com/plitc) 協助後端 docker 化