import os

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

load_dotenv()


def create_collection():
    """
    Create and initialize a Qdrant collection for storing facts.
    """
    try:
        client = QdrantClient(
            host=os.getenv("QDRANT_HOST"), port=int(os.getenv("QDRANT_PORT"))
        )

        collection_name = "facts_db"
        vector_size = 384
        distance_metric = Distance.COSINE

        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=distance_metric),
        )

        print(f"[INFO] Collection '{collection_name}' created successfully with:")
        print(f"  - Vector Dimension: {vector_size}")
        print(f"  - Distance Metric: {distance_metric.name}")

    except Exception as e:
        print(f"[ERROR] Failed to create collection: {e}")


def main():
    """
    Main function to set up Qdrant Vector Database.
    """
    print("[INFO] Initializing Qdrant Vector Database...")
    create_collection()
    print("[INFO] Vector Database setup completed successfully.")


if __name__ == "__main__":
    main()
