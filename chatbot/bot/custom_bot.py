from chatbot.config.bot_config import (
    ACCEPTANCE,
    MINIMAL_CONFIDENCE,
    FALLBACK_RESPONSE,
)
from chatterbot import ChatBot
from difflib import SequenceMatcher


class CustomBot:
    def __init__(self, name, debug=False):
        self.bot = ChatBot(
            name,
            read_only=True,
            statement_comparison_function=self.__compare_messages,
            response_selection_method=self.__select_answer,
            logic_adapters=[
                {
                    "import_path": "chatterbot.logic.BestMatch",
                }
            ],
        )
        self.isDebug = debug

    def __compare_messages(self, question, answer):
        if question.text and answer.text:
            question_text = question.text
            answer_text = answer.text

            similarity = SequenceMatcher(None, question_text, answer_text)

            similarity = round(similarity.ratio(), 2)
            if self.isDebug:
                print(f"Question: {question_text}")
                print(f"Possible answer: {answer_text}")
                print(f"Similarity: {similarity}")

            if similarity >= ACCEPTANCE:
                return similarity

        return 0.0

    def __select_answer(self, message, answers, storage=None):
        if self.isDebug:
            print(f"Selected answer: {answers[0]}")

        return answers.pop(0)

    def get_chatterbot(self):
        return self.bot

    def get_answer(self, question):
        answer = self.bot.get_response(question)

        if answer.confidence > MINIMAL_CONFIDENCE:
            return answer.text

        return FALLBACK_RESPONSE
