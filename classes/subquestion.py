class Subquestion:

    def __init__(self, id: int, question: str, filters: dict):
        self.id = id
        self.question = question
        self.filters = filters


    def __str__(self):
        return f"Subquestion {self.id}: {self.question} with filters [{self.filters}]"