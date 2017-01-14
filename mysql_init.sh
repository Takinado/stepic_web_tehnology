sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE web CHARACTER SET utf8 COLLATE utf8_general_ci;"
#mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON web.* TO 'root'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
sudo /etc/init.d/mysql restart 
python /home/box/web/ask/manage.py collectstatic
python /home/box/web/ask/manage.py syncdb
#echo ''
#echo 'Launch "python /home/box/web/ask/manage.py syncdb" manualy'
#echo ''
