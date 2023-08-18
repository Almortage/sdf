import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Webot = Client(
   "Telegraph Uploader",
   api_id=Config.API_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

@Webot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>مرحبًا ، أنا Telegraph Bot يمكنني تحميل الصور أو مقاطع الفيديو للتلغراف. 
By : @Almortagel_12 
اضغط على زر المساعدة لمعرفة المزيد حول كيفية استخدامي</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "كيفيه الاستخدام 🍂💕", callback_data="help"),
                                        InlineKeyboardButton(
                                            "Channel", url="https://t.me/AlmortagelTech")
                                    ],[
                                      InlineKeyboardButton(
                                            "𝑫𝒆𝒗", url="https://t.me/Almortagel_12")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>دليل استخدام البوت 🍂💕

عشان تستخدام البوت كل الي عليك انك تبعت الصورة او الفيد للبوت وهو هيحملها علي سيرفر التلجراف ويديلك اللينك ، بشرط انها تكون اقل من 5 ميجا 🔰💕

𝒄𝒉 ~ @AlmortagelTech </b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="start"),
                                        InlineKeyboardButton(
                                            "About", callback_data="about"),
                                  ],[
                                        InlineKeyboardButton(
                                            "قناه البوت 🍂💕", url="https://t.me/AlmortagelTech")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await Webot.send_message(
               chat_id=message.chat.id,
               text="""<b>About Telegraph Bot!</b>

<b>♞ owner:</b> <a href="https://t.me/Almortagel_12">ALMORTAGEL </a>

<b>♞ Support:</b> <a href="https://t.me/AlmortagelTech">ALMORTAGELTECH </a>

<b>~ @AlmortagelTech</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "Back", callback_data="help"),
                                        InlineKeyboardButton(
                                            "للمزيد من البوتات الخدميه 🍂💕", url="https://t.me/AlmortagelTech")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")

@Webot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("يتم الرفع علي تليجراف.....")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("حجم الصورة اكبر من 5 ميجا !") 
    else:
        await msg.edit_text(f'**تم الرفع علي تليجراف\n\n https://telegra.ph{response[0]}\n\nJoin @AlmortagelTech**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("يتم الرفع علي تليجراف.....")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("حجم الفيديو اكبر من 5ميجا !") 
    else:
        await msg.edit_text(f'**تم الرفع علي تليجراف\n\n https://telegra.ph{response[0]}\n\nJoin @AlmortagelTech**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

@Webot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("يتم الرفع علي تليجراف.....")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("حجم هذا الGif اكبر من 5ميجا.!") 
    else:
        await msg.edit_text(f'**تم الرفع علي تليجراف\n\n https://telegra.ph{response[0]}\n\nJoin @AlmortagelTech**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
        
@Webot.on_message(filters.message("تليجراف نص"))
async def telegraphtext(client, message):
	msg = await message.reply_text("يتم الرفع علي تليجراف.....")
    download_location = await client.download_media(
        message=message, file_name='root/jetg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("حجم هذا الGif اكبر من 5ميجا.!") 
    else:
        await msg.edit_text(f'**تم الرفع علي تليجراف\n\n https://telegra.ph{response[0]}\n\nJoin @AlmortagelTech**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
	
@Webot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)

print(
    """
تم تنصيب بوت التليجراف بنجاح 💕🍂
لو محتاج مساعده @Almortagel_12
"""
)

Webot.run()
