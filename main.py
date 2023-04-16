from telebot import types
import telebot
import os

bot = telebot.TeleBot("EMPTY TOKEN")
admins = [,]

@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Бонус/Подарок")
	back = types.KeyboardButton("Проблема/Вопрос по товару")
	markup.add(btn1, back)
	bot.register_next_step_handler(bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Мы ценим каждого клиента и заботимся о наших покупателях! Теперь Вы часть семьи Consalatio! Нажмите на интересующую Вас кнопку⤵', reply_markup=markup), selector)

def selector(message):
	try:
		if message.text == 'Бонус/Подарок':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			btn1 = types.KeyboardButton("Я уже подписался")
			markup.add(btn1)
			bot.register_next_step_handler(bot.send_message(message.chat.id, 'Получите 100 рублей  на баланс телефона или сразу на карту! Вам нужно будет выполнить несколько простых действий. Подписаться на наш Telegram канал – там мы показываем работу нашего Бренда и уведомляем Вас о скидках и новых товарах! \nСсылка на канал: https://t.me/consolatio', reply_markup=markup), selector)

		elif message.text == "Проблема/Вопрос по товару":
			bot.register_next_step_handler(bot.send_message(message.chat.id, 'Опишите Нам вашу проблему'), describe)


		elif message.text == 'Я уже подписался':
			try:
				print(bot.get_chat_member(-1001922894617, message.from_user.id))
				markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
				btn1 = types.KeyboardButton("Прислать фото отзыва")
				back = types.KeyboardButton("Проблема/Вопрос по товару")
				markup.add(btn1, back)
				bot.register_next_step_handler(bot.send_message(message.chat.id, '''
Спасибо за подписку! Если вам понравился товар и Вы довольны его качеством, то оставьте положительный отзыв ★★★★★. Мы также подарим вам бонусные 50 рублей, если в отзыве будут фотографии!
Важные моменты!!! (можно изменить шрифт текста, чтобы он выделялся)
1-Текст и фото (если Вы пожелаете) должны быть без упоминания визитки! 
2- После публикации, нажмите на кнопку «прислать фото отзыва»
3- Если у вас еще остались вопросы или проблемы по товару, то нажмите на кнопку «Проблема/вопрос по товару»
	''', reply_markup=markup), selector)

			except telebot.apihelper.ApiTelegramException as e:
				print("Не подписан")
				bot.register_next_step_handler(bot.send_message(message.chat.id, 'Для продолжения подпишитесь, пожалуйста, на наш Telegram канал'), selector)

		elif message.text == 'Прислать фото отзыва':
			bot.register_next_step_handler(bot.send_message(message.chat.id, 'Спасибо, что написали отзыв, отправьте фотографию или скриншот!', reply_markup=None), selector)

		elif 'НОВЫЙ' in message.text:
			photo1 = open(f'uploads/{message.from_user.id}.jpg', 'rb')
			try:
				for admin in admins:
					bot.send_photo(admin, photo1, caption=message.text + f"НОВАЯ! ЗАЯВКА! ИЗМЕНЕНИЕ ДАННЫХ! \n\nНОВАЯ\nID: {message.from_user.id}\nUSERNAME: @{message.from_user.username}\nName: {message.from_user.first_name}")
				
			except:
				pass

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			btn1 = types.KeyboardButton("Прислать фото отзыва")
			back = types.KeyboardButton("Проблема/Вопрос по товару")
			markup.add(btn1, back)			
			bot.send_message(message.chat.id, 'Администратору успешно направлена новая информация!', reply_markup=markup)

		elif message.content_type == 'photo':
			try:
				file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
				downloaded_file = bot.download_file(file_info.file_path)
				if not os.path.isdir("uploads/"+str(message.from_user.id)):
					os.makedirs("uploads/"+str(message.from_user.id))
				src='uploads/'+str(message.from_user.id)+".jpg"
				with open(src, 'wb') as new_file:
					new_file.write(downloaded_file)

				bot.register_next_step_handler(bot.send_message(message.chat.id, '''
		Пришлите, пожалуйста, данные Вашей карты по следующему шаблону. 

		НОМЕР КАРТЫ ИЗ 16 цифр: 0000 0000 0000 0000 

		НОМЕР ТЕЛЕФОНА ПРИКРЕПЛЁННЫЙ К БАНКУ: +79ХХХХХХХХХ

		НАЗВАНИЕ БАНКА: Сбербанк, Тинькоф и т.д.

		ПОЛУЧАТЕЛЬ: Иванов Андрей Иванович.

		Чтобы получить деньги на номер телефона: +79ХХХХХХХХХ и название вашего сотового оператора.

		Важно отправлять полные данные для корректной оплаты''', reply_markup=None), cards)

			except:
				bot.send_message(message.chat.id, 'Что-то не похоже на картинку, попробуйте снова!')


	except TypeError:
			file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
			downloaded_file = bot.download_file(file_info.file_path)
			if not os.path.isdir("uploads/"+str(message.from_user.id)):
				os.makedirs("uploads/"+str(message.from_user.id))
			src='uploads/'+str(message.from_user.id)+".jpg"
			with open(src, 'wb') as new_file:
				new_file.write(downloaded_file)

			bot.register_next_step_handler(bot.send_message(message.chat.id, '''
Пришлите, пожалуйста, данные Вашей карты по следующему шаблону. 

НОМЕР КАРТЫ ИЗ 16 цифр: 0000 0000 0000 0000 

НОМЕР ТЕЛЕФОНА ПРИКРЕПЛЁННЫЙ К БАНКУ: +79ХХХХХХХХХ

НАЗВАНИЕ БАНКА: Сбербанк, Тинькоф и т.д.

ПОЛУЧАТЕЛЬ: Иванов Андрей Иванович.

Чтобы получить деньги на номер телефона: +79ХХХХХХХХХ и название вашего сотового оператора.

Важно отправлять полные данные для корректной оплаты''', reply_markup=None), cards)


def cards(message):
	try:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Бонус/Подарок")
		back = types.KeyboardButton("Проблема/Вопрос по товару")
		markup.add(btn1, back)
		bot.register_next_step_handler(bot.send_message(message.chat.id, '''
	Ваша заявка принята!
	Выплата производится в течение 24 часов.
	Если в реквизитах заметили ошибку, не волнуйтесь, пришлите нам исправленные реквизиты с пометкой "НОВЫЙ". Благодарим за сотрудничество!''', reply_markup=markup), selector)
		photo1 = open(f'uploads/{message.from_user.id}.jpg', 'rb')

		for admin in admins:
			bot.send_photo(admin, photo1, caption=message.text + f"\n\nID: {message.from_user.id}\nUSERNAME: @{message.from_user.username}\nName: {message.from_user.first_name}")
	except:
		photo1.close()
		pass
def describe(message):
	try:
		for admin in admins:
			bot.forward_message(admin, message.chat.id, message.message_id)
			bot.send_message(admin, f"ID: {message.from_user.id}\nUSERNAME: @{message.from_user.username}\nName: {message.from_user.first_name}")
		bot.register_next_step_handler(bot.send_message(message.chat.id, 'Спасибо, за обратную связь, в течение 24 часов с вами свяжется наш менеджер!'), selector)

	except:
		pass

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Бонус/Подарок")
	back = types.KeyboardButton("Проблема/Вопрос по товару")
	markup.add(btn1, back)
	bot.register_next_step_handler(bot.send_message(message.chat.id, 'Спасибо, за обратную связь, в течение 24 часов с вами свяжется наш менеджер!', reply_markup=markup), selector)

@bot.message_handler(func=lambda message: 'НОВЫЙ' in message.text.lower(), content_types=['text'])
def lalala(message):
	try:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Бонус/Подарок")
		back = types.KeyboardButton("Проблема/Вопрос по товару")
		markup.add(btn1, back)
		photo1 = open(f'uploads/{message.from_user.id}.jpg', 'rb')

		for admin in admins:
			bot.send_photo(admin, photo1, caption=message.text + f"ИСПРАВЛЕНИЕ ДАННЫХ! НОВОЕ!\n\nID: {message.from_user.id}\nUSERNAME: @{message.from_user.username}\nName: {message.from_user.first_name}")
		

		bot.register_next_step_handler(bot.send_message(message.chat.id, '''
	Спасибо, мы прислали вашу исправленную заявку. 
	Ваша заявка принята!
	Выплата производится в течение 24 часов.
	Если в реквизитах заметили ошибку, не волнуйтесь, пришлите нам исправленные реквизиты с пометкой "НОВЫЙ". Благодарим за сотрудничество!''', reply_markup=markup), selector)

	except:
		pass


bot.polling()