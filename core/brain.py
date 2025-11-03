# core/brain.py
from config import config
from core.memory import Memory
from modules import nlp  # Contoh modul

class Brain:
    def __init__(self):
        self.name = config.AI_NAME
        self.version = config.VERSION
        self.memory = Memory()

    def process_input(self, user_input):
        # Di sini lo bisa tambahin logika buat proses input dari user
        # Contoh: Pake modul NLP buat analisis input
        processed_input = nlp.analyze(user_input)

        # Ambil informasi dari memory
        context = self.memory.get_context(user_input)

        # Gabung input dan context, lalu kasih jawaban
        response = self.generate_response(processed_input, context)

        # Simpen interaksi ke memory
        self.memory.store_interaction(user_input, response)

        return response

    def generate_response(self, processed_input, context):
        # Logika buat generate jawaban berdasarkan input dan context
        # Bisa pake model machine learning atau rule-based system
        if "hello" in processed_input:
            return f"Hello, I am {self.name} version {self.version}."
        else:
            return "I don't understand. Can you be more specific?"
