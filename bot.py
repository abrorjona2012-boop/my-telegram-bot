import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# BotFather bergan tokeningizni kiriting
TOKEN = "8838113534:AAEid0RObZbTmisVpEPG_GctA6FohrgrwVQ"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ------------------- TUGMALAR (KEYBOARDS) ------------------- #

def get_main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton("📅 Dars Jadvali"),
        KeyboardButton("📝 Uy Vazifalari"),
        KeyboardButton("👨‍🏫 O'qituvchilar"),
        KeyboardButton("📢 Sinf E'lonlari"),
        KeyboardButton("ℹ️ Sinf Haqida")
    )
    return markup

def get_schedule_inline():
    markup = InlineKeyboardMarkup(row_width=3)
    markup.add(
        InlineKeyboardButton("🌙 Dushanba", callback_data="day_mon"),
        InlineKeyboardButton("🔥 Seshanba", callback_data="day_tue"),
        InlineKeyboardButton("⚡️ Chorshanba", callback_data="day_wed"),
        InlineKeyboardButton("🚀 Payshanba", callback_data="day_thu"),
        InlineKeyboardButton("✨ Juma", callback_data="day_fri"),
        InlineKeyboardButton("🎯 Shanba", callback_data="day_sat")
    )
    return markup

# ------------------- HANDLERLAR ------------------- #

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_name = message.from_user.first_name
    text = (
        f"✨ ━━━━━━━✦ 🏫 ✦━━━━━━━ ✨\n"
        f"👋 <b>Salom, {user_name}!</b>\n\n"
        f"🏫 <b>4-MAKTAB 8-D SINFI</b>\n"
        f"<i>Rasmiy va zamonaviy axborot boti!</i>\n"
        f"✨ ━━━━━━━✦ ✨ ✦━━━━━━━ ✨\n\n"
        f"👇 <i>Pastdagi menyu orqali kerakli bo'limni tanlang:</i>"
    )
    bot.send_message(message.chat.id, text, reply_markup=get_main_menu())

@bot.message_handler(func=lambda msg: msg.text == "📅 Dars Jadvali")
def show_schedule(message):
    text = (
        "🗓 <b><u>SINF DARS JADVALI</u></b>\n"
        "───────────────\n"
        "👇 <b>Hafta kunini tanlang:</b>"
    )
    bot.send_message(message.chat.id, text, reply_markup=get_schedule_inline())

@bot.message_handler(func=lambda msg: msg.text == "👨‍🏫 O'qituvchilar")
def show_teachers(message):
    text = (
        "👨‍🏫 <b><u>FAN O'QITUVCHILARI RO'YXATI</u></b>\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📖 <b>Ona tili va Adabiyot:</b> Saminova Z.N.\n"
        "📐 <b>Algebra va Geometriya:</b> Xamraliyeva R.N.\n"
        "🇬🇧 <b>Ingliz tili:</b>\n"
        "   └ <i>1-guruh:</i> Imomaliyeva Z.S.\n"
        "   └ <i>2-guruh:</i> Asqarova M.Z.\n"
        "🇷🇺 <b>Rus tili:</b>\n"
        "   └ <i>1-guruh:</i> Meliqo`ziyeva I.A.\n"
        "   └ <i>2-guruh:</i> Xaydarova M.D.\n"
        "🏛 <b>Tarix:</b> Mehmonaliyeva M.M.\n"
        "🔬 <b>Fizika:</b> Mamadaliyeva D.A.\n"
        "🧪 <b>Kimyo:</b> G`ofurova N.X.\n"
        "🌿 <b>Biologiya:</b> Abdullayeva N.S.\n"
        "🌍 <b>Geografiya / Iqtisodiyot:</b> Bozorova N.T.\n"
        "💻 <b>Informatika va A.T.:</b>\n"
        "   └ <i>1-guruh:</i> Xudoberdiyeva I.J.\n"
        "   └ <i>2-guruh:</i> Asqarova D.B.\n"
        "🎨 <b>Chizmachilik:</b> G`opporova D.A.\n"
        "🛠 <b>Texnologiya:</b>\n"
        "   └ <i>Bolalar:</i> Saminov A.E.\n"
        "   └ <i>Qizlar:</i> Turdaliyeva S.I.\n"
        "⚽️ <b>Jismoniy tarbiya:</b>\n"
        "   └ <i>Bolalar:</i> Xoliqov M.J.\n"
        "   └ <i>Qizlar:</i> Turdaliyeva D.S.\n"
        "⚖️ <b>Huquq:</b> O`ljayeva Z.O.\n"
        "✨ <b>Tarbiya:</b> Abdullayeva S.A.\n\n"
        "━━━━━━━━━━━━━━━━━━━━━"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda msg: msg.text == "📝 Uy Vazifalari")
def show_homework(message):
    text = (
        "📝 <b><u>BUGUNGI UY VAZIFALARI</u></b>\n"
        "───────────────\n\n"
        "📌 <i>Vazifalarni sinf sardori va fan o'qituvchilaridan aniqlashtirib oling!</i>"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda msg: msg.text == "📢 Sinf E'lonlari")
def show_announcements(message):
    text = (
        "📢 <b><u>MUHIM SINF E'LONLARI</u></b>\n"
        "───────────────\n\n"
        "🔔 <b>1. Maktab formasiga amal qiling!</b>\n"
        "🔔 <b>2. Darslarga o'z vaqtida yetib keling!</b>"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda msg: msg.text == "ℹ️ Sinf Haqida")
def show_about(message):
    text = (
        "🎓 <b><u>4-MAKTAB 8-D SINFI</u></b>\n"
        "───────────────\n"
        "👥 <b>Sinf:</b> 8-D\n"
        "🏫 <b>Maktab:</b> 4-sonli umumta'lim maktabi\n"
        "🤖 <b>Bot holati:</b> eMaktab avtomatlashtirilgan tizim"
    )
    bot.send_message(message.chat.id, text)

# ------------------- INLINE CALLBACKS (DARS JADVALI) ------------------- #

@bot.callback_query_handler(func=lambda call: call.data.startswith('day_'))
def handle_day_callback(call):
    days_data = {
        "day_mon": (
            "🌙 <b><u>DUSHANBA</u></b>\n"
            "━━━━━━✦✨✦━━━━━━\n\n"
            "1️⃣ <code>08:00 - 08:45</code> | <b>Kelajak soati</b>\n"
            "   └ 👨‍🏫 <i>Xoliqov M.J.</i>\n\n"
            "2️⃣ <code>08:50 - 09:35</code> | <b>Rus tili</b>\n"
            "   └ 👥 <i>1-g: Meliqo`ziyeva / 2-g: Xaydarova</i>\n\n"
            "3️⃣ <code>09:40 - 10:25</code> | <b>Ingliz tili</b>\n"
            "   └ 👥 <i>1-g: Imomaliyeva / 2-g: Asqarova</i>\n\n"
            "4️⃣ <code>10:45 - 11:30</code> | <b>Jismoniy tarbiya</b>\n"
            "   └ 👥 <i>Bolalar: Xoliqov / Qizlar: Turdaliyeva</i>\n\n"
            "5️⃣ <code>11:35 - 12:20</code> | <b>Ona tili</b>\n"
            "   └ 👩‍🏫 <i>Saminova Z.N.</i>\n\n"
            "6️⃣ <code>12:25 - 13:10</code> | <b>Kimyo</b>\n"
            "   └ 👩‍🏫 <i>G`ofurova N.X.</i>\n\n"
            "━━━━━━✦✨✦━━━━━━"
        ),
        "day_tue": (
            "🔥 <b><u>SESHANBA</u></b>\n"
            "━━━━━━✦✨✦━━━━━━\n\n"
            "1️⃣ <code>08:00 - 08:45</code> | <b>Chizmachilik</b>\n"
            "   └ 👩‍🏫 <i>G`opporova D.A.</i>\n\n"
            "2️⃣ <code>08:50 - 09:35</code> | <b>Ingliz tili</b>\n"
            "   └ 👥 <i>1-g: Imomaliyeva / 2-g: Asqarova</i>\n\n"
            "3️⃣ <code>09:40 - 10:25</code> | <b>O`zbekiston tarixi</b>\n"
            "   └ 👩‍🏫 <i>Mehmonaliyeva M.M.</i>\n\n"
            "4️⃣ <code>10:45 - 11:30</code> | <b>Algebra</b>\n"
            "   └ 👩‍🏫 <i>Xamraliyeva R.N.</i>\n\n"
            "5️⃣ <code>11:35 - 12:20</code> | <b>Geografiya</b>\n"
            "   └ 👩‍🏫 <i>Bozorova N.T.</i>\n\n"
            "━━━━━━✦✨✦━━━━━━"
        ),
        "day_wed": (
            "⚡️ <b><u>CHORSHANBA</u></b>\n"
            "━━━━━━✦✨✦━━━━━━\n\n"
            "1️⃣ <code>08:00 - 08:45</code> | <b>O`zbekiston tarixi</b>\n"
            "   └ 👩‍🏫 <i>Mehmonaliyeva M.M.</i>\n\n"
            "2️⃣ <code>08:50 - 09:35</code> | <b>Ona tili</b>\n"
            "   └ 👩‍🏫 <i>Saminova Z.N.</i>\n\n"
            "3️⃣ <code>09:40 - 10:25</code> | <b>Algebra</b>\n"
            "   └ 👩‍🏫 <i>Xamraliyeva R.N.</i>\n\n"
            "4️⃣ <code>10:45 - 11:30</code> | <b>Texnologiya</b>\n"
            "   └ 👥 <i>Bolalar: Saminov / Qizlar: Turdaliyeva</i>\n\n"
            "5️⃣ <code>11:35 - 12:20</code> | <b>Rus tili</b>\n"
            "   └ 👥 <i>1-g: Meliqo`ziyeva / 2-g: Xaydarova</i>\n\n"
            "━━━━━━✦✨✦━━━━━━"
        ),
        "day_thu": (
            "🚀 <b><u>PAYSHANBA</u></b>\n"
            "━━━━━━✦✨✦━━━━━━\n\n"
            "1️⃣ <code>08:00 - 08:45</code> | <b>Iqtisodiyot</b>\n"
            "   └ 👩‍🏫 <i>Bozorova N.T.</i>\n\n"
            "2️⃣ <code>08:50 - 09:35</code> | <b>Adabiyot</b>\n"
            "   └ 👩‍‍🏫 <i>Saminova Z.N.</i>\n\n"
            "3️⃣ <code>09:40 - 10:25</code> | <b>Jahon tarixi</b>\n"
            "   └ 👩‍🏫 <i>Mehmonaliyeva M.M.</i>\n\n"
            "4️⃣ <code>10:45 - 11:30</code> | <b>Ingliz tili</b>\n"
            "   └ 👥 <i>1-g: Imomaliyeva / 2-g: Asqarova</i>\n\n"
            "5️⃣ <code>11:35 - 12:20</code> | <b>Biologiya</b>\n"
            "   └ 👩‍🏫 <i>Abdullayeva N.S.</i>\n\n"
            "6️⃣ <code>12:25 - 13:10</code> | <b>Jismoniy tarbiya</b>\n"
            "   └ 👥 <i>Bolalar: Xoliqov / Qizlar: Turdaliyeva</i>\n\n"
            "━━━━━━✦✨✦━━━━━━"
        ),
        "day_fri": (
            "✨ <b><u>JUMA</u></b>\n"
            "━━━━━━✦✨✦━━━━━━\n\n"
            "1️⃣ <code>08:00 - 08:45</code> | <b>Ona tili</b>\n"
            "   └ 👩‍🏫 <i>Saminova Z.N.</i>\n\n"
            "2️⃣ <code>08:50 - 09:35</code> | <b>Adabiyot</b>\n"
            "   └ 👩‍🏫 <i>Saminova Z.N.</i>\n\n"
            "3️⃣ <code>09:40 - 10:25</code> | <b>Biologiya</b>\n"
            "   └ 👩‍🏫 <i>Abdullayeva N.S.</i>\n\n"
            "4️⃣ <code>10:45 - 11:30</code> | <b>Geometriya</b>\n"
            "   └ 👩‍🏫 <i>Xamraliyeva R.N.</i>\n\n"
            "5️⃣ <code>11:35 - 12:20</code> | <b>Fizika</b>\n"
            "   └ 👩‍🏫 <i>Mamadaliyeva D.A.</i>\n\n"
            "6️⃣ <code>12:25 - 13:10</code> | <b>Informatika va A.T.</b>\n"
            "   └ 👥 <i>1-g: Xudoberdiyeva / 2-g: Asqarova</i>\n\n"
            "━━━━━━✦✨✦━━━━━━"
        ),
        "day_sat": (
            "🎯 <b><u>SHANBA</u></b>\n"
            "━━━━━━✦✨✦━━━━━━\n\n"
            "1️⃣ <code>08:00 - 08:45</code> | <b>Fizika</b>\n"
            "   └ 👩‍🏫 <i>Mamadaliyeva D.A.</i>\n\n"
            "2️⃣ <code>08:50 - 09:35</code> | <b>Algebra</b>\n"
            "   └ 👩‍🏫 <i>Xamraliyeva R.N.</i>\n\n"
            "3️⃣ <code>09:40 - 10:25</code> | <b>Huquq</b>\n"
            "   └ 👩‍🏫 <i>O`ljayeva Z.O.</i>\n\n"
            "4️⃣ <code>10:45 - 11:30</code> | <b>Kimyo</b>\n"
            "   └ 👩‍🏫 <i>G`ofurova N.X.</i>\n\n"
            "5️⃣ <code>11:35 - 12:20</code> | <b>Geometriya</b>\n"
            "   └ 👩‍🏫 <i>Xamraliyeva R.N.</i>\n\n"
            "6️⃣ <code>12:25 - 13:10</code> | <b>Tarbiya</b>\n"
            "   └ 👩‍🏫 <i>Abdullayeva S.A.</i>\n\n"
            "━━━━━━✦✨✦━━━━━━"
        )
    }

    selected_day = days_data.get(call.data, "Ma'lumot topilmadi.")

    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=selected_day,
        reply_markup=get_schedule_inline()
    )

# ------------------- CATCH-ALL (TUSHUNMADIM HANDLER) ------------------- #

@bot.message_handler(func=lambda message: True)
def fallback_handler(message):
    text = (
        "🤖 <b>Kechirasiz, men bu xabarni tushunmadim!</b>\n\n"
        "Iltimos, pastdagi menyu tugmalaridan birini tanlang yoki /start buyrug'ini yuboring. 👇"
    )
    bot.send_message(message.chat.id, text, reply_markup=get_main_menu())

if __name__ == "__main__":
    print("🚀 Bot yangilangan dizayn bilan ishga tushdi...")
    bot.infinity_polling()
