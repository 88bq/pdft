import telebot
from telebot import types
from PIL import Image
import fitz
import os
from PyPDF2 import PdfFileMerger
import requests
token = '1601467114:AAEQhSKTf8pSbSBFcSkG-KzDPlYZONee0X8'
bot = telebot.TeleBot("1601467114:AAEQhSKTf8pSbSBFcSkG-KzDPlYZONee0X8")
pdf = []
jpg = []
chang = []
num = []
numpdf = []
open('pdf.txt', 'a', encoding='utf-8').write('')
idi = 209501902


@bot.message_handler(commands=['help'])
def key(msg):
    ch = msg.chat.id
    z = open('pdf.txt', 'r', encoding='utf-8')
    if f'{ch}\n' in z:
        pass
    else:
        open('pdf.txt', 'a', encoding='utf-8').write(f'{ch}\n')
        bot.send_video(ch, 'BAACAgIAAxkBAANnYEeQh64ha7wNoD8WWtio0ee4OeYAAt0KAAJv6TlKKRX8zenMT78eBA')
    bot.send_video(ch, 'BAACAgIAAxkBAANnYEeQh64ha7wNoD8WWtio0ee4OeYAAt0KAAJv6TlKKRX8zenMT78eBA')


@bot.message_handler(commands=['start'])
def key(msg):
    ch = msg.chat.id
    z = open('pdf.txt', 'r', encoding='utf-8')
    #if f'{ch}\n' in z:
        #pass
    #else:
        #open('pdf.txt', 'a', encoding='utf-8').write(f'{ch}\n')
        #bot.send_video(ch, 'BAACAgIAAxkBAANnYEeQh64ha7wNoD8WWtio0ee4OeYAAt0KAAJv6TlKKRX8zenMT78eBA')
    r1 = requests.session()
    idd = msg.chat.id
    res = \
        r1.get(f'https://api.telegram.org/bot{token}/getChatMember?chat_id=@akokybot&user_id={idd}').json()[
            'result'][
            'status']
    if res == 'left' and msg.chat.id not in [idi, 1490464385]:
        bot.send_message(ch, 'يجب عليك الاشتراك في القناة اول و من ثم استخدم البوت \nلطفا💚\n@akokybot')
    else:
        if ch == idi:
            n = types.InlineKeyboardMarkup()
            n1 = types.InlineKeyboardButton('Member', callback_data='mem')
            n2 = types.InlineKeyboardButton("الاذاعة", callback_data='ad')
            n.add(n1, n2)
            bot.send_message(ch, 'Hi, The sodu 💚', reply_markup=n)
        else:
            q = types.InlineKeyboardMarkup()
            a9 = types.InlineKeyboardButton("المطور 💚", url="https://t.me/Q5QQQQ")
            a10 = types.InlineKeyboardButton("قناه الاعلانات↗️", url="https://t.me/akokybot")
            q.add(a9)
            q.add(a10)
            bot.send_message(ch, '\nاضغط للحصول على فيديو توضحيحي  /help بوت يشمل جميع مواصفات ال pdf✅', reply_markup=q)


@bot.message_handler(content_types=['document'])
def key(msg):
    ch = msg.chat.id
    z = open('pdf.txt', 'r', encoding='utf-8')
    if f'{ch}\n' in z:
        pass
    else:
        open('pdf.txt', 'a', encoding='utf-8').write(f'{ch}\n')
        bot.send_video(ch, 'BAACAgIAAxkBAANnYEeQh64ha7wNoD8WWtio0ee4OeYAAt0KAAJv6TlKKRX8zenMT78eBA')
    r1 = requests.session()
    idd = msg.chat.id
    res = \
        r1.get(f'https://api.telegram.org/bot{token}/getChatMember?chat_id=@akokybot&user_id={idd}').json()[
            'result'][
            'status']
    if res == 'left' and msg.chat.id not in [idi, 1490464385]:
        bot.send_message(ch, 'يجب عليك الاشتراك في القناة اول و من ثم استخدم البوت \nلطفا💚\n@akokybot')
    else:
        file_info = bot.get_file(msg.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        name = msg.document.file_name[-4:].lower()
        if name == '.pdf' or name == '.PDF':
            if ch in pdf and ch in numpdf:
                pass
            else:
                pdf.append(ch)
                pdf.append(f'{ch}end')

            pdf.insert(pdf.index(ch) + 1, downloaded_file)
            xx = len(pdf[pdf.index(ch):pdf.index(f'{ch}end')]) - 1
            n = types.InlineKeyboardMarkup()
            n1 = types.InlineKeyboardButton('استخراج الصور من pdf🌁', callback_data='n2')
            n2 = types.InlineKeyboardButton('تحويل pdf الى صور🖼🔄', callback_data='n3')
            n6 = types.InlineKeyboardButton('تغير اسم الملف المرسل ♻️', callback_data='chang2')
            n.add(n1, n2)
            n.add(n6)
            if xx > 1:
                n3 = types.InlineKeyboardButton(f'لديك {xx}  من ال pdf\n اضغط ليتم الدمج بملف واحد📁', callback_data='n4')
                n4 = types.InlineKeyboardButton(f'الغاء الدمج ❌', callback_data='n5')
                n.add(n3)
                n.add(n4)
            bot.send_message(ch, 'اختر الاوامر التي تريد القيام بها💚⤵️', reply_markup=n)
        elif name == '.txt' and ch == idi:
            file_info = bot.get_file(msg.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            with open(f'pdf1.txt', 'wb') as new_file:
                new_file.write(downloaded_file)
            z = open(f'pdf1.txt', 'r', encoding='utf-8').read().split('\n')
            i = 0
            while i < len(z):
                if z[i] in open('pdf.txt', 'r', encoding='utf-8').read():
                    pass
                else:
                    open('pdf.txt', 'a', encoding='utf-8').write(f'{z[i]}\n')
                i += 1
            bot.send_message(ch, 'Done')
        else:
            bot.reply_to(msg, f'عذرا هذا الملف من نوع {name} و البوت يستقبل فقط pdf ☑️⚠️')


@bot.message_handler(content_types=['photo'])
def key(msg):
    ch = msg.chat.id
    z = open('pdf.txt', 'r', encoding='utf-8')
    if f'{ch}\n' in z:
        pass
    else:
        open('pdf.txt', 'a', encoding='utf-8').write(f'{ch}\n')
        bot.send_video(ch, 'BAACAgIAAxkBAANnYEeQh64ha7wNoD8WWtio0ee4OeYAAt0KAAJv6TlKKRX8zenMT78eBA')
    r1 = requests.session()
    idd = msg.chat.id
    res = \
        r1.get(f'https://api.telegram.org/bot{token}/getChatMember?chat_id=@akokybot&user_id={idd}').json()[
            'result'][
            'status']
    if res == 'left' and msg.chat.id not in [idi, 1490464385]:
        bot.send_message(ch, 'يجب عليك الاشتراك في القناة اول و من ثم استخدم البوت \nلطفا💚\n@akokybot')
    else:
        file_info = bot.get_file(
            str(msg).split("file_id': '")[-1][:str(msg).split("file_id': '")[-1].find("', 'file_unique_id")])
        downloaded_file = bot.download_file(file_info.file_path)
        if ch in jpg and ch in num:
            pass
        else:
            jpg.append(ch)
            jpg.append(f'{ch}end')
        jpg.insert(jpg.index(ch) + 1, downloaded_file)
        xx = len(jpg[jpg.index(ch):jpg.index(f'{ch}end')]) - 1
        n = types.InlineKeyboardMarkup()
        n1 = types.InlineKeyboardButton('لتحويل الى pdf🔄📚', callback_data='n1')
        n.add(n1)
        bot.send_message(ch, f'اصبح الان لديك {xx} من الصور \n اضغط لتحويل الى pdf⤵️🔁', reply_markup=n)


@bot.callback_query_handler(lambda call: True)
def any(call):
    markup = types.ForceReply(selective=False)
    ch = call.message.chat.id
    z = open('pdf.txt', 'r', encoding='utf-8')
    if f'{ch}\n' in z:
        pass
    else:
        open('pdf.txt', 'a', encoding='utf-8').write(f'{ch}\n')
        bot.send_video(ch, 'BAACAgIAAxkBAANnYEeQh64ha7wNoD8WWtio0ee4OeYAAt0KAAJv6TlKKRX8zenMT78eBA')
    r1 = requests.session()
    idd = ch
    res = \
        r1.get(f'https://api.telegram.org/bot{token}/getChatMember?chat_id=@akokybot&user_id={idd}').json()[
            'result'][
            'status']
    if res == 'left' and ch not in [idi, 1490464385]:
        bot.send_message(ch, 'يجب عليك الاشتراك في القناة اول و من ثم استخدم البوت \nلطفا💚\n@akokybot')
    else:
        if call.data == 'chang2':
            if ch in chang:
                pass
            else:
                chang.append(ch)
            chang.insert(chang.index(ch) + 1, pdf[pdf.index(f'{ch}end') -1])

            bot.send_message(ch, 'ارسل اسم الملف الذي تريدة↕️', reply_markup=markup)
        if call.data == 'chang':
            if ch in chang:
                pass
            else:
                chang.append(ch)

            file_info = bot.get_file(call.message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            chang.insert(chang.index(ch) + 1, downloaded_file)
            bot.send_document(ch, call.message.document.file_id)
            bot.send_message(ch, 'ارسل اسم الملف الذي تريدة↕️', reply_markup=markup)
        if call.data == 'n1':                             ################### photo
            if ch in jpg:
                try:
                    xx = len(jpg[jpg.index(ch):jpg.index(f'{ch}end')]) - 1
                    zz = jpg[jpg.index(ch):jpg.index(f'{ch}end')]
                    merger = PdfFileMerger()
                    i = 0
                    while i < len(zz) - 1:

                        x = zz[xx - i]

                        with open(f'xc.jpg', 'wb') as new_file:
                            new_file.write(x)

                        img = Image.open('xc.jpg')
                        if img.mode == 'RGBA':
                            img = img.convert('RGB')

                        img.save(f'test{i}.pdf', 'PDF', resolution=200.0)
                        merger.append(f'test{i}.pdf')
                        i += 1
                    # merger.append(img.save('test10.pdf', 'PDF', resolution=100.0))
                    merger.write(f"Ahmed Bot {ch}.pdf")
                    merger.close()
                    aa = types.InlineKeyboardMarkup()
                    aa1 = types.InlineKeyboardButton('تغير اسم الملف💚🔀', callback_data='chang')
                    aa.add(aa1)
                    bot.send_document(ch, open(f'Ahmed Bot {ch}.pdf', 'rb'), reply_markup=aa)
                    try:
                        try:
                            new_file.close()
                        except:
                            pass
                        os.unlink(f'Ahmed Bot {ch}.pdf')
                        os.unlink(f'{ch}.png')
                    except:
                        pass
                    xx = len(jpg[jpg.index(ch):jpg.index(f'{ch}end')]) - 1
                    i = 0
                    while i < xx:
                        jpg.remove(jpg[jpg.index(ch) + 1])
                        os.unlink(f'test{i}.pdf')
                        i += 1

                except:
                    bot.answer_callback_query(call.id, 'قم بارسال الصور ليتم تحويلها🖼', show_alert=True)
            else:
                bot.answer_callback_query(call.id, 'قم بارسال الصور ليتم تحويلها🖼', show_alert=True)
        elif call.data == 'n2':                              ##################### extrct
            if ch in pdf:
                try:
                    xx = len(pdf[pdf.index(ch):pdf.index(f'{ch}end')]) - 1
                    with open(f'{ch}.pdf', 'wb') as new_file:
                        new_file.write(pdf[pdf.index(ch) + 1])
                    doc = fitz.open(f'{ch}.pdf')
                    v = 0
                    for i in range(len(doc)):
                        for img in doc.getPageImageList(i):
                            xref = img[0]
                            pix = fitz.Pixmap(doc, xref)
                            if pix.n < 5:  # this is GRAY or RGB
                                pix.writePNG(f"{ch}.png")
                                z = bot.send_photo(ch, open(f'{ch}.png', 'rb'))
                                v += 1
                            else:  # CMYK: convert to RGB first
                                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                                pix1.writePNG("p%s-%s.png" % (i, xref))
                                pix1 = None
                            pix = None

                    try:
                        try:
                            new_file.close()
                        except:
                            pass
                        os.unlink(f'{ch}.png')
                        os.remove(f'{ch}.pdf')
                    except:
                        pass
                    if v == 0:
                        bot.send_message(ch, 'لا توجد هنالك اي صوره ليتم استخراجها⚠️')
                    i = 0
                    while i < xx:
                        pdf.remove(pdf[pdf.index(ch) + 1])
                        i += 1

                except:
                    bot.answer_callback_query(call.id, 'قم بارسال pdf ليتم استخراج الصور✳️', show_alert=True)
            else:
                bot.answer_callback_query(call.id, 'قم بارسال pdf ليتم استخراج الصور✳️', show_alert=True)

        elif call.data == 'n3':                          ######################## convert
            if ch in pdf:
                try:
                    xx = len(pdf[pdf.index(ch):pdf.index(f'{ch}end')]) - 1
                    with open(f'{ch}.pdf', 'wb') as new_file:
                        new_file.write(pdf[pdf.index(ch) + 1])
                    doc = fitz.open(f'{ch}.pdf')
                    
                    v = 0
                    for i in doc:
                        page = doc.loadPage(v)  # number of page
                        pix = page.getPixmap()
                        output = f"{ch}.png"
                        pix.writePNG(output)
                        bot.send_photo(ch, open(f'{ch}.png', 'rb'))
                        v += 1
                    try:
                        try:
                            new_file.close()
                        except:
                            pass
                        os.unlink(f'{ch}.png')
                        os.unlink(f'{ch}.pdf')
                    except:
                        pass
                    i = 0
                    while i < xx:
                        pdf.remove(pdf[pdf.index(ch) + 1])
                        i += 1

                except:
                    bot.answer_callback_query(call.id, 'قم بارسال pdf ليتم تحويلها لصور🔁🖼', show_alert=True)
            else:
                bot.answer_callback_query(call.id, 'قم بارسال pdf ليتم تحويلها لصور🔁🖼', show_alert=True)

        elif call.data == 'n5':
            try:
                xx = len(pdf[pdf.index(ch):pdf.index(f'{ch}end')]) - 1
                i = 0
                while i < xx:
                    pdf.remove(pdf[pdf.index(ch) + 1])
                    i += 1
                bot.send_message(ch, 'تم الغاء الدمج بنجاح 💟')
            except:
                bot.send_message(ch, 'تم الغاء الدمج بنجاح 💟')

        elif call.data == 'n4':                               ########################## dmg
            pdfs = []
            if ch in pdf:
                try:
                    xx = len(pdf[pdf.index(ch):pdf.index(f'{ch}end')]) - 1
                    merger = PdfFileMerger()
                    i = 0
                    while i < xx:
                        with open(f'tset{i}.pdf', 'wb') as new_file:
                            new_file.write(pdf[pdf.index(ch) + xx - i])
                            pdfs.append(f'tset{i}.pdf')
                        i += 1
                    for pdf1 in pdfs:
                        merger.append(pdf1)
                    merger.write(f"Ahmed Bot {ch}.pdf")
                    merger.close()
                    aa = types.InlineKeyboardMarkup()
                    aa1 = types.InlineKeyboardButton('تغير اسم الملف💚🔀', callback_data='chang')
                    aa.add(aa1)
                    bot.send_document(ch, open(f'Ahmed Bot {ch}.pdf', 'rb'), reply_markup=aa)
                    try:
                        try:
                            new_file.close()
                        except:
                            pass
                        os.unlink(f'Ahmed Bot {ch}.pdf')
                        os.unlink(f'{ch}.png')
                    except:
                        pass

                    i = 0
                    while i < xx:
                        pdf.remove(pdf[pdf.index(ch) + 1])
                        i += 1

                except:
                    bot.answer_callback_query(call.id, 'قم بارسال مجموعه من pdf ليتم دمجهم☯️', show_alert=True)
            else:
                bot.answer_callback_query(call.id, 'قم بارسال مجموعه من pdf ليتم دمجهم☯️', show_alert=True)
        elif call.data == 'mem' and ch == idi:            ############# Member
            x = open('pdf.txt', 'r', encoding='utf-8').read().split('\n')
            bot.send_message(ch, f'Member is {len(x)}')
            bot.send_document(ch, open('pdf.txt', 'rb'))
        elif call.data == 'ad' and ch == idi:
            markup = types.ForceReply(selective=False)
            bot.send_message(ch, 'ur Ads', reply_markup=markup)
            

@bot.message_handler(content_types='text')
def an(msg):
    ch = msg.chat.id
    x = msg.text
    z = open('pdf.txt', 'r', encoding='utf-8')
    if f'{ch}\n' in z:
        pass
    else:
        open('pdf.txt', 'a', encoding='utf-8').write(f'{ch}\n')
        bot.send_video(ch, 'BAACAgIAAxkBAANnYEeQh64ha7wNoD8WWtio0ee4OeYAAt0KAAJv6TlKKRX8zenMT78eBA')
    try:
        if msg.reply_to_message.text == 'ارسل اسم الملف الذي تريدة↕️':
            bot.send_message(ch, 'انتظر قليلا من فظلك 🎶♻️')
            if ch in chang:
                qq = chang[chang.index(ch) + 1]

                with open(f'{msg.text}.pdf', 'wb') as new_file:
                    new_file.write(qq)
                bot.send_document(ch, open(f'{msg.text}.pdf', 'rb'))
                try:
                    try:
                        new_file.close()
                    except:
                        pass
                    os.unlink(f'{msg.text}.pdf')
                    os.unlink(f'{ch}.png')
                except:
                    pass
            else:
                bot.send_message(ch, 'قم بارسال الملف من جديد من فظلك*️⃣')
    except:
        pass
    if ch == idi:
        try:
            if msg.reply_to_message.text == "ur Ads":
                xx = open('pdf.txt', 'r').read().split('\n')
                for i in xx:
                    try:
                        bot.send_message(i, x)
                    except:
                        pass
        except:
            pass
    else:
        q = types.InlineKeyboardMarkup()
        a9 = types.InlineKeyboardButton("المطور 💚", url="https://t.me/Q5QQQQ")
        a10 = types.InlineKeyboardButton("قناه الاعلانات↗️", url="https://t.me/akokybot")
        q.add(a9)
        q.add(a10)
        bot.send_message(ch, '''البوت يستقبل كل الاتي 💚
1- تستطيع تحويل مجموعه من الصور الى pdf🔄📁
2- تستطيع استخراج الصور من pdf📤🏙
3- تستطيع تحويل pdf الى صور 🔄🌌
4- تستطيع دمج مجموعه pdf ب ملف واحد🗂
اضغط للحصول على الفيديو التوضيحي 
/help''', reply_markup=q)


bot.polling(none_stop=True)
