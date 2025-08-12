# earth_mars_orbital_range.py

def earth_mars_distance():
    # Average distances from the sun in kilometers
    earth_sun = 149_600_000  # km
    mars_sun = 227_900_000   # km

    # Closest approach (opposition) - approx
    min_distance = mars_sun - earth_sun  # km

    # Farthest distance (conjunction) - approx
    max_distance = mars_sun + earth_sun  # km

    print("Approximate Earth-Mars Distance Range:")
    print(f"Closest approach: {min_distance:,} km")
    print(f"Farthest distance: {max_distance:,} km")

if __name__ == "__main__":
    earth_mars_distance()

