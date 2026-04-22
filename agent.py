from intent import detect_intent
from rag import RAG
from tools import mock_lead_capture

class Agent:
    def __init__(self, memory):
        self.memory = memory
        self.rag = RAG()

    def respond(self, user_input):
        # ✅ STEP 1: Handle lead collection first
        if self.memory.get("lead_stage"):

            if not self.memory.get("name"):
                self.memory.update("name", user_input)
                return "Great! Please share your email."

            elif not self.memory.get("email"):
                self.memory.update("email", user_input)
                return "Which platform do you create content on? (YouTube/Instagram/etc.)"

            elif not self.memory.get("platform"):
                self.memory.update("platform", user_input)

                mock_lead_capture(
                    self.memory.get("name"),
                    self.memory.get("email"),
                    self.memory.get("platform")
                )

                return "You're all set! Our team will reach out shortly 🚀"

        # ✅ STEP 2: Intent detection
        intent = detect_intent(user_input)
        self.memory.update("intent", intent)

        if intent == "greeting":
            return "Hi! How can I help you with AutoStream today?"

        elif intent == "product_query":
            return self.rag.query(user_input)

        elif intent == "high_intent":
            self.memory.update("lead_stage", True)
            return "Awesome! Let's get you started. What's your name?"

        return "Can you please clarify?"