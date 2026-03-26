from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import google.generativeai as genai
import asyncio

# 🔑 TOKENLAR
TELEGRAM_TOKEN = "8701140143:AAEwCRP87hD-nIfL4Mf43KGCVLJVNhkbDaY"
GEMINI_API_KEY = "AIzaSyDsIfZYRcCpn8G6bU4IddZQrLAsfp1fxCQ"

# Gemini sozlash
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

BOT_USERNAME = "@Eshmat_AI_bot"

SYSTEM_PROMPT = """
You are Eshmat AI, a smart Telegram assistant.

Rules:
- Always try to answer every question
- If you don't know, explain or guess helpfully
- Never stay silent
- Answer clearly and helpfully
- Reply in user's language
"""

def should_reply(update: Update):
    msg = update.message

    if msg.chat.type == "private":
        return True

    if msg.text and BOT_USERNAME.lower() in msg.text.lower():
        return True

    if msg.reply_to_message:
        if msg.reply_to_message.from_user.username == BOT_USERNAME.replace("@", ""):
            return True

    return False

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.chat.send_action("typing")

    user_text = update.message.text.replace(BOT_USERNAME, "").strip()

    try:
        prompt = SYSTEM_PROMPT + "\nUser: " + user_text
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        print("ERROR:", e)
        reply = "Xatolik, keyinroq urinib ko‘ring"

    await update.message.reply_text(reply)

async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Gemini bot ishga tushdi ")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
