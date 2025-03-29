from models.questions import Question
from models import db
from schemas.questions import QuestionCreate, QuestionResponse
from controllers.categories import get_category_by_id


def get_all_questions() -> list[dict[str, int | str]]:
    questions = Question.query.all()

    questions_data = [
        QuestionResponse.model_validate(question).model_dump()
        for question in questions
    ]

    return questions_data


def get_question_by_id(id_: int) -> Question | None:
    question = Question.query.get(id_)

    return question


def create_new_question(row_data: dict[str, str | int]) -> Question:
    question_obj = QuestionCreate.model_validate(row_data).model_dump()

    get_category_by_id(question_obj["category_id"])

    question = Question(**question_obj)

    db.session.add(question)
    db.session.commit()

    return question


def update_question(entity: Question, row_data: dict[str, str]) -> Question:
    entity.text = row_data["text"]
    db.session.commit()
    return entity
