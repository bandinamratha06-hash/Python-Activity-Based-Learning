
print("SMART HOSTEL RESOURCE MONITORING")
print("--------------------------------")

# Room details
rooms = ["101", "102", "201", "202", "301", "302"]
floors = [1, 1, 2, 2, 3, 3]

# Electricity consumption in units (kWh)
electricity = [80, 120, 150, 90, 200, 110]

# Water consumption in litres
water = [800, 1200, 1500, 900, 2000, 1000]

# Rates and limits
electricity_rate = 8       # Rs. per unit
water_rate = 0.05          # Rs. per litre
electricity_limit = 150
water_limit = 1500

floor_electricity = {}
floor_water = {}

print("\n--------- ROOM-WISE REPORT ---------")

for i in range(len(rooms)):
    electricity_charge = electricity[i] * electricity_rate
    water_charge = water[i] * water_rate
    total_charge = electricity_charge + water_charge

    print("\nRoom:", rooms[i], "| Floor:", floors[i])
    print("Electricity:", electricity[i], "units")
    print("Water:", water[i], "litres")
    print("Electricity Charge: Rs.", electricity_charge)
    print("Water Charge: Rs.", water_charge)
    print("Total Charge: Rs.", total_charge)

    # Check threshold violations
    if electricity[i] > electricity_limit:
        print("Warning: Electricity limit exceeded!")

    if water[i] > water_limit:
        print("Warning: Water limit exceeded!")

    # Add consumption floor-wise
    floor = floors[i]

    if floor not in floor_electricity:
        floor_electricity[floor] = 0
        floor_water[floor] = 0

    floor_electricity[floor] += electricity[i]
    floor_water[floor] += water[i]

# Compare resource consumption across floors
print("\n--------- FLOOR-WISE SUMMARY ---------")

for floor in floor_electricity:
    print("\nFloor:", floor)
    print("Total Electricity:", floor_electricity[floor], "units")
    print("Total Water:", floor_water[floor], "litres")

# Identify highest consumption floors
highest_electricity_floor = max(floor_electricity, key=floor_electricity.get)
highest_water_floor = max(floor_water, key=floor_water.get)

print("\n--------- FINAL SUMMARY ---------")
print("Highest Electricity Usage: Floor", highest_electricity_floor)
print("Highest Water Usage: Floor", highest_water_floor)
