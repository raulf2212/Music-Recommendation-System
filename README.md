# Music-Recommendation-System
Interactive command line application that gives song suggestions using a dataset of the top 1.680+ tracks on Spotify.

When a user searches for a keyword (e.g. song title, artist or genre) the application filters the dataset and allows the user to pick a baseline song from the provided results. 

<br>

<img width="732" height="405" alt="image" src="https://github.com/user-attachments/assets/fa7d20f8-ee69-4065-ba45-1253d7c062ca" />

<p>&nbsp;</p>

Once a song is chosen, the application calculates mathematical similarity distance metrics (using the BPM and Energy Levels of the song) and outputs the top 5 similar songs to the chosen track found in the dataset.

<br>

<img width="629" height="680" alt="image" src="https://github.com/user-attachments/assets/89f36854-309f-4165-a6d9-b44b70501178" />

<img width="890" height="370" alt="image" src="https://github.com/user-attachments/assets/ef0fd685-97fc-4374-b29c-e42a45003649" />

# Data Structure & Algorithms Used 

### 1. Naive String Matching Algorithm
Used as the initial dataset search system. When a user types a keyword, the algorithm loops character-by-character through the title, artist, and genre text fields of each record. It slides a search window across the text segments and matches sub-strings sequentially in a case-insensitive manner.

### 2. Euclidean Distance Formula
To calculate the music similarity between the chosen track and the songs inside of the dataset, the program uses the Euclidean Distance Formula with the BPM and Energy Levels of the songs as the x and y coordinates. Where the smaller the distance is, the higher the similarity is. The formula is:

√(BPM1-BPM2)²+(ELevel1-Elevel2)²

### 3. Bounded Max-Heap Data Structure
To be able to sort the distances accordingly and be able to find the top 5 recommendations, the application feeds the calculated distances of all of the songs into a Max-Heap with a limit of 10 elements. Because it is a Max-Heap, the data structure forces the highest distance (lowest similarity) scored song to be at the root node for easy removal. 

If an inserted track's score is bigger than the root, it is rejected. If it is smaller, it overwrites the root and shifts down to its correct position inside of the tree. This is repeated until it has gone through all songs in the dataset and prints out the final tree visualizing the top 10 similar songs.

<img width="632" height="366" alt="image" src="https://github.com/user-attachments/assets/36324188-55a4-4bf4-8897-d20e4e6bcfe3" />

# How to run the program

### Prerequisites

- Python 3.12

### Execution

1. Open your system's terminal
2. Navigate to the project's folder directory
3. Run main.py
4. Interact with the application using your console


# References

The dataset used in the making of this project:

* **Dataset Title:** Spotify Music Dataset
* **Author / Provider:** Solomon Ameh (2024)
* **Source Platform:** Kaggle
* **Dataset Link:** [Kaggle Spotify Music Dataset](https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset/data)
