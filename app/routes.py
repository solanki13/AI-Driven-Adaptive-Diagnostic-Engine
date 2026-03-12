from fastapi import APIRouter
from app.database import sessions_collection
from app.adaptive_engine import update_ability, get_next_question
from app.ai_plan import generate_study_plan

router = APIRouter()


@router.post("/start-session")
def start_session(user_id: str):

    session = {
        "user_id": user_id,
        "ability": 0.5,
        "score": 0
    }

    sessions_collection.insert_one(session)

    return {"message": "Session started", "ability": 0.5}


@router.get("/next-question")
def next_question(user_id: str):

    session = sessions_collection.find_one({"user_id": user_id})

    ability = session["ability"]

    question = get_next_question(ability)

    return question


@router.post("/submit-answer")
def submit_answer(user_id: str, answer: str, correct_answer: str):

    session = sessions_collection.find_one({"user_id": user_id})

    ability = session["ability"]

    correct = answer == correct_answer

    new_ability = update_ability(ability, correct)

    sessions_collection.update_one(
        {"user_id": user_id},
        {"$set": {"ability": new_ability}}
    )

    return {"correct": correct, "new_ability": new_ability}


from fastapi import Form

@router.post("/study-plan")
def study_plan(topics: str = Form(...)):

    topics_list = topics.split(",")

    from app.ai_plan import generate_study_plan

    plan = generate_study_plan(topics_list)

    return {"study_plan": plan}