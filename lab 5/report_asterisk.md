<b><h1>Лабораторная работа №5</h1></b>

<b><h3>Сложное задание:</h3></b>
Настроить алерт кодом IaaC (например через конфиг алертменеджера, главное - не в интерфейсе графаны:), показать пример его срабатывания. Попробовать сделать так, чтобы он приходил, например, на почту или в телеграм. Если не получится - показать имеющийся результат и аргументировать, почему дальше невозможно реализовать. <i>спойлер: у нас все получилось!</i>

<b><h3>Выполнение:</h3></b>
<ol>
  <li>С помощью BotFather создан тг-бот</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/asterisk/1.jpg" alt="1" title="title" style="width: 70%"> 
  
  <li>Создан новый Helm Chart</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/asterisk/2.jpg" alt="2" title="title">
  
  <li>Изменены файлы deployment.yaml и service.yaml</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/asterisk/3.jpg" alt="3" title="title" style="width: 50%"> 

  <i>Файлы, собственно, прилагаются:</i>
  
  service.yaml
  ```
  apiVersion: v1
  kind: Service
  metadata:
    name: {{ .Release.Name }}-nginx-service
  spec:
    selector:
      app: nginx
    ports:
    - protocol: TCP
      port: 80
      targetPort: 80
    type: NodePort
  ```

  deployment.yaml
  ```
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: {{ .Release.Name }}-nginx
  spec:
    replicas: 2
    selector:
      matchLabels:
        app: nginx
    template:
      metadata:
        labels:
          app: nginx
      spec:
        containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
          - containerPort: 80
  ```
  
  <li>Устанавливаем Helm Chart в кластере кубера</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/asterisk/4.jpg" alt="4" title="title">
  
  <li>выкраден токен для тг-бота из FATHERRR, также выкраден id_chat из конфига по ссылке <a href="">https://api.telegram.org/bot<i>Секреееет</i>/getUpdates</a> (в данном случае это id пользователя)</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/asterisk/6.jpg" alt="6" title="title">
  
  <li>о боги девопса, заработало! апгрейднули кофниг и всё, теперь работает...</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/asterisk/5.jpg" alt="5" title="title">

  а вот и коФНиг (честно, это очепятка, но так прикольнее звучит...)

  alert.yaml
  ```
  alertmanager:
  config:
    global:
      resolve_timeout: 1m
      telegram_api_url: "https://api.telegram.org"

    route:
      receiver: telegram

    receivers:
      - name: telegram
        telegram_configs:
          - chat_id: секрееет 
            bot_token: секрееет
            api_url: "https://api.telegram.org"
            send_resolved: true
            parse_mode: Markdown
            message: |-
              {{ range .Alerts }}
                ❗ *Alert:* {{ .Annotations.summary }}
                📝 *Description:* {{ .Annotations.description }}
              {{ end }}

serverFiles:
  alerting_rules.yml:
    groups:
      - name: nginx-alerts
        rules:
          - alert: NginxDown
            expr: absent(up{job="kubernetes-pods", app="nginx"} == 1)
            for: 1m
            labels:
              severity: critical
            annotations:
              summary: "nginx died sorry"
              description: "nginx died sorry"
  ```
  
  <li>показало сообщение о том что <s>бобик</s> NGINX сдох</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/asterisk/7.jpg" alt="7" title="title">
  
  <li>в алертманагере тоже показало, что NGINX сдох</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/asterisk/8.jpg" alt="8" title="title">

  <b><h3>Выводы</h3></b>
  Эта лаба тоже убила очень много сил. К сожалению. Очень трудно было разбираться, как создавать телеграм-бота, так как ранее не было опыта. Хорошо, что хороший способ нашелся. Искать chat_id тоже стало испытанием. Благо, с этой лабой теперь можно и бота сделать будет при огромном желании. Насчет алертменеджера, хочется сказать, что в целом полезная вещь, если нужен мониторинг сети 24/7, чтоб знать, когда что-то <i>(например, бобик)</i> умерло или легло. Кстати, тот кот из базового отчёта сюда тоже вполне подходит.
