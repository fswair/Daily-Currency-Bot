import pyrogram
import tgcrypto
import time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import *
from pyrogram import Client, filters
from doviz import *
from datetime import datetime as d

def pattern():
    job = DovizKurlari()
    usd = job.DegerSor()['USD']['ForexSelling']
    eur = job.DegerSor()['EUR']['ForexSelling']
    gbp = job.DegerSor()['GBP']['ForexSelling']
    dx = d.now().today()
    dy = d.now()
    weekend = dy.strftime("%A") in ["Saturday", "Sunday"]
    date = {"day": dx.day, "month":dx.month, "year": dx.year, "hour":dx.hour, "minute": dx.minute}
    months = ["", "Ocak", "Şubat", "Mart", "Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül", "Ekim", "Kasım", "Aralık"]
    datePattern = f'Bugün, {date["day"]} {months[date["month"]]} {date["year"]}\n\n🇺🇸 USD/TRY: {usd}\n\n🇪🇺 EUR/TRY: {eur}\n\n🇬🇧 GBP/TRY: {gbp}\n\nKaynak: https://bit.ly/3Gfr4Ea' if not weekend else "Haftasonu nedeniyle kapalıyız!"
    return datePattern

job = DovizKurlari()
usd = job.DegerSor()['USD']['ForexSelling']
eur = job.DegerSor()['EUR']['ForexSelling']
gbp = job.DegerSor()['GBP']['ForexSelling']

app = Client(session_name="session_name", api_id=123456789, api_hash="api_hash", bot_token="bot_token")

def jobs():
    app.send_photo(chat_id=-123456,photo="dolar.jpg",caption=pattern())

scheduler = AsyncIOScheduler(timezone="Europe/Istanbul")
scheduler.add_job(jobs, "interval", hours=24)

scheduler.start()
app.run()