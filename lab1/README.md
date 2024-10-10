# Лабораторная 1. 

## Требования к настройке nginx:
1. Работает по https c сертификатом.
2. Настроено принудительное перенаправление HTTP-запросов (порт 80) на HTTPS (порт 443) для обеспечения безопасного соединения.
3. Использован alias для создания псевдонимов путей к файлам или каталогам на сервере.
4. Настроены виртуальные хосты для обслуживания нескольких доменных имен на одном сервере.

## Результат: 
Предположим, что у вас есть два пет проекта на одном сервере, которые должны быть доступны по https. Настроенный вами веб сервер умеет работать по https, относить нужный запрос к нужному проекту, переопределять пути исходя из требований пет проектов.

## Ход работы:
Был установлен веб-сервер nginx версии 1.26.2, последней на данный момент. Для этого был скачан и извлечён архив с программой.

Далее были сгенерированы самоподписанные сертификаты с помощью программы OpenSSL. Так как программа уже была установлена на данный ПК, то настривать её не пришлось. Для удобства в папке с извлечённым архивом была создна папка ssl. Для создания серфиката и ключа было достаточно перейти в данную папку с помощью командной строки и задать следующую команду:
```
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout privateKey.key -out certificate.crt
```
где:
- x509 — уточнение, что нужен именно самоподписанный сертификат;
- newkey — автоматическое создание ключа сертификата;
- days — срок действия сертификата в днях;
- keyout — путь (если указан) и имя файла ключа;
- out —  путь (если указан) и имя файла сертификата.

Далее были введены требуемые от нас код страны, её название, город, название компании,
название отдела, FQDN сервера или имя и адрес электронной почты ~~(которые нигде не пригодились)~~. В итоге, теперь в папке ssl есть privateKey.key в качестве ключа и certificate.crt — сертификата. Чтобы защитить сертификатом виртуальные хосты, были написаны следующие строки: 
```
server {
  listen              443 ssl;
  server_name         [domain.com];

  ssl_certificate     C:/tryn/nginx-1.26.2/ssl/certificate.crt; 
  ssl_certificate_key C:/tryn/nginx-1.26.2/ssl/privateKey.key;
}
```
где:
- listen: через какой порт будет прослушиваться трафик;
- server_name: имя домена;
- ssl_certificate: путь до созданного файла с сертификатом;
- ssl_certificate_key: путь до файла с приватным ключом.
  
Следующим был настроен редирект с незашифрованного веб-трафика HTTP на зашифрованный HTTPS. Для этого в файле конфигурации Nginx было написаны следующие команды:
```
server {
  listen        80;
  server_name   sminex-news.com techzone-catalog.com;
  return 301    https://$host$request_uri;
}
```
где:
- listen 80: через какой порт система будет перехватывать весь HTTP-трафик;
- server_name: имена необходимых доменов;
- return 301: показатель постоянного перенаправления;
- https://$host$request_uri: указание версии HTTPS того, что набрал пользователь.

Последним был использован alias для создания псевдонимов путей к папке со стилями к проектам. Для этого достаточно ввести, например, следующее:
```
location /css {
  alias C:/tryn/nginx-1.26.2/html/techzone-catalog.com/css;
}	
```
Итоговый конфигурационный файл выглядит следующим образом:
```
http {
  server {
    listen        80;
    server_name   sminex-news.com techzone-catalog.com;
    return 301    https://$host$request_uri;
  }

  server {
    listen        443 ssl;
    server_name   sminex-news.com;

    ssl_certificate       C:/tryn/nginx-1.26.2/ssl/certificate.crt;
    ssl_certificate_key   C:/tryn/nginx-1.26.2/ssl/privateKey.key;

  location / {
    root   C:/tryn/nginx-1.26.2/html/sminex-news.com;
    index  index.html;
  }

  location /css {
    alias C:/tryn/nginx-1.26.2/html/sminex-news.com/css;
    }
  }

  server {
    listen       443 ssl;
    server_name  techzone-catalog.com;

    ssl_certificate       C:/tryn/nginx-1.26.2/ssl/certificate.crt;
    ssl_certificate_key   C:/tryn/nginx-1.26.2/ssl/privateKey.key;

    location / {
      root   C:/tryn/nginx-1.26.2/html/techzone-catalog.com;
      index  index.html;
    }

    location /css {
      alias C:/tryn/nginx-1.26.2/html/techzone-catalog.com/css;
    }
  }
}
```

Итого, если ввести sminex-news.com в браузер, можно увидеть, что происходит перенаправление с http на https и сайт отображается как надо:

![sminex-news.com](screenshots/sminex-news.png)
Аналогично и со вторым доменом techzone-catalog.com:

![techzone-catalog.com](screenshots/techzone-catalog.png)

Ура ура :)

## Список полезных источников
1. https://levashove.ru/install-nginx-server-windows
2. https://trueconf.ru/blog/baza-znaniy/kak-sgenerirovat-samopodpisannyj-sertifikat
3. https://wiki.merionet.ru/articles/kak-nastroit-redirekt-s-http-na-https-v-nginx
4. https://www.youtube.com/watch?v=yjZPP-wQZlo&t=8s&ab_channel=RyudithTutorial
5. https://www.youtube.com/watch?v=8P2r0xSXk28&ab_channel=TonyTeachesTech
