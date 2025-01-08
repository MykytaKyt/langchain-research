import os
import uuid

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from embedding import get_embedding

load_dotenv()

client = QdrantClient(host=os.getenv("QDRANT_HOST"), port=int(os.getenv("QDRANT_PORT")))


def add_facts_to_vector_db(facts: list, source: str):
    """
    Add a list of facts to the Qdrant vector database.

    Args:
        facts (list): A list of strings representing facts to be stored.
        source (str): The source of these facts (e.g., PDF name, manual entry).
    """
    try:
        if not facts:
            print("[ERROR] No facts provided for insertion.")
            return

        points = []
        for fact in facts:
            embedding = get_embedding(fact)
            if not embedding:
                print(f"[WARNING] Failed to generate embedding for fact: {fact}")
                continue

            point = PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={"fact": fact, "source": source},
            )
            points.append(point)

        if points:
            client.upsert(collection_name="facts_db", points=points)
            print(
                f"[INFO] Successfully added {len(points)} facts to the vector database."
            )
        else:
            print("[ERROR] No valid points to insert into Qdrant.")

    except Exception as e:
        print(f"[ERROR] Failed to add facts to vector DB: {e}")
