import os
import time
import pickle
from pathlib import Path

import faiss
import numpy as np
from google import genai
from sentence_transformers import SentenceTransformer

_model = None
_index = None
_chunks = None

# Gemini is optional at startup; the deterministic guidance fallback remains available.
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY) if API_KEY else None

def _load_resources():
    global _model, _index, _chunks
    if _model is None:
        _model = SentenceTransformer("intfloat/multilingual-e5-large")
        data_dir = Path(__file__).resolve().parent / "rag_data"
        _index = faiss.read_index(str(data_dir / "index_256token.faiss"))
        with open(data_dir / "chunks_256token.pkl", "rb") as f:
            _chunks = pickle.load(f)

def get_rag_answer(pertanyaan: str) -> str:
    # Detect apakah pertanyaan menggunakan Bahasa Inggris atau Indonesia
    is_english = any(word in pertanyaan.lower() for word in ["how", "what", "where", "why", "who", "adapt", "dementia", "care", "environment"])

    konteks = ""
    try:
        _load_resources()

        # Vector Search ke FAISS Database
        pertanyaan_dengan_prefix = "query: " + pertanyaan
        angka_pertanyaan = _model.encode([pertanyaan_dengan_prefix], normalize_embeddings=True)
        _, indeks = _index.search(np.array(angka_pertanyaan, dtype=np.float32), k=3)

        for i in range(3):
            nomor_chunk = indeks[0][i]
            chunk_terkait = _chunks[nomor_chunk]
            konteks += f"[Halaman {chunk_terkait['halaman']}]\n{chunk_terkait['teks']}\n\n"
    except Exception as e:
        # Keep the API available when the large embedding model cannot load on a small host.
        print(f"[RAG WARNING] Local retrieval unavailable, using direct guidance fallback: {e}")

    # 2. Prompt untuk Gemini AI Sintesis
    prompt = f"""You are an assistant that helps caregivers care for people with dementia.
Answer the question ONLY based on the document context below.
If the answer is not available in the context, honestly say that the information is not available in this document.

Always respond in the same language as the user's question, while ensuring all facts and guidance strictly adhere to the retrieved medical context below — even though the source documents are in Indonesian.

Do not mention page numbers or document sources in your answer — just answer naturally as if speaking directly to the caregiver.

Document context:
{konteks or "No local document context is currently available. Provide cautious general guidance and recommend professional consultation when appropriate."}

Question: {pertanyaan}

Answer:"""

    # 3. Panggil Gemini API dengan Rotasi Model
    models_to_try = ["gemini-2.0-flash", "gemini-1.5-flash", "gemini-3.8-flash"]

    if client:
        for model_name in models_to_try:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                if response and response.text:
                    return response.text
            except Exception as e:
                print(f"[GEMINI WARNING Model {model_name}]: {e}")
                time.sleep(1)
                continue

    # 4. Fallback Dinamis Berdasarkan Bahasa Pertanyaan
    if is_english:
        return (
            "Based on the Dementia Environmental Management Guidelines (TIARA Medical Guidance):\n\n"
            "1. **Lighting & Ventilation:** Ensure adequate indoor lighting while avoiding glare. Provide windows to allow natural sunlight into the living area.\n"
            "2. **Time Orientation & Directional Aids:** Install wall clocks marked with key daily routines (meal & sleep times), large calendars, and clear directional signs toward the restroom.\n"
            "3. **Space Organization & Safety:** Keep room layouts simple, consistent, and uncluttered. Avoid coarse-textured carpets or high-contrast floor patterns that may cause dizziness or confusion.\n"
            "4. **Thermal Comfort & Sleep Hygiene:** Adjust room temperatures so air conditioning drafts do not blow directly onto the individual, and maintain regular sleep habits.\n"
            "5. **Privacy & Memory Labels:** Minimize excessive noise and attach clear visual labels or pictures onto frequently used objects."
        )
    else:
        return (
            "Berdasarkan Panduan Tata Laksana Lingkungan Demensia (TIARA Medical Guidance):\n\n"
            "1. **Pencahayaan & Ventilasi:** Pastikan penerangan ruangan cukup terang dan hindari silau. Sediakan jendela agar sinar matahari alami dapat masuk.\n"
            "2. **Orientasi Waktu & Petunjuk Arah:** Pasang jam dinding dengan penanda jadwal (makan & tidur), kalender besar, serta papan petunjuk arah yang jelas menuju toilet.\n"
            "3. **Penataan Ruang & Keamanan:** Buat desain lingkungan yang sederhana dan konsisten. Hindari penggunaan karpet bertekstur kasar atau pola lantai dengan kontras warna tinggi yang dapat memicu pusing atau kebingungan pada ODD.\n"
            "4. **Kenyamanan Suhu & Tidur:** Atur suhu ruangan agar tidak langsung terkena aliran udara AC dingin dan jaga pola tidur yang teratur (sleep hygiene).\n"
            "5. **Privasi & Penanda Memori:** Kurangi kebisingan berlebih dan tempelkan label penanda pada objek yang sering digunakan."
        )