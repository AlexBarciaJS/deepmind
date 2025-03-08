# pdf_processor/chunker.py

def chunk_text(text, chunk_size=1500, chunk_overlap=100):
    """
    Split text into chunks for embedding generation.
    'chunk_size' is the number of words per chunk.
    'chunk_overlap' is the number of words to overlap between chunks.
    """
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunks.append(" ".join(words[start:end]))
        start += chunk_size - chunk_overlap
    return chunks
