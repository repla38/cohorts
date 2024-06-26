import math

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# List of points as (x, y) tuples
points = [(1, 2), (4, 6), (7, 8), (2, 1), (9, 10)]

# List to store distances
distances = []

# Calculate distances between each pair of points
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Print the list of distances
print(distances)