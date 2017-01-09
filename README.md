# stepic_web_tehnology

git clone https://github.com/takinado/stepic_web_tehnology.git /home/box/web

bash /home/box/web/init.sh

1.8.12

Отдача статических файлов

1) Установите Web-сервер nginx

2) В директории /home/box (домашняя директория) создайте следующую структуру директорий

/home/box/web
          |---public
          |   |---img
          |   |---css
          |   |---js
          |---uploads
          |---etc

3) Настройте nginx так что бы:

    Все URL, начинающиеся с /uploads/  (например /uploads/1.jpeg) отдавались из директории /home/box/web/uploads
    Все URL с расширением (например /img/1.jpeg) отдавались из директории /home/box/web/public
    Все URL без расширения (например /question/123)  возвращали HTTP 404

4) Фрагмент конфига nginx который обслуживает ваш проект должен находиться в файле /home/box/web/etc/nginx.conf и должен быть включен в основной конфиг с помощью символической ссылки.

5) Запустите nginx, так что бы он принимал запросы на порту 80 и обслуживал бы любые домены.

6) Не забудьте закомитить и сохранить на github полученную структуру директорий и конфиги.
