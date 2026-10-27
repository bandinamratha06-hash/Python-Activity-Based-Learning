
print("INTERNSHIP CANDIDATE RANKING SYSTEM")
print("-----------------------------------")

# Candidate details
names = ["Ravi", "Sita", "Rahul", "Priya", "Arjun"]
marks = [85, 90, 75, 90, 80]
assessment = [80, 85, 90, 85, 70]
attendance = [90, 95, 80, 85, 75]

qualified = []

for i in range(len(names)):

    # Check eligibility conditions
    if marks[i] >= 60 and assessment[i] >= 60 and attendance[i] >= 75:

        # Calculate total score
        total = marks[i] * 0.4 + assessment[i] * 0.4 + attendance[i] * 0.2

        qualified.append([
            names[i],
            marks[i],
            assessment[i],
            attendance[i],
            total
        ])

    else:
        print(names[i], "is not eligible")

# Rank candidates
# Tie-breaking rules:
# 1. Higher total score
# 2. Higher assessment score
# 3. Higher marks
# 4. Alphabetical order

qualified.sort(key=lambda x: (-x[4], -x[2], -x[1], x[0]))

print("\n--------- RANKING OF QUALIFIED CANDIDATES ---------")
print("Rank  Name       Marks  Assessment  Attendance  Score")

for i in range(len(qualified)):
    candidate = qualified[i]

    print(i + 1, "   ", candidate[0], "   ",
          candidate[1], "    ",
          candidate[2], "       ",
          candidate[3], "       ",
          round(candidate[4], 2))

print("\nTotal Candidates:", len(names))
print("Qualified Candidates:", len(qualified))
print("Not Qualified:", len(names) - len(qualified))

if len(qualified) > 0:
    print("Selected Candidate:", qualified[0][0])
else:
    print("No candidates qualified")
