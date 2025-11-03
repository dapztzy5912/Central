# main.py
from core.brain import Brain
from config import config

if __name__ == "__main__":
    brain = Brain()
    print(f"Starting {config.AI_NAME} version {config.VERSION}...")

    while True:
        user_input = input("You: ")
        response = brain.process_input(user_input)
        print(f"{config.AI_NAME}: {response}")
