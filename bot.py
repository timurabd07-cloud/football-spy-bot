import random
import asyncio
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8698655440:AAFKvfG3JSEDv22TYgj1ViwwA6djVnRWiRE")

CATEGORIES = {
    "🌟 ТОП-10 ЗМ за 21 век": [
        "🇧🇷 Рафинья", "🇦🇷 Лионель Месси", "🇪🇸 Ламин Ямаль", "🇺🇾 Луис Суарес",
        "🇧🇷 Неймар", "🇵🇹 Криштиану Роналду", "🇫🇷 Карим Бензема", "🇫🇷 Усман Дембеле",
        "🇵🇹 Витинья", "🇵🇹 Нуно Мендес", "🇪🇸 Педри", "🇫🇷 Килиан Мбаппе",
        "🇪🇬 Мохаммед Салах", "🇫🇷 Дезире Дуэ", "🇦🇷 Лаутаро Мартинес",
        "🇧🇷 Винисиус Жуниор", "🇪🇸 Родри", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джуд Беллингем",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Гарри Кейн", "🇳🇴 Эрлинг Холанд", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Фил Фоден",
        "🇪🇸 Дани Карвахаль", "🇩🇪 Тони Кроос", "🇩🇪 Флориан Виртц",
        "🇫🇷 Антуан Гризманн", "🇵🇱 Роберт Левандовски", "🇧🇪 Кевин Де Брёйне",
        "🇦🇷 Хулиан Альварес", "🇳🇬 Виктор Осимхен", "🇵🇹 Бернарду Силва",
        "🇭🇷 Лука Модрич", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Трент Александер-Арнольд",
        "🇮🇹 Жоржиньо", "🇮🇹 Джорджо Кьеллини", "🇵🇹 Бруну Фернандеш",
        "🇩🇪 Томас Мюллер", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джейдон Санчо", "🇳🇱 Вирджил ван Дейк",
        "🇸🇳 Садио Мане", "🇧🇷 Алиссон Бекер", "🇳🇱 Френки де Йонг",
        "🇳🇱 Маттейс де Лигт", "🇧🇪 Эден Азар", "🇪🇸 Серхио Рамос",
        "🇭🇷 Иван Ракитич", "🇸🇮 Ян Облак", "🇧🇷 Марсело",
        "🇭🇷 Марио Манджукич", "🇫🇷 Н'Голо Канте", "🇧🇷 Роберто Фирмино",
        "🇺🇾 Диего Годин", "🇪🇸 Тьяго Алькантара", "🇺🇾 Эдинсон Кавани",
        "🇬🇦 Пьер-Эмерик Обамеянг", "🇦🇷 Гонсало Игуаин", "🇦🇷 Пауло Дибала",
        "🇪🇸 Андрес Иньеста", "🇪🇸 Хави", "🇩🇪 Мануэль Нойер",
        "🇨🇱 Алексис Санчес", "🇦🇷 Серхио Агуэро", "🇩🇿 Рияд Марез",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Гарет Бэйл", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джейми Варди",
        "🇸🇪 Златан Ибрагимович", "🇪🇸 Фернандо Торрес", "🇳🇱 Уэсли Снейдер",
        "🇫🇷 Франк Рибери", "🇨🇿 Павел Недвед", "🇺🇦 Александр Зинченко",
        "🇧🇷 Роналдо", "🇧🇷 Роналдиньо", "🇧🇷 Кака",
        "🇫🇷 Зинедин Зидан", "🇮🇹 Фабио Каннаваро", "🇳🇱 Робин ван Перси",
        "🇳🇱 Арьен Роббен", "🇮🇹 Андреа Пирло", "🇺🇾 Диего Форлан",
        "🇪🇸 Икер Касильяс", "🇪🇸 Давид Вилья", "🇨🇮 Дидье Дрогба",
        "🇪🇸 Хаби Алонсо", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Фрэнк Лэмпард", "🇫🇷 Тьерри Анри",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Стивен Джеррард", "🇮🇹 Паоло Мальдини", "🇨🇲 Самюэль Это'О",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Уэйн Руни", "🇧🇷 Роберто Карлос", "🇪🇸 Рауль",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Дэвид Бекхэм", "🇷🇺 Андрей Аршавин", "🇮🇹 Франческо Тотти",
        "🇧🇷 Робиньо"
    ],
    "🏆 ТОП-КЛУБЫ": [
        "🇪🇸 Ламин Ямаль", "🇧🇷 Рафинья", "🇪🇸 Педри", "🇪🇸 Гави",
        "🇫🇷 Килиан Мбаппе", "🇧🇷 Винисиус Жуниор", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джуд Беллингем",
        "🇳🇴 Эрлинг Холанд", "🇪🇬 Мохаммед Салах", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Гарри Кейн",
        "🇵🇱 Роберт Левандовски", "🇫🇷 Антуан Гризманн", "🇧🇪 Кевин Де Брёйне",
        "🇦🇷 Лаутаро Мартинес", "🇩🇪 Джамал Мусиала", "🇵🇹 Рафаэл Леау",
        "🇳🇱 Вирджил ван Дейк", "🇧🇷 Алиссон Бекер", "🇸🇮 Ян Облак",
        "🇩🇪 Мануэль Нойер", "🇧🇷 Родриго", "🇵🇹 Бернарду Силва",
        "🇪🇸 Родри", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Фил Фоден", "🇦🇷 Хулиан Альварес",
        "🇫🇷 Усман Дембеле", "🇬🇪 Хвича Кварацхелия", "🇳🇱 Френки де Йонг",
        "🇵🇹 Бруну Фернандеш", "🇦🇷 Пауло Дибала"
    ],
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 АПЛ (звёзды 2020-2025)": [
        "🇪🇬 Мохаммед Салах", "🇳🇱 Вирджил ван Дейк", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Трент Александер-Арнольд",
        "🇧🇷 Алиссон Бекер", "🇸🇳 Садио Мане", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джордан Хендерсон",
        "🇳🇴 Эрлинг Холанд", "🇧🇪 Кевин Де Брёйне", "🇵🇹 Бернарду Силва",
        "🇪🇸 Родри", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Фил Фоден", "🇦🇷 Хулиан Альварес",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Букайо Сака", "🇳🇴 Мартин Эдегор", "🇧🇷 Габриэль Мартинелли",
        "🇫🇷 Вильям Салиба", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Деклан Райс", "🇧🇷 Габриэль Жезус",
        "🇵🇹 Бруну Фернандеш", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Маркус Рэшфорд", "🇧🇷 Каземиро",
        "🇰🇷 Сон Хын Мин", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Гарри Кейн", "🇦🇷 Кристиан Ромеро",
        "🇸🇳 Николя Джексон", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Коул Палмер", "🇦🇷 Энцо Фернандес",
        "🇧🇷 Тьяго Силва", "🇦🇷 Эмилиано Мартинес", "🇧🇷 Бруно Гимарайнш"
    ]
}

ALL_FOOTBALLERS = []
for cat_players in CATEGORIES.values():
    ALL_FOOTBALLERS.extend(cat_players)
ALL_FOOTBALLERS = list(set(ALL_FOOTBALLERS))
CATEGORIES["🌍 ALL (все)"] = ALL_FOOTBALLERS


class Game:
    def __init__(self):
        self.players = {}
        self.spy = None
        self.footballer = None
        self.category = None
        self.active = False
        self.host = None
        self.votes = {}
        self.roles = {}
        self.offline_mode = False


games = {}

def get_game(chat_id):
    if chat_id not in games:
        games[chat_id] = Game()
    return games[chat_id]


def get_status(g):
    if not g.host:
        return "⏳ Ожидание: /newgame или /offline"
    if g.offline_mode:
        if not g.active:
            return "⏳ Ожидание: /offline ЧИСЛО"
        else:
            return "🎮 Офлайн-игра идёт! Жмите кнопки."
    if not g.category:
        return "📂 Шаг 1: Выберите категорию кнопкой выше"
    if not g.active:
        return f"👥 Шаг 2: Игроки заходят /join\n📂 Категория: {g.category}\n👥 Игроков: {len(g.players)}/50"
    if g.active and not g.votes:
        return f"💬 Шаг 3: Обсуждение!\n👥 Игроков: {len(g.players)}\nВедущий: /vote когда готовы"
    if g.votes:
        return f"🗳 Шаг 4: Голосование!\nПроголосовало: {len(g.votes)}/{len(g.players)}"
    return "✅ Игра завершена"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    g = get_game(chat_id)
    await update.message.reply_text(
        "⚽🕵️ *ФУТБОЛЬНЫЙ ШПИОН* 🕵️⚽\n\n"
        f"📋 *Статус:* {get_status(g)}\n\n"
        "📱 */newgame* — начать онлайн\n"
        "🏠 */offline* — офлайн\n"
        "📋 */status* — что делать\n"
        "📖 */rules* — правила",
        parse_mode="Markdown"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    g = get_game(chat_id)
    await update.message.reply_text(f"📋 *СТАТУС:*\n{get_status(g)}", parse_mode="Markdown")


async def newgame(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    g = get_game(chat_id)
    if g.active:
        await update.message.reply_text("⚠️ Идёт игра! /end")
        return
    g.__init__()
    g.host = update.effective_user.id
    g.players[update.effective_user.id] = update.effective_user.first_name
    g.offline_mode = False
    keyboard = [[InlineKeyboardButton(cat_name, callback_data=f"cat_{cat_name}")] for cat_name in CATEGORIES]
    await update.message.reply_text(
        f"⚽ *НОВАЯ ИГРА!*\n👑 Ведущий: *{update.effective_user.first_name}*\n\n📂 *ШАГ 1: Выбери категорию:*",
        reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
    )


async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    g = get_game(chat_id)
    if not g.host or g.offline_mode or g.active:
        await update.message.reply_text("⚠️ Нельзя войти!")
        return
    if g.category is None:
        await update.message.reply_text("⚠️ Сначала выбери категорию!")
        return
    uid = update.effective_user.id
    if uid in g.players:
        await update.message.reply_text("⚠️ Ты уже в игре!")
        return
    g.players[uid] = update.effective_user.first_name
    await update.message.reply_text(f"✅ *{update.effective_user.first_name}* в игре! ({len(g.players)}/50)", parse_mode="Markdown")


async def deal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    g = get_game(chat_id)
    if g.offline_mode or update.effective_user.id != g.host:
        await update.message.reply_text("⚠️ Нельзя!")
        return
    if g.category is None or len(g.players) < 3:
        await update.message.reply_text("❌ Минимум 3 игрока и выбери категорию!")
        return
    players_list_cat = CATEGORIES.get(g.category, [])
    if not players_list_cat:
        await update.message.reply_text("⚠️ Категория пустая!")
        return
    g.active = True
    g.footballer = random.choice(players_list_cat)
    g.spy = random.choice(list(g.players.keys()))
    g.roles = {uid: "spy" if uid == g.spy else "civilian" for uid in g.players}
    g.votes = {}
    keyboard = [[InlineKeyboardButton("🔍 ПОСМОТРЕТЬ РОЛЬ", callback_data="show_role")]]
    await update.message.reply_text(
        f"✅ *РОЛИ РАЗДАНЫ!*\n👥 Игроков: *{len(g.players)}*\n📂 *{g.category}*\n\nЖмите кнопку, потом /vote",
        reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
    )


async def offline(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    g = get_game(chat_id)
    args = context.args
    if not args:
        g.__init__()
        g.offline_mode = True
        g.host = update.effective_user.id
        keyboard = [[InlineKeyboardButton(cat_name, callback_data=f"offcat_{cat_name}")] for cat_name in CATEGORIES]
        await update.message.reply_text(
            "🏠 *ОФЛАЙН*\n1️⃣ Выбери категорию\n2️⃣ Потом: /offline ЧИСЛО",
            reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
        )
        return
    try:
        num = int(args[0])
    except:
        await update.message.reply_text("/offline ЧИСЛО")
        return
    if num < 3 or num > 50:
        await update.message.reply_text("❌ 3-50 игроков!")
        return
    if not g.category:
        g.category = "🌍 ALL (все)"
    g.offline_mode = True
    g.active = True
    g.footballer = random.choice(CATEGORIES.get(g.category, ALL_FOOTBALLERS))
    for i in range(1, num + 1):
        g.players[i] = f"Игрок {i}"
    g.spy = random.choice(list(g.players.keys()))
    g.roles = {uid: "spy" if uid == g.spy else "civilian" for uid in g.players}
    keyboard = [[InlineKeyboardButton(f"🎭 Игрок {i} — ПОСМОТРЕТЬ РОЛЬ", callback_data=f"offline_{i}")] for i in range(1, num + 1)]
    await update.message.reply_text(
        f"🏠 *ОФЛАЙН {num} игроков*\n📂 {g.category}\n\nЖмите на свой номер!",
        reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data
    uid = q.from_user.id
    chat_id = q.message.chat.id
    g = get_game(chat_id)

    if data.startswith("cat_"):
        cat_name = data[4:]
        if cat_name in CATEGORIES:
            g.category = cat_name
            await q.edit_message_text(f"✅ *{cat_name}*\nТеперь /join", parse_mode="Markdown")

    elif data.startswith("offcat_"):
        cat_name = data[7:]
        if cat_name in CATEGORIES:
            g.category = cat_name
            await q.edit_message_text(f"✅ *{cat_name}*\nТеперь /offline ЧИСЛО", parse_mode="Markdown")

    elif data == "show_role":
        if uid not in g.roles:
            await q.answer("⚠️ Ты не в игре!", show_alert=True)
            return
        text = (
            f"🕵️ *Ты — ШПИОН!*\nСписок:\n" + "\n".join(CATEGORIES.get(g.category, []))
            if g.roles[uid] == "spy" else
            f"⚽ *Ты — МИРНЫЙ!*\n🔥 Загадан: *{g.footballer}*"
        )
        try:
            await context.bot.send_message(uid, text, parse_mode="Markdown")
            await q.answer("✅ Роль в ЛС!", show_alert=True)
        except:
            await q.answer("❌ Напиши боту /start!", show_alert=True)

    elif data.startswith("offline_"):
        player_num = int(data.split("_")[1])
        if player_num not in g.roles:
            await q.answer("⚠️ Ошибка!", show_alert=True)
            return
        text = f"🕵️ Игрок {player_num} — ШПИОН!" if g.roles[player_num] == "spy" else f"⚽ Игрок {player_num} — МИРНЫЙ!\nЗагадан: {g.footballer}"
        role_msg = await context.bot.send_message(chat_id, text, parse_mode="Markdown")
        await asyncio.sleep(5)
        try:
            await role_msg.delete()
        except:
            pass
        new_keyboard = []
        for row in q.message.reply_markup.inline_keyboard:
            new_row = [InlineKeyboardButton("✅ Просмотрено", callback_data="viewed") if btn.callback_data == data else btn for btn in row]
            new_keyboard.append(new_row)
        await q.edit_message_reply_markup(InlineKeyboardMarkup(new_keyboard))

    elif data.startswith("vote_"):
        if uid not in g.players or uid in g.votes:
            await q.answer("⚠️ Уже голосовал!", show_alert=True)
            return
        g.votes[uid] = int(data.split("_")[1])
        await q.answer(f"✅ ({len(g.votes)}/{len(g.players)})", show_alert=True)
        if len(g.votes) == len(g.players):
            await calculate_results(context, chat_id)

async def vote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    g = get_game(chat_id)
    if g.offline_mode or not g.active or update.effective_user.id != g.host:
        await update.message.reply_text("⚠️ Нельзя!")
        return
    g.votes = {}
    keyboard = [[InlineKeyboardButton(f"🕵️ {name}", callback_data=f"vote_{uid}")] for uid, name in g.players.items()]
    await update.message.reply_text(
        f"🗳 *ГОЛОСОВАНИЕ!* 0/{len(g.players)}",
        reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown"
    )

async def calculate_results(context, chat_id):
    g = get_game(chat_id)
    vote_count = {}
    for t in g.votes.values():
        vote_count[t] = vote_count.get(t, 0) + 1
    most = max(vote_count, key=vote_count.get)
    caught = (most == g.spy)
    msg = "📊 *ИТОГИ:*\n\n"
    for uid, name in g.players.items():
        msg += f"{'🕵️' if uid == g.spy else '⚽'} {name}: {vote_count.get(uid, 0)}\n"
    msg += f"\n⚽ Загадан: *{g.footballer}*\n"
    msg += f"✅ Шпион пойман! /guess Имя" if caught else f"🕵️ Шпион победил!"
    await context.bot.send_message(chat_id, msg, parse_mode="Markdown")
    g.active = False

async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    g = get_game(chat_id)
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("/guess Имя")
        return
    if text.lower() == g.footballer.lower():
        await update.message.reply_text(f"🎉 Верно! Шпион спасся!")
    else:
        await update.message.reply_text(f"❌ Было: {g.footballer}")

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 *ПРАВИЛА:*\n/newgame → /join → /deal → /vote → /guess\n/offline ЧИСЛО — офлайн",
        parse_mode="Markdown"
    )

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    g = get_game(chat_id)
    g.__init__()
    await update.message.reply_text("🛑 Игра завершена!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    for cmd, handler in [
        ("start", start), ("status", status), ("newgame", newgame),
        ("join", join), ("deal", deal), ("offline", offline),
        ("vote", vote), ("guess", guess), ("rules", rules), ("end", end)
    ]:
        app.add_handler(CommandHandler(cmd, handler))
    app.add_handler(CallbackQueryHandler(button))
    print("⚽ Бот запущен! Много чатов — много игр!")
    app.run_polling()

if __name__ == "__main__":
    main()
