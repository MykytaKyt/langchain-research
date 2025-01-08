from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


def load_and_split_pdf(pdf_path: str, chunk_size: int = 500, chunk_overlap: int = 100):
    """
    Load a PDF file, extract text, and split it into chunks.

    Args:
        pdf_path (str): Path to the PDF file.
        chunk_size (int): Size of each text chunk.
        chunk_overlap (int): Overlap between consecutive chunks.

    Returns:
        List[str]: List of text chunks.
    """
    try:
        # Load PDF file
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        chunks = text_splitter.split_documents(documents)

        print(f"[INFO] Loaded and split {len(chunks)} chunks from {pdf_path}")
        return chunks

    except Exception as e:
        print(f"[ERROR] Failed to process PDF: {e}")
        return []


if __name__ == "__main__":
    pdf_path = "test_file.pdf"

    chunks = load_and_split_pdf(pdf_path, chunk_size=500, chunk_overlap=100)

    for i, chunk in enumerate(chunks[:3]):
        print(f"Chunk {i + 1}: {chunk.page_content[:200]}...")
