# earth_to_mars_distance.py

def calculate_distance_earth_to_mars():
    # Average distance from the Sun (in kilometers)
    earth_distance_from_sun = 149.6e6  # 149.6 million km
    mars_distance_from_sun = 227.9e6   # 227.9 million km

    # Maximum possible distance (when Mars is on the opposite side of the Sun)
    max_distance = mars_distance_from_sun + earth_distance_from_sun

    # Minimum possible distance (when both are closest)
    min_distance = mars_distance_from_sun - earth_distance_from_sun

    # Average distance
    avg_distance = (max_distance + min_distance) / 2

    print("Distance from Earth to Mars:")
    print(f"Minimum Distance: {min_distance:.2f} km")
    print(f"Maximum Distance: {max_distance:.2f} km")
    print(f"Average Distance: {avg_distance:.2f} km")

if __name__ == "__main__":
    calculate_distance_earth_to_mars()

