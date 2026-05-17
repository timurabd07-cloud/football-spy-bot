import random
import asyncio
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8698655440:AAEcTLpBGEuhroRLHq3dosKMcaq6sswRU78")

# ===== КАТЕГОРИИ =====
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
        "🇪🇸 Пау Кубарси", "🇪🇸 Эрик Гарсия", "🇪🇸 Жоан Гарсия", "🇪🇸 Алехандро Бальде",
        "🇫🇷 Жюль Кунде", "🇵🇱 Роберт Левандовски", "🇳🇱 Френки де Йонг",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Маркус Рэшфорд", "🇵🇱 Войцех Щенсны",
        "🇫🇷 Килиан Мбаппе", "🇺🇾 Федерико Вальверде", "🇫🇷 Эдуардо Камавинга",
        "🇧🇷 Винисиус Жуниор", "🇧🇷 Родриго", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джуд Беллингем",
        "🇦🇷 Фран Гарсия", "🇺🇦 Андрей Лунин", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Трент Александер-Арнольд",
        "🇩🇪 Антонио Рюдигер", "🇧🇷 Эдер Милитао", "🇹🇷 Арда Гюлер",
        "🇪🇸 Нико Уильямс", "🇦🇷 Хулиан Альварес", "🇦🇷 Науэль Молина",
        "🇸🇮 Ян Облак", "🇪🇸 Коке", "🇳🇬 Адемола Лукман",
        "🇪🇸 Робин Ле Норман", "🇪🇸 Маркос Льоренте", "🇫🇷 Антуан Гризманн",
        "🇦🇷 Родриго Де Пауль",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Гарри Кейн", "🇫🇷 Майкл Олисе", "🇩🇪 Джамал Мусиала",
        "🇳🇱 Маттейс де Лигт", "🇩🇪 Йонатан Та", "🇩🇪 Леон Горетцка",
        "🇩🇪 Серж Гнабри", "🇩🇪 Йозуа Киммих", "🇦🇹 Конрад Лаймер",
        "🇩🇪 Александар Павлович",
        "🇫🇷 Усман Дембеле", "🇬🇪 Хвича Кварацхелия", "🇵🇹 Гонсалу Рамуш",
        "🇫🇷 Брэдли Барколя", "🇵🇹 Витинья", "🇪🇨 Вильян Пачо",
        "🇵🇹 Жоау Невеш", "🇫🇷 Уоррен Заир-Эмери", "🇧🇷 Маркиньос",
        "🇷🇺 Матвей Сафонов", "🇲🇦 Ашраф Хакими", "🇵🇹 Нуно Мендес",
        "🇪🇸 Фабиан Руис", "🇫🇷 Дезире Дуэ",
        "🇦🇷 Лаутаро Мартинес", "🇮🇹 Федерико Димарко", "🇮🇹 Николо Барелла",
        "🇮🇹 Алессандро Бастони", "🇹🇷 Хакан Чалханоглу", "🇭🇷 Лука Модрич",
        "🇺🇸 Кристиан Пулишич", "🇵🇹 Рафаэл Леау", "🇹🇷 Кенан Йылдыз",
        "🇫🇷 Маркус Тюрам", "🇫🇷 Тео Эрнандес", "🇧🇷 Бремер",
        "🇦🇷 Нико Пас", "🇮🇹 Мануэль Локателли", "🇷🇸 Душан Влахович",
        "🇳🇱 Коди Гакпо", "🇳🇱 Вирджил ван Дейк", "🇫🇷 Ибраима Конате",
        "🇧🇷 Алиссон Бекер", "🇦🇷 Алексис Мак Аллистер", "🇳🇱 Райан Гравенберх",
        "🇭🇷 Йошко Гвардиол", "🇳🇴 Эрлинг Холанд", "🇳🇱 Натан Аке",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Фил Фоден", "🇪🇸 Родри", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джон Стоунз",
        "🇵🇹 Бернарду Силва",
        "🇦🇷 Энцо Фернандес", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Коул Палмер", "🇸🇳 Николя Джексон",
        "🇳🇱 Нони Мадуэке", "🇫🇷 Уэсли Фофана", "🇪🇸 Марк Кукурелья",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джейдон Санчо", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Рис Джеймс", "🇵🇹 Педру Нету",
        "🇵🇹 Бруну Фернандеш", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Гарри Магуайр", "🇧🇷 Каземиро",
        "🇳🇱 Джошуа Зиркзе",
        "🇸🇪 Деян Кулусевски", "🇦🇷 Кристиан Ромеро", "🇧🇷 Ришарлисон",
        "🇺🇾 Родриго Бентанкур", "🇧🇷 Жоэлинтон"
    ],

    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 АПЛ (звёзды 2020-2025)": [
        "🇪🇬 Мохаммед Салах", "🇳🇱 Вирджил ван Дейк", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Трент Александер-Арнольд",
        "🇧🇷 Алиссон Бекер", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джордан Хендерсон", "🇸🇳 Садио Мане",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Эндрю Робертсон", "🇦🇷 Алексис Мак Аллистер", "🇳🇱 Райан Гравенберх",
        "🇳🇱 Коди Гакпо", "🇭🇺 Доминик Собослаи", "🇫🇷 Ибраима Конате",
        "🇵🇹 Диогу Жота",
        "🇳🇴 Эрлинг Холанд", "🇧🇪 Кевин Де Брёйне", "🇵🇹 Бернарду Силва",
        "🇪🇸 Родри", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Фил Фоден", "🇦🇷 Хулиан Альварес",
        "🇵🇹 Рубен Диаш", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джон Стоунз", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Кайл Уокер",
        "🇧🇷 Эдерсон", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Коул Палмер", "🇩🇪 Илкай Гюндоган",
        "🇭🇷 Йошко Гвардиол", "🇳🇱 Натан Аке", "🇧🇪 Жереми Доку",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Букайо Сака", "🇳🇴 Мартин Эдегор", "🇧🇷 Габриэль Мартинелли",
        "🇫🇷 Вильям Салиба", "🇧🇷 Габриэль Магальяйнс", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Деклан Райс",
        "🇩🇪 Кай Хаверц", "🇧🇪 Леандро Троссард", "🇪🇸 Давид Райя",
        "🇮🇹 Жоржиньо",
        "🇵🇹 Бруну Фернандеш", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Маркус Рэшфорд", "🇧🇷 Каземиро",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Гарри Магуайр", "🇦🇷 Лисандро Мартинес", "🇦🇷 Алехандро Гарначо",
        "🇨🇲 Андре Онана",
        "🇸🇳 Николя Джексон", "🇪🇸 Марк Кукурелья", "🇳🇱 Нони Мадуэке",
        "🇫🇷 Уэсли Фофана", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Рис Джеймс", "🇦🇷 Энцо Фернандес",
        "🇵🇹 Педру Нету", "🇫🇷 Кристофер Нкунку", "🇧🇷 Тьяго Силва",
        "🇰🇷 Сон Хын Мин", "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Гарри Кейн", "🇸🇪 Деян Кулусевски",
        "🇦🇷 Кристиан Ромеро", "🇧🇷 Ришарлисон", "🇺🇾 Родриго Бентанкур",
        "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Джеймс Мэддисон", "🇮🇹 Гульельмо Викарио", "🇧🇷 Бруно Гимарайнш",
        "🇸🇪 Александер Исак", "🇦🇷 Эмилиано Мартинес", "🇧🇷 Жоэлинтон"
    ]
}

# Создаём ALL
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

game = Game()

def get_status():
    if not game.host:
        return "⏳ Ожидание: /newgame или /offline"
    if game.offline_mode:
        if not game.active:
            return "⏳ Ожидание: /offline ЧИСЛО"
        else:
            return "🎮 Офлайн-игра идёт! Жмите кнопки."
    if not game.category:
        return "📂 Шаг 1: Выберите категорию кнопкой выше"
    if not game.active:
        return f"👥 Шаг 2: Игроки заходят /join\n📂 Категория: {game.category}\n👥 Игроков: {len(game.players)}/50"
    if game.active and not game.votes:
        return f"💬 Шаг 3: Обсуждение!\n👥 Игроков: {len(game.players)}\nВедущий: /vote когда готовы"
    if game.votes:
        return f"🗳 Шаг 4: Голосование!\nПроголосовало: {len(game.votes)}/{len(game.players)}"
    return "✅ Игра завершена"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status = get_status()
    await update.message.reply_text(
        "⚽🕵️ *ФУТБОЛЬНЫЙ ШПИОН* 🕵️⚽\n\n"
        f"📋 *Статус:* {status}\n\n"
        "🎮 *РЕЖИМЫ:*\n\n"
        "📱 *ОНЛАЙН (в группе):*\n"
        "/newgame — создать игру\n"
        "/join — войти в игру\n"
        "/players — список игроков\n"
        "/deal — раздать роли\n"
        "/vote — начать голосование\n"
        "/status — что сейчас делать\n\n"
        "🏠 *ОФЛАЙН (в ЛС бота):*\n"
        "/offline 6 — игра на 6 человек\n\n"
        "/rules — правила\n"
        "/end — закончить игру",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📋 *СТАТУС ИГРЫ:*\n{get_status()}", parse_mode="Markdown")

async def newgame(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if game.active:
        await update.message.reply_text("⚠️ Идёт игра! /end чтобы закончить")
        return
    game.__init__()
    game.host = update.effective_user.id
    game.players[update.effective_user.id] = update.effective_user.first_name
    game.offline_mode = False
    keyboard = []
    for cat_name in CATEGORIES:
        keyboard.append([InlineKeyboardButton(cat_name, callback_data=f"cat_{cat_name}")])
    await update.message.reply_text(
        f"⚽ *НОВАЯ ИГРА!*\n\n"
        f"👑 Ведущий: *{update.effective_user.first_name}*\n\n"
        f"📂 *ШАГ 1: Выбери категорию:*",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not game.host:
        await update.message.reply_text("⚠️ Сначала /newgame")
        return
    if game.offline_mode:
        await update.message.reply_text("⚠️ Это офлайн-игра!")
        return
    if game.active:
        await update.message.reply_text("⚠️ Игра уже идёт!")
        return
    if game.category is None:
        await update.message.reply_text("⚠️ Сначала ведущий должен выбрать категорию!")
        return
    if len(game.players) >= 50:
        await update.message.reply_text("❌ Максимум 50 игроков!")
        return
    uid = update.effective_user.id
    if uid in game.players:
        await update.message.reply_text("⚠️ Ты уже в игре!")
        return
    game.players[uid] = update.effective_user.first_name
    await update.message.reply_text(
        f"✅ *{update.effective_user.first_name}* в игре!\n"
        f"👥 Игроков: *{len(game.players)}/50*\n\n"
        f"📋 Когда все соберутся — ведущий пишет /deal",
        parse_mode="Markdown"
    )

async def players_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not game.players:
        await update.message.reply_text("👥 Нет игроков.")
        return
    mode = "🏠 ОФЛАЙН" if game.offline_mode else "📱 ОНЛАЙН"
    cat = f"\n📂 Категория: {game.category}" if game.category else ""
    msg = f"👥 *ИГРОКИ ({len(game.players)}/50)* | {mode}{cat}\n\n"
    for uid, name in game.players.items():
        crown = "👑" if uid == game.host else "⚽"
        msg += f"{crown} {name}\n"
    msg += f"\n📋 *Что дальше:* {get_status()}"
    await update.message.reply_text(msg, parse_mode="Markdown")

async def deal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if game.offline_mode:
        await update.message.reply_text("⚠️ В офлайне роли уже готовы! Жмите кнопки.")
        return
    if update.effective_user.id != game.host:
        await update.message.reply_text("⚠️ Только ведущий раздаёт роли!")
        return
    if game.category is None:
        await update.message.reply_text("⚠️ Сначала выбери категорию!")
        return
    if len(game.players) < 3:
        await update.message.reply_text(f"❌ Минимум 3 игрока! Сейчас: {len(game.players)}")
        return
    players_list_cat = CATEGORIES.get(game.category, [])
    if not players_list_cat:
        await update.message.reply_text("⚠️ Категория пустая!")
        return
    game.active = True
    game.footballer = random.choice(players_list_cat)
    game.spy = random.choice(list(game.players.keys()))
    game.roles = {}
    game.votes = {}
    for uid in game.players:
        game.roles[uid] = "spy" if uid == game.spy else "civilian"
    keyboard = [[InlineKeyboardButton("🔍 ПОСМОТРЕТЬ РОЛЬ", callback_data="show_role")]]
    await update.message.reply_text(
        f"✅ *РОЛИ РАЗДАНЫ!*\n\n"
        f"👥 Игроков: *{len(game.players)}*\n"
        f"📂 Категория: *{game.category}*\n\n"
        f"📋 *ШАГ 3: Обсуждение*\n"
        f"1️⃣ Каждый жмёт «Посмотреть роль»\n"
        f"2️⃣ Обсуждайте без ограничений\n"
        f"3️⃣ Ведущий: /vote\n\n"
        f"🕵️ Среди вас шпион!",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def offline(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if game.active:
        await update.message.reply_text("⚠️ Игра уже идёт! /end")
        return
    args = context.args
    if not args:
        game.__init__()
        game.offline_mode = True
        game.host = update.effective_user.id
        keyboard = []
        for cat_name in CATEGORIES:
            keyboard.append([InlineKeyboardButton(cat_name, callback_data=f"offcat_{cat_name}")])
        await update.message.reply_text(
            "🏠 *ОФЛАЙН-РЕЖИМ*\n\n"
            "1️⃣ Выбери категорию (кнопки ниже)\n"
            "2️⃣ Потом напиши: /offline ЧИСЛО\n"
            "Например: /offline 8\n\n"
            "📂 *Категории:*",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )
        return
    try:
        num = int(args[0])
    except:
        await update.message.reply_text("✏️ Пиши: /offline ЧИСЛО\nПример: /offline 8")
        return
    if num < 3:
        await update.message.reply_text("❌ Минимум 3 игрока!")
        return
    if num > 50:
        await update.message.reply_text("❌ Максимум 50 игроков!")
        return
    if not game.category:
        game.category = "🌍 ALL (все)"
    game.offline_mode = True
    game.active = True
    game.host = update.effective_user.id
    players_list_cat = CATEGORIES.get(game.category, ALL_FOOTBALLERS)
    if not players_list_cat:
        await update.message.reply_text(f"⚠️ Категория '{game.category}' пустая!")
        return
    game.footballer = random.choice(players_list_cat)
    for i in range(1, num + 1):
        game.players[i] = f"Игрок {i}"
    game.spy = random.choice(list(game.players.keys()))
    game.roles = {}
    for uid in game.players:
        game.roles[uid] = "spy" if uid == game.spy else "civilian"
    keyboard = []
    for uid in game.players:
        keyboard.append([InlineKeyboardButton(
            f"🎭 Игрок {uid} — ПОСМОТРЕТЬ РОЛЬ",
            callback_data=f"offline_{uid}"
        )])
    await update.message.reply_text(
        f"🏠 *ОФЛАЙН-РЕЖИМ*\n\n"
        f"👥 Игроков: *{num}*\n"
        f"📂 Категория: *{game.category}*\n\n"
        f"📱 Передавайте телефон по кругу!\n\n"
        f"Каждый нажимает на свой номер.\n"
        f"Роль появится в чате на 5 сек и исчезнет.\n\n"
        f"⚠️ Не подглядывайте!\n\n"
        f"/end — закончить.",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    data = q.data
    uid = q.from_user.id

    if data.startswith("cat_"):
        cat_name = data[4:]
        if cat_name in CATEGORIES:
            game.category = cat_name
            await q.edit_message_text(
                f"✅ *Категория выбрана:* {cat_name}\n\n"
                f"👥 Игроков: *{len(game.players)}/50*\n\n"
                f"📋 *ШАГ 2:* Игроки пишут /join\n"
                f"Когда все готовы — /deal",
                parse_mode="Markdown"
            )

    elif data.startswith("offcat_"):
        cat_name = data[7:]
        if cat_name in CATEGORIES:
            game.category = cat_name
            await q.edit_message_text(
                f"✅ *Категория выбрана:* {cat_name}\n\n"
                f"Теперь введи: /offline ЧИСЛО\n"
                f"Например: /offline 6",
                parse_mode="Markdown"
            )

    elif data == "show_role":
        if uid not in game.roles:
            await q.answer("⚠️ Ты не в игре!", show_alert=True)
            return
        if game.roles[uid] == "spy":
            text = (
                f"🕵️ *Ты — ШПИОН!*\n\n"
                f"Все знают футболиста, а ты — нет.\n"
                f"Задавай вопросы, вычисляй!\n\n"
                f"⚽ *Список футболистов ({game.category}):*\n"
                + "\n".join(CATEGORIES.get(game.category, []))
            )
        else:
            text = f"⚽ *Ты — МИРНЫЙ!*\n\n🔥 Загадан: *{game.footballer}*"
        try:
            await context.bot.send_message(uid, text, parse_mode="Markdown")
            await q.answer("✅ Роль отправлена в ЛС!", show_alert=True)
        except:
            await q.answer("❌ Сначала напиши боту в ЛС /start!", show_alert=True)

    elif data.startswith("offline_"):
        player_num = int(data.split("_")[1])
        if player_num not in game.roles:
            await q.answer("⚠️ Ошибка! Начни заново", show_alert=True)
            return
        if game.roles[player_num] == "spy":
            text = f"🕵️ *Игрок {player_num} — ШПИОН!*\n\nВсе знают футболиста, а ты — нет. Вычисляй!"
        else:
            text = f"⚽ *Игрок {player_num} — МИРНЫЙ!*\n\n🔥 Загадан: *{game.footballer}*"
        role_msg = await context.bot.send_message(q.message.chat.id, text, parse_mode="Markdown")
        await asyncio.sleep(5)
        try:
            await role_msg.delete()
        except:
            pass
        keyboard = q.message.reply_markup
        new_keyboard = []
        for row in keyboard.inline_keyboard:
            new_row = []
            for btn in row:
                if btn.callback_data == data:
                    new_row.append(InlineKeyboardButton("✅ Просмотрено", callback_data="viewed"))
                else:
                    new_row.append(btn)
            new_keyboard.append(new_row)
        await q.edit_message_reply_markup(InlineKeyboardMarkup(new_keyboard))
        await q.answer("✅ Роль показана! Исчезнет через 5 сек.", show_alert=True)

    elif data.startswith("vote_"):
        if uid not in game.players:
            await q.answer("⚠️ Ты не в игре!", show_alert=True)
            return
        if uid in game.votes:
            await q.answer("⚠️ Ты уже голосовал!", show_alert=True)
            return
        target = int(data.split("_")[1])
        game.votes[uid] = target
        await q.answer(f"✅ Ты проголосовал! ({len(game.votes)}/{len(game.players)})", show_alert=True)
        keyboard = q.message.reply_markup
        await q.edit_message_text(
            f"🗳 *ГОЛОСОВАНИЕ*\n\n"
            f"Проголосовало: *{len(game.votes)}/{len(game.players)}*\n\n"
            f"Остальные тоже жмите на имя!",
            parse_mode="Markdown",
            reply_markup=keyboard
        )
        if len(game.votes) == len(game.players):
            await calculate_results(context, q.message.chat.id)

async def vote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if game.offline_mode:
        await update.message.reply_text("⚠️ В офлайне голосуйте вживую!")
        return
    if not game.active:
        await update.message.reply_text("⚠️ Игра не активна!")
        return
    if update.effective_user.id != game.host:
        await update.message.reply_text("⚠️ Только ведущий!")
        return
    game.votes = {}
    keyboard = []
    for uid, name in game.players.items():
        keyboard.append([InlineKeyboardButton(f"🕵️ {name}", callback_data=f"vote_{uid}")])
    await update.message.reply_text(
        f"🗳 *ГОЛОСОВАНИЕ!*\n\n"
        f"Все *{len(game.players)}* игроков должны нажать на имя!\n"
        f"Проголосовало: *0/{len(game.players)}*",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def calculate_results(context, chat_id):
    vote_count = {}
    for t in game.votes.values():
        vote_count[t] = vote_count.get(t, 0) + 1
    most = max(vote_count, key=vote_count.get)
    caught = (most == game.spy)
    msg = "📊 *ИТОГИ ГОЛОСОВАНИЯ:*\n\n"
    for uid, name in game.players.items():
        em = "🕵️" if uid == game.spy else "⚽"
        msg += f"{em} {name}: {vote_count.get(uid, 0)} голосов\n"
    msg += f"\n⚽ Загадан: *{game.footballer}*\n"
    if caught:
        msg += (
            f"\n✅ *Шпион пойман!* — {game.players[game.spy]}\n"
            f"🕵️ Шпион, последний шанс: /guess Имя"
        )
    else:
        msg += f"\n🕵️ *Шпион победил!* — {game.players[game.spy]}"
    await context.bot.send_message(chat_id, msg, parse_mode="Markdown")
    game.active = False

async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != game.spy:
        await update.message.reply_text("⚠️ Ты не шпион!")
        return
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("✏️ Напиши: /guess Имя Футболиста")
        return
    if text.lower() == game.footballer.lower():
        await update.message.reply_text(f"🎉 *Верно!* {game.footballer}\nШпион спасся!", parse_mode="Markdown")
    else:
        await update.message.reply_text(f"❌ *Неверно.* Было: {game.footballer}\nПобеда мирных!", parse_mode="Markdown")

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚽ *ПРАВИЛА ФУТБОЛЬНОГО ШПИОНА:*\n\n"
        "📱 *ОНЛАЙН (в группе):*\n"
        "1. /newgame — создать\n"
        "2. Выбрать категорию\n"
        "3. /join — всем зайти\n"
        "4. /deal — раздать роли\n"
        "5. Жать «Посмотреть роль»\n"
        "6. Обсуждение\n"
        "7. /vote — голосование\n"
        "8. /guess — шпион угадывает\n\n"
        "🏠 *ОФЛАЙН (в ЛС бота):*\n"
        "Сначала выбери категорию: /offline\n"
        "Потом: /offline ЧИСЛО\n\n"
        "/status — что сейчас делать",
        parse_mode="Markdown"
    )

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if game.active and game.footballer:
        await update.message.reply_text(f"🛑 Игра завершена!\n⚽ Загадан: *{game.footballer}*", parse_mode="Markdown")
    else:
        await update.message.reply_text("🛑 Игра завершена!")
    game.__init__()

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("newgame", newgame))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("players", players_list))
    app.add_handler(CommandHandler("deal", deal))
    app.add_handler(CommandHandler("offline", offline))
    app.add_handler(CommandHandler("vote", vote))
    app.add_handler(CommandHandler("guess", guess))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(CommandHandler("end", end))
    app.add_handler(CallbackQueryHandler(button))
    print("⚽ Футбольный Шпион запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()