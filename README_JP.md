<p align="center">
<img align="center" src="./media/whale_readme.jpg">
<p>

--------------------------------------------------------------------------------
[English](./README.md) | [中文](./README_CHS.md) | [繁體中文](./README_CHT.md)  | [Français](./README_FR.md) | 日本語

# AgenticSeek: Deepseek R1エージェントによって動作するManusのようなAI。


**Manus AIの完全なローカル代替品**、音声対応のAIアシスタントで、コードを書き、ファイルシステムを探索し、ウェブを閲覧し、ミスを修正し、データをクラウドに送信することなくすべてを行います。DeepSeek R1のような推論モデルを使用して構築されており、この自律エージェントは完全にハードウェア上で動作し、データのプライバシーを保護します。

[![Visit AgenticSeek](https://img.shields.io/static/v1?label=Website&message=AgenticSeek&color=blue&style=flat-square)](https://fosowl.github.io/agenticSeek.html) ![License](https://img.shields.io/badge/license-GPL--3.0-green) [![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.gg/8hGDaME3TC) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/fosowl.svg?style=social&label=Update%20%40Fosowl)](https://x.com/Martin993886460)

> 🛠️ **進行中の作業** – 貢献者を探しています！




https://github.com/user-attachments/assets/fe9e8006-0462-4793-8b31-25bd42c6d1eb




*そしてもっと多くのことができます！*

> *大阪と東京のAIスタートアップを深く調査し、少なくとも5つ見つけて、research_japan.txtファイルに保存してください*

> *C言語でテトリスゲームを作れますか？*

> *新しいプロジェクトファイルインデックスをmark2として設定したいです。*


## 特徴:

- **100%ローカル**: クラウドなし、ハードウェア上で動作。データはあなたのものです。

- **ファイルシステムの操作**: bashを使用してファイルを簡単にナビゲートおよび操作します。

- **自律的なコーディング**: Python、C、Golangなどのコードを書き、デバッグし、実行できます。

- **エージェントルーティング**: タスクに最適なエージェントを自動的に選択します。

- **計画**: 複雑なタスクの場合、複数のエージェントを起動して計画および実行します。

- **自律的なウェブブラウジング**: 自律的なウェブナビゲーション。

- **メモリ**: 効率的なメモリとセッション管理。 

---

## **インストール**

chrome driver、docker、およびpython3.10（またはそれ以降）がインストールされていることを確認してください。

chrome driverに関連する問題については、**Chromedriver**セクションを参照してください。

### 1️⃣ **リポジトリをクローンしてセットアップ**

```sh
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

### 2️ **仮想環境を作成**

```sh
python3 -m venv agentic_seek_env
source agentic_seek_env/bin/activate     
# Windowsの場合: agentic_seek_env\Scripts\activate
```

### 3️⃣ **パッケージをインストール**

**自動インストール:**

```sh
./install.sh
```

** テキスト読み上げ（TTS）機能で日本語をサポートするには、fugashi（日本語分かち書きライブラリ）をインストールする必要があります：**

```
pip3 install --upgrade pyopenjtalk jaconv mojimoji unidic fugashi
pip install unidic-lite
python -m unidic download
```

**手動で:**

```sh
pip3 install -r requirements.txt
# または
python3 setup.py install
```

---

## ローカルマシンでLLMを実行するためのセットアップ

**少なくともDeepseek 14Bを使用することをお勧めします。小さいモデルでは、特にウェブブラウジングのタスクで苦労する可能性があります。**

**ローカルプロバイダーをセットアップする**  

たとえば、ollamaを使用してローカルプロバイダーを開始します:

```sh
ollama serve
```

以下に、サポートされているローカルプロバイダーのリストを示します。

**config.iniを更新する**

config.iniファイルを変更して、`provider_name`をサポートされているプロバイダーに設定し、`provider_model`を`deepseek-r1:14b`に設定します。

注意: `deepseek-r1:14b`は例です。ハードウェアが許可する場合は、より大きなモデルを使用してください。
```sh
[MAIN]
is_local = True # ローカルで実行するか、リモートプロバイダーを使用するか
provider_name = ollama # または lm-studio、openai など
provider_model = deepseek-r1:14b # ハードウェアに適したモデルを選択
provider_server_address = 127.0.0.1:11434
agent_name = Jarvis # AIの名前
recover_last_session = True # 前回のセッションを復元するかどうか
save_session = True # 現在のセッションを記憶するかどうか
speak = True # テキスト読み上げ
listen = False # 音声認識、CLIのみ
work_dir =  /Users/mlg/Documents/workspace # AgenticSeekのワークスペース
jarvis_personality = False # より「Jarvis」らしい性格を使用するかどうか（実験的）
languages = en zh # 言語のリスト、テキスト読み上げはリストの最初の言語がデフォルトになります
[BROWSER]
headless_browser = True # ヘッドレスブラウザを使用するかどうか、ウェブインターフェースを使用する場合のみ推奨
stealth_mode = True # ブラウザ検出を減らすために検出されないSeleniumを使用
```

警告: LM-studioでLLMを実行する場合、provider_nameを`openai`に設定しないでください。`lm-studio`に設定してください。

注意: 一部のプロバイダー(例：lm-studio)では、IPの前に`http://`が必要です。例えば`http://127.0.0.1:1234`のように設定してください。

**ローカルプロバイダーのリスト**

| プロバイダー  | ローカル? | 説明                                               |
|-----------|--------|-----------------------------------------------------------|
| ollama    | はい    | ollamaをLLMプロバイダーとして使用して、ローカルでLLMを簡単に実行 |
| lm-studio  | はい    | LM studioを使用してローカルでLLMを実行（`provider_name`を`lm-studio`に設定）|
| openai    | はい    | OpenAI互換APIを使用  |

次のステップ: [サービスを開始してAgenticSeekを実行する](#Start-services-and-Run)  

*問題が発生している場合は、**既知の問題**セクションを参照してください。*

*ハードウェアがDeepseekをローカルで実行できない場合は、**APIを使用した実行**セクションを参照してください。*

*詳細な設定ファイルの説明については、**設定**セクションを参照してください。*

---

## APIを使用したセットアップ

`config.ini`で希望するプロバイダーを設定してください。

```sh
[MAIN]
is_local = False
provider_name = openai
provider_model = gpt-4o
provider_server_address = 127.0.0.1:5000
```

警告: `config.ini`に末尾のスペースがないことを確認してください。

ローカルのOpenAIベースのAPIを使用する場合は、`is_local`をTrueに設定してください。

OpenAIベースのAPIが独自のサーバーで実行されている場合は、IPアドレスを変更してください。

次のステップ: [サービスを開始してAgenticSeekを実行する](#Start-services-and-Run)

*問題が発生している場合は、**既知の問題**セクションを参照してください。*

*詳細な設定ファイルの説明については、**設定**セクションを参照してください。*

---

## サービスの開始と実行

必要に応じてPython環境をアクティブにしてください。
```sh
source agentic_seek_env/bin/activate
```

必要なサービスを開始します。これにより、docker-compose.ymlから以下のサービスがすべて開始されます:
- searxng
- redis (searxngに必要)
- フロントエンド

```sh
sudo ./start_services.sh # MacOS
start ./start_services.cmd # Windows
```

**オプション1:** CLIインターフェースで実行。

```sh
python3 cli.py
```

**オプション2:** Webインターフェースで実行。

注意: 現在、CLIの使用を推奨しています。Webインターフェースは開発中です。

バックエンドを開始します。

```sh
python3 api.py
```

`http://localhost:3000/`にアクセスすると、Webインターフェースが表示されます。

現在、Webインターフェースではメッセージのストリーミングがサポートされていないことに注意してください。

---

## 使い方

警告: 現在、サポートされている言語は英語、中国語、フランス語のみです。他の言語でのプロンプトは機能しますが、適切なエージェントにルーティングされない場合があります。

サービスが`./start_services.sh`で起動していることを確認し、`python3 cli.py`でagenticSeekを実行します。

```sh
sudo ./start_services.sh
python3 cli.py
```

`>>> `と表示されます
これは、agenticSeekが指示を待っていることを示します。
configで`listen = True`を設定することで、音声認識を使用することもできます。

終了するには、単に`goodbye`と言います。

以下は使用例です:

### コーディング/バッシュ

> *Pythonでスネークゲームを作成*

> *C言語で行列の掛け算を教えて*

> *Golangでブラックジャックを作成*

### ウェブ検索

> *日本の最先端のAI研究を行っているクールなテックスタートアップを見つけるためにウェブ検索を行う*

> *agenticSeekを作成したのは誰かをインターネットで見つけることができますか？*

> *オンラインの燃料計算機を使用して、ニースからミラノまでの旅行の費用を見積もることができますか？*

### ファイルシステム

> *契約書.pdfがどこにあるか見つけてくれませんか？*

> *ディスクにどれだけの空き容量があるか教えて*

> *READMEを読んでプロジェクトを/home/path/projectにインストールしてください*

### カジュアル

> *フランスのレンヌについて教えて*

> *博士号を追求すべきですか？*

> *最高のワークアウトルーチンは何ですか？*


クエリを入力すると、agenticSeekはタスクに最適なエージェントを割り当てます。

これは初期のプロトタイプであるため、エージェントルーティングシステムはクエリに基づいて常に適切なエージェントを割り当てるとは限りません。

したがって、何を望んでいるか、AIがどのように進行するかについて非常に明確にする必要があります。たとえば、ウェブ検索を行いたい場合は、次のように言わないでください:

`一人旅に良い国を知っていますか？`

代わりに、次のように尋ねてください:

`ウェブ検索を行い、一人旅に最適な国を見つけてください`

---

## **ボーナス: 自分のサーバーでLLMを実行するためのセットアップ**  

強力なコンピュータやサーバーを持っていて、それをラップトップから使用したい場合、リモートサーバーでLLMを実行するオプションがあります。

AIモデルを実行する「サーバー」で、IPアドレスを取得します。

```sh
ip a | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1 # ローカルIP
curl https://ipinfo.io/ip # 公開IP
```

注意: WindowsまたはmacOSの場合、IPアドレスを見つけるには、それぞれ`ipconfig`または`ifconfig`を使用してください。

リポジトリをクローンし、`server/`フォルダーに移動します。

```sh
git clone --depth 1 https://github.com/Fosowl/agenticSeek.git
cd agenticSeek/server/
```

サーバー固有の依存関係をインストールします:

```sh
pip3 install -r requirements.txt
```

サーバースクリプトを実行します。

```sh
python3 app.py --provider ollama --port 3333
```

`ollama`と`llamacpp`のどちらかをLLMサービスとして選択できます。

次に、個人用コンピュータで以下を行います:

`config.ini`ファイルを変更し、`provider_name`を`server`に、`provider_model`を`deepseek-r1:xxb`に設定します。
`provider_server_address`をモデルを実行するマシンのIPアドレスに設定します。

```sh
[MAIN]
is_local = False
provider_name = server
provider_model = deepseek-r1:70b
provider_server_address = x.x.x.x:3333
```

次のステップ: [サービスを開始してAgenticSeekを実行する](#Start-services-and-Run)  


---

## 音声認識

現在、音声認識は英語でのみ動作することに注意してください。

音声認識機能はデフォルトで無効になっています。有効にするには、config.iniファイルでlistenオプションをTrueに設定します:

```
listen = True
```

有効にすると、音声認識機能はトリガーキーワード（エージェントの名前）を待ちます。その後、入力を処理します。エージェントの名前は*config.ini*ファイルの`agent_name`値を更新することでカスタマイズできます:

```
agent_name = Friday
```

最適な認識のために、"John"や"Emma"のような一般的な英語の名前をエージェント名として使用することをお勧めします。

トランスクリプトが表示され始めたら、エージェントの名前を大声で言って起動します（例："Friday"）。

クエリを明確に話します。

リクエストを終了する際に確認フレーズを使用してシステムに進行を通知します。確認フレーズの例には次のようなものがあります:
```
"do it", "go ahead", "execute", "run", "start", "thanks", "would ya", "please", "okay?", "proceed", "continue", "go on", "do that", "go it", "do you understand?"
```

## 設定

設定例:
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
work_dir =  /Users/mlg/Documents/ai_folder
jarvis_personality = False
languages = en ja
[BROWSER]
headless_browser = False
stealth_mode = False
```

**説明**:

- is_local -> エージェントをローカルで実行する（True）か、リモートサーバーで実行する（False）。
- provider_name -> 使用するプロバイダー（`ollama`、`server`、`lm-studio`、`deepseek-api`のいずれか）。
- provider_model -> 使用するモデル、例: deepseek-r1:1.5b。
- provider_server_address -> サーバーアドレス、例: 127.0.0.1:11434（ローカルの場合）。非ローカルAPIの場合は何でも設定できます。
- agent_name -> エージェントの名前、例: Friday。TTSのトリガーワードとして使用されます。
- recover_last_session -> 最後のセッションから再開する（True）か、しない（False）。
- save_session -> セッションデータを保存する（True）か、しない（False）。
- speak -> 音声出力を有効にする（True）か、しない（False）。
- listen -> 音声入力を有効にする（True）か、しない（False）。
- work_dir -> AIがアクセスするフォルダー。例: /Users/user/Documents/。
- jarvis_personality -> JARVISのようなパーソナリティを使用する（True）か、しない（False）。これは単にプロンプトファイルを変更するだけです。
- headless_browser -> ウィンドウを表示せずにブラウザを実行する（True）か、しない（False）。
- stealth_mode -> ボット検出を難しくします。唯一の欠点は、anticaptcha拡張機能を手動でインストールする必要があることです。
- languages -> List of supported languages. Required for agent routing system. The longer the languages list the more model will be downloaded.

## プロバイダー

以下の表は利用可能なプロバイダーを示しています:

| プロバイダー  | ローカル? | 説明                                               |
|-----------|--------|-----------------------------------------------------------|
| ollama    | はい    | ollamaをLLMプロバイダーとして使用して、ローカルでLLMを簡単に実行 |
| server    | はい    | モデルを別のマシンでホストし、ローカルマシンで実行         |
| lm-studio | はい    | LM studio（`lm-studio`）を使用してローカルでLLMを実行      |
| openai    | 場合による | ChatGPT API（非プライベート）またはopenai互換APIを使用   |
| deepseek-api | いいえ  | Deepseek API（非プライベート）                          |
| huggingface| いいえ  | Hugging-Face API（非プライベート）                        |
| togetherAI | いいえ  | together AI API（非プライベート）を使用                  


プロバイダーを選択するには、config.iniを変更します:

```
is_local = False
provider_name = openai
provider_model = gpt-4o
provider_server_address = 127.0.0.1:5000
```
`is_local`: ローカルで実行されるLLMの場合はTrue、それ以外の場合はFalse。

`provider_name`: 使用するプロバイダーを名前で選択します。上記のプロバイダーリストを参照してください。

`provider_model`: エージェントが使用するモデルを設定します。

`provider_server_address`: サーバープロバイダーを使用しない場合は何でも設定できます。

# 既知の問題

## Chromedriverの問題

**既知のエラー#1:** *chromedriverの不一致*

`Exception: Failed to initialize browser: Message: session not created: This version of ChromeDriver only supports Chrome version 113
Current browser version is 134.0.6998.89 with binary path`

これは、ブラウザとchromedriverのバージョンが一致しない場合に発生します。

最新バージョンをダウンロードするには、次のリンクにアクセスしてください:

https://developer.chrome.com/docs/chromedriver/downloads

Chromeバージョン115以降を使用している場合は、次のリンクにアクセスしてください:

https://googlechromelabs.github.io/chrome-for-testing/

お使いのOSに対応するchromedriverバージョンをダウンロードします。

![alt text](./media/chromedriver_readme.png)

このセクションが不完全な場合は、問題を報告してください。

## FAQ

**Q: どのようなハードウェアが必要ですか？**  

| モデルサイズ  | GPU  | コメント                                               |
|-----------|--------|-----------------------------------------------------------|
| 7B        | 8GB VRAM | ⚠️ 推奨されません。パフォーマンスが低く、頻繁に幻覚を起こし、プランナーエージェントが失敗する可能性が高いです。 |
| 14B        | 12GB VRAM (例: RTX 3060) | ✅ 簡単なタスクには使用可能です。ウェブブラウジングや計画タスクには苦労する可能性があります。 |
| 32B        | 24GB以上のVRAM (例: RTX 4090) | 🚀 ほとんどのタスクで成功しますが、タスク計画にはまだ苦労する可能性があります。 |
| 70B+        | 48GB以上のVRAM (例: Mac Studio) | 💪 優れた性能。高度なユースケースに推奨されます。 |

**Q: なぜ他のモデルではなくDeepseek R1を選ぶのですか？**  

Deepseek R1は、そのサイズに対して推論とツールの使用に優れています。私たちのニーズに最適だと考えています。他のモデルも問題なく動作しますが、Deepseekが私たちの主な選択です。

**Q: `cli.py`を実行するとエラーが発生します。どうすればよいですか？**  

Ollamaが実行中であることを確認してください（`ollama serve`）、`config.ini`がプロバイダーに一致していること、および依存関係がインストールされていることを確認してください。それでも解決しない場合は、問題を報告してください。

**Q: 本当に100%ローカルで実行できますか？**  

はい、OllamaまたはServerプロバイダーを使用すると、すべての音声認識、LLM、および音声合成モデルがローカルで実行されます。非ローカルオプション（OpenAIまたは他のAPI）はオプションです。

**Q: Manusを持っているのに、なぜAgenticSeekを使用する必要があるのですか？**

これは、AIエージェントに関する興味から始まったサイドプロジェクトです。特別な点は、ローカルモデルを使用し、APIを避けることです。
私たちは、JarvisやFriday（アイアンマン映画）からインスピレーションを得て、「クール」にしようとしましたが、機能性に関してはManusから多くのインスピレーションを得ています。なぜなら、人々が最初に求めているのはローカルのManusの代替品だからです。
Manusとは異なり、AgenticSeekは外部システムからの独立性を優先し、より多くの制御、プライバシーを提供し、APIのコストを回避します。

## 貢献

AgenticSeekを改善するための開発者を探しています！オープンな問題やディスカッションを確認してください。

[![Star History Chart](https://api.star-history.com/svg?repos=Fosowl/agenticSeek&type=Date)](https://www.star-history.com/#Fosowl/agenticSeek&Date)

## 著者:
 > [Fosowl](https://github.com/Fosowl)
 > [steveh8758](https://github.com/steveh8758) 
