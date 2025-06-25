from pathlib import Path
import json

def load_documents_from_folder(folder_path):
    documents = []
    for file in Path(folder_path).rglob("*.json"):  # <== recursive glob
        try:
            with open(file, encoding="utf-8") as f:
                data = json.load(f)
                text = data.get("description", "").strip()
                if not text:
                    continue
                documents.append({
                    "text": text,
                    "metadata": {
                        "title": data.get("title", ""),
                        "artist": data.get("artist", ""),
                        "culture": data.get("culture", ""),
                        "date": data.get("dated", ""),
                        "file": str(file)
                    }
                })
        except Exception as e:
            print(f"Failed to load {file}: {e}")
    return documents
