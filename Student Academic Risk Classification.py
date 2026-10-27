
print("STUDENT ACADEMIC RISK CLASSIFICATION")
print("------------------------------------")

# Lists of student data
names = ["Ravi", "Sita", "Rahul", "Priya", "Arjun"]
marks = [35, 75, 40, 25, 85]
attendance = [80, 60, 75, 55, 90]
lab_scores = [70, 80, 35, 30, 90]

low_risk = 0
medium_risk = 0
high_risk = 0

for i in range(len(names)):
    risk_factors = []

    if marks[i] < 40:
        risk_factors.append("Low Marks")

    if attendance[i] < 75:
        risk_factors.append("Low Attendance")

    if lab_scores[i] < 40:
        risk_factors.append("Low Lab Score")

    # Classify academic risk
    if len(risk_factors) >= 2:
        category = "High Risk"
        high_risk += 1
    elif len(risk_factors) == 1:
        category = "Medium Risk"
        medium_risk += 1
    else:
        category = "Low Risk"
        low_risk += 1

    print("\nStudent:", names[i])
    print("Marks:", marks[i])
    print("Attendance:", attendance[i], "%")
    print("Lab Score:", lab_scores[i])
    print("Risk Factors:", risk_factors if risk_factors else "None")
    print("Risk Category:", category)

# Summary report
print("\n--------- SUMMARY REPORT ---------")
print("Low Risk Students:", low_risk)
print("Medium Risk Students:", medium_risk)
print("High Risk Students:", high_risk)
print("Total Students:", len(names))
