import ollama

from utils.prompt_loader import load_prompt


def extract_facts_from_text(text: str, max_facts: int = 5) -> list:
    """
    Use Ollama to extract key facts from a given text.

    Args:
        text (str): Text to process.
        max_facts (int): Maximum number of facts to extract.

    Returns:
        list: List of extracted facts.
    """
    try:
        prompt = load_prompt("fact_extraction", text=text, max_facts=max_facts)

        if not prompt:
            raise ValueError(
                "[ERROR] Failed to load the prompt from YAML configuration."
            )
        response = ollama.chat(
            model="llama3.2:1b", messages=[{"role": "user", "content": prompt}]
        )

        if "message" not in response or "content" not in response["message"]:
            raise ValueError("[ERROR] Unexpected response structure from Ollama API.")

        facts = response["message"]["content"]

        fact_list = [
            fact.strip("- ").strip() for fact in facts.split("\n") if fact.strip()
        ]
        print("[INFO] Extracted Facts:", fact_list)

        return fact_list

    except KeyError as e:
        print(f"[ERROR] Missing key in Ollama response: {e}")
        return []
    except ValueError as e:
        print(e)
        return []
    except Exception as e:
        print(f"[ERROR] Fact extraction failed: {e}")
        return []


if __name__ == "__main__":
    sample_text = """
    Machine learning is a subset of artificial intelligence. It includes supervised,
    unsupervised, and reinforcement learning techniques. Supervised learning uses labeled datasets,
    while unsupervised learning uncovers hidden patterns.
    """

    facts = extract_facts_from_text(sample_text, max_facts=5)

    print("\nExtracted Facts:")
    if facts:
        for i, fact in enumerate(facts):
            print(f"{i + 1}. {fact}")
    else:
        print("[ERROR] No facts extracted.")
