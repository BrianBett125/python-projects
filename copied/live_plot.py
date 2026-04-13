import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Simulated live data source
data = []

def update(frame):
    # Simulate incoming data
    data.append(random.randint(0, 100))
    data[:] = data[-50:]  # Keep only the last 50 points

    plt.cla()  # Clear the current plot
    plt.plot(data, label="Random Value")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Real-time Data Plot")
    plt.legend(loc="upper right")

# Create animation
ani = animation.FuncAnimation(plt.gcf(), update, interval=500)

plt.tight_layout()
plt.show()

