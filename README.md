**For English description see below**

Kaiten -- система управления проектами, часто используется в разработке, может быть использована в том числе как CRM система. 
Изначально разрабатывался в России, но есть и продукт для зарубежных рынков.

Система построена на досках и карточках. Карточка отражает более или менее крупную задачу и может иметь дочерние карточки с подзадачами. 
Пример: Родительская карточка "Сделать сайт для ООО Ромашка" может иметь десяток карточек с дочерними задачами типа "Уточнить у заказчика Х", "Проработать Y" и так далее.

Данный парсер позволяет автоматически собирать все описания и комментарии из родительской и дочерних карточек, а затем собирает их в общий текстовый документ.
Позволяет увидеть всю информацию о большой задаче в одном месте и, при желании, загрузить её целиком в CRM систему, или тот же Кайтен.
Я использую для анализа NotebookLM от Google, чтобы получить саммари или найти нужную информацию.

Для команды реализован интерфейс в чат-боте, что позволят получать быстрые саммари по карточкам разными членами команды.

__Структура проекта__:  
gathering_data_from_cards.py -- непосредственно реализация парсера  
functions.py -- прописанные функции, которые используются в парсере  
config.py -- отдельный файл для загрузки переменных  
params.yaml -- файл с id карточки, которую используем как основание для парсинга  
.env.template -- шаблон для внесение собственных переменных окружения  

Подробнее про API Кайтена по [ссылке](https://developers.kaiten.ru/)

---

**Kaiten** is a project management system, commonly used in software development, but it can also be used as a CRM system.
It was originally developed in Russia, but there is also a version of the product for international markets.

The system is based on boards and cards. A card represents a larger task and can have child cards for subtasks.
Example: a parent card called "Create a website for LLC Romashka" might have a dozen child cards with tasks like "Clarify X with the client," "Work out Y," and so on. In our case, there could be more than 100 child cards about the one client's project.

This parser automatically collects all descriptions and comments from parent and child cards, and then compiles them into a single text document.
This allows users to see all information related to a large task in one place and, if needed, upload it entirely into a CRM system or back into Kaiten.
I use Google’s **NotebookLM** to analyze this content, generate summaries, or search for specific information.

A chatbot interface has been created for the team, allowing different team members to quickly receive card summaries.

**Project structure**:

* `gathering_data_from_cards.py` – the core parser implementation
* `functions.py` – functions used by the parser
* `config.py` – a separate file for loading environment variables
* `params.yaml` – contains the ID of the card used as the basis for parsing
* `.env.template` – a template for defining custom environment variables

More information about the Kaiten API can be found [here](https://developers.kaiten.ru/).
