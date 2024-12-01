<b><h1>Лабораторная работа №5</h1></b>

<b><h3>Базовое задание:</h3></b>
Сделать мониторинг сервиса, поднятого в кубере (использовать, например, prometheus и grafana). Показать хотя бы два рабочих графика, которые будут отражать состояние системы. Приложить скриншоты всего процесса настройки.

<b><h3>Выполнение:</h3></b>
<h4>Установка необходимых инструментов для работы</h4>
<ol>
  <li>Запускаем консоль с правами администратора (иначе ничерта не заработает и не установится)</li>
  <li>Установка chocolatey</li> 
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-1.jpg" alt="1-1" title="title size:70%">

  <li>Перезапуск консоли - о святая перезагрузочка</li>

  <li>choco --version, показывает версию - значит всё гут</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-2.jpg" alt="1-2" title="title">

  <li>Успешная установка minikube</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-3.jpg" alt="1-3" title="title">
  
  <li>Установка helm - и вполне себе успешная</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-4.jpg" alt="1-4" title="title">
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-5.jpg" alt="1-5" title="title">
    
  <li>Запуск minikube и проверка статуса кластера</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-6.jpg" alt="1-6" title="title">
 
  <li>Добавление репозитория с чарта Prometheus</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-7.jpg" alt="1-7" title="title">
  

  <li>Установка Prometheus</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-8.jpg" alt="1-8" title="title">
 
  <li>Добавление репозитория с чарта Grafana</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-9.jpg" alt="1-9" title="title">
  
   <li>Установка Grafana</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-11.jpg" alt="1-11" title="title">
  
   <li>Обновляем репу</li>
  <img src="https://github.com/elyaroman/cloud-systems-and-technologies/blob/main/lab%205/images/basic/1-10.jpg" alt="1-10" title="title">  
</ol>

<h4>Grafana-nananana</h4>
<ol>
  <li>Используем утилиту certutil, которая доступна по умолчанию в Windows, чтоб выкрасть пароль как истинные хацкеры</li>
  <img src="" alt="1-4" title="title"> скрин 1
  <li>Меняем пароль для простоты ввода</li>
  <img src="" alt="1-4" title="title">   скрин 3.1
  <li>Перенаправляем локальный порт 3000 на порт 80 сервиса Grafana</li>
   <img src="" alt="1-4" title="title">  скрин 2
  <li>Теперь по урле http://localhost:3000 доступна графана</li>
   <img src="" alt="1-4" title="title">  скрин 3
  <li>Вводим логин-пароль - все гут</li>
  <img src="" alt="1-4" title="title">   скрин 5
  <li>Алиллуя господи запустилось</li>
  <img src="" alt="1-4" title="title">   скрин 6
  <li>Добавляем источник данных</li>
  <img src="" alt="1-4" title="title">   скрин 7
  <li>В настройках указываем ур<s>су</s>лу http://prometheus-server.default.svc.cluster.local</li>
  <img src="" alt="1-4" title="title">   скрин 8
  <li>Затем сохранили - добавляем визуализацию</li>
  <img src="" alt="1-4" title="title">   скрин 9
  <li>Метрика etcd_request_duration_seconds_count показывает общее кол-во запросов, выполненных к etcd - система хранения всяких конфиг-данных, что позволяет оценить общую нагрузку на систему</li>
  <img src="" alt="1-4" title="title">   скрин 10
  <li>Метрика authorization_duration_seconds_sum показывает сколько тратит пользователь на авторизацию</li>
  <img src="" alt="1-4" title="title">   скрин 11
</ol>
