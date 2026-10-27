
import math

# Store geographical coordinates as tuples (x, y)
points = (
    (0, 0),
    (3, 4),
    (6, 8),
    (12, 8)
)

longest_distance = 0
longest_segment = 0

print("ROUTE DISTANCE ANALYSIS")
print("-----------------------")

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]

    # Calculate distance using the formula
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("Distance from point", i + 1, "to point", i + 2, "=", distance)

    if distance > longest_distance:
        longest_distance = distance
        longest_segment = i + 1

print("\nLongest route segment:", longest_segment)
print("Longest distance:", longest_distance)
