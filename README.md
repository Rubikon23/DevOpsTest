# devops-flask-test

# Реализация 1-ой части задания:
Dockerfile создан

# Реализация 2-ой части задания:
Мониторинг реализован на Zabbix, включающий в себя 3 контейнера - Zabbix сервер, Zabbix web и сервер БД
В файле docker-compose описанна установка 3 контейнеров Zabbix и контейнера с приложением Flask. Образы для установки скачиваются с личного репозитория на docker hub.
Снятие и отправка метрик реализована на python скрипте, который опрашивает Flask каждую секунду. В скрипте реализован расчет количества новых пользователей за секунду. Запуск скрипта реализован через cron в контейнере Flask. Отправка метрик реализована через Zabbix trap. Zabbix доступен по порту 8080


# Реализация 3-ей части задания:
В Zabbix создан шаблон и узел сети, для которого отправляются значения. Создан график, размещен на основном дашборде.

![Item](https://user-images.githubusercontent.com/51418727/110631640-ca6be900-81b7-11eb-8278-7db9a65cf703.jpg)
![график](https://user-images.githubusercontent.com/51418727/110636539-6ba96e00-81bd-11eb-81ed-8def8d7f506b.jpg)




# Реализация 4-ой части задания:
На скриншоте показан вывод Apache bench и график

![AB](https://user-images.githubusercontent.com/51418727/110636556-7237e580-81bd-11eb-978f-34b7da7228c8.jpg)
![график](https://user-images.githubusercontent.com/51418727/110636539-6ba96e00-81bd-11eb-81ed-8def8d7f506b.jpg)


Не реализованно:
При разворачивании через файл docker-compose, происходит установка "чистого" Zabbix. Для реализации установки настроенной системы, необходимо монтировать БД во внешнее хранилище
