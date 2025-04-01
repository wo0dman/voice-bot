import os
import io
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from speech_recognition import Recognizer, AudioFile
from pydub import AudioSegment

load_dotenv()

class TranscriberBot:
    def __init__(self):
        self.recognizer = Recognizer()
        self.app = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
        
        self.app.add_handler(
            MessageHandler(filters.VOICE, self.handle_voice)
        )
    
    async def handle_voice(self, update: Update, _):
        voice_file = await update.message.voice.get_file()
        audio_bytes = await voice_file.download_as_bytearray()
        
        try:
            # Конвертация OGG -> WAV
            ogg_stream = io.BytesIO(audio_bytes)
            audio = AudioSegment.from_ogg(ogg_stream)
            wav_stream = io.BytesIO()
            audio.export(wav_stream, format="wav")
            wav_stream.seek(0)
            
            # Распознавание речи
            with AudioFile(wav_stream) as source:
                audio_data = self.recognizer.record(source)
                text = self.recognizer.recognize_google(
                    audio_data, 
                    language="ru-RU",
                    show_all=False
                )
                await update.message.reply_text(text)
                
        except Exception as e:
            await update.message.reply_text(f"Ошибка: {str(e)}")
        finally:
            ogg_stream.close()
            wav_stream.close()

if __name__ == "__main__":
    bot = TranscriberBot()
    bot.app.run_polling()