 #!/usr/bin/python

 # начинаем скрипт с переменных конфигурации

 source_folder = ' ' # каталог с html-файлами внутри которых есть линки вида img.auctiva.com/imgdata/8/4/0/3/3/0/webimg/815355468_o.gif
 image_folder = ' '  # каталог куда надо скачать картинки со всей вложеностью подкаталогов imgdata/8/4/0/3/3/0/webimg/815355468_o.gif по линкам из файлов
 newsite_name = ' '  # имя сайта, на которое надо поменять img.auctiva.com в коде файлов в goal_folder
 goal_folder = ' '   # каталог с файлами-копиями из source_folder, но с измененными линками с img.auctiva.com на newsite_name, файлы в source_folder не меняем