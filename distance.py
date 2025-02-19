import math
from itertools import combinations

points = [(1, 2), (4, 6), (7, 8), (2, 3)]

def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

distances = [(p1, p2, euclidean_distance(p1, p2)) for p1, p2 in combinations(points, 2)]

min_distance = min(distances, key=lambda x: x[2])

print("Tüm mesafeler:")
for p1, p2, d in distances:
    print(f"{p1} ve {p2} arasındaki mesafe: {d:.2f}")

print("\nEn kısa mesafe:")
print(f"{min_distance[0]} ve {min_distance[1]} arasındaki mesafe: {min_distance[2]:.2f}")