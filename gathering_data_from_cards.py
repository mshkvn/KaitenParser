from functions import get_card_data, get_card_comments, get_child_cards
from config import CARD_ID


with open("card_data.txt", "w", encoding="utf-8") as file:
    card_data = get_card_data(CARD_ID)
    if card_data:
        file.write(f"ID: {card_data.get('id')}\n")
        file.write(f"Title: {card_data.get('title')}\n")
        file.write(f"Description: {card_data.get('description')}\n")
        file.write(f"Created: {card_data.get('created')}\n")
        file.write(f"Updated: {card_data.get('updated')}\n\n")

        comments = get_card_comments(CARD_ID)
        file.write("Comments:\n")
        for comment in comments:
            file.write(f"- {comment.get('text')} (Author: {comment.get('author_id')}, Date: {comment.get('created')})\n")
        file.write("\n")

        child_cards = get_child_cards(CARD_ID)
        file.write("Child cards:\n")
        for child in child_cards:
            child_data = get_card_data(child.get("id"))
            if child_data:
                file.write(f"- {child_data.get('title')} (ID: {child_data.get('id')})\n")
                file.write(f"  Description: {child_data.get('description')}\n")
                file.write(f"  Created: {child_data.get('created')}\n")
                file.write(f"  Updated: {child_data.get('updated')}\n")

                child_comments = get_card_comments(child_data.get("id"))
                file.write("  Comments:\n")
                for comment in child_comments:
                    file.write(f"  - {comment.get('text')} (Author: {comment.get('author_id')}, Date: {comment.get('created')})\n")
                file.write("\n")

print("Data collected in card_data.txt")