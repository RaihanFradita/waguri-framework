from waguri import WaguriClient
from waguri.adapters.ollama import OllamaAdapter


def main() -> None:
    client = WaguriClient(model=OllamaAdapter(model="llama3.2"))
    result = client.answer(
        question="What is the reported revenue?",
        context=["The report lists revenue as Rp50 million."],
    )
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
