# main.py
from structures import BoundedMaxHeap, string_match, calculate_similarity
from songs import load_songs_from_csv


def process_and_visualize_recommendations(target_song, database, limit=10, num_recommendations=5):
    heap = BoundedMaxHeap(capacity=limit)
    seen_titles = {target_song["title"].lower()}

    for song in database:
        title_lower = song["title"].lower()
        if title_lower in seen_titles:
            continue

        distance = calculate_similarity(target_song, song)
        heap.insert(distance, song)
        seen_titles.add(title_lower)

    print("\n=======================================================")
    print(f"STEP 2: Visualization of the final Max-Heap Tree({limit} Elements)")
    print("=======================================================")
    heap.visualize_heap()

    all_top_items = []
    while not heap.is_empty():
        all_top_items.append(heap.extract_max())

    all_top_items.reverse()
    recommendations = [item[1] for item in all_top_items[:num_recommendations]]
    return recommendations


def main():
    dataset_file = "high_popularity_spotify_data.csv"
    song_database = load_songs_from_csv(dataset_file)

    if not song_database:
        return

    print(f"\n--- LOADED {len(song_database)} TRACKS ---")
    search_query = input("Search for a song by title, artist, or genre: ")

    matches = []
    seen_matches = set()
    for song in song_database:
        match_key = (song["title"].lower(), song["artist"].lower())
        if match_key in seen_matches:
            continue

        if (string_match(search_query, song["title"]) or
                string_match(search_query, song["artist"]) or
                string_match(search_query, song["genre"])):
            matches.append(song)
            seen_matches.add(match_key)

    if not matches:
        print("No songs found matching that criteria.")
        return

    print("\nResults found:")
    for idx, song in enumerate(matches[:15]):
        print(f"[{idx + 1}] {song['title']} by {song['artist']} ({song['genre']})")

    try:
        choice = int(input("\nSelect the song number you like: ")) - 1
        if choice < 0 or choice >= len(matches[:15]):
            print("Invalid choice.")
            return
        selected_song = matches[choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\n=======================================================")
    print("Step 1: Song Choice Metrics")
    print("=======================================================")
    print(f" Track Title:  {selected_song['title']}")
    print(f" Track Artist: {selected_song['artist']}")
    print(f" Genre Group:  {selected_song['genre'].upper()}")
    print(f" Tempo (BPM):  {selected_song['bpm']:.1f}")
    print(f" Energy Score: {selected_song['energy']:.1f}/10")

    recs = process_and_visualize_recommendations(selected_song, song_database, limit=10, num_recommendations=5)

    print("\n=======================================================")
    print(f"STEP 3: FINAL RECOMMENDATIONS (Top 5)")
    print("=======================================================")
    for i, rec in enumerate(recs):
        print(f"{i + 1}. {rec['title']} by {rec['artist']} (Genre: {rec['genre']})")


if __name__ == "__main__":
    main()