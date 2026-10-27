
print("FOOD SUPPLY CHAIN STOCK RECONCILIATION")
print("--------------------------------------")

locations = int(input("Enter number of locations: "))

for i in range(1, locations + 1):
    print("\nLocation", i)

    name = input("Enter location name: ")
    food = input("Enter food item: ")

    received = int(input("Enter quantity received (kg): "))
    distributed = int(input("Enter quantity distributed (kg): "))
    damaged = int(input("Enter quantity damaged (kg): "))
    actual = int(input("Enter actual remaining stock (kg): "))
    target = int(input("Enter target stock (kg): "))

    expected = received - distributed - damaged
    discrepancy = actual - expected
    replenishment = max(0, target - actual)

    print("\n--- Stock Report ---")
    print("Location:", name)
    print("Food item:", food)
    print("Expected remaining stock:", expected, "kg")
    print("Actual remaining stock:", actual, "kg")
    print("Discrepancy:", discrepancy, "kg")
    print("Replenishment required:", replenishment, "kg")

    if discrepancy < 0:
        print("Alert: Stock shortage detected!")
    elif discrepancy > 0:
        print("Alert: Extra stock detected!")
    else:
        print("Stock matches expected quantity.")

print("\nStock reconciliation completed!")
