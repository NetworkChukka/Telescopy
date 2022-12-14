strings = {'ru': {'start': 'Приветствую, {}!\nЯ Telescopy и я умею преобразовывать квадратные Видео в круглые'
                           ' <i>Видеосообщения</i>, просто отправь мне медиафайл.\n\n'
                           'Используй команду /help если у тебя есть вопросы.',
                  'error': 'Ой, что-то пошло не так, попробуй другой файл',
                  'content_error': 'Я поддерживаю только квадратные Видео! (не GIF)',
                  'text_handler': 'Отправь мне квадратное Видео',
                  'video_note_handler': 'Это и так <i>Видеосообщение!</i>',
                  'size_handler': 'Файл слишком большой!\nМаксимальный размер файла *8 MB!*',
                  'dimensions_handler': 'Слишком большой ролик! Telegram поддерживает квадратные видео размером ДО 640x640px (качество 360p)',
                  'duration_handler': 'Максимальная продолжительность видео 60 секунд!',
                  'converting': '<i>Конвертирую</i> <code>{0:.2f}%</code>',
                  'downloading': '<i>Скачиваю файл...</i>',
                  'uploading': '<i>Колдую...</i>',
                  'webm': 'WebM формат пока не поддерживается 😓',
                  'help': '<a href="http://telegra.ph/Telescopy-FAQ-Ru-05-21-3">FAQ</a>',
                  'not_square': 'Это видео не квадратное (соотношение сторон 1:1)!'},
           'en': {'start': 'Greetings, {}!\nI am Telescopy and i can convert your square Video to a round'
                           ' <i>Video Message</i>, just send me your media.\n\n'
                           'Use /help command if you have any questions.',
                  'error': 'Ooops, something went wrong, try another file',
                  'content_error': 'I support only square Videos! (not GIFs)',
                  'text_handler': 'Send me square Video',
                  'video_note_handler': "It's already a <i>Video message!</i>",
                  'size_handler': 'File is too big!\nMaximum file size is *8 MB*',
                  'dimensions_handler': 'File is too big! Telegram supports square videos up to 640x640px (360p quality)',
                  'duration_handler': 'The maximum video duration is 60 seconds!',
                  'converting': '<i>Converting</i> <code>{0:.2f}%</code>',
                  'downloading': '<i>Downloading file...</i>',
                  'uploading': '<i>Doing some magic stuff...</i>',
                  'webm': 'WebMs are currently unsupported 😓',
                  'help': '<a href="http://telegra.ph/Telescopy-FAQ-En-05-21-2">FAQ</a>',
                  'not_square': "It's not a square video (1:1 Aspect ratio)!"},
           'de': {'start': 'Hallo, {}!\n Ich bin Telescopy und ich kann dein quadratisches Video zu einer runden'
                           ' <i>Videonachricht</i> konvertieren. Sende mir einfach deine Medien.\n\n'
                           'Benutze einfach /help, wenn du irgendwelche Fragen hast.',
                  'error': 'Ooops, irgendwas ist schief gelaufen, probier eine andere Datei',
                  'content_error': 'Ich unterstütze nur quadratische Videos! (keine GIFs)',
                  'text_handler': 'Sende mir ein quadratisches Video',
                  'video_note_handler': "Es ist schon eine <i>Videonachricht!</i>",
                  'size_handler': 'Die Datei ist zu groß!\nDie Maximumgröße ist *8 MB*',
                  'dimensions_handler': 'Die Datei ist zu groß! Telegram unterstützt quadratische Videos bis zu 640x640px (360p-Qualität)',
                  'duration_handler': 'Die maximale Videodauer beträgt 60 Sekunden!',
                  'converting': '<i>Konvertiere</i> <code>{0:.2f}%</code>',
                  'downloading': '<i>Downloade die Datei...</i>',
                  'uploading': '<i>Mache magische Sachen...</i>',
                  'webm': 'WebMs sind aktuell nicht unterstützt 😓',
                  'help': '<a href="http://telegra.ph/Telescopy-FAQ-En-05-21-2">FAQ</a>',
                  'not_square': "Es ist kein quadratisches Video (1:1 Aspect ratio)!"},
           'tr': {'start': 'Merhaba, {}!\nBen Telescopy ve kare videonu yuvarlak'
                           ' <i>Video Mesaja</i> dönüştürebilirim, sadece medyanı gönder.\n\n'
                           'Herhangi bir sorun varsa, /help komutunu kullan.',
                  'error': 'Ups, bir şeyler ters gitti, başka bir doya dene',
                  'content_error': 'Sadece kare Videoları destekliyorum! (GIF değil)',
                  'text_handler': 'Bana kare Video gönder',
                  'video_note_handler': "Bu zaten bir <i>Video mesaj!</i>",
                  'size_handler': 'Dosya çok büyük!\nMaksimum dosya boyutu *8 MB*',
                  'dimensions_handler': 'Dosya çok büyük! Telegram, 640x640 piksele (360p kalite) kadar kare videoları destekler',
                  'duration_handler': 'Maksimum video süresi 60 saniyedir!',
                  'converting': '<i>Dönüştürülüyor</i> <code>{0:.2f}%</code>',
                  'downloading': '<i>Dosya indiriliyor...</i>',
                  'uploading': '<i>Birkaç sihirli şey yapılıyor...</i>',
                  'webm': 'WebM şu anda desteklenmiyor 😓',
                  'help': '<a href="https://telegra.ph/Telescopy-FAQ-TR-10-06">SSS</a>',
                  'not_square': "Bu kare video (1:1 en-boy oranı) değil!"},
           'ar': {'start': """تحية طيبة، {}!
أنا تلسكوبي ويمكنني تحويل الفيديو الخاص بك مربع إلى <i> رسالة فيديو </i> ، فقط أرسل لي وسائل الإعلام الخاصة بك.

استخدم /help الأمر إذا كان لديك أي أسئلة.""",
                  'error': 'عفوًا ، حدث خطأ ما ، جرب ملفًا آخر',
                  'content_error': 'أنا أدعم فقط أشرطة الفيديو مربع! (لا صور GIF)',
                  'text_handler': 'أرسل لي مربع الفيديو',
                  'video_note_handler': "إنها بالفعل <i>رسالة فيديو</i> !",
                  'size_handler': 'الملف كبير جدًا! \n أقصى حجم للملف هو * 8 ميغابايت *',
                  'dimensions_handler': 'الملف كبير جدًا! يدعم Telegram مقاطع الفيديو المربعة حتى 640×640 بكسل (جودة 360 بكسل)',
                  'duration_handler': 'الحد الأقصى لمدة الفيديو 60 ثانية!',
                  'converting': '<i>Converting</i> <code>{0:.2f}%</code>',
                  'downloading': '<i>Downloading file...</i>',
                  'uploading': '<i>Doing some magic stuff...</i>',
                  'webm': 'WebMs غير مدعومة حاليا 😓',
                  'help': '<a href="http://telegra.ph/Telescopy-FAQ-En-05-21-2">FAQ</a>',
                  'not_square': "انها ليست فيديو مربع (1: 1 نسبة الارتفاع)!"},
           'fa': {'start': """با درود، {}!
من تلسکوپی هستم و می توانم ویدیوی مربع شما را به یک دور <i> پیام ویدیویی </i> تبدیل کنم، فقط رسانه های خود را بفرستید

اگر سوالی دارید، از دستور /help استفاده کنید.""",
                  'error': 'اووپ، چیزی اشتباه گرفته شد، فایل دیگری را امتحان کنید',
                  'content_error': 'من فقط از فیلم های مربع پشتیبانی می کنم! (نه GIF)',
                  'text_handler': 'مربع ویدئو را به من بفرست',
                  'video_note_handler': "این یک پیام <i> ویدیویی است! </i>",
                  'size_handler': 'پرونده خیلی بزرگ است!\nحداکثر اندازه فایل* 8 MB است*',
                  'dimensions_handler': 'پرونده خیلی بزرگ است! تلگرام از فیلم های مربعی تا 640x640px (کیفیت 360p) پشتیبانی می کند',
                  'duration_handler': 'حداکثر مدت زمان فیلم 60 ثانیه است!',
                  'converting': '<i>Converting</i> <code>{0:.2f}%</code>',
                  'downloading': '<i>Downloading file...</i>',
                  'uploading': '<i>Doing some magic stuff...</i>',
                  'webm': 'WebMs در حال حاضر پشتیبانی نشده 😓',
                  'help': '<a href="http://telegra.ph/Telescopy-FAQ-En-05-21-2">FAQ</a>',
                  'not_square': "این ویدیو مربعی نیست (نسبت تصویر 1: 1)!"}}
