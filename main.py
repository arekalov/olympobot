import telebot
from telebot import types

from config import token
import data

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])  # Обработчик функции /start
def start_f(message):
    bot.send_message(message.chat.id, data.about_bot)
    menu_func(message)


@bot.message_handler(commands=['menu'])  # Обработчик функции /menu
def menu_func(message):
    kb = telebot.types.InlineKeyboardMarkup(row_width=1)
    a = telebot.types.InlineKeyboardButton(text="Перечневые олимпиады", callback_data="perech")
    b = telebot.types.InlineKeyboardButton(text="ВСОШ", callback_data="vsosh")
    c = telebot.types.InlineKeyboardButton(text="О Olympobot", callback_data="about")
    z = telebot.types.InlineKeyboardButton(text="Полезные материалы", callback_data="materials")
    kb.add(a, b, c, z)
    bot.send_message(message.chat.id, "Выберите действие", reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)  # Обработчик коллбэков от функции menu_func
def callback_func(callback):
    if callback.data == "perech":
        kb = telebot.types.InlineKeyboardMarkup(row_width=2)
        a = telebot.types.InlineKeyboardButton(text='Высшая проба', callback_data="veshka")
        b = telebot.types.InlineKeyboardButton(text="Ломоносов", callback_data="lomonosov")
        c = telebot.types.InlineKeyboardButton(text="Покори Воробьевы горы", callback_data="vorov")
        d = telebot.types.InlineKeyboardButton(text="СПБГУ", callback_data="spbgu")
        e = telebot.types.InlineKeyboardButton(text="РАНХИГС", callback_data="ranh")
        f = telebot.types.InlineKeyboardButton(text="Плехановская", callback_data="plehan")
        g = telebot.types.InlineKeyboardButton(text="Евразийская", callback_data="evra")
        h = telebot.types.InlineKeyboardButton(text="КФУ", callback_data="kfu")
        i = telebot.types.InlineKeyboardButton(text="РГГУ", callback_data="rggu")
        j = telebot.types.InlineKeyboardButton(text="Ведомственная", callback_data="vedom")
        k = telebot.types.InlineKeyboardButton(text="Челябинская", callback_data="chell")
        m = telebot.types.InlineKeyboardButton(text="Учитель школы будущего", callback_data="uchit")
        n = telebot.types.InlineKeyboardButton(text="Герценовская", callback_data="gercen")
        o = telebot.types.InlineKeyboardButton(text="Формула единства", callback_data="formula")
        kb.add(a, b, c, d, e, f, g, h, i, j, k, m, n, o)
        bot.send_message(callback.from_user.id, 'Выбери олимпиаду', reply_markup=kb)
    elif callback.data == "materials":
        bot.send_message(callback.from_user.id, 'https://www.youtube.com/watch?v=Mfl1vnCtDgY')
        bot.send_message(callback.from_user.id, 'https://vk.com/olymp_english')
        bot.send_message(callback.from_user.id, 'https://vk.com/olymp_eng')
        bot.send_message(callback.from_user.id, 'https://vk.com/climbolympus')

    elif callback.data == "vsosh":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_vsosh")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_vsosh)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_vsosh, reply_markup=kb)
    elif callback.data == "about":
        bot.send_message(callback.from_user.id, data.about_bot)
    elif callback.data == "veshka":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_veshka")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_veshka)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_veshka, reply_markup=kb)
    elif callback.data == "lomonosov":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_lomonosov")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_lomonosov)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_lomonosov, reply_markup=kb)
    elif callback.data == "vorov":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_vorov")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_vorov)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_vorov, reply_markup=kb)
    elif callback.data == "spbgu":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_spbgu")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_spbgu)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_spbgu, reply_markup=kb)
    elif callback.data == "ranh":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_ranh")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_ranh)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_ranh, reply_markup=kb)
    elif callback.data == "plehan":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_plehan")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_plehan)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_plehan, reply_markup=kb)
    elif callback.data == "evra":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_evra")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_evra)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_evra, reply_markup=kb)
    elif callback.data == "kfu":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_kfu")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_kfu)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_kfu, reply_markup=kb)
    elif callback.data == "rggu":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_rggu")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_rggu)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_rggu, reply_markup=kb)
    elif callback.data == "vedom":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_vedom")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_vedom)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_vedom, reply_markup=kb)
    elif callback.data == "chell":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_chell")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_chell)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_chell, reply_markup=kb)
    elif callback.data == "uchit":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_uchit")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_uchit)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_uchit, reply_markup=kb)
    elif callback.data == "formula":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_formula")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_formula)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_formula, reply_markup=kb)
    elif callback.data == "gercen":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_gercen")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_gercen)
        kb.add(b, c)
        bot.send_message(callback.from_user.id, data.about_gercen, reply_markup=kb)
    elif callback.data == "exercises_vsosh":
        bot.send_message(callback.from_user.id, 'Подождите немного')
        file = open('exerсise/exercise_vsosh.rar', 'rb')
        bot.send_document(callback.from_user.id, file)

    elif callback.data == "exercises_veshka":
        file = open('exerсise/exercise_veshka.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_lomonosov":
        file = open('exerсise/exercise_lomonosov.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_vorov":
        file = open('exerсise/exercise_vorov.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_spbgu":
        file = open('exerсise/exercise_spbgu.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_ranh":
        file = open('exerсise/exercise_ranh.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_plehan":
        file = open('exerсise/exercise_plehan.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_evra":
        file = open('exerсise/exercise_evra.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_kfu":
        file = open('exerсise/exercise_kfu.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_rggu":
        file = open('exerсise/exercise_rggu.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_vedom":
        file = open('exerсise/exercise_vedom.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_chell":
        file = open('exerсise/exercise_chell.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_uchit":
        file = open('exerсise/exercise_uchit.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_formula":
        file = open('exerсise/exercise_formula.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()
    elif callback.data == "exercises_gercen":
        file = open('exerсise/exercise_gercen.rar', 'rb')
        bot.send_document(callback.from_user.id, file)
        file.close()


@bot.message_handler(content_types=["photo", "sticker", "document", "text"])  # Обработчик мусора
def trash_func(message):
    bot.send_message(message.chat.id, 'Простите, не понимаю вас')


bot.polling(none_stop=True, interval=0)
