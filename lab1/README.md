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

### Самоподписанные сертификаты OpenSSL
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

### Перенаправление HTTP-запросов на HTTPS
  
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

### Псведонимы alias

Последним был использован alias для создания псевдонимов путей к папке со стилями к проектам. Для этого достаточно ввести, например, следующее:
```
location /css {
  alias C:/tryn/nginx-1.26.2/html/techzone-catalog.com/css;
}	
```
### Результаты

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

Теперь, если ввести sminex-news.com в браузер, можно увидеть, что происходит перенаправление с http на https и сайт отображается как надо:

![sminex-news.com](screenshots/sminex-news.png)
Аналогично и со вторым доменом techzone-catalog.com:

![techzone-catalog.com](screenshots/techzone-catalog.png)

Ура ура :)

# Лабораторная 1. Со звёздочкой

## Цель
Необходимо проверить на уязвимости (минимум 3) nginx другой команды, например, path traversal, перебор страниц через ffuf и/или любые другие на ваш выбор. Взлом считается успешным, если вы попали туда, куда не планировалось попадать пользователю, даже если там ничего нет. Успешность взлома не влияет на оценку лаб обеих команд. 

## Ход работы
### Заголовки безопасности
Настройка заголовков безопасности в nginx является необходимой для повышения безопасности сайта. Заголовки безопасности защищают против различного вида атак, таких как, cross site scripting (межсайтовый скриптинг, XSS), clickjacking (захват клика) и других. Они говорят браузеру, как работать с контентом на странице, создавая дополнительный уровень безопасности. Ниже представлены некоторые из них:

*X-XSS-Protection*: заголовок, который обеспечивает запрет выполнения встроенного JavaScript-кода в браузерах без поддержки политики безопасности контента (Content Security Policy). Для настройки заголовка в конфигурационный файл необходимо добавить следующее:

```add_header X-XSS-Protection "1; mode=block";```

*HTTP Strict Transport Security*: для сайтов, работающих по протоколу HTTPS, рекомендуется указывать заголовок ответа HSTS для принудительного перенаправления страниц с HTTP на HTTPS. Для настройки заголовка в конфигурационный файл необходимо добавить следующее:

```add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains; preload';```

*X-Content-Type-Options*: отправка заголовка ответа со значением nosniff не позволит браузеру анализировать MIME ответ, отличный от объявленного типа содержимого. Директива nosniff применяется только к типам script и style. Для настройки заголовка в конфигурационный файл необходимо добавить следующее:

```aadd_header X-Content-Type-Options nosniff;```

В представленном командой конфигурационном файле не было добавлено никаких заголовков безопасности, соотвественно, он может быть уязвим к атакам.

### Path Traversal 
Уязвимость обхода пути (Path Traversal) позволяет злоумышленникам обходить приложение для доступа к ограниченным файлам/каталогам сервера. Используя эту уязвимость, злоумышленник может получить доступ к коду, учетным данным внутренних серверов, файлам/библиотекам операционной системы и т.д. В OWASP Top 10 2022 данная уязвимость входит в раздел A1: Broken Access Control. 94 процента веб-приложений в той или иной форме имеют нарушенный контроль доступа, как отмечает OWASP.

Данная проблема проявляется только в конфигурациях с директивой "alias", размещённой внутри блока "location", параметр которой не завершается на символ "/". Директива alias должна быть указана внутри location и должна заканчиваться косой чертой. В представленном конфигурационном файле как раз можно наблюдать неправильно сконфигурированный alias:

```
#неправильно
location /styles {
  alias D:/nginx-1.27.2/html/styles;  
}

#правильно
location /styles/ {
  alias D:/nginx-1.27.2/html/styles;  
}
```
### 



## Список полезных источников
1. https://levashove.ru/install-nginx-server-windows
2. https://trueconf.ru/blog/baza-znaniy/kak-sgenerirovat-samopodpisannyj-sertifikat
3. https://wiki.merionet.ru/articles/kak-nastroit-redirekt-s-http-na-https-v-nginx
4. https://www.youtube.com/watch?v=yjZPP-wQZlo&t=8s&ab_channel=RyudithTutorial
5. https://www.youtube.com/watch?v=8P2r0xSXk28&ab_channel=TonyTeachesTech
6. https://linuxcapable.com/how-to-configure-security-headers-in-nginx/
7. https://blog.dubkov.org/learn/secure/security-headers-for-nginx/
8. https://habr.com/ru/articles/745718/
