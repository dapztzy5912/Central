# core/brain.py
from config import config
from core.memory import Memory
from modules import nlp

class Brain:
    def __init__(self):
        self.name = config.AI_NAME
        self.version = config.VERSION
        self.memory = Memory()

    def process_input(self, user_input):
        processed_input = nlp.analyze(user_input)
        context = self.memory.get_context(user_input)
        response = self.generate_response(processed_input, context)
        self.memory.store_interaction(user_input, response)
        return response

    def generate_response(self, processed_input, context):
        # Daftar kata kunci dan responsnya
        keywords = {
            # Greeting
            ("halo", "hai", "hello", "hi", "hei"): 
                f"Halo! Saya {self.name} versi {self.version}. Ada yang bisa saya bantu?",
            
            # Nama
            ("nama", "siapa kamu", "who are you", "kamu siapa"):
                f"Nama saya {self.name}, saya adalah AI assistant versi {self.version}.",
            
            # Kabar
            ("apa kabar", "how are you", "kabar"):
                "Saya baik-baik saja, terima kasih! Bagaimana dengan kamu?",
            
            # Terima kasih
            ("terima kasih", "thanks", "thank you", "makasih"):
                "Sama-sama! Senang bisa membantu.",
            
            # Bye
            ("bye", "dadah", "selamat tinggal", "goodbye"):
                "Sampai jumpa! Semoga harimu menyenangkan!",
            
            # Bantuan
            ("help", "bantuan", "tolong"):
                "Saya bisa menjawab pertanyaan sederhana. Coba tanya nama saya atau sapa saya!",
        }
        
        # Cek apakah ada kata kunci yang cocok
        for keywords_tuple, response in keywords.items():
            for keyword in keywords_tuple:
                if keyword in processed_input:
                    return response
        
        # Kalau nggak ada yang cocok
        return "Maaf, saya belum mengerti. Coba tanya hal lain atau ketik 'help' untuk bantuan."
