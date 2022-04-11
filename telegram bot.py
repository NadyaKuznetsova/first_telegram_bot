from telebot import TeleBot
from telebot import types

import random

API_TOKEN = '5108766299:AAGlVJkc644VEe3Wk41x_RGlt-SwfPaPfVY'
bot = TeleBot(API_TOKEN)
otvet_session = []
img = open('decorator.PNG', 'rb')

questions_Data = [
    'В чём разница между списком и кортежем?',
    'Пример декоратора',
    'Почему мы должны взять именно Вас?',
    'Почему Вы хотите работать у нас?',
    'Как Вы справляетесь с конфликтными ситуациями?',
    'Как Вы развиваете себя как специалиста?',
    'Какие сложные задачи встречались Вам в работе?',
    'Какой Ваш идеальный работодатель?',
    'Есть ли у Вас дети?',
    'Как Вы относитесь к работе в сверхурочное время?',
    'Почему Вы выбрали данную специальность?',
    'Какие Ваши карьерные цели?']

otvet_Data = [
    ('Разница между списком и кортежем заключается в том,'
     ' что список объявляется в квадратных скобках и может быть изменен,'
     ' в то время как кортеж объявляется в круглых скобках и не может быть изменен.'
     ' Однако вы можете взять части существующих кортежей для создания новых кортежей.'
     ),
    (img),
    ('Что же можно и нужно говорить: что у Вас есть опыт работы в определенной сфере или в определенных условиях,'
     ' что позволит Вам справиться со своими обязанностями на новом месте;'
     ' что на прошлых местах работы Вы добились конкретных результатов и можете такую же пользу принести и здесь;'
     ' что Вы в полной мере обладаете теми навыками,'
     ' которые требуются для работы в компании (тут нужно будет привести примеры навыков и тех задач, которые они позволят решить).'
     ),
    ('Какой же может быть причина: возможности профессионального роста; репутация компании,'
     ' отзывы о ней; ее ценности; ее стремительный рост на рынке;'
     ' ее долгая и стабильная история;'
     ' интересные для Вас проекты; возможности обучиться чему-то новому.'
     ),
    ('Как отвечать на вопрос про конфликты: Без лишних деталей описываем причину конфликта.'
     ' Описываем действия, которые Вы предприняли,'
     ' чтобы спокойно и профессионально выйти из ситуации.'
     ),
    ('Курсы, частные уроки; профессиональная литература;'
     ' специализированные статьи; тренинги, конференции;'
     ' отраслевые новости.'
     ),
    ('Стрессоустойчивость; умение критически мыслить;'
     ' креативность; инициативность.'
     ),
    ('Такой вопрос задается с целью понять Вашу «совместимость» с компанией и ее порядками, стилем управления.'
     ' Ваше представление об идеальном работодателе в таком случае должно максимально совпадать с описанием компании,'
     ' в которой Вы проходите собеседование. Для этого понадобится, опять же, изучить доступную о ней информацию, отзывы.'
     ' Какие критерии сюда входят: необходимость работать сверхурочно;'
     ' вид и периодичность отчетности; степень свободы/контроля сотрудников при решении задач и пр.'
     ),
    ('Если дети есть: отметьте, что с ребенком есть кому посидеть (няня, бабушка),'
     ' что на прошлой работе проблем никаких с этим не возникало и вашим обязанностям это не мешало.'
     ' При этом, если Вы знаете,'
     ' что действительно нужно будет часто брать отгулы или больничные ради ребенка,'
     ' лучше признаться в этом честно — ведь это все равно случится, и тогда Вам придется расставлять приоритеты.'
     ' Если детей нет: в таком случае рекрутера может взволновать вопрос Вашего возможного ухода в декрет.'
     ' Стандартный ответ тут — «В ближайшее время заводить детей не планирую».'
     ),
    ('Если Вы трудоголик и действительно можете чуть ли не ночевать на работе, то и никаких «но» тут не понадобится.'
     ' Ну а если Вы все-таки категорически не хотите работать сверх графика,'
     ' честно об этом скажите, чтобы избежать проблем в дальнейшем.'
     ),
    ('Каким может быть ответ: Вы еще со школы мечтали о такой работе,'
     ' и это то, что Вам нравится делать больше всего; Ваши родители или друзья занимаются этой деятельностью,'
     ' и Вы последовали их примеру; во время учебы Вы демонстрировали самые большие успехи именно в этой сфере;'
     ' Вы прошли профориентационное тестирование, и эта специальность подошла Вам идеально.'
     ),
    ('Варианты ответов на вопрос о профессиональных целях:'
     ' выпустить качественный продукт, закончить полезный проект;'
     ' вертикально или горизонтально вырасти по службе; обучиться новым программам,'
     ' применить новые подходы; работать в международной компании и прочее.')]

otvet_session_quiz = []
num_quiz = []
quiz_Data = ['Python интерпретируемый язык?',
             'Комментарии на Python начинаются с *?',
             'Нет ли предельно допустимой длины идентификатора?',
             'Арифметические оператор % возводит в степень?',
             'Освобождается ли вся память при выходе из Python?',
             'Функция range() принимает только один аргумент?',
             'Можно ли прокоментировать несколько строк?',
             'В Python только локальные переменные?',
             'Обязательны ли отступы в Python?',
             'Тип наследования в Python один?']

quiz_otvet = ["да", "нет"] * 5

keyboard_Q_menu = types.InlineKeyboardMarkup(row_width=2)
but_num = types.InlineKeyboardButton("Выбрать вопрос по номеру", callback_data="num_questions")
but_random = types.InlineKeyboardButton("Выбрать рандомный вопрос", callback_data="random_questions")
but_quiz = types.InlineKeyboardButton("Викторина", callback_data="quiz")
keyboard_Q_menu.add(but_num, but_random, but_quiz)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот, который помогает готовиться к собеседованиям.\n'
                                      'У меня есть такие команды как:\n'
                                      '/questions - выдаёт список всех вопросов\n'
                                      '/add_question - позволяет вам допонить меня любым вопросом\n'
                                      '/exit - выводит номера вопросов, которые были изучены.')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     'Команды: /questions - выдаёт список всех  вопросов, /add_question - добавить вопрос и /exit - выводит номера вопросов, которые были изучены.')


@bot.message_handler(commands=["questions"])
def questions(message):
    t = ''
    for i in range(len(questions_Data)):
        t = t + f"Вопрос №{i + 1}:\n" + f"{questions_Data[i]}\n"
    bot.send_message(message.chat.id, t)

    bot.send_message(message.chat.id, "Выбери действие", reply_markup=keyboard_Q_menu)


def rand_questions(message):
    try:
        number = int(message.text) - 1
        if 0 <= number < len(questions_Data) and number != 1:

            if len(otvet_session) == 0:
                otvet_session.append([message.chat.id, number])

            elif len(otvet_session) > 0:
                for i in otvet_session:
                    if i[0] == message.chat.id:
                        try:
                            [number != j for j in i].index(False)
                        except:
                            i.append(number)
                    else:
                        otvet_session.append([message.chat.id, number])

            bot.send_message(message.chat.id, f'Вопрос №{number + 1}:\n'
                                              f'{questions_Data[number]}')
            bot.send_message(message.chat.id, f'Ответ:\n'

                                              f'{otvet_Data[number]}', reply_markup=keyboard_Q_menu)
        elif number == 1:
            if len(otvet_session) == 0:
                otvet_session.append([message.chat.id, number])

            elif len(otvet_session) > 0:
                for i in otvet_session:
                    if i[0] == message.chat.id:
                        try:
                            [number != j for j in i].index(False)
                        except:
                            i.append(number)
                    else:
                        otvet_session.append([message.chat.id, number])

            img = open('decorator.PNG', 'rb')
            bot.send_message(message.chat.id, f'Вопрос №{number + 1}:\n'
                                              f'{questions_Data[number]}')
            bot.send_photo(message.chat.id, img, reply_markup=keyboard_Q_menu)
            img.close()
        else:
            bot.send_message(message.chat.id, f"Вы уверены, что ввели число от 1 до 12?", reply_markup=keyboard_Q_menu)
    except:
        bot.send_message(message.chat.id, f"Вы уверены, что ввели число? Введите число от 1 до 12",
                         reply_markup=keyboard_Q_menu)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'num_questions':
            bot.send_message(call.message.chat.id, 'Введите номер вопроса')
            bot.register_next_step_handler(call.message, rand_questions)
        elif call.data == 'random_questions':
            rand = random.randint(0, len(questions_Data) - 1)

            if len(otvet_session) == 0:
                otvet_session.append([call.message.chat.id, rand])
            elif len(otvet_session) > 0:
                for i in otvet_session:
                    if i[0] == call.message.chat.id:
                        try:
                            [rand != j for j in i].index(False)
                        except:
                            i.append(rand)
                    else:
                        otvet_session.append([call.message.chat.id, rand])

            if 0 <= rand < len(questions_Data) and rand != 1:
                bot.send_message(call.message.chat.id, f'Рандомный вопрос №{rand + 1}:\n'
                                                       f'{questions_Data[rand]}')

                bot.send_message(call.message.chat.id, f'Ответ:\n'
                                                       f'{otvet_Data[rand]}', reply_markup=keyboard_Q_menu)
            elif rand == 1:
                img = open('decorator.PNG', 'rb')
                bot.send_message(call.message.chat.id, f'Вопрос №{rand + 1}:\n'
                                                       f'{questions_Data[rand]}')

                bot.send_photo(call.message.chat.id, img, reply_markup=keyboard_Q_menu)
                img.close()
        elif call.data == "quiz":
            try:
                otvet_session_quiz.pop([j[0] for j in otvet_session_quiz].index(call.message.chat.id))
            except:
                pass

            try:
                num_quiz.pop([j[0] for j in num_quiz].index(call.message.chat.id))
            except:
                pass



            but = []
            for i in range(len(quiz_Data)):
                but.append(types.InlineKeyboardButton(f"{i + 1}", callback_data=f"quiz_{i}"))

            keyboard = types.InlineKeyboardMarkup(row_width=3)
            keyboard.add(*but)

            bot.send_message(call.message.chat.id, "Выбери!!!", reply_markup=keyboard)
        else:
            for questions in range(len(quiz_Data)):
                if call.data == f"quiz_{questions}":
                    if len(num_quiz) == 0:
                        num_quiz.append([call.message.chat.id])

                    if len(num_quiz) > 0:
                        for number in num_quiz:
                            if number[0] == call.message.chat.id:
                                try:
                                    number.index(questions)
                                    bot.send_message(call.message.chat.id, f"Не повторяйся!!!")
                                except:
                                    if len(otvet_session_quiz) == 0:
                                        otvet_session_quiz.append(
                                            [call.message.chat.id, *[i for i in range(len(quiz_Data))]])
                                    elif len(otvet_session_quiz) > 0:
                                        for session in otvet_session_quiz:
                                            if session[0] == call.message.chat.id:
                                                try:
                                                    session.index(call.message.chat.id)
                                                except:
                                                    session.append(
                                                        [call.message.chat.id, *[i for i in range(len(quiz_Data))]])

                                    for session in otvet_session_quiz:
                                        if session[0] == call.message.chat.id:
                                            a = random.choice([session[j] for j in range(1, len(session))])

                                    print(a)
                                    keyboard = types.InlineKeyboardMarkup(row_width=1)
                                    but_yes = types.InlineKeyboardButton(f"Да", callback_data=f"quiz_yes{a}")
                                    but_no = types.InlineKeyboardButton(f"Нет", callback_data=f"quiz_no{a}")
                                    keyboard.add(but_yes, but_no)

                                    bot.send_message(call.message.chat.id, f"{quiz_Data[a]}", reply_markup=keyboard)

                                    for session in otvet_session_quiz:
                                        if session[0] == call.message.chat.id:
                                            session.pop(session.index(a))
                                            number.append(questions)

            options = ["Неверно", "Верно"]
            for i in range(len(quiz_Data)):
                if call.data == f"quiz_yes{i}":
                    bot.send_message(call.message.chat.id, options[int(quiz_otvet[i] == "да")])
                elif call.data == f"quiz_no{i}":
                    bot.send_message(call.message.chat.id, options[int(quiz_otvet[i] == "нет")])


@bot.message_handler(commands=['add_question'])
def add_guestion(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        'Напишите вопрос и ответ', url='telegram.me/sleepforeverrrr13')
    )
    bot.send_message(
        message.chat.id, 'Добавить вопрос', reply_markup=keyboard
    )


@bot.message_handler(commands=["exit"])
def exit(message):
    t = ""


    try:
        [j[0] for j in otvet_session].index(message.chat.id)

        for i in otvet_session:
            if i[0] == message.chat.id:
                if len(i) >= 2:
                    id = i[0]
                    i.pop(0)
                    i.sort()
                    for j in range(0, len(i)):
                        t = (t + f"№{int(i[j] + 1)}\n")

                    bot.send_message(message.chat.id, f'Номера изученных вопросов:\n{t}')

                    otvet_session.pop(otvet_session.index(i))


                else:
                    bot.send_message(message.chat.id, f'Что-то явно не так')
    except:
        bot.send_message(message.chat.id, f'Вы не изучили не одного вопроса')

    try:
        otvet_session_quiz.pop([j[0] for j in otvet_session_quiz].index(message.chat.id))
    except:
        pass

    try:
        num_quiz.pop([j[0] for j in num_quiz].index(message.chat.id))
    except:
        pass




bot.polling()