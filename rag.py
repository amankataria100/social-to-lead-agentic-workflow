import json

class RAG:
    def __init__(self, path="knowledge_base.json"):
        with open(path, "r") as f:
            self.data = json.load(f)

    def query(self, question: str):
        question = question.lower()

        if "price" in question or "plan" in question:
            response = "Here are our pricing plans:\n"
            for plan in self.data["plans"]:
                response += f"\n{plan['name']} - {plan['price']}\n"
                for f in plan["features"]:
                    response += f"  - {f}\n"
            return response

        elif "refund" in question or "policy" in question:
            return "Policies:\n" + "\n".join(self.data["policies"])

        return "I can help with pricing, features, and policies."