from functions import get_card_data, get_card_comments, get_child_cards
from config import CARD_ID


with open("card_data.txt", "w", encoding="utf-8") as file:
    card_data = get_card_data(CARD_ID)
    if card_data:
        file.write(f"ID: {card_data.get('id')}\n")
        file.write(f"Название: {card_data.get('title')}\n")
        file.write(f"Описание: {card_data.get('description')}\n")
        file.write(f"Дата создания: {card_data.get('created')}\n")
        file.write(f"Дата обновления: {card_data.get('updated')}\n\n")

        comments = get_card_comments(CARD_ID)
        file.write("Комментарии:\n")
        for comment in comments:
            file.write(f"- {comment.get('text')} (Автор: {comment.get('author_id')}, Дата: {comment.get('created')})\n")
        file.write("\n")

        child_cards = get_child_cards(CARD_ID)
        file.write("Дочерние карточки:\n")
        for child in child_cards:
            child_data = get_card_data(child.get("id"))
            if child_data:
                file.write(f"- {child_data.get('title')} (ID: {child_data.get('id')})\n")
                file.write(f"  Описание: {child_data.get('description')}\n")
                file.write(f"  Дата создания: {child_data.get('created')}\n")
                file.write(f"  Дата обновления: {child_data.get('updated')}\n")

                child_comments = get_card_comments(child_data.get("id"))
                file.write("  Комментарии:\n")
                for comment in child_comments:
                    file.write(f"  - {comment.get('text')} (Автор: {comment.get('author_id')}, Дата: {comment.get('created')})\n")
                file.write("\n")

print("Данные сохранены в card_data.txt")