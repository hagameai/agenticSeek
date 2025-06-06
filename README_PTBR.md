# AgenticSeek: Alternativa Privada e Local ao Manus AI

<p align="center">
  <img align="center" src="./media/agentic_seek_logo.png" width="300" height="300" alt="Agentic Seek Logo">
</p>

[English](./README.md) | [中文](./README_CHS.md) | [繁體中文](./README_CHT.md) | [Français](./README_FR.md) | [日本語](./README_JP.md) | [Português (Brasil)](./README_PTBR.md)

> Uma **alternativa 100% local ao Manus AI**, este assistente de IA habilitado por voz navega autonomamente na web, escreve código e planeja tarefas mantendo todos os dados no seu dispositivo. Projetado para modelos de raciocínio locais, roda inteiramente no seu hardware, garantindo total privacidade e zero dependência de nuvem.

[![Visit AgenticSeek](https://img.shields.io/static/v1?label=Website&message=AgenticSeek&color=blue&style=flat-square)](https://fosowl.github.io/agenticSeek.html) ![License](https://img.shields.io/badge/license-GPL--3.0-green) [![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?logo=discord&logoColor=white)](https://discord.gg/8hGDaME3TC) [![Twitter](https://img.shields.io/twitter/url/https/twitter.com/fosowl.svg?style=social&label=Update%20%40Fosowl)](https://x.com/Martin993886460) [![GitHub stars](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=social)](https://github.com/Fosowl/agenticSeek/stargazers)

---

## Por que AgenticSeek?

* 🔒 **Totalmente Local & Privado**  
  Roda integralmente na sua máquina — sem nuvem, sem compartilhamento de dados. Seus arquivos, conversas e buscas permanecem sob seu controle.

* 🌐 **Navegação Web Inteligente**  
  AgenticSeek pode navegar na internet sozinho — buscar, ler, extrair informações, preencher formulários — tudo de forma autônoma.

* 💻 **Assistente de Programação Autônomo**  
  Precisa de código? Ele escreve, depura e executa programas em Python, C, Go, Java e muito mais — sem supervisão constante.

* 🧠 **Seleção Inteligente de Agentes**  
  Você faz a pergunta, ele escolhe automaticamente o melhor "agente" para a tarefa. É como ter uma equipe de especialistas sempre à disposição.

* 📋 **Planeja e Executa Tarefas Complexas**  
  De roteiros de viagem a projetos grandes — divide grandes objetivos em etapas e realiza tudo usando múltiplos agentes de IA.

* 🎙️ **Habilitado por Voz**  
  Integração limpa de texto para fala e fala para texto — fale com ele como se fosse um assistente de ficção científica.

---

## **Demonstração**

> **Exemplo de uso**  
>
> _"Pode buscar na web informações sobre o projeto AgenticSeek, identificar requisitos, abrir o arquivo `CV_candidates.zip` e me dizer qual currículo se adequa melhor?"_

https://github.com/user-attachments/assets/b8ca60e9-7b3b-4533-840e-08f9ac426316

> **Aviso:** Esta demonstração, incluindo todos os arquivos que aparecem (ex.: `CV_candidates.zip`), é totalmente fictícia. Não somos uma corporação e buscamos contribuições de código, não candidatos.

> 🛠️ **Em Desenvolvimento** – Buscando colaboradores!

---

## Instalação

Certifique-se de ter instalado: ChromeDriver, Docker, Docker Compose e Python 3.10.  
Recomendamos usar **exatamente** Python 3.10 para evitar erros de dependência.

Para problemas com ChromeDriver, veja a seção **Problemas Conhecidos**.

### 1️⃣ Clone o repositório e configure o ambiente

```bash
git clone https://github.com/Fosowl/agenticSeek.git
cd agenticSeek
mv .env.example .env
```

## 2️⃣ Instale o Gerenciador de Pacotes UV

### Para Linux/macOS:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Para Windows:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 3️⃣ Crie um Ambiente Virtual
```bash
uv venv
```

### 4️⃣ Instale o pacote

#### Instalação Automática (Recomendada)

- **Linux/macOS**  
  ```bash
  ./install.sh
  ```
- **Windows**  
  ```powershell
  .\install.bat
  ```

#### Instalação Manual

> **Obs.:** Verifique sempre se a versão do ChromeDriver corresponde à do seu Chrome (`google-chrome --version`).

- **Linux (Debian/Ubuntu)**  
  ```bash
  sudo apt update
  sudo apt install -y alsa-utils portaudio19-dev python3-pyaudio \
                      libgtk-3-dev libnotify-dev libgconf-2-4 \
                      libnss3 libxss1 chromium-chromedriver
  pip3 install --upgrade pip setuptools wheel
  pip3 install -r requirements.txt
  ```

- **macOS**  
  ```bash
  brew update
  brew install --cask chromedriver
  brew install portaudio
  python3 -m pip install --upgrade pip setuptools wheel
  pip3 install -r requirements.txt
  ```

- **Windows**  
  ```powershell
  pip install pyreadline3
  # Instale o portaudio (via vcpkg ou binário)
  pip install pyaudio
  # Baixe e coloque o ChromeDriver no PATH:
  # https://sites.google.com/chromium.org/driver/getting-started
  pip3 install -r requirements.txt
  ```

---

## Configuração para rodar LLM localmente

### Requisitos de Hardware

Para modelos grandes (~14B+), é recomendada **GPU** com 8 GB+ de VRAM. Veja a seção **FAQ** para detalhes.

### 1️⃣ Inicie seu provedor local (ex.: Ollama)

```bash
ollama serve
```

### 2️⃣ Edite o `config.ini`

```ini
[MAIN]
is_local = True                # Executar localmente
provider_name = ollama         # ou lm-studio, server, openai, etc.
provider_model = deepseek-r1:14b
provider_server_address = 127.0.0.1:11434
agent_name = Jarvis            # Nome do assistente
recover_last_session = True    # Retomar sessão anterior
save_session = True            # Salvar histórico de sessão
speak = True                   # Texto para fala
listen = False                 # Fala para texto (CLI)
work_dir = /caminho/para/workspace
languages = en zh pt

[BROWSER]
headless_browser = True        # Modo headless (recomendado para API)
stealth_mode = True            # Modo furtivo (undetected selenium)
```

> **Atenção:**  
> - Ao usar `provider_name = lm-studio`, adicione `http://` em `provider_server_address`, se necessário.  
> - Não use `provider_name = openai` junto com LM-studio sem prefixo `http://`.

---

## Configuração para rodar com API remota

Se preferir usar nuvem:

```ini
[MAIN]
is_local = False
provider_name = google       # openai, huggingface, togetherAI, etc.
provider_model = gemini-2.0-flash
provider_server_address = 127.0.0.1:5000
```

Exporte sua chave de API:

```bash
export OPENAI_API_KEY="sua_chave_aqui"
# ou export GOOGLE_API_KEY, TOGETHER_API_KEY, etc.
```

---

## Iniciando serviços e executando o AgenticSeek

1. Ative o virtualenv, se ainda não estiver ativo.  
2. Suba os serviços (Docker Compose):

   - **Linux/macOS**
     ```bash
     sudo ./start_services.sh
     ```
   - **Windows**
     ```powershell
     .\start_services.cmd
     ```

3. Ative o ambiente virtual e escolha a interface:

   ```bash
   source .venv/bin/activate
   ```

   - **CLI**  
     ```bash
     python3 cli.py
     ```
     > Dica: defina `headless_browser = False` no `config.ini` para ver o navegador.

   - **Web**  
     ```bash
     python3 api.py
     ```
     Acesse `http://localhost:3000/` no navegador.

---

## Uso

Após iniciar os serviços, execute:

- **CLI**: `python3 cli.py`  
- **Web**: `python3 api.py` e visite `http://localhost:3000/`

Para usar fala → texto (CLI), ajuste `listen = True` no `config.ini`.  
Para encerrar, diga ou digite `goodbye`.

**Exemplos de comandos:**

> *Crie um jogo da cobrinha em Python!*  
> *Busque cafés em Rennes, França, e salve três endereços em `rennes_cafes.txt`.*  
> *Escreva em Go um programa para calcular fatorial e salve em `factorial.go`.*  
> *Procure JPGs na pasta `summer_pictures`, renomeie com a data de hoje e liste em `photos_list.txt`.*  
> *Pesquise notícias de IA de 2025, selecione três artigos e gere um script em Python para extrair títulos e resumos, salvando em `ai_news.txt`.*  

---

## Configuração para executar o LLM em servidor remoto

Se você tem um servidor potente e quer acessá-lo do laptop:

1. No servidor, descubra seu IP:
   ```bash
   # IP local
   ip a | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | cut -d/ -f1
   # IP público
   curl https://ipinfo.io/ip
   ```

2. Clone e entre na pasta do servidor:
   ```bash
   git clone --depth 1 https://github.com/Fosowl/agenticSeek.git
   cd agenticSeek/llm_server/
   ```

3. Instale requisitos e execute:
   ```bash
   pip3 install -r requirements.txt
   python3 app.py --provider ollama --port 3333
   ```

4. No seu computador, ajuste `config.ini`:
   ```ini
   [MAIN]
   is_local = False
   provider_name = server
   provider_model = deepseek-r1:70b
   provider_server_address = <IP_DO_SERVIDOR>:3333
   ```
   
## FAQ

**P: Que hardware eu preciso?**  

| Tamanho do Modelo  | GPU  | Comentário                                               |
|-----------|--------|-----------------------------------------------------------|
| 7B        | 8GB VRAM | ⚠️ Não recomendado. Performance ruim, alucinações frequentes, e agentes planejadores provavelmente falharão. |
| 14B        | 12 GB VRAM (ex: RTX 3060) | ✅ Usável para tarefas simples. Pode ter dificuldades com navegação web e tarefas de planejamento. |
| 32B        | 24+ GB VRAM (ex: RTX 4090) | 🚀 Sucesso com a maioria das tarefas, ainda pode ter dificuldades com planejamento de tarefas |
| 70B+        | 48+ GB VRAM (ex: mac studio) | 💪 Excelente. Recomendado para casos de uso avançados. |

**P: Por que Deepseek R1 em vez de outros modelos?**  

Deepseek R1 se destaca em raciocínio e uso de ferramentas para seu tamanho. Achamos que é uma escolha sólida para nossas necessidades, outros modelos funcionam bem, mas Deepseek é nossa escolha principal.

**P: Recebo um erro ao executar `cli.py`. O que faço?**  

Certifique-se de que o local está rodando (`ollama serve`), seu `config.ini` corresponde ao seu provedor, e as dependências estão instaladas. Se nada funcionar, sinta-se à vontade para abrir uma issue.

**P: Pode realmente rodar 100% localmente?**  

Sim, com provedores Ollama, lm-studio ou server, todos os modelos de fala para texto, LLM e texto para fala rodam localmente. Opções não-locais (OpenAI ou outras APIs) são opcionais.

**P: Por que devo usar AgenticSeek quando tenho Manus?**

Isso começou como um Projeto Paralelo que fizemos por interesse em agentes de IA. O que é especial sobre isso é que queremos usar modelos locais e evitar APIs.
Nos inspiramos em Jarvis e Friday (filmes do Homem de Ferro) para torná-lo "legal", mas para funcionalidade nos inspiramos mais no Manus, porque é isso que as pessoas querem em primeiro lugar: uma alternativa local ao Manus.
Ao contrário do Manus, o AgenticSeek prioriza a independência de sistemas externos, dando a você mais controle, privacidade e evitando custos de API.

## Contribuir

Estamos procurando desenvolvedores para melhorar o AgenticSeek! Confira issues abertas ou discussões.

[Guia de contribuição](./docs/CONTRIBUTING.md)

[![Star History Chart](https://api.star-history.com/svg?repos=Fosowl/agenticSeek&type=Date)](https://www.star-history.com/#Fosowl/agenticSeek&Date)

## Mantenedores:

 > [Fosowl](https://github.com/Fosowl) | Horário de Paris | (Às vezes ocupado)

 > [https://github.com/antoineVIVIES](antoineVIVIES) | Horário de Taipei | (Frequentemente ocupado)

 > [steveh8758](https://github.com/steveh8758) | Horário de Taipei | (Sempre ocupado)
   