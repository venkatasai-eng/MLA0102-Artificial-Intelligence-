def decision_tree(age, income):
    if age < 25:
        return "Student"
    elif income < 50000:
        return "Employee"
    else:
        return "Business Person"

print("Age: 20, Income: 10000 →", decision_tree(20, 10000))
print("Age: 30, Income: 30000 →", decision_tree(30, 30000))
print("Age: 40, Income: 80000 →", decision_tree(40, 80000))