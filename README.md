# web_arch
Сервис петиций. Хранилище петиций с возможностью просмотра, добавления и голосования. Пользователь может просмотреть список петиций, проголосовать за или против, увидеть состояние петиции. Петиция состоит из названия, текста петиции, даты создания, даты окончания голосования. числа проголосовавших.

Выбран REST подход.

1)**Получение списка петиций.**
Возвращает список петиций.
**REQ:  GET /petition
RESP:  200 Content-Type: application/vnd.petitions.list+json**
```json
{
	"links": {
		"self": "/petition"
	},
	"petitions": [{
			"title": "petition title",
			"links": {
				"self": "/petition/123"
			}
		}
	]
}
```

2)**Получение петиции по id.**
Возвращает заголовок и текст петиции, а так же даты создания и окончания сбора подписей
**REQ:  GET /petition/{id}
RESP:  200 Content-Type: application/vnd.petition+json**
```json
{
	"title": "petition title",
	"text": "petition text",
	"creation_date": "20/10/2010",
	"expiry_date": "20/11/2010",
	"links": {
		"self": "/petition/123",
		"vote": "/petition/123/vote"
	}
}
```

3)**Добавление своей загадки.**
Принимает текст загадки, возможные ответы и верный ответ. Возвращает ссылку на созданную загадку.
**REQ: POST /petition
RESP:  201 Location: /petition/{id}**
```json
{
	"title": "petition title",
	"text": "petition text",
	"expiry_date": "expiry date"
}
```

4)**Проголосовать.** 
Если согласен в петицией, то choice = true, сл ине согласен -- choice = false. Возвращает заголовок петиции в поле title, дату окончания сбора подписей в поле expiry_date, количество согласных с петицией в поле amount_yes, количество сесогласных в поле amount_no.
**REQ: POST /petition/{id}/result**
```json
{
	"choice": true
}
```
**RESP: 200 Content-Type: application/vnd.petition.stat+json**
```json
{
	"title": "title",
	"expiry_date": "expiry_date",
	"amount_yes": "100",
	"amount_no": "10",
	"links": {
		"self": "/petition/123/result",
		"petition": "/petition/123"
	}
}
```
