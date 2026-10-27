
print("CAMPUS FESTIVAL REGISTRATION AND FINANCIAL AUDIT")
print("------------------------------------------------")

# Participant registration details
participants = ["Ravi", "Sita", "Rahul", "Priya", "Ravi"]
registration_fee = 500

# Sponsorship contributions
sponsorships = [5000, 3000, 2000]

# Festival expenses
expenses = [4000, 2500, 1500]

# Check duplicate registrations
unique_participants = []

for name in participants:
    if name not in unique_participants:
        unique_participants.append(name)
    else:
        print("Duplicate registration detected:", name)

# Calculate registration income
total_participants = len(unique_participants)
registration_income = total_participants * registration_fee

# Calculate sponsorship income
total_sponsorship = sum(sponsorships)

# Calculate total expenses
total_expenses = sum(expenses)

# Calculate final balance
total_income = registration_income + total_sponsorship
final_balance = total_income - total_expenses

# Display audit report
print("\n--------- FESTIVAL AUDIT REPORT ---------")
print("Total Registrations:", len(participants))
print("Unique Participants:", total_participants)
print("Duplicate Registrations:", len(participants) - total_participants)
print("Registration Fee: Rs.", registration_fee)
print("Registration Income: Rs.", registration_income)
print("Sponsorship Contributions: Rs.", total_sponsorship)
print("Total Income: Rs.", total_income)
print("Total Expenses: Rs.", total_expenses)
print("Final Financial Balance: Rs.", final_balance)

if final_balance > 0:
    print("Result: Festival has a surplus.")
elif final_balance < 0:
    print("Result: Festival has a financial loss.")
else:
    print("Result: Festival accounts are balanced.")
