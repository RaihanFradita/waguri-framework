class DemoAdapter:

    def generate(self, prompt: str) -> str:
        if "revenue" in prompt.lower():
            return "The reported revenue is Rp50 million."

        return "There is insufficient information to answer."