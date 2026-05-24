class Person:
    def __init__(self, name, age, role):
        self.__name = name
        self.__age = age
        self.role = role

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 18:
            print("Error: Age must be 18 or above. Age not updated.")
        else:
            self.__age = new_age

    def display_info(self):
        print(f"Name : {self.name}\nAge : {self.age}\nRole:  {self.role}")


class Staff(Person):
    def __init__(self, name, age, role, department, salary):
        super().__init__(name, age, role)
        self.department = department
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Department : {self.department}\nSalary : ₦{self.salary}\n")

    def give_raise(self, amount):
        self.salary += amount
        print(
            f"{self.name} received a raise of ₦{amount}. New salary: ₦{self.salary}\n"
        )


class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def display_expense(self):
        print(
            f"Description : {self.description} \nAmount : {self.amount} \nCategory : {self.category}\n"
        )

    def update_amount(self, new_amount):
        self.amount = new_amount
        print(f"✔ {self.description} updated to ₦{self.amount} \n")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.expenses = []
        self.staff_list = []
        self.income = 0

    def add_expense(self, expense_object):
        self.expenses.append(expense_object)

    def add_income(self, amount):
        self.income += amount

    def add_staff(self, staff_object):
        self.staff_list.append(staff_object)

        description = f"{staff_object.name}'s salary"
        amount = staff_object.salary
        category = "staff Salary"
        expense = Expense(description, amount, category)
        self.expenses.append(expense)

    def calculate_profit(self):
        total_expenses = 0
        for expens in self.expenses:
            total_expenses += expens.amount
        profit = self.income - total_expenses

        print(
            f"Department : {self.department_name} \nIncome : ₦{self.income} \nExpenses : ₦{total_expenses} \nProfit : ₦{profit}\n"
        )


dept1 = Department("Production")
dept2 = Department("Distribution")
dept3 = Department("Operations")

staff1 = Staff("Emeka Obi", 34, "Baker", "Production", 85000)
staff2 = Staff("Ngozi Eze", 28, "Driver", "Distribution", 60000)
staff3 = Staff("Chidi Nwosu", 41, "Manager", "Operations", 150000)

expense1 = Expense("Flour Purchase", 45000, "Raw Material")
expense2 = Expense("Van Maintenance", 25000, "Maintenance")
expense3 = Expense("Generator Fuel", 18000, "Utility")
expense4 = Expense("Yeast Purchase", 12000, "Raw Material")



# Add staff to their departments
# add_staff() automatically records their salary as an expense
dept1.add_staff(staff1)  # Emeka → Production
dept2.add_staff(staff2)  # Ngozi → Distribution
dept3.add_staff(staff3)  # Chidi → Operations

# Add expenses to their departments
dept1.add_expense(expense1)  # Flour → Production
dept2.add_expense(expense2)  # Van Maintenance → Distribution
dept3.add_expense(expense3)  # Generator Fuel → Operations

dept1 = Department("Production")
dept2 = Department("Distribution")
dept3 = Department("Operations")

# Record income for each department
dept1.add_income(320000)
dept2.add_income(180000)
dept3.add_income(0)

# Calculate profit or loss for each department
dept1.calculate_profit()
dept2.calculate_profit()
dept3.calculate_profit()


print("\n" + "═" * 45)
print("   DAVID'S BAKERY — FINAL FINANCIAL REPORT")
print("═" * 45)

dept1.calculate_profit()
dept2.calculate_profit()
dept3.calculate_profit()

total_income = dept1.income + dept2.income + dept3.income
total_expenses = (
    sum(e.amount for e in dept1.expenses)
    + sum(e.amount for e in dept2.expenses)
    + sum(e.amount for e in dept3.expenses)
)
net_profit = total_income - total_expenses

print("═" * 45)
print(f"  Total Income   : ₦{total_income:,.0f}")
print(f"  Total Expenses : ₦{total_expenses:,.0f}")
print(f"  NET PROFIT     : ₦{net_profit:,.0f}")
print("═" * 45)
