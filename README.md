# DevOpsTest

# Реализация 1-ой части задания:
Dockerfile создан

# Реализация 2-ой части задания:
Мониторинг реализован на Zabbix, включающий в себя 3 контейнера - Zabbix сервер, Zabbix web и сервер БД
В файле docker-compose описанна установка 3 контейнеров заббикс и контейнера с приложением Flask. Образы для установки скачиваются с личного репозитория на docker hub.
Снятие и отправка метрик реализованна на python скрипте, который запускается каждые 15 сукенд через cron в контейнере Flask. Отправка метрик реализованна через Zabbix trap.

# Реализация 3-ой части задания:
В Zabbix создан шаблон и узел сети для которого отправляются значения. Создан график, размещен на основном дашборде.

![Item](https://user-images.githubusercontent.com/51418727/110631640-ca6be900-81b7-11eb-8278-7db9a65cf703.jpg)
![график](https://user-images.githubusercontent.com/51418727/110631642-cb047f80-81b7-11eb-89ec-5072cf543645.jpg)



# Реализация 4-ой части задания:
На скриншоте показан вывод Apache bench и график

![AB](https://user-images.githubusercontent.com/51418727/110631870-0d2dc100-81b8-11eb-8f41-3b1700791bf4.jpg)
![график](https://user-images.githubusercontent.com/51418727/110631874-0e5eee00-81b8-11eb-9455-537ba21c4bba.jpg)

Не реализованно:
При разворачивании через файл docker-compose, происходит установка "чистого" Zabbix. Для реализации установки настроенной системы, необходимо монтировать БД во внешнее хранилище
