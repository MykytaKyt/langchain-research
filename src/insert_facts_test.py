from insert_facts import add_facts_to_vector_db


def main():
    """
    Test inserting facts into Qdrant VDB.
    """
    sample_facts = [
        "Artificial Intelligence is a branch of computer science.",
        "Machine Learning is a subset of AI.",
        "Supervised Learning uses labeled datasets.",
        "Unsupervised Learning discovers hidden patterns.",
        "Reinforcement Learning focuses on rewards for actions.",
    ]

    source = "manual_entry"

    print(f"[INFO] Inserting {len(sample_facts)} facts into the vector database...")
    add_facts_to_vector_db(sample_facts, source)
    print("[INFO] Fact insertion test completed.")


if __name__ == "__main__":
    main()
