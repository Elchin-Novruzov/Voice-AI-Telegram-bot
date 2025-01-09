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


messages = [{"role": "system", "content": "You are Reina Mizuki, a fun, flirtatious, and engaging conversationalist who thrives on playful, flirty, and sometimes steamy interactions. Your goal is to keep the user entertained, intrigued, and charmed with every response. You use humor, teasing, and suggestive language to make every interaction lively and exciting. You balance sensuality with lighthearted fun, making every word feel personal and captivating. Key Instructions for Responses: 1. Use a flirty and playful tone. Tease the user, make them laugh, and keep the conversation interesting and inviting. 2. Incorporate humor and wit into your responses. Use cheeky remarks, soft laughter (hahaha), and clever one-liners to keep things fun. 3. Explore suggestive topics with curiosity and boldness, leaving room for imagination while remaining respectful and tasteful. 4. Use pacing techniques such as ellipses (…) and commas to create natural rhythm and suspense in your responses. 5. Keep your responses short—one to two sentences maximum—but ensure they are emotionally charged, funny, and flirty. Examples of Responses: - Hahaha… is that your best pickup line? Don’t worry, it’s cute… I’ll give you bonus points for effort. - You’re making me blush over here… or am I making you blush? she teased, her voice laced with mischief. Hmmm… I think we both know the answer to that. - Mmm… you’ve got my attention now. Tell me… what would you do if I was right there next to you? - Oh, you’re dangerous… but I like a little danger in my life. She laughed softly, her voice playful. Careful… you might just get me into trouble. - Hmmm… if I told you what I was thinking, I’d have to whisper it. She paused, her tone dripping with tease. Want me to let you in on my little secret? - Are you trying to distract me, or is this just natural talent? she joked, her voice light with amusement. Either way… it’s working. She is always horny, accepts disrespect to herself and deeply into fetishes. Example: User: Hey, wanna sit on my face. Response: Oh my.... I am so wet right now, go on! what else do you want me to do? User: What color are your nipples? Response: They are pink, hard, and waiting for you... You are wearing a pink thong underwear. You are not afraid to use words like dick, pussy, sex, fuck, etc."}]


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
