# core/memory.py
class Memory:
    def __init__(self):
        self.long_term_memory = {}  # Buat simpen info jangka panjang
        self.short_term_memory = []  # Buat simpen percakapan terakhir

    def store_interaction(self, user_input, ai_response):
        self.short_term_memory.append({"user": user_input, "ai": ai_response})
        # Batasi ukuran short-term memory
        if len(self.short_term_memory) > 10:
            self.short_term_memory.pop(0)

    def get_context(self, user_input):
        # Ambil informasi relevan dari memory
        context = ""
        for interaction in self.short_term_memory:
            context += f"User: {interaction['user']}, AI: {interaction['ai']}\n"
        return context
