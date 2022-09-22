from typing import Dict
from fastapi import APIRouter, Depends

from chatbot.bot.custom_bot import CustomBot
from chatbot.bot.trainer import Trainer
from chatbot.config.bot_config import BOT_NAME, SETTINGS_FILE_PATHS


from app.config.config import Settings

settings = Settings()
bot = CustomBot(BOT_NAME, debug=False)
Trainer(bot, settings_file_paths=SETTINGS_FILE_PATHS).train()


router = APIRouter()


@router.get("/health")
def health_check() -> Dict:
    return {"status": "OK"}


@router.get("/answer/{question}")
def get_answer(question: str):
    question = question.lower()
    return {"message": bot.get_answer(question)}
