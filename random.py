import random

def estimate_pi(n):
    points_inside_circle = 0
    total_points = n

    for _ in range(total_points):
        # Generate random x and y coordinates between 0 and 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Check if the point is inside the unit circle (x^2 + y^2 <= 1)
        distance = x**2 + y**2
        if distance <= 1:
            points_inside_circle += 1

    # Formula: pi is roughly 4 * (points inside circle / total points)
    return 4 * points_inside_circle / total_points

# Run the simulation with 1 million points
n = 1_000_000
pi_approx = estimate_pi(n)

print(f"Total points: {n}")
print(f"Estimated value of π: {pi_approx}")
