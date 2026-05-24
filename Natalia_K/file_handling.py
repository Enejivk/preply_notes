import csv

data = [
    ["description", "amount", "category", "department", "Income/Expense"],
    ["Emeka Obi salary", 85000, "staff Salary", "Production", 200000],
    ["Ngozi Eze salary", 60000, "staff Salary", "Distribution", 150000],
    ["Chidi Nwosu salary", 150000, "staff Salary", "Operations", 300000],
    ["Flour Purchase", 45000, "Raw Material", "Production", 0],
    ["Van Maintenance", 25000, "Maintenance", "Distribution", 0],
    ["Generator Fuel", 18000, "Utility", "Operations", 20000]
]
with open('new_result.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(data)
