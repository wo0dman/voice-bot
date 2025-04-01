
# 🎤 Voice2Text Telegram Bot / Голосовой Бот для Транскрибации

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

**Convert voice messages to text in Telegram**  
**Конвертация голосовых сообщений в текст в Телеграме**

---

## 🇷🇺 Русская Версия

### 📝 Описание
Бот преобразует голосовые сообщения и аудиофайлы в текст с использованием:
- Google Speech Recognition (онлайн)
- PyDub для обработки аудио
- FFmpeg для конвертации форматов

### 🌟 Особенности
- Поддержка форматов: OGG, WAV, MP3
- Автоматическая обработка длинных сообщений
- Мультиязычная транскрипция (русский/английский)
- Кэширование результатов

### ⚙️ Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/voice-bot.git
   cd voice-bot
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Установите FFmpeg:
   - Windows: [Скачать](https://ffmpeg.org/download.html)
   - Ubuntu: `sudo apt install ffmpeg`

4. Создайте файл `.env`:
   ```ini
   TELEGRAM_TOKEN=ваш_токен_бота
   ```

### 🚀 Запуск
```bash
python bot.py
```

### 🎮 Использование
1. Начните диалог с ботом: `/start`
2. Отправьте голосовое сообщение или аудиофайл
3. Получите текстовую расшифровку

### ⚠️ Важно
- Для работы Google Speech требуется интернет
- Максимальная длина аудио: 5 минут
- Токен бота храните в секрете!

---

## 🇺🇸 English Version

### 📝 Description
A Telegram bot that converts voice messages and audio files to text using:
- Google Speech Recognition (online)
- PyDub for audio processing
- FFmpeg format conversion

### 🌟 Features
- Supported formats: OGG, WAV, MP3
- Automatic long message handling
- Multilingual transcription (RU/EN)
- Result caching

### ⚙️ Installation
1. Clone repository:
   ```bash
   git clone https://github.com/yourusername/voice-bot.git
   cd voice-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install FFmpeg:
   - Windows: [Download](https://ffmpeg.org/download.html)
   - Ubuntu: `sudo apt install ffmpeg`

4. Create `.env` file:
   ```ini
   TELEGRAM_TOKEN=your_bot_token
   ```

### 🚀 Launch
```bash
python bot.py
```

### 🎮 Usage
1. Start conversation: `/start`
2. Send voice message or audio file
3. Receive text transcription

### ⚠️ Important
- Google Speech requires internet
- Max audio length: 5 minutes
- Keep bot token secret!

---

## 📄 License
MIT License - see [LICENSE](LICENSE) for details
