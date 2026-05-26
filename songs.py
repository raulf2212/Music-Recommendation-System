# songs.py
import csv


def load_songs_from_csv(file_path):
    song_database = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for idx, row in enumerate(reader):
                try:
                    title = row.get("track_name")
                    artist = row.get("track_artist")
                    genre = row.get("playlist_genre", "Unknown")
                    tempo_val = row.get("tempo")
                    energy_val = row.get("energy")

                    if not title or not artist or not tempo_val or not energy_val:
                        continue

                    bpm = float(tempo_val)
                    energy = float(energy_val)

                    if energy <= 1.0:
                        energy = energy * 10.0

                    song = {
                        "id": idx + 1,
                        "title": title,
                        "artist": artist,
                        "genre": genre,
                        "bpm": bpm,
                        "energy": energy
                    }
                    song_database.append(song)
                except (KeyError, ValueError):
                    continue
    except FileNotFoundError:
        print(f"\n[!] Error: Could not find '{file_path}'.")
        print("[!] Please make sure your file is placed inside the exact same directory folder.")

    return song_database