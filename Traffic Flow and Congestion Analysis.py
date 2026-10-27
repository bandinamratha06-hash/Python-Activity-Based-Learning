
print("TRAFFIC FLOW AND CONGESTION ANALYSIS")
print("------------------------------------")

# Road names
roads = ["Main Road", "Market Road", "College Road"]

# Vehicle counts during different time intervals
times = ["8 AM", "10 AM", "1 PM", "6 PM"]

traffic = [
    [80, 120, 90, 180],
    [100, 160, 130, 200],
    [60, 90, 70, 140]
]

# Maximum vehicle capacity per interval
capacity = 150

for i in range(len(roads)):
    print("\nRoad:", roads[i])

    peak_count = 0
    peak_time = ""

    for j in range(len(times)):
        vehicles = traffic[i][j]

        # Find peak traffic period
        if vehicles > peak_count:
            peak_count = vehicles
            peak_time = times[j]

        # Classify congestion
        if vehicles < 80:
            level = "Low"
        elif vehicles <= 150:
            level = "Moderate"
        else:
            level = "High"

        print(times[j], "-", vehicles, "vehicles -", level, "Congestion")

        # Check capacity
        if vehicles > capacity:
            print("WARNING: Capacity exceeded at", times[j])

    print("Peak Traffic Time:", peak_time)
    print("Peak Vehicle Count:", peak_count)

# Find busiest time across all roads
print("\n--------- OVERALL TRAFFIC SUMMARY ---------")

overall_peak = 0
overall_road = ""
overall_time = ""

for i in range(len(roads)):
    for j in range(len(times)):
        if traffic[i][j] > overall_peak:
            overall_peak = traffic[i][j]
            overall_road = roads[i]
            overall_time = times[j]

print("Busiest Road:", overall_road)
print("Peak Period:", overall_time)
print("Maximum Vehicles:", overall_peak)
