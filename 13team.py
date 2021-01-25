import telebot

from telebot import types

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("1529668627:AAGwqc4PeSEl2lxFgpjGeHC9gd81KcRCYBk", skip_pending=True)

@bot.message_handler(commands=["start"])

def menu(message):

markup = InlineKeyboardMarkup(row_width=2)

grup = InlineKeyboardButton("💬 Qrupumuz", url="https://t.me/team13chat")

kanal = InlineKeyboardButton("📣 Kanalımız", url="https://t.me/team13resmi")

sahip = InlineKeyboardButton("İrəli", callback_data="devam")

markup.add(grup,kanal,sahip)

bot.send_message(message.chat.id, """

⚜️*13Team*⚜️

_Haqqında Məlumat Almaq Üçün Hazırlanmış Botdur

⚜️13Team⚜️ Qrupunuzu Qoşmaq üçün 

• 500+ Qrupunuz Olmalıdır

• Bizim Tagımızı, Federasiya Kanalı,Ve Rəsmi Botumuzu Qrup Biosuna Yazılmalıdır 

[ɢᴀᴢᴀʜᴋᴢᴀᴅᴀ13 ](tg://user?id=1370412675)

⚜️13Team⚜️ Telegram Sahibi 

*TAG:* #13

_Tagımızımdan istifade üçün 13Team'ə bildirməlidir..._

""", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "devam")

def call(call):

markup = InlineKeyboardMarkup(row_width=3)

kimiz = InlineKeyboardButton("🤔 ⚜️13Team⚜️ kimdir?", callback_data="kimik")

userbot= InlineKeyboardButton("🤖UserBot", callback_data="userbot")

iletisim = InlineKeyboardButton("📞 Əlaqə Üçün", url=”https://t.me/gazahkzada13")

geri = InlineKeyboardButton("🔄Geriye Dön", callback_data="geri")

markup.add(kimiz, userbot, iletisim, geri)

bot.delete_message(call.message.chat.id, call.message.message_id)

bot.send_message(call.message.chat.id, """

Salam [{}](tg://user?id={}), . Aşağıdakı Butonlardan İstifadə Edərək ⚜️13Team⚜️ Haqqında Məlumata Sahib Ola bilərsiniz

_Reklam Və Əlaqə üçün Əlaqə Butonuna Basın!_""".format(call.from_user.first_name, call.from_user.id), reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "geri")

def menu(call):

markup = InlineKeyboardMarkup(row_width=2)

grup = InlineKeyboardButton("💬 Qrupumuz", url="https://t.me/team13chat")

kanal = InlineKeyboardButton("📣 Kanalımız", url="https://t.me/team13resmi")

sahip = InlineKeyboardButton("İrəli", callback_data="devam")

markup.add(grup,kanal,sahip)

bot.delete_message(call.message.chat.id, call.message.message_id)

bot.send_message(call.message.chat.id, """

⚜️*13Team*⚜️

_Haqqında Məlumat Almaq Üçün Hazırlanmış Botdur

⚜️13Team⚜️ Qrupunuzu Qoşmaq üçün 

• 500+ Qrupunuz Olmalıdır

• Bizim Tağımızdan Mütləq İstifade Etməlidir

[ɢᴀᴢᴀʜᴋᴢᴀᴅᴀ13](tg://user?id=1370412675)

🇦🇿*13Team Telegram Sahibi*🇦🇿

*TAG:* #13

_Tağımızımdan istifade üçün 13Team'ə bildirməlidir..._

""", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "kimik")

def menu(call):

markup = InlineKeyboardMarkup(row_width=2)

grup = InlineKeyboardButton("🔄Geriyə Gəl", callback_data="dəvam")

markup.add(grup)

bot.delete_message(call.message.chat.id, call.message.message_id)

bot.send_message(call.message.chat.id, """

⚜️*13Team*⚜️

🇦🇿

_Yaranma Tarixi 01.04.2020

⚜️13ᴛᴇᴀᴍ⚜️ yanvar ayının 4'ü @Gazahkzada13 tərəfindən yaradılmışdır ilk yarandığı müddətdə 12 nəfərlik esas heyyət sahib olmuştur ve mart ayında bəzi sebeblere göre dağılmışdır ve sentyabrın 19'u yenidən @Gazahkzada13'ün sahibliyi altında qaldığı yerden işine davam etmişdir.Bu müddətdə⚜️13ᴛᴇᴀᴍ⚜️bir çox qruplara lazımlı cavabını vermişdir.⚜️13ᴛᴇᴀᴍ⚜️  kiminsə əziyyetini yerə vurmaq üçün yaranmamışdır amaki kime necə lazımdırsa cavabını vermişdir ve həmişə cavabı verəcək...

🇬🇧

establishment 01.04.2020

⚜️13ᴛᴇᴀᴍ⚜️ January 4 was created by @Gazahkzada13. It had a main staff of 12 people when it was first established, and in March it was disbanded for some reason, and September 19 resumed its work from where it was owned by @Gazahkzada13. During this period⚜️13ᴛᴇᴀᴍ ⚜️He gave the necessary answers to many groups.⚜️13ᴛᴇᴀᴍ⚜️ He was not created to put someone's suffering on the ground.._
""", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == 'userbot')

def user(call):

markup = InlineKeyboardMarkup(row_width=1)

grup = InlineKeyboardButton("🔄 Geriyə Gəl", callback_data="dəvam")

markup.add(grup)

bot.delete_message(call.message.chat.id, call.message.message_id)

bot.send_message(call.message.chat.id, """

🇦🇿

*Sadəcə Biraz Səbr Edin*

CANCELFORWARD 1 DELETE 1 REPLY EDIT
