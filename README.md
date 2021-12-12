Kullanım için gerekli hususlar:

1) Bot gönderim sıklığını değiştirmek için bot.py > "scheduler.add_job(jobs, "interval", hours=24)" kısmında hours yerine minutes, days, years ve benzeri zaman kavramlarını ekleyin.
2) Konfigürasyon için bot.py > Client() nesnesinde api_id, api_hash, bot_token ve session_name değerlerini güncelleyin.
3) bot.py > jobs() fonksiyonunda "app.send_message()" kısmında mesaj göndermek istediğiniz kanal/grup/kişi id'sini yazmalısınız. (@username_to_id_bot)

doviz.py dosyası, https://github.com/tayfunulu/DovizKurlari adresinden alınmıştır.

Bot hakkında daha fazla doküman için: https://docs.pyrogram.org/
