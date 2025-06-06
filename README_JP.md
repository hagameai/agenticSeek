# AgenticSeek: プライベートでローカルな Manus の代替

<p align="center">
<img align="center" src="./media/agentic_seek_logo.png" width="300" height="300" alt="Agentic Seek Logo">
<p>

    English | [中文](./README_CHS.md) | [繁體中文](./README_CHT.md) | [Français](./README_FR.md) | [日本語](./README_JP.md) | [Português (Brasil)](./README_PTBR.md)

**100%ローカルで動作するManus AIの代替**となる音声対応AIアシスタントです。ウェブの自律的な閲覧、コードの作成、タスクの計画を行い、すべてのデータをあなたのデバイス上に保持します。ローカル推論モデル向けに最適化されており、完全なプライバシーとクラウド依存ゼロを実現します。

[![Visit AgenticSeek](https://img.shields.io/static/v1?label=Website&message=AgenticSeek&color=blue&style=flat-square)](https://fosowl.github.io/agenticSeek.html) ![License](https://img.shields.io/badge/license-GPL--3.0-green) [![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.gg/8hGDaME3TC) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/fosowl.svg?style=social&label=Update%20%40Fosowl)](https://x.com/Martin993886460) [![GitHub stars](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=social)](https://github.com/Fosowl/agenticSeek/stargazers)

### なぜAgenticSeekなのか？

* 🔒 完全ローカル＆プライベート - すべてがあなたのマシン上で動作。クラウドやデータ共有は一切なし。ファイル、会話、検索はすべてプライベートに保たれます。

* 🌐 スマートなウェブブラウジング - AgenticSeekは自動でインターネットを検索・閲覧・情報抽出・フォーム入力までハンズフリーで実行します。

* 💻 自律型コーディングアシスタント - コードが必要ですか？Python、C、Go、Javaなどのプログラムを自動で作成・デバッグ・実行します。

* 🧠 スマートエージェント選択 - あなたの要望に応じて最適なエージェントを自動で選択。まるで専門家チームが常にサポートしてくれるようです。

* 📋 複雑なタスクの計画と実行 - 旅行計画からプロジェクト管理まで、大きなタスクを分割し、複数のAIエージェントで実行します。

* 🎙️ 音声対応 - 未来的で高速な音声認識＆音声合成。まるでSF映画のパーソナルAIのように会話できます（開発中）。

### **デモ**

> *agenticSeekプロジェクトを検索し、必要なスキルを調べてからCV_candidates.zipを開き、プロジェクトに最も合う候補者を教えて*

https://github.com/user-attachments/assets/b8ca60e9-7b3b-4533-840e-08f9ac426316

注意: このデモや登場するファイル（例: CV_candidates.zip）はすべて架空のものです。私たちは企業ではなく、オープンソースの貢献者を募集しています。

> 🛠⚠️️ **開発中のプロジェクトです**

> 🙏 このプロジェクトはサイドプロジェクトとして始まり、ロードマップや資金はありません。GitHub Trending入りするほど成長しました。貢献・フィードバック・ご理解に感謝します。

## 前提条件

chrome driver、docker、python3.10がインストールされていることを確認してください。

chrome driver関連の問題は**Chromedriver**セクションを参照してください。

### 1. **リポジトリのクローンとセットアップ**

```sh
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

### 2. .envファイルの内容を変更

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

**APIキーはローカルでLLMを実行する場合は完全にオプションです。十分なハードウェアがある場合は空欄で構いません。**

以下の環境変数はアプリケーションの接続やAPIキーを設定します。必要に応じて`.env`ファイルを編集してください。

- **SEARXNG_BASE_URL**: 変更不要
- **REDIS_BASE_URL**: 変更不要
- **WORK_DIR**: ローカル作業ディレクトリのパス。AgenticSeekがこのディレクトリのファイルを読み書きします。
- **OLLAMA_PORT**: Ollamaサービスのポート番号
- **LM_STUDIO_PORT**: LM Studioサービスのポート番号
- **CUSTOM_ADDITIONAL_LLM_PORT**: カスタムLLMサービスのポート番号

APIキーは**すべてオプション**です。外部APIを使う場合のみ設定してください。

### 3. **Dockerの起動**

Dockerがインストールされ、起動していることを確認してください。以下のコマンドで起動できます。

- **Linux/macOSの場合:**  
        ターミナルで
        ```sh
        sudo systemctl start docker
        ```
        またはアプリケーションメニューからDocker Desktopを起動

- **Windowsの場合:**  
        スタートメニューからDocker Desktopを起動

Dockerが動作しているか確認するには
```sh
docker info
```
と入力し、情報が表示されればOKです。

---

## ローカルでLLMを実行する場合のセットアップ

**ハードウェア要件:**

ローカルでLLMを動かすには十分なハードウェアが必要です。最低でもQwen/Deepseek 14Bが動作するGPUが必要です。詳細はFAQを参照してください。

**ローカルプロバイダーの起動例**  

例: ollamaを使う場合

```sh
ollama serve
```

対応プロバイダーは下記参照。

**config.iniの更新**

config.iniファイルでprovider_nameをサポートされているプロバイダー名、provider_modelを対応モデルに設定してください。推論モデルは*Qwen*や*Deepseek*を推奨します。

FAQで必要なハードウェアを確認してください。

```sh
[MAIN]
is_local = True
provider_name = ollama
provider_model = deepseek-r1:14b
provider_server_address = 127.0.0.1:11434
agent_name = Jarvis
recover_last_session = True
save_session = True
speak = False
listen = False
jarvis_personality = False
languages = en zh
[BROWSER]
headless_browser = True
stealth_mode = True
```

**注意:**

- `config.ini`はコメントをサポートしません。例の設定をそのままコピペせず、コメントを除いて手動で編集してください。
- LM-studioを使う場合、provider_nameは`lm-studio`にしてください（`openai`ではありません）。
- 一部プロバイダー（例: lm-studio）はIPアドレスの前に`http://`が必要です（例: `http://127.0.0.1:1234`）。

**ローカルプロバイダー一覧**

| プロバイダー  | ローカル? | 説明                                               |
|-----------|--------|-----------------------------------------------------------|
| ollama    | はい    | ollamaでローカルLLMを簡単に実行 |
| lm-studio  | はい    | LM studioでローカルLLMを実行（`provider_name`は`lm-studio`）|
| openai    | はい/いいえ | openai互換API（例: llama.cppサーバー）  |

次のステップ: [サービスの起動とAgenticSeekの実行](#Start-services-and-Run)  

*問題がある場合は**Known issues**セクション参照*

*ローカルでdeepseekが動かない場合は**Run with an API**セクション参照*

*詳細な設定は**Config**セクション参照*

---

## APIで実行する場合のセットアップ

**API利用はオプションです。ローカル実行は上記参照。**

`config.ini`で希望のプロバイダーを設定してください。APIプロバイダー一覧は下記参照。

```sh
[MAIN]
is_local = False
provider_name = google
provider_model = gemini-2.0-flash
provider_server_address = 127.0.0.1:5000 # 任意
```
注意: configに余計なスペースがないようにしてください。

APIキーをエクスポート: `export <<PROVIDER>>_API_KEY="xxx"`

例: `export TOGETHER_API_KEY="xxxxx"`

**APIプロバイダー一覧**
    
| プロバイダー  | ローカル? | 説明                                               |
|-----------|--------|-----------------------------------------------------------|
| openai    | 場合による  | ChatGPT API  |
| deepseek  | いいえ     | Deepseek API（非プライベート）                            |
| huggingface| いいえ    | Hugging-Face API（非プライベート）                            |
| togetherAI | いいえ    | together AI API（非プライベート）                         |
| google | いいえ    | google gemini API（非プライベート）                         |

geminiではコーディングやbashが失敗する場合があります。deepseek r1向けに最適化されたプロンプトを無視する傾向があります。gpt-4oも同様にプロンプトとの相性が悪い場合があります。

次のステップ: [サービスの起動とAgenticSeekの実行](#Start-services-and-Run)

*問題がある場合は**Known issues**セクション参照*

*詳細な設定は**Config**セクション参照*

---

## サービスの起動とAgenticSeekの実行

必要なサービスを起動します。docker-compose.ymlから以下のサービスが起動します:
        - searxng
        - redis（searxng用）
        - frontend
        - backend（`full`の場合）

```sh
./start_services.sh full # MacOS
start ./start_services.cmd full # Windows
```

**注意:** このステップで全Dockerイメージがダウンロード・展開されるため最大30分かかる場合があります。backendサービスが完全に起動するまで（ログにbackend: <info>が表示されるまで）待ってください。

`http://localhost:3000/`にアクセスするとWebインターフェースが表示されます。

**オプション:** CLIインターフェースで実行

CLIで実行する場合はホストにパッケージをインストールしてください。

```sh
./install.sh
./install.bat # windows
```

サービス起動:

```sh
./start_services.sh # MacOS
start ./start_services.cmd # Windows
```

その後 `python3 cli.py` を実行

---

## 使い方

`./start_services.sh full`でサービスが起動していることを確認し、Webインターフェースは`localhost:3000`です。

CLIモードで音声認識を使う場合はconfigで`listen = True`にしてください。

終了するには「goodbye」と入力または発話してください。

使用例:

> *pythonでスネークゲームを作って！*

> *フランス・レンヌの人気カフェをウェブ検索し、3つ選んで住所とともにrennes_cafes.txtに保存して。*

> *Go言語で階乗を計算するプログラムを書き、workspaceにfactorial.goとして保存して。*

> *summer_picturesフォルダ内のJPGファイルをすべて検索し、今日の日付でリネームし、リストをphotos_list.txtに保存して。*

> *2024年の人気SF映画をウェブで調べ、今夜観る3本を選んでmovie_night.txtに保存して。*

> *2025年の最新AIニュース記事をウェブ検索し、3つ選んでタイトルと要約をPythonスクリプトでスクレイピング。news_scraper.pyにスクリプト、ai_news.txtに要約を保存して。*

> *金曜日、無料の株価APIをウェブで探し、supersuper7434567@gmail.comで登録後、Teslaの日次株価を取得するPythonスクリプトを書き、stock_prices.csvに保存して。*

*フォーム入力機能は実験的で失敗する場合があります。*


クエリを入力すると、AgenticSeekが最適なエージェントを自動で割り当てます。

初期プロトタイプのため、エージェントの割り当てが最適でない場合があります。

そのため、AIにしてほしいことや手順を明確に伝えてください。例えばウェブ検索をさせたい場合は

`Do you know some good countries for solo-travel?`

ではなく

`Do a web search and find out which are the best country for solo-travel`

のように依頼してください。

---

## **自分のサーバーでLLMを実行する場合**  

高性能なPCやサーバーを持っていて、ノートPCから利用したい場合は、カスタムLLMサーバーを使ってリモート実行できます。

AIモデルを動かす「サーバー」でIPアドレスを取得

```sh
ip a | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 # ローカルIP
curl https://ipinfo.io/ip # グローバルIP
```

WindowsやmacOSの場合はipconfigやifconfigで確認

リポジトリをクローンし、`server/`フォルダへ

```sh
git clone --depth 1 https://github.com/Fosowl/agenticSeek.git
cd agenticSeek/llm_server/
```

サーバー用依存パッケージをインストール

```sh
pip3 install -r requirements.txt
```

サーバースクリプトを実行

```sh
python3 app.py --provider ollama --port 3333
```

LLMサービスは`ollama`または`llamacpp`から選択可能です。

個人PC側では

`config.ini`で`provider_name`を`server`、`provider_model`を`deepseek-r1:xxb`に設定。
`provider_server_address`はサーバーのIPアドレスに設定。

```sh
[MAIN]
is_local = False
provider_name = server
provider_model = deepseek-r1:70b
provider_server_address = x.x.x.x:3333
```

次のステップ: [サービスの起動とAgenticSeekの実行](#Start-services-and-Run)  

---

## 音声認識（Speech to Text）

注意: 現在音声認識はCLIモードのみ対応

現状、音声認識は英語のみ対応です。

デフォルトでは無効です。有効にするにはconfig.iniでlistenをTrueにしてください。

```
listen = True
```

有効時は、エージェント名（例: Friday）をトリガーワードとして発話すると認識が始まります。エージェント名は*config.ini*の`agent_name`で変更可能です。

```
agent_name = Friday
```

認識精度向上のため、"John"や"Emma"など一般的な英語名を推奨します。

トランスクリプトが表示され始めたら、エージェント名を発話して起動してください（例: "Friday"）。

クエリを明瞭に話してください。

リクエストの終了時に以下のような確認フレーズを発話してください:
```
"do it", "go ahead", "execute", "run", "start", "thanks", "would ya", "please", "okay?", "proceed", "continue", "go on", "do that", "go it", "do you understand?"
```

## 設定ファイル（Config）

設定例:
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

**各項目の説明:**

- is_local -> ローカル実行（True）かリモート（False）か

- provider_name -> 使用するプロバイダー名（`ollama`, `server`, `lm-studio`, `deepseek-api`など）

- provider_model -> 使用モデル例: deepseek-r1:32b

- provider_server_address -> サーバーアドレス例: 127.0.0.1:11434（ローカルの場合）。API利用時は任意。

- agent_name -> エージェント名（例: Friday）。TTSのトリガーワード

- recover_last_session -> 前回セッションから再開（True）/しない（False）

- save_session -> セッションデータ保存（True）/しない（False）

- speak -> 音声出力有効（True）/無効（False）

- listen -> 音声入力有効（True）/無効（False）

- jarvis_personality -> JARVIS風パーソナリティ（True）/通常（False）。プロンプトファイルが変わります。

- languages -> サポート言語リスト。エージェントルーティングに必要。多すぎる/似た言語は非推奨。

- headless_browser -> ブラウザを非表示で実行（True）/表示（False）

- stealth_mode -> ボット検出回避。anticaptcha拡張の手動インストールが必要

- languages -> サポート言語リスト。ルーティング用。多いほどモデルダウンロード数増加

## プロバイダー一覧

| プロバイダー  | ローカル? | 説明                                               |
|-----------|--------|-----------------------------------------------------------|
| ollama    | はい    | ollamaでローカルLLMを簡単に実行 |
| server    | はい    | 別マシンでモデルをホストし、ローカルから利用 |
| lm-studio  | はい    | LM studioでローカルLLMを実行（`lm-studio`）             |
| openai    | 場合による  | ChatGPT API（非プライベート）またはopenai互換API  |
| deepseek-api  | いいえ     | Deepseek API（非プライベート）                            |
| huggingface| いいえ    | Hugging-Face API（非プライベート）                            |
| togetherAI | いいえ    | together AI API（非プライベート）                         |
| google | いいえ    | google gemini API（非プライベート）                         |

プロバイダーの選択はconfig.iniで

```
is_local = True
provider_name = ollama
provider_model = deepseek-r1:32b
provider_server_address = 127.0.0.1:5000
```
`is_local`: ローカルLLMならTrue、それ以外はFalse

`provider_name`: 上記リストから選択

`provider_model`: 使用モデル

`provider_server_address`: serverプロバイダー以外は任意

# 既知の問題

## Chromedriverの問題

**既知のエラー #1:** *chromedriverのバージョン不一致*

`Exception: Failed to initialize browser: Message: session not created: This version of ChromeDriver only supports Chrome version 113
Current browser version is 134.0.6998.89 with binary path`

これはブラウザとchromedriverのバージョンが一致していない場合に発生します。

最新版は下記からダウンロードしてください:

https://developer.chrome.com/docs/chromedriver/downloads

Chrome 115以降の場合は

https://googlechromelabs.github.io/chrome-for-testing/

からOSに合ったchromedriverをダウンロード

![alt text](./media/chromedriver_readme.png)

このセクションが不十分な場合はissueを立ててください。

##  connection adaptersの問題

```
Exception: Provider lm-studio failed: HTTP request failed: No connection adapters were found for '127.0.0.1:11434/v1/chat/completions'
```

provider IPアドレスの前に`http://`を付けてください:

`provider_server_address = http://127.0.0.1:11434`

## SearxNG base URLが必要

```
raise ValueError("SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.")
ValueError: SearxNG base URL must be provided either as an argument or via the SEARXNG_BASE_URL environment variable.
```

`.env.example`を`.env`にリネームしていない場合に発生します。もしくは下記でエクスポート:

`export  SEARXNG_BASE_URL="http://127.0.0.1:8080"`

## FAQ

**Q: どんなハードウェアが必要？**  

| モデルサイズ  | GPU  | コメント                                               |
|-----------|--------|-----------------------------------------------------------|
| 7B        | 8GB Vram | ⚠️ 推奨しません。性能が低く、幻覚やプランナー失敗が多発します。 |
| 14B        | 12 GB VRAM (例: RTX 3060) | ✅ 簡単なタスクなら使用可。ウェブブラウジングや計画タスクは苦手。 |
| 32B        | 24+ GB VRAM (例: RTX 4090) | 🚀 ほとんどのタスクで成功。計画タスクはやや苦手 |
| 70B+        | 48+ GB Vram (例: mac studio) | 💪 高度な用途に最適。推奨 |

**Q: なぜDeepseek R1を推奨？**  

Deepseek R1は推論やツール利用に優れています。他モデルも使えますが、Deepseekが主力です。

**Q: `cli.py`実行時にエラーが出る場合は？**  

`ollama serve`が動作しているか、`config.ini`が正しいか、依存パッケージがインストールされているか確認してください。解決しない場合はissueを立ててください。

**Q: 本当に100%ローカルで動作する？**  

Ollama、lm-studio、serverプロバイダーなら音声認識・LLM・音声合成すべてローカルで動作します。API利用はオプションです。

**Q: ManusがあるのにAgenticSeekを使う理由は？**

このプロジェクトはローカルモデル利用とAPI回避を目的に始まりました。JarvisやFriday（アイアンマン）風の「かっこよさ」とManusの機能性を両立。Manusと違い外部依存を排除し、プライバシーとコスト削減を重視しています。

## コントリビュート

AgenticSeekの改善にご協力ください！issueやディスカッションをチェック

[コントリビューションガイド](./docs/CONTRIBUTING.md)

[![Star History Chart](https://api.star-history.com/svg?repos=Fosowl/agenticSeek&type=Date)](https://www.star-history.com/#Fosowl/agenticSeek&Date)

## メンテナー:

 > [Fosowl](https://github.com/Fosowl) | パリ時間 

 > [antoineVIVIES](https://github.com/antoineVIVIES) | 台北時間 

 > [steveh8758](https://github.com/steveh8758) | 台北時間 

## Special Thanks:

 > [tcsenpai](https://github.com/tcsenpai) および [plitc](https://github.com/plitc) バックエンドDocker化への貢献に感謝

