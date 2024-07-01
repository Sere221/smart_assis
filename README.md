# Голосовой помощник

**Библиотеки:**

- `speech_recognition`: используется для распознавания речи.
- `webbrowser`: позволяет работать с браузером.
- `pyttsx3`: преобразует текст в речь.
- `anecAPI`: предоставляет доступ к базе данных анекдотов.
- `yaml`: упрощает работу с YAML-файлами, позволяя удобно создавать словарь команд или ответов.
- `openai`: это API, которое позволяет использовать ChatGPT. Для этого необходим специальный ключ от chat_gpt.

**Функции и ключевые переменные**

* `CMD_LIST` — это список команд, хранящийся в файле commands.yaml.
* `ANS_LIST` — это список ответов, хранящийся в файле answers.yaml.
* `talk` — это функция, которая преобразует ответ помощника.
* `generate_response` — это функция для работы с GPT, которая принимает на вход текст, которого нет в CMD_LIST.
* `command` — это функция для подслушивания команд.
* `makeSomething` — это функция для работы с голосовым помощником, где можно развивать функционал бесконечно.

## Кратко как получить `KEY`

Если не работают санкции до можно зарегестрироваться на прямую https://openai.com/

А остальном случае надо покупать KEY через стороников которые продают аккаунты
