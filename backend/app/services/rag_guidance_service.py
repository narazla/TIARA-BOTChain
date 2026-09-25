import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from google import genai
import os

_model = None
_index = None
_chunks = None
_client = None

def _load_resources():
    global _model, _index, _chunks, _client
    if _model is None:
        _model = SentenceTransformer("intfloat/multilingual-e5-large")
        _index = faiss.read_index("app/services/rag_data/index_256token.faiss")
        with open("app/services/rag_data/chunks_256token.pkl", "rb") as f:
            _chunks = pickle.load(f)
        _client = genai.Client()

def get_rag_answer(pertanyaan: str) -> str:
    _load_resources()

    pertanyaan_dengan_prefix = "query: " + pertanyaan
    angka_pertanyaan = _model.encode([pertanyaan_dengan_prefix], normalize_embeddings=True)
    skor, indeks = _index.search(np.array(angka_pertanyaan, dtype=np.float32), k=3)

    konteks = ""
    for i in range(3):
        nomor_chunk = indeks[0][i]
        chunk_terkait = _chunks[nomor_chunk]
        konteks += f"[Halaman {chunk_terkait['halaman']}]\n{chunk_terkait['teks']}\n\n"

    prompt = f"""You are an assistant that helps caregivers care for people with dementia.
Answer the question ONLY based on the document context below.
If the answer is not available in the context, honestly say that the information is not available in this document.

Always respond in the same language as the user's question, while ensuring all facts and guidance strictly adhere to the retrieved medical context below — even though the source documents are in Indonesian.

Do not mention page numbers or document sources in your answer — just answer naturally as if speaking directly to the caregiver.

Document context:
{konteks}

Question: {pertanyaan}

Answer:"""

    respons = _client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    return respons.text