import matplotlib.pyplot as plt

# Apply ggplot style
plt.style.use('ggplot')

# Runs scored over years
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]

# Plotting the data
plt.plot(years, kohli, color='black', linestyle='--', linewidth=4, label="Kohli")
plt.plot(years, sehwag, color='yellow', linestyle='-', linewidth=5, label="Sehwag")
plt.plot(years, sachin, color='red', linestyle='-.', linewidth=6, label="Tendulkar")

# Labeling
plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Performance Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Display the chart
plt.show()
