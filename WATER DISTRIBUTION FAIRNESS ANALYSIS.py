
print("WATER DISTRIBUTION FAIRNESS ANALYSIS")
print("------------------------------------")

# Area names
areas = ["Area A", "Area B", "Area C", "Area D"]

# Daily water demand in litres
demand = [1000, 1200, 800, 1500]

# Water supplied to each area over 3 days
supply = [
    [800, 700, 750],
    [1000, 1100, 900],
    [800, 750, 800],
    [900, 800, 850]
]

days = ["Day 1", "Day 2", "Day 3"]

most_underserved = ""
highest_shortage = -1

print("\n--------- AREA-WISE REPORT ---------")

for i in range(len(areas)):
    total_supply = sum(supply[i])
    total_demand = demand[i] * len(days)
    shortage = total_demand - total_supply

    print("\nArea:", areas[i])
    print("Total Demand:", total_demand, "litres")
    print("Total Supply:", total_supply, "litres")
    print("Total Shortage:", shortage, "litres")

    # Daily supply details
    for j in range(len(days)):
        daily_shortage = demand[i] - supply[i][j]

        if daily_shortage < 0:
            daily_shortage = 0

        print(days[j], "- Supply:", supply[i][j],
              "litres, Shortage:", daily_shortage, "litres")

    # Identify most underserved area
    if shortage > highest_shortage:
        highest_shortage = shortage
        most_underserved = areas[i]

# Compare total distribution
print("\n--------- FINAL SUMMARY ---------")

for i in range(len(areas)):
    print(areas[i], "- Average Daily Supply:",
          round(sum(supply[i]) / len(days), 2), "litres")

print("\nMost Underserved Area:", most_underserved)
print("Highest Total Shortage:", highest_shortage, "litres")
