import os

sep = os.path.abspath(os.sep)
dir = os.getcwd()

BOT_NAME = "Robô de atendimento para distribuidora de peças de moto"
SETTINGS_FILE_PATHS = [
    f"{dir}{sep}chatbot{sep}data{sep}greetings.json",
]
ACCEPTANCE = 0.7
MINIMAL_CONFIDENCE = 0.6
SERVER_VERSION = "0.1"
FALLBACK_RESPONSE = "Não consigo responder essa pergunta.\nPergunte outra coisa"
