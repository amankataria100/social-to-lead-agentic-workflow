from agent import Agent
from memory import Memory

def run():
    print("🤖 AutoStream AI Agent (type 'exit' to quit)\n")

    memory = Memory()
    agent = Agent(memory)

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        response = agent.respond(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    run()