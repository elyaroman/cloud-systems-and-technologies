<b><h1>Лабораторная работа №5</h1></b>

<b><h3>Базовое задание:</h3></b>
Сделать мониторинг сервиса, поднятого в кубере (использовать, например, prometheus и grafana). Показать хотя бы два рабочих графика, которые будут отражать состояние системы. Приложить скриншоты всего процесса настройки.

<b><h3>Выполнение:</h3></b>
<h4>Установка необходимых инструментов для работы</h4>
<ol>
  <li>Запускаем консоль с правами администратора (иначе ничерта не заработает и не установится)</li>
  <li>Установка chocolatey</li> 
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-1.jpg" alt="1-1" title="title">
  <li>Перезапуск консоли - о святая перезагрузочка</li>
  <li>choco --version, показывает версию - значит всё гут</li>
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-2.jpg
  <li>Успешная установка minikube</li>
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-3.jpg
  <li>Установка helm - и вполне себе успешная</li>
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-4.jpg
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-5.jpg
  <li>Запуск minikube и проверка статуса кластера</li>
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-6.jpg
  <li>Добавление репозитория с чарта Prometheus</li>
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-7.jpg
  <li>Установка Prometheus</li>
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-8.jpg
  <li>Добавление репозитория с чарта Grafana</li>
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-9.jpg
   <li>Установка Grafana</li>
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-11.jpg
   <li>Обновляем репу</li>
  https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-10.jpg
</ol>

<h4>Grafana-nananana</h4>
<ol>
  <li>Используем утилиту certutil, которая доступна по умолчанию в Windows, чтоб выкрасть пароль как истинные хацкеры</li>
  скрин 1
  <li>Меняем пароль для простоты ввода</li>
  скрин 3.1
  <li>Перенаправляем локальный порт 3000 на порт 80 сервиса Grafana</li>
  скрин 2
  <li>Теперь по урле http://localhost:3000 доступна графана</li>
  скрин 3
  <li>Вводим логин-пароль - все гут</li>
  скрин 5
  <li>Алиллуя господи запустилось</li>
  скрин 6
  <li>Добавляем источник данных</li>
  скрин 7
  <li>В настройках указываем ур<s>су</s>лу http://prometheus-server.default.svc.cluster.local</li>
  скрин 8
  <li>Затем сохранили - добавляем визуализацию</li>
  скрин 9
  <li>Метрика etcd_request_duration_seconds_count показывает общее кол-во запросов, выполненных к etcd - система хранения всяких конфиг-данных, что позволяет оценить общую нагрузку на систему</li>
  скрин 10
  <li>Метрика authorization_duration_seconds_sum показывает сколько тратит пользователь на авторизацию</li>
  скрин 11
</ol>
