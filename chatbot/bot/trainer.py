from chatterbot.trainers import ListTrainer
import json


class Trainer:
    def __init__(self, bot, settings_file_paths=[]):
        self.trainer = ListTrainer(bot.get_chatterbot())
        self.__load_settings_file(settings_file_paths)

    def __load_settings_file(self, settings_file_paths):
        self.settings = []

        for path in settings_file_paths:
            with open(path, "r", encoding="utf-8") as settings_file:
                self.settings.extend(json.load(settings_file))
                settings_file.close()

    def train(self):
        for setting in self.settings:
            questions = setting["questions"]
            answer = setting["answer"]

            for question in questions:
                self.trainer.train([question, answer])
