from app.database import questions_collection

def update_ability(current_ability: float, correct: bool) -> float:
    learning_rate = 0.1

    if correct:
        current_ability += learning_rate
    else:
        current_ability -= learning_rate

    # Keep ability between 0.1 and 1.0
    current_ability = max(0.1, min(1.0, current_ability))

    return current_ability


def get_next_question(ability: float):

    question = questions_collection.find_one({
        "difficulty": {
            "$gte": ability - 0.1,
            "$lte": ability + 0.1
        }
    })

    if question:
        question["_id"] = str(question["_id"])

    return question