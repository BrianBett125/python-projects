# mars_distance_calculator.py

def au_to_km(au):
    """Convert astronomical units to kilometers."""
    return au * 149_597_870.7  # 1 AU = ~149.6 million km

def light_time_km(distance_km):
    """Calculate light travel time in minutes."""
    speed_of_light_kmps = 299_792.458  # km/s
    return (distance_km / speed_of_light_kmps) / 60  # in minutes

def calculate_mars_distance():
    # Average Earth-Mars distance in AU
    avg_distance_au = 1.52 - 1.0  # Mars: 1.52 AU, Earth: 1.0 AU

    # Convert to kilometers
    distance_km = au_to_km(avg_distance_au)

    # Light travel time
    light_minutes = light_time_km(distance_km)

    print("Average Earth to Mars Distance:")
    print(f"{distance_km:.2f} km")
    print(f"Light travel time: {light_minutes:.2f} minutes")

if __name__ == "__main__":
    calculate_mars_distance()

