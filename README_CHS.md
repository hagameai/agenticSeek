<p align="center">
<img align="center" src="./media/whale_readme.jpg">
<p>


[English](./README.md) | 中文 | [日本語](./README_JP.md)

# AgenticSeek: 類似 Manus 但基於 Deepseek R1 Agents 的本地模型。

**Manus AI 的本地替代品**，它是一个具有语音功能的大语言模型秘书，可以 Coding、访问你的电脑文件、浏览网页，并自动修正错误与反省，最重要的是不会向云端传送任何资料。采用 DeepSeek R1 等推理模型构建，完全在本地硬体上运行，进而保证资料的隐私。

[![Visit AgenticSeek](https://img.shields.io/static/v1?label=Website&message=AgenticSeek&color=blue&style=flat-square)](https://fosowl.github.io/agenticSeek.html) ![License](https://img.shields.io/badge/license-GPL--3.0-green) [![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.gg/m37d7XxZ) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/fosowl.svg?style=social&label=Update%20%40Fosowl)](https://x.com/Martin993886460)

> 🛠️ **目前还在开发阶段** – 欢迎任何贡献者加入我们！

https://github.com/user-attachments/assets/4bd5faf6-459f-4f94-bd1d-238c4b331469

> *在大阪和东京深入搜寻人工智慧新创公司，至少找到 5 家，然后储存在 research_japan.txt 档案中*

> *你可以用 C 语言制作俄罗斯方块游戏吗？*

> *我想设定一个新的专案档案索引，命名为 mark2。*



## Features:

- **100% 本机运行**: 本机运行，不使用云端服务，所以资料绝不会散布出去，我的东西还是我的！不会被当作其他服务的训练资料。

- **文件的交互系统**: 使用 bash 去浏览本机资料和操作本机系统。

- **自主 Coding**: AgenticSeek 可以自己运行、Debug、编译 Python、C、Golang 和各种语言。

- **代理助理**: 不同的工作由不同的助理去处理问题。AgenticSeek 会自己寻找最适合的助理去做相对应的工作。

- **规划**: 对于复杂的任务，AgenticSeek 会交办给不同的助理进行规划和执行。

- **自主学习**: 自动在网路上寻找资料。

- **记忆功能**: 对于每次的对话进行统整、保存对话，并且在本地储存用户的使用习惯。

---

## **安装**

确保已安装了 Chrome driver，Docker 和 Python 3.10（或更新）。

有关于 Chrome driver 的问题，请参见 **Chromedriver** 部分。

### 1️⃣ **复制储存库与设置环境变数**

```sh
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

### 2️ **建立虚拟环境**

```sh
python3 -m venv agentic_seek_env
source agentic_seek_env/bin/activate
# On Windows: agentic_seek_env\Scripts\activate
```

### 3️⃣ **安装所需套件**

**自动安装:**

```sh
./install.sh
```

** 若要让文本转语音（TTS）功能支持中文，你需要安装 jieba（中文分词库）和 cn2an（中文数字转换库）：**

```
pip3 install jieba cn2an
```

**手动安装:**

```sh
pip3 install -r requirements.txt
# or
python3 setup.py install
```

## 在本地机器上运行 AgenticSeek

**建议至少使用 Deepseek 14B 以上参数的模型，较小的模型难以使用助理功能并且很快就会忘记上下文之间的关系。**

**本地运行助手**

启动你的本地提供者，例如使用 ollama：

```sh
ollama serve
```

请参阅下方支持的本地提供者列表。

修改 `config.ini` 文件，将 `provider_name` 设置为支持的提供者，并将 `provider_model` 设置为 `deepseek-r1:14b`。

注意：`deepseek-r1:14b` 只是一个示例，如果你的硬件允许，可以使用更大的模型。

```sh
[MAIN]
is_local = True
provider_name = ollama # 或 lm-studio, openai 等
provider_model = deepseek-r1:14b
provider_server_address = 127.0.0.1:11434
```

**本地提供者列表**

| 提供者 | 本地? | 描述 |
|-------------|--------|-------------------------------------------------------|
| ollama | 是 | 使用 ollama 作为 LLM 提供者，轻松本地运行 LLM |
| lm-studio | 是 | 使用 LM Studio 本地运行 LLM（将 `provider_name` 设置为 `lm-studio`）|
| openai | 否 | 使用兼容的 API |

下一步： [Start services and run AgenticSeek](#Start-services-and-Run)

---

## **Run with an API （透过 API 执行）**

设定 `config.ini`。

```sh
[MAIN]
is_local = False
provider_name = openai
provider_model = gpt-4o
provider_server_address = 127.0.0.1:5000
```

警告：确保 `config.ini` 没有行尾空格。

如果使用基于本机的 openai-based api 则把 `is_local` 设定为 `True`。

同时更改你的 IP 为 openai-based api 的 IP。

下一步： [Start services and run AgenticSeek](#Start-services-and-Run)

---

## Start services and Run
(启动服务并运行)

如果需要，请激活你的 Python 环境。
```sh
source agentic_seek_env/bin/activate
```

启动所需的服务。这将启动 `docker-compose.yml` 中的所有服务，包括：
- searxng
- redis（由 redis 提供支持）
- 前端

```sh
sudo ./start_services.sh # MacOS
start ./start_services.cmd # Windows
```

**选项 1:** 使用 CLI 界面运行。

```sh
python3 cli.py
```

**选项 2:** 使用 Web 界面运行。

注意：目前我們建議您使用 CLI 界面。Web 界面仍在積極開發中。

启动后端服务。

```sh
python3 api.py
```

访问 `http://localhost:3000/`，你应该会看到 Web 界面。

请注意，目前 Web 界面不支持消息流式传输。


*如果你不知道如何开始，请参阅 **Usage** 部分*

---

## Usage （使用方法）

为确保 agenticSeek 在中文环境下正常工作，请确保在 config.ini 中设置语言选项。
languages = en zh
更多信息请参阅 Config 部分

确定所有的核心档案都启用了，也就是执行过这条命令 `./start_services.sh` 然后你就可以使用 `python3 cli.py` 来启动 AgenticSeek 了！

```sh
sudo ./start_services.sh
python3 cli.py
```

当你看到执行后显示 `>>> `
这表示一切运作正常，AgenticSeek 正在等待你给他任何指令。
你也可以透过设定 `config.ini` 内的 `listen = True` 来启用语音转文字。

要退出时，只要和他说 `goodbye` 就可以退出！

以下是一些用法：

### Coding/Bash

> *在 Golang 中帮助我进行矩阵乘法*

> *使用 nmap 扫描我的网路，找出是否有任何可疑装置连接*

> *用 Python 制作一个贪食蛇游戏*

### 网路搜寻

> *进行网路搜寻，找出日本从事尖端人工智慧研究的酷炫科技新创公司*

> *你能在网路上找到谁创造了 AgenticSeek 吗？*

> *你能在哪个网站上找到便宜的 RTX 4090 吗？*

### 档案浏览与搜寻

> *嘿，你能找到我遗失的 million_dollars_contract.pdf 在哪里吗？*

> *告诉我我的磁碟还剩下多少空间*

> *寻找并阅读 README.md，并按照安装说明进行操作*

### 日常聊天

> *告诉我关于法国的事*

> *人生的意义是什么？*

> *我应该在锻炼前还是锻炼后服用肌酸？*


当你把指令送出后，AgenticSeek 会自动调用最能提供帮助的助理，去完成你交办的工作和指令。

但也有可能出现怪怪的情况，或是你要找飞机机票，他跑去教你如何一步步做出一台飞机（开玩笑的，但真的可能出现），因为这是一个早期专案，我们会努力教导他、完善他的！

所以我们希望你在使用时，能明确地表明你希望他要怎么做，下面给你一个范例！

你该说：
- 进行网络搜索，找出哪些国家最适合独自旅行


而不是说：
- 你知道哪些国家适合独自旅行？

---


---

## **在本地执行属于你的 LLM 伺服器**

如果你有一台功能强大的电脑或伺服器，但你想透过笔记型电脑使用它，那么你可以选择在远端伺服器上执行 LLM。

### 1️⃣ **设定并启动伺服器脚本**

在运行 AI 模型的「伺服器」上，取得 IP 位址

```sh
ip a | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1
```

注意：请在 Windows 或 MacOS，分别使用 `ipconfig` 与 `ifconfig` 来寻找 IP 位址。

**如果你希望使用基于 Openai 的服务，请按照 *透过 API 执行* 部分进行。**

复制储存库并且进入 `server/` 资料夹。

```sh
git clone --depth 1 https://github.com/Fosowl/agenticSeek.git
cd agenticSeek/server/
```

安装伺服器所需的套件：

```sh
pip3 install -r requirements.txt
```

执行伺服器脚本。

```sh
python3 app.py --provider ollama --port 3333
```

您可以选择使用 `ollama` 或 `llamacpp` 作为 LLM 的服务框架。

### 2️⃣ **执行**

在你的电脑上：

- 更改 `config.ini`
- `provider_name = server`
- `provider_model = deepseek-r1:14b`
- `provider_server_address = {你执行模型的电脑的 IP 位址}`

```sh
[MAIN]
is_local = False
provider_name = server
provider_model = deepseek-r1:14b
provider_server_address = x.x.x.x:3333
```


---

## 语音转文字

请注意，目前语音转文字功能仅支持英语。

预设状况下，语音转文字功能是停用的。若要启用它，请在 `config.ini` 档案中，将 `listen` 选项设为 `True`：

```
listen = True
```

启用后 AgenticSeek 会聆听你是否呼唤他，他才会开始听你说的话，你可以在 *config.ini* 内去设定，要怎么叫他。

```
agent_name = Friday
```

为了获得比较好的结果，我们建议使用常见的英文名称（如 “John” 或 “Emma”）作为他的名字。

当你看到程式开始执行时，请大声说出他的名字，就可以唤醒 AgenticSeek 去聆听！（如：Friday）

清楚说出你的需求。

用确认短句结束你说的话，以通知 AgenticSeek 继续。确认短句的范例包括：
```
"do it", "go ahead", "execute", "run", "start", "thanks", "would ya", "please", "okay?", "proceed", "continue", "go on", "do that", "go it", "do you understand?"
```

## Config

Config 范例：
```
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:1.5b
provider_server_address = 127.0.0.1:11434
agent_name = Friday
recover_last_session = False
save_session = False
speak = False
listen = False
work_dir = /Users/mlg/Documents/ai_folder
jarvis_personality = False
languages = en zh
[BROWSER]
headless_browser = False
stealth_mode = False
```

**说明**:
- is_local
- True：在本地运行。
- False：在远端伺服器运行。
- provider_name
- 框架类型
- `ollama`, `server`, `lm-studio`, `deepseek-api`
- provider_model
- 运行的模型
- `deepseek-r1:1.5b`, `deepseek-r1:14b`
- provider_server_address
- 伺服器 IP
- `127.0.0.1:11434`
- agent_name
- AgenticSeek 的名字，用作TTS的触发单词。
- `Friday`
- recover_last_session
- True：从上个对话继续。
- False：重启对话。
- save_session
- True：储存对话纪录。
- False：不保存。
- speak
- True：启用语音输出。
- False：关闭语音输出。
- listen
- True：启用语音输入。
- False：关闭语音输入。
- work_dir
- AgenticSeek 拥有能存取与交互的工作目录。
- jarvis_personality
> 就是那个钢铁人的 JARVIS
- True：启用 JARVIS 个性。
- False：关闭 JARVIS 个性。
- headless_browser
- True：前景浏览器。（很酷，推荐使用他 XD）
- False：背景执行浏览器。
- stealth_mode
- 隐私模式，但需要你自己安装反爬虫扩充功能。
- languages
- 支持的语言列表。用于代理路由系统。语言列表越长，下载的模型越多。

## 框架

下表显示了可用的框架：

| 框架 | 本地? | 描述|
|-|-|-|
| ollama | 可 | 使用 ollama 框架去执行本地模型 |
| server | 可 | 本地伺服器执行模型远端调用 |
| lm-studio | 可 | 使用 LM Studio 在本地运行 LLM（设定provider_name为lm-studio）|
| openai | 不可 | 使用 ChatGPT API（无法保证隐私）|
| deepseek-api | 不可 | 使用 Deepseek API (无法保证隐私)|
| huggingface | 不可 | 使用 Hugging-Face API (无法保证隐私)|

若要选择框架，请变更 `config.ini` 文件：

```
is_local = False
provider_name = openai
provider_model = gpt-4o
provider_server_address = 127.0.0.1:5000
```
`is_local`: 对于任何本地运行的 LLM 都应该为 True，否则为 False。

`provider_name`: 透过名称选择要使用的框架，请参阅上面的框架清单。

`provider_model`: 设定 AgenticSeek 使用的模型。

`provider_server_address`: 如果不使用云端 API，则可以将其设定为任何内容。

# Known issues （已知问题）

## Chromedriver Issues

**已知问题 #1:** *chromedriver mismatch*

`Exception: Failed to initialize browser: Message: session not created: This version of ChromeDriver only supports Chrome version 113
Current browser version is 134.0.6998.89 with binary path`

如果你的浏览器和 chromedriver 版本不一样，就会发生这种情况。

你可以透过以下连结下载最新版本：

https://developer.chrome.com/docs/chromedriver/downloads

如果您使用的是 Chrome 版本 115 或更新版本，请前往：

https://googlechromelabs.github.io/chrome-for-testing/

下载与你的作业系统相符的 chromedriver 版本。

![alt text](./media/chromedriver_readme.png)

如果有其他问题，请提供尽量详细的叙述到 Issues 上，尽可能包含当前环境和问题是怎么发生的。

## FAQ

**Q: 我需要什麼硬體？**  

| 模型大小  | GPU  | 備註                                               |
|-----------|--------|-----------------------------------------------------------|
| 7B        | 8GB Vram | ⚠️ 不推薦。性能較差，經常出現幻覺，規劃代理可能會失敗。 |
| 14B        | 12 GB VRAM (例如 RTX 3060) | ✅ 適用於簡單任務。可能在網頁瀏覽和規劃任務上表現不佳。 |
| 32B        | 24+ GB VRAM (例如 RTX 4090) | 🚀 大多數任務成功，但可能仍在任務規劃上有困難。 |
| 70B+        | 48+ GB Vram (例如 mac studio) | 💪 表現優異。建議用於高級使用情境。 |

**Q：为什么选择 Deepseek R1 而不是其他模型？**

就其尺寸而言，Deepseek R1 在推理和使用方面表现出色。我们认为非常适合我们的需求，其他模型也很好用，但 Deepseek 是我们最后选定的模型。

**Q：我在执行时 `cli.py` 时出现错误。我该怎么办？**

1. 确保 Ollama 正在运行（ollama serve）
2. 你 `config.ini` 内 `provider_name` 的框架选择正确。
3. 依赖套件已安装
4. 如果均无效，请随时提出 Issues，同样尽可能包含当前环境和问题是怎么发生的。

**Q：它真的是 100% 本地运行吗？**

是的，透过 Ollama 或其他框架，所有语音转文字、LLM 和文字转语音模型都在本地运行。
*但你能选择非本地执行（OpenAI 或其他 API），同样也是可以的*


**Q：我有 Manus 为甚么还要用 AgenticSeek？**

这是我们因为兴趣做的一个小 Side-Project，他特别的点在于是一个全部本地化的模型，而且可以像钢铁人里面一样与 `Jarvis` 对话，听起来就超级酷的吧！随着 Manus 的进化，我们也相应的加入更多功能！

**Q：它比 Manus 好在哪里？**

不不不，AgenticSeek 和 Manus 是不同取向的东西，我们优先考虑的是本地执行和隐私，而不是基于云端。这是一个与 Manus 相比起来更有趣且易使用的方案！

**Q: 是否支持中文以外的语言？**

DeepSeek R1 天生会说中文

但注意：代理路由系统只懂英文，所以必须通过 config.ini 的 languages 参数（如 languages = en zh）告诉系统：

如果不设置中文？后果可能是：你让它写代码，结果跳出来个"医生代理"（虽然我们根本没有这个代理... 但系统会一脸懵圈！）

实际上会下载一个小型翻译模型来协助任务分配

## 贡献

我们正在寻找开发者来改善 AgenticSeek！你可以在 Issues 查看未解决的问题或和我们讨论更酷的新功能！

[![Star History Chart](https://api.star-history.com/svg?repos=Fosowl/agenticSeek&type=Date)](https://www.star-history.com/#Fosowl/agenticSeek&Date)

[Contribution guide](./docs/CONTRIBUTING.md)

## 作者:
> [Fosowl](https://github.com/Fosowl)
> [steveh8758](https://github.com/steveh8758)
