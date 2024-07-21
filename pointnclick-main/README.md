# Point & Click

## Team
* **Горбатенко Алёна Юрьевна** - TL, Frontend
* **Малкова Марина Артемьевна** - Artist
* **Грядунов Артемий Павлович** - Backend

***

### Описание
Данный проект - сайт интерактивных комиксов с возможностью выбора вариантов развития сюжета. Создан с помощью языка программирования `python` и фреймворка для веб-приложений `django`.

### Запуск
Советуем обновить pip и apt командами `pip install --upgrade pip`, `sudo apt-get update`

1. Переходим в папку для проекта, создаем и запускаем виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```
> Возможно потребуется установить `venv` командой `sudo apt install -y python3-venv`

2. Устанавливаем фреймворк `django`:
```
pip install django
```
3. Далее клонируем git репозиторий:
```
git clone https://gitlab.informatics.ru/2022-2023/vk/s103/pointnclick.git
```
4. Переходим в папку с проектом и запускаем сервер:
```
cd pointnclick/thingy/projectik___
python manage.py runserver
```