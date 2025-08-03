# earth_mars_haversine_sim.py

import math

def to_cartesian(radius_km, angle_deg):
    """Convert polar coordinates to 2D cartesian coordinates."""
    angle_rad = math.radians(angle_deg)
    x = radius_km * math.cos(angle_rad)
    y = radius_km * math.sin(angle_rad)
    return x, y

def distance_between_points(p1, p2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def simulate_earth_mars_distance():
    # Average orbital radius from Sun in km
    earth_radius = 149_600_000  # km
    mars_radius = 227_900_000   # km

    # Assume angles from sun in degrees (you can change for other scenarios)
    earth_angle = 0       # Earth at 0°
    mars_angle = 135      # Mars at 135° (roughly opposite)

    earth_pos = to_cartesian(earth_radius, earth_angle)
    mars_pos = to_cartesian(mars_radius, mars_angle)

    distance_km = distance_between_points(earth_pos, mars_pos)

    print("Simulated Earth-Mars Distance Based on Angles:")
    print(f"{distance_km:.2f} km")

if __name__ == "__main__":
    simulate_earth_mars_distance()

