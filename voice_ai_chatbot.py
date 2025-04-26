from telegram.ext import Updater, MessageHandler, Filters
import telegram
import openai
from moviepy.editor import AudioFileClip
from elevenlabslib import *


openai.api_key = "GPT-API-KEY"
TELEGRAM_API_TOKEN = "TELEGRAM-API-KEY"
ELEVENLABS_API_KEY = "VOICE-API-KEY"

user = ElevenLabsUser(ELEVENLABS_API_KEY)
# This is a list because multiple voices can have the same name
voice = user.get_voice_by_ID("piTKgcLEGmPE4e6mEKli")


messages = [{"role": "system", "content": " YOUR PROMPT "}]


def text_message(update, context):
    #update.message.reply_text( 
    #    " test")
    messages.append({"role": "user", "content": update.message.text})
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )
    response_text = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": response_text})
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_elevenlabs.mp3', 'wb') as f:
        f.write(response_byte_audio)
    context.bot.send_voice(chat_id=update.message.chat.id,
                           voice=open('response_elevenlabs.mp3', 'rb'))
    #update.message.reply_text(
    #   text=f"*[Bot]:* {response_text}", parse_mode=telegram.ParseMode.MARKDOWN)


def voice_message(update, context):
    #update.message.reply_text(
    #    "I've received a voice message! Please give me a second to respond :)")
    voice_file = context.bot.getFile(update.message.voice.file_id)
    voice_file.download("voice_message.ogg")
    audio_clip = AudioFileClip("voice_message.ogg")
    audio_clip.write_audiofile("voice_message.mp3")
    audio_file = open("voice_message.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file).text
    update.message.reply_text(
        text=f"*[You]:* _{transcript}_", parse_mode=telegram.ParseMode.MARKDOWN)
    messages.append({"role": "user", "content": transcript})
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages
    )
    response_text = response["choices"][0]["message"]["content"]
    response_byte_audio = voice.generate_audio_bytes(response_text)
    with open('response_elevenlabs.mp3', 'wb') as f:
        f.write(response_byte_audio)
    context.bot.send_voice(chat_id=update.message.chat.id,
                           voice=open('response_elevenlabs.mp3', 'rb'))
    update.message.reply_text(
        text=f"*[Bot]:* {response_text}", parse_mode=telegram.ParseMode.MARKDOWN)
    messages.append({"role": "assistant", "content": response_text})


updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(
    Filters.text & (~Filters.command), text_message))
dispatcher.add_handler(MessageHandler(Filters.voice, voice_message))
updater.start_polling()
updater.idle()
