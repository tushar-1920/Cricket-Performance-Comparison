import matplotlib.pyplot as plt
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
plt.plot(years, kohli,'ro--', label="Virat Kohli")
plt.plot(years, sehwag,'g^:', label="Virender Sehwag")

plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Performance Comparison")
plt.legend()
plt.show()
