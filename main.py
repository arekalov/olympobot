import os

import telebot
from telebot import types

import config
from config import token
import data
from orm_data import db_session
from orm_data.review import Review

bot = telebot.TeleBot(token)
db_session.global_init("db/database.db")


@bot.message_handler(commands=['start'])  # Обработчик функции /start
def start_f(message):
    db_sess = db_session.create_session()
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    nickname = message.from_user.username
    if user_id in config.admins:
        is_admin = 1
    else:
        is_admin = 0

    if not db_sess.query(Review).filter(Review.user_id == user_id).first():
        print(user_id, first_name, last_name, nickname)
        rev = Review(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            is_admin=is_admin,
            mark=None

        )
        db_sess.add(rev)
        db_sess.commit()
        db_sess.close()
    bot.send_message(message.chat.id, data.about_bot)
    menu_func(message)


@bot.message_handler(commands=['menu'])  # Обработчик функции /menu
def menu_func(message, is_callback=False):
    kb = telebot.types.InlineKeyboardMarkup(row_width=2)
    a = telebot.types.InlineKeyboardButton(text="Перечневые олимпиады", callback_data="perech")
    b = telebot.types.InlineKeyboardButton(text="ВСОШ", callback_data="vsosh")
    c = telebot.types.InlineKeyboardButton(text="О Olympobot", callback_data="about")
    z = telebot.types.InlineKeyboardButton(text="Полезные материалы", callback_data="materials")
    d = telebot.types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review")
    kb.add(a, b, c, z, d)
    if not is_callback:
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=kb)
    else:
        bot.send_message(message, "Выберите действие", reply_markup=kb)


@bot.message_handler(commands=['review'])
def rewiews_f(message, is_callback=False):
    db_sess = db_session.create_session()
    summ = 0
    count = 0
    for i in db_sess.query(Review):
        if i.mark:
            summ += i.mark
            count += 1
    db_sess.close()
    kb = telebot.types.InlineKeyboardMarkup(row_width=1)
    a = telebot.types.InlineKeyboardButton(text="5", callback_data="mark_5")
    b = telebot.types.InlineKeyboardButton(text="4", callback_data="mark_4")
    c = telebot.types.InlineKeyboardButton(text="3", callback_data="mark_3")
    d = telebot.types.InlineKeyboardButton(text="2", callback_data="mark_2")
    e = telebot.types.InlineKeyboardButton(text="1", callback_data="mark_1")
    g = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
    kb.add(a, b, c, d, e, g)
    if not is_callback:
        bot.send_message(message.chat.id, f"На данный момент рейтинг {round(summ / count, 2)}")
        bot.send_message(message.chat.id, "Пожалуйста, оцените нашего бота", reply_markup=kb)
    else:
        bot.send_message(message, f"На данный момент рейтинг {round(summ / count, 2)}")
        bot.send_message(message, "Пожалуйста, оцените нашего бота", reply_markup=kb)


@bot.message_handler(commands=['admin'])
def admin_f(message):
    db_sess = db_session.create_session()
    user_id = message.from_user.id
    if db_sess.query(Review).filter(Review.user_id == user_id).first().is_admin == 1:
        kb = telebot.types.InlineKeyboardMarkup()
        b = telebot.types.InlineKeyboardButton(text="Пользователи и статистика", callback_data="stats")
        c = types.InlineKeyboardButton(text="В меню", callback_data='menu')
        kb.add(b, c)
        bot.send_message(message.chat.id, 'Здравствуй, покровитель, чего желаешь?', reply_markup=kb)
    else:
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        c = types.InlineKeyboardButton(text="В меню", callback_data='menu')
        kb.add(c)
        bot.send_message(message.chat.id, 'У вас нет прав администратора!', reply_markup=kb)


@bot.message_handler(commands=['help'])
def help_f(message):
    kb = telebot.types.InlineKeyboardMarkup()
    c = types.InlineKeyboardButton(text="В меню", callback_data='menu')
    kb.add(c)
    bot.send_message(message.chat.id, data.about_bot, reply_markup=kb)

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
        p = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(a, b, c, d, e, f, g, h, i, j, k, m, n, o, p)
        bot.send_message(callback.from_user.id, 'Выбери олимпиаду', reply_markup=kb)
    elif callback.data == "materials":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        a = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(a)
        bot.send_message(callback.from_user.id, 'https://www.youtube.com/watch?v=Mfl1vnCtDgY')
        bot.send_message(callback.from_user.id, 'https://vk.com/olymp_english')
        bot.send_message(callback.from_user.id, 'https://vk.com/olymp_eng')
        bot.send_message(callback.from_user.id, 'https://vk.com/climbolympus', reply_markup=kb)
    elif callback.data == "vsosh":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_vsosh")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_vsosh)
        d = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_vsosh, reply_markup=kb)
    elif callback.data == "veshka":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_veshka")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_veshka)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_veshka, reply_markup=kb)
    elif callback.data == "lomonosov":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_lomonosov")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_lomonosov)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_lomonosov, reply_markup=kb)
    elif callback.data == "vorov":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_vorov")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_vorov)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_vorov, reply_markup=kb)
    elif callback.data == "spbgu":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_spbgu")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_spbgu)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_spbgu, reply_markup=kb)
    elif callback.data == "ranh":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_ranh")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_ranh)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_ranh, reply_markup=kb)
    elif callback.data == "plehan":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_plehan")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_plehan)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_plehan, reply_markup=kb)
    elif callback.data == "evra":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_evra")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_evra)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_evra, reply_markup=kb)
    elif callback.data == "kfu":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_kfu")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_kfu)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_kfu, reply_markup=kb)
    elif callback.data == "rggu":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_rggu")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_rggu)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_rggu, reply_markup=kb)
    elif callback.data == "vedom":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_vedom")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_vedom)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_vedom, reply_markup=kb)
    elif callback.data == "chell":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_chell")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_chell)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_chell, reply_markup=kb)
    elif callback.data == "uchit":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_uchit")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_uchit)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_uchit, reply_markup=kb)
    elif callback.data == "formula":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_formula")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_formula)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
        bot.send_message(callback.from_user.id, data.about_formula, reply_markup=kb)
    elif callback.data == "gercen":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="Задания", callback_data="exercises_gercen")
        c = types.InlineKeyboardButton(text="Сайт олимпиады", url=data.site_gercen)
        d = telebot.types.InlineKeyboardButton(text="К списку олимпиад", callback_data="perech")
        kb.add(b, c, d)
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

    elif callback.data == "mark_5":
        user_id = callback.from_user.id
        db_sess = db_session.create_session()
        obj = db_sess.query(Review).filter(Review.user_id == user_id).first()
        if obj.mark:
            if obj.mark == 5:
                text = f'Вы уже оценили бота на {obj.mark}'
            else:
                text = f'Ваша оценка изменена с {obj.mark} на 5 , спасибо!'
        else:
            text = 'Спасибо за высокую оценку, ваш голос учтен!'
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(b)
        obj.mark = 5
        db_sess.commit()
        db_sess.close()
        bot.send_message(callback.from_user.id, text, reply_markup=kb)
    elif callback.data == "mark_4":
        user_id = callback.from_user.id
        db_sess = db_session.create_session()
        obj = db_sess.query(Review).filter(Review.user_id == user_id).first()
        if obj.mark:
            if obj.mark == 4:
                text = f'Вы уже оценили бота на {obj.mark}'
            else:
                text = f'Ваша оценка изменена с {obj.mark} на 4 , спасибо!'
        else:
            text = 'Спасибо за хорошую оценку, мы работаем над удучшением функционала бота,ваш голос учтен!'
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(b)
        obj.mark = 4
        db_sess.commit()
        db_sess.close()
        bot.send_message(callback.from_user.id, text, reply_markup=kb)
    elif callback.data == "mark_3":
        user_id = callback.from_user.id
        db_sess = db_session.create_session()
        obj = db_sess.query(Review).filter(Review.user_id == user_id).first()
        if obj.mark:
            if obj.mark == 3:
                text = f'Вы уже оценили бота на {obj.mark}'
            else:
                text = f'Ваша оценка изменена с {obj.mark} на 3 , спасибо!'
        else:
            text = 'Спасибо за оценку, мы работаем над удучшением функционала бота, ваш голос учтен!'
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(b)
        obj.mark = 3
        db_sess.commit()
        db_sess.close()
        bot.send_message(callback.from_user.id, text, reply_markup=kb)
    elif callback.data == "mark_2":
        user_id = callback.from_user.id
        db_sess = db_session.create_session()
        obj = db_sess.query(Review).filter(Review.user_id == user_id).first()
        if obj.mark:
            if obj.mark == 2:
                text = f'Вы уже оценили бота на {obj.mark}'
            else:
                text = f'Ваша оценка изменена с {obj.mark} на 2 , спасибо!'
        else:
            text = 'Спасибо за оценку, мы работаем над удучшением функционала бота, ваш голос учтен!'
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(b)
        obj.mark = 2
        db_sess.commit()
        db_sess.close()
        bot.send_message(callback.from_user.id, text, reply_markup=kb)
    elif callback.data == "mark_1":
        user_id = callback.from_user.id
        db_sess = db_session.create_session()
        obj = db_sess.query(Review).filter(Review.user_id == user_id).first()
        if obj.mark:
            if obj.mark == 1:
                text = f'Вы уже оценили бота на {obj.mark}'
            else:
                text = f'Ваша оценка изменена с {obj.mark} на 1 , спасибо!'
        else:
            text = 'Спасибо за оценку, мы работаем над удучшением функционала бота, ваш голос учтен!'
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(b)
        obj.mark = 1
        db_sess.commit()
        db_sess.close()
        bot.send_message(callback.from_user.id, text, reply_markup=kb)

    elif callback.data == "review":
        rewiews_f(callback.from_user.id, True)
    elif callback.data == "menu":
        menu_func(callback.from_user.id, True)
    elif callback.data == "about":
        kb = telebot.types.InlineKeyboardMarkup(row_width=1)
        b = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(b)
        bot.send_message(callback.from_user.id, data.about_bot, reply_markup=kb)

    elif callback.data == 'stats':
        db_sess = db_session.create_session()
        summ = 0
        count = 0
        for i in db_sess.query(Review):
            if i.mark:
                summ += i.mark
                count += 1
        kb = telebot.types.InlineKeyboardMarkup()
        a = telebot.types.InlineKeyboardButton(text="Тек"
                                                    "стовый", callback_data="text_stats")
        b = telebot.types.InlineKeyboardButton(text="БД", callback_data="bd_stats")
        c = telebot.types.InlineKeyboardButton(text="В меню", callback_data="menu")
        kb.add(a, b, c)
        bot.send_message(callback.from_user.id,
                         f"На данный момент рейтинг {round(summ / count, 2)}, проголосовало {count} человек",
                         reply_markup=kb)
        db_sess.close()

    elif callback.data == 'text_stats':
        db_sess = db_session.create_session()
        with open('db.txt', 'w') as file:
            file.write(f'id user_id first_name last_name nickname is_admin mark\n')
            summ = 0
            count = 0
            for i in db_sess.query(Review):
                file.write(f'{i.id} {i.user_id} {i.first_name} {i.last_name} {i.nickname} {i.is_admin} {i.mark}\n')
                if i.mark:
                    count += 1
                    summ += i.mark
            file.write(f'Mean mark {round(summ / count, 3)}')
        with open('db.txt') as to_send:
            bot.send_document(callback.from_user.id, to_send)
        os.remove('db.txt')


    elif callback.data == 'bd_stats':
        with open('db//database.db') as file:
            bot.send_document(callback.from_user.id, file)


@bot.message_handler(content_types=["photo", "sticker", "document", "text"])  # Обработчик мусора
def trash_func(message):
    bot.send_message(message.chat.id, 'Простите, не понимаю вас')


bot.polling(none_stop=True, interval=0)
