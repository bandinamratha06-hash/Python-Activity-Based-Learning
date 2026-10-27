
print("CAMPUS TRANSPORT ALLOCATION")
print("---------------------------")

routes = int(input("Enter number of routes: "))

for i in range(1, routes + 1):
    print("\nRoute", i)

    name = input("Enter route name: ")
    passengers = int(input("Enter number of passengers: "))
    capacity = int(input("Enter bus capacity: "))

    if capacity <= 0 or passengers < 0:
        print("Invalid input! Enter valid values.")
        continue

    buses = (passengers + capacity - 1) // capacity
    served = min(passengers, buses * capacity)
    unserved = passengers - served

    print("\n--- Route Details ---")
    print("Route:", name)
    print("Total passengers:", passengers)
    print("Bus capacity:", capacity)
    print("Buses required:", buses)
    print("Passengers served:", served)
    print("Unserved passengers:", unserved)

    if unserved > 0:
        print("Alert: More buses are needed!")
    else:
        print("All passengers can be served.")

print("\nTransport allocation completed!")
