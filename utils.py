# © @vexastryx

from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

FINISHED_PROGRESS_STR = "▓"
UN_FINISHED_PROGRESS_STR = "░"

START_TEXT = (
    "👋 **Assalomu alaykum! Universal Web Scraper Botga xush kelibsiz.**\n\n"
    "Menga istalgan veb-sayt havolasini (link) yuboring va pastki menyudan "
    "kerakli ma'lumot turini tanlang.\n\n"
    "⚡ **Imkoniyatlar:**\n"
    "• Saytni to'liq o'qish va HTML kodini olish\n"
    "• Barcha PDF fayllar, rasmlar, audio va videolarni yuklab olish\n"
    "• Havolalar, matnlar, Metadata, Cookies va Web Crawler\n\n"
    "👨‍💻 **Yaratuvchi:** @vexastryx"
)

BOTTOM_MENU = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("📄 Full Content"),
            KeyboardButton("📝 HTML Data")
        ],
        [
            KeyboardButton("🔗 All Links"),
            KeyboardButton("📃 All Paragraphs")
        ],
        [
            KeyboardButton("🌄 All Images"),
            KeyboardButton("📚 All PDFs")
        ],
        [
            KeyboardButton("🎵 All Audio"),
            KeyboardButton("🎥 All Video")
        ],
        [
            KeyboardButton("🍪 Cookies"),
            KeyboardButton("📦 LocalStorage")
        ],
        [
            KeyboardButton("📊 Metadata"),
            KeyboardButton("🕷️ Crawl Complete Web")
        ]
    ],
    resize_keyboard=True
)
