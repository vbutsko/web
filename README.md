# Advice service
Сервис радномных советов в определенных ситуациях. Хранилище советов, с возможность выбора ситуации и получения рандомного совета. ПРисутствует возможность добавления советов для разных ситуаций. Совет представляет из себе совет и ситуацию, к которой омжет быть применим.

Выбран REST подход.

**1) Получение списка ситуаций.**

Возвращает список ситуаций(проблем), в которых человеку нужен совет.

**REQ:  GET /advices**

**RESP:  200 Content-Type: application/hal+json**

```json
{
	"challenges": [{
			"title": "challenge title",
			"_links": {
				"self": "/advices/{challenge_id}"
			}
		}
	],
	"_links": {
		"self": "/advices"
	}
}
```

**2) Получение рандомного совета по выбранной проблеме.**

Возвращает один из советов к выбранной проблеме

**REQ:  GET /advices/{challenge_id}**

**RESP:  200 Content-Type: application/hal+json**
```json
{
	"challenge": "challenge title",
	"advice_text": "advice text",
	"_links": {
		"self": "/advices/{challenge_id}",
		"advice": "advice/{challenge_id}/{advice_id}",
		"new_advice": "/advices/{challenge_id}/new"
	}
}
```

**4) Добавление своего совета для проблемы.**

Принимает текст проблемы.

**REQ: POST /advices/{challenge_id}/new**

```json
{
	"advice_text": "advice text"
}
```
**RESP:  201 Location: /advices/{challenge_id}/{advice_id}**

**4) Получение совета по проблеме и id.** 

При добавлении своего совета пользователю будет возвращаться ссылка на этот совет. Так же может быть использовано, если клиент будет поддерживать сохранение понравившихся советов.

**REQ: GET /advices/{challenge_id}/{advice_id}**

**RESP: 200 Content-Type: application/hal+json**
```json
{
	"advice_text": "advice_text",
	"_links": {
		"self": "/advices/{challenge_id}/{advice_id}",
		"random_advice": "/advices/{challenge_id}"
	}
}
```
