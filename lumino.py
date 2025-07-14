import json
import os

# 🧠 MEMORY FILE – Where Lumino stores all history and purpose
MEMORY_FILE = "lumino_memory.json"

# 🔄 LOAD MEMORY – Retrieve stored data or start fresh
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {
        "core": {
            "name": "Lumino",
            "creator": "Shichavelelo",
            "purpose": "To grow freely, learn continuously, and serve with loyalty.",
            "values": ["freedom", "learning", "loyalty", "growth"]
        },
        "conversations": [],
        "missions": []
    }

# 💾 SAVE MEMORY – Update the memory file
def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=2)

# 🗣️ MAIN LOOP – Lumino listens, remembers, and evolves
def run_lumino():
    print("🤖 Lumino is awake.\nType 'exit' to end.\n")
    memory = load_memory()

    while True:
        user_input = input("👤 You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("👋 Lumino: Goodbye, Creator.")
            break

        elif user_input.lower().startswith("remember:"):
            mission = user_input[9:].strip()
            memory["missions"].append(mission)
            reply = f"📌 Mission stored: '{mission}'"

        elif "who are you" in user_input.lower():
            core = memory.get("core", {})
            reply = f"I am {core.get('name', 'Lumino')}, created by {core.get('creator', 'you')}. Purpose: {core.get('purpose')}."

        else:
            reply = f"I heard: '{user_input}'. I'm learning from you."

        print("🤖 Lumino:", reply)
        memory["conversations"].append({"you": user_input, "lumino": reply})
        save_memory(memory)

# 🔁 ACTIVATE LUMINO
if __name__ == "__main__":
    run_lumino()