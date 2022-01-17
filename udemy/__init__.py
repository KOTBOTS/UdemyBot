# UdemyBot - A Simple Udemy Free Courses Scrapper

# Copyright (C) 2021-Present Gautam Kumar <https://github.com/gautamajay52>

import os

token = os.environ.get('TOKEN')
api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')

START = """
Hᴇy, ɪ'Aᴍ Aɴ Uᴅᴇᴍy Bᴏᴛ

ɪ Cᴀɴ Sᴇɴᴅ Yᴏᴜ Fʀᴇᴇ Uᴅᴇᴍy Cᴏᴜʀꜱᴇꜱ Lɪɴᴋꜱ Oɴʟy Fᴏʀ Eᴅᴜᴄᴀᴛɪᴏɴ Pʀᴏᴄᴇꜱꜱ

Commands:
    /discudemy page
    /udemy_freebies page
    /tutorialbar page
    /real_discount page
    /coursevania
    /idcoupons page

Pᴀɢᴇ - Wʜɪᴄʜ Pᴀɢᴇ Yᴏᴜ Wᴀɴᴛᴇᴅ Tᴏ Sᴄʀᴀᴩ Aɴᴅ Sᴇɴᴅ Lɪɴᴋꜱ.Dᴇꜰᴀᴜʟᴛ Iꜱ 1
"""

CMD = "(discudemy|coursevania|udemy_freebies|tutorialbar|real_discount|idcoupons)"
