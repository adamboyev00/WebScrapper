# © @vexastryx

import os
from pyrogram import Client, filters
from dotenv import load_dotenv
from pyrogram.types import Message
from scraper import (
    all_audio_scraping,
    all_images_scraping,
    all_links_scraping,
    all_paragraph_scraping,
    all_pdf_scraping,
    all_video_scraping,
    extract_cookies,
    extract_local_storage,
    html_data_scraping,
    raw_data_scraping,
    extract_metadata
)
from crawler import crawl_web
from utils import BOTTOM_MENU, START_TEXT

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
CRAWL_LOG_CHANNEL = os.getenv("CRAWL_LOG_CHANNEL")

if bot_token is None or api_id is None or api_hash is None:
    raise ValueError("Please set the BOT_TOKEN, API_ID, and API_HASH environment variables.")

app = Client(
    "WebScrapperBot", bot_token=bot_token, api_id=int(api_id), api_hash=api_hash
)

# Har bir foydalanuvchining oxirgi yuborgan linkini saqlash
user_links = {}

# scraper.py funksiyalari ishlashi uchun moslashtirilgan obyekt
class DummyCallback:
    def __init__(self, message: Message, url: str):
        self.message = message
        self.message.text = url
        self.from_user = message.from_user


@app.on_message(filters.command(["start"]) & filters.private)
async def start(_, message: Message):
    await message.reply_text(
        text=START_TEXT,
        reply_markup=BOTTOM_MENU,
        disable_web_page_preview=True,
        quote=True
    )


@app.on_message(
    (filters.regex("https://") | filters.regex("http://") | filters.regex("www."))
    & filters.private
)
async def save_link(_, message: Message):
    user_links[message.from_user.id] = message.text.strip()
    await message.reply_text(
        "✅ **Havola qabul qilindi!**\nEndi pastki menyudan kerakli bo'limni tanlang:\n\n"
        "👨‍💻 @vexastryx",
        reply_markup=BOTTOM_MENU,
        disable_web_page_preview=True
    )


@app.on_message(filters.text & filters.private)
async def handle_menu(bot: Client, message: Message):
    user_id = message.from_user.id
    text = message.text

    if user_id not in user_links:
        await message.reply_text(
            "⚠️ **Avval sayt havolasini (link) yuboring!**\nMasalan: `https://example.com`",
            reply_markup=BOTTOM_MENU
        )
        return

    url = user_links[user_id]
    status_msg = await message.reply_text("⏳ **Ma'lumot yuklanmoqda, kuting...**")
    dummy_update = DummyCallback(status_msg, url)

    if text == "📄 Full Content":
        await raw_data_scraping(dummy_update)
    elif text == "📝 HTML Data":
        await html_data_scraping(dummy_update)
    elif text == "🔗 All Links":
        await all_links_scraping(dummy_update)
    elif text == "📃 All Paragraphs":
        await all_paragraph_scraping(dummy_update)
    elif text == "🌄 All Images":
        await all_images_scraping(bot, dummy_update)
    elif text == "🎵 All Audio":
        await all_audio_scraping(bot, dummy_update)
    elif text == "🎥 All Video":
        await all_video_scraping(bot, dummy_update)
    elif text == "📚 All PDFs":
        await all_pdf_scraping(dummy_update)
    elif text == "🍪 Cookies":
        await extract_cookies(dummy_update)
    elif text == "📦 LocalStorage":
        await extract_local_storage(dummy_update)
    elif text == "📊 Metadata":
        await extract_metadata(dummy_update)
    elif text == "🕷️ Crawl Complete Web":
        if CRAWL_LOG_CHANNEL:
            await crawl_web(bot, dummy_update)
        else:
            await status_msg.edit_text("⚠️ **Web Crawler** ishlashi uchun Render'dagi Environment Variables bo'limiga `CRAWL_LOG_CHANNEL` (kanal ID raqami) qo'shishingiz kerak.")
    else:
        await status_msg.edit_text("❓ Pastki menyudagi tugmalardan birini tanlang yoki yangi havola yuboring.")


print("Bot Running....")
app.run()
