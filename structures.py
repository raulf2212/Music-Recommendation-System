import math


class BoundedMaxHeap:
    def __init__(self, capacity=10):
        self.heap = []
        self.capacity = capacity

    def insert(self, distance, song_data):
        if len(self.heap) < self.capacity:
            self.heap.append((distance, song_data))
            self._heapify_up(len(self.heap) - 1)
        elif distance < self.heap[0][0]:
            self.heap[0] = (distance, song_data)
            self._heapify_down(0)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_item

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] > self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def is_empty(self):
        return len(self.heap) == 0

    def visualize_heap(self, index=0, level=0):
        if index >= len(self.heap):
            return

        self.visualize_heap(2 * index + 2, level + 1)
        indent = "    " * level
        distance = self.heap[index][0]
        song_title = self.heap[index][1]["title"]
        print(f"{indent}└── [Dist: {distance:.1f}] {song_title}")
        self.visualize_heap(2 * index + 1, level + 1)


def string_match(pattern, text):
    p = pattern.lower()
    t = text.lower()
    n = len(t)
    m = len(p)

    if m == 0:
        return True

    for i in range(n - m + 1):
        j = 0
        while j < m:
            if t[i + j] != p[j]:
                break
            j += 1
        if j == m:
            return True
    return False

# √ (bpm1-bpm2)^2 + (energy1-energy2)^2)
def calculate_similarity(song1, song2):
    bpm_diff = (song1["bpm"] - song2["bpm"]) ** 2
    energy_diff = (song1["energy"] - song2["energy"]) ** 2
    return math.sqrt(bpm_diff + energy_diff)