# 🦊 Bot FURIA – Telegram Chatbot

Este repositório contém o protótipo de um chatbot da FURIA desenvolvido com foco em fãs que desejam interagir com o time de forma rápida, prática e divertida através do Telegram. O projeto inclui uma **landing page** funcional que redireciona para o bot e um **bot integrado** com múltiplas funcionalidades.

---

## 📁 Estrutura do Repositório

```
furia-bot/
│
├── bot/                 # Código-fonte do bot em Python
│   ├── bot.py
│   └── .env             # Variáveis de ambiente (não subir para o GitHub)
│
├── landing-page/       # Código da landing page
│   ├── index.html
│   └── logo.png
│
└── README.md            # Documentação geral do projeto
```

---

## 📲 Funcionalidades do Bot

O bot foi criado no Telegram para centralizar as principais interações com fãs da FURIA:

- 📰 Notícias atualizadas sobre o time  
- 🏆 Últimos resultados dos jogos  
- 📅 Informações sobre a próxima partida  
- 🎤 Simulador de torcida (mensagens e emojis animados)  
- 📡 Status ao vivo fictício para simular uma partida  
- 📲 Atendimento inteligente via WhatsApp  
- 📱 Links das redes sociais da FURIA  
- 🛒 Acesso direto à loja oficial  

---

## 🌐 Landing Page

A landing page foi desenvolvida com **HTML5 e Tailwind CSS**. Ela apresenta o bot, explica sua proposta e fornece um botão direto para iniciá-lo no Telegram.

📍 **Veja a landing page em produção:**  
👉 [https://nicolasthomee.github.io/FURIAbot/](https://nicolasthomee.github.io/FURIAbot/)

---

## 🚀 Como Rodar Localmente

### Requisitos

- Python 3.10+
- [Python Telegram Bot](https://docs.python-telegram-bot.org/)
- python-dotenv

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
cd furia-bot/bot
```

2. Instale as dependências:
```bash
pip install python-telegram-bot python-dotenv
```

3. Crie o arquivo `.env` com o seguinte conteúdo:
```env
BOT_TOKEN=seu_token_aqui
```

4. Execute o bot:
```bash
python bot.py
```

---

## 📌 Observações

- Este projeto é um **protótipo** e pode ser expandido com notificações em tempo real, integração com APIs de eSports, e muito mais.
- O bot está hospedado localmente no momento, mas pode ser facilmente migrado para um servidor com `python-telegram-bot` + Docker ou cloud (Heroku, Railway, etc.).