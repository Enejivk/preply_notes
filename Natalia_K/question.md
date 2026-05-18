Here is the full capstone project with test objects built into each class section:

---

# OOP Capstone Project: David's Bakery Management System

**Course:** Object-Oriented Programming with Python
**Type:** Capstone Project
**Submission:** Single `.py` file with all classes and test code at the bottom

---

## The Problem

David owns a bakery in Calabar. For months, his bakery was making sales every single day — bread was produced, vans went out every morning, customers bought bread — but at the end of every month, there was no profit left. Money was disappearing and David could not explain where.

His financial analyst sat him down and said:

> *"David, your bakery is not dying because sales stopped. Your problem is that you have no system. You cannot see your money. You do not know which part of your business is healthy and which part is bleeding. Until you can see it, you cannot fix it."*

Your job as a developer is to build the system David needs. You will use Python and Object-Oriented Programming to model his bakery, track his staff, record his expenses, and produce a financial report that tells David exactly where his money is going — and which department is causing the loss.

---

## Class 1: `Person`

### Purpose
Holds personal information about any individual connected to the bakery. Personal data must be protected from being freely read or changed outside the class.

### Attributes
- `__name` — private
- `__age` — private
- `role` — public

### Methods

| Method | What It Must Do |
|---|---|
| `get_name()` | Returns the private name. The only way to read it from outside the class |
| `get_age()` | Returns the private age |
| `set_age(new_age)` | If `new_age` is below 18, print an error and do not update. Otherwise update and confirm |
| `display_info()` | Prints name, age, and role in a readable format using `get_name()` and `get_age()` |

---

### Test Objects for `Person`

After you write the `Person` class, create these three objects and test every method on each one:

```python
person1 = Person("Amara Okafor", 30, "Supplier")
person2 = Person("Tunde Bello", 45, "Accountant")
person3 = Person("Chisom Eze", 25, "Visitor")
```

### What to Call on Each Object

```python
# Test display_info()
person1.display_info()
person2.display_info()
person3.display_info()

# Test get_name() and get_age()
print(person1.get_name())
print(person2.get_age())

# Test set_age() with a valid age
person1.set_age(31)

# Test set_age() with an invalid age — should print an error
person2.set_age(15)

# Test set_age() on person3 with a valid age
person3.set_age(26)
```

### Expected Output for `Person`

```
  Name : Amara Okafor
  Age  : 30
  Role : Supplier

  Name : Tunde Bello
  Age  : 45
  Role : Accountant

  Name : Chisom Eze
  Age  : 25
  Role : Visitor

Amara Okafor
45

  ✔ Amara Okafor's age updated to 31
  ✖ Error: Age must be 18 or above. Age not updated.
  ✔ Chisom Eze's age updated to 26
```

---

## Class 2: `Staff` (inherits from `Person`)

### Purpose
Represents a bakery employee. Inherits everything from `Person` and adds what is specific to a staff member — their department and salary.

### Additional Attributes
- `department` — which bakery section they work in
- `salary` — monthly salary in Naira

### Methods

| Method | What It Must Do |
|---|---|
| `__init__()` | Call `super().__init__()` to handle inherited attributes, then set `department` and `salary` |
| `display_info()` | Override the parent method. Call `super().display_info()` first, then print department and salary |
| `give_raise(amount)` | Add `amount` to salary. Print staff name using `get_name()`, the raise amount, and the new salary |

---

### Test Objects for `Staff`

After you write the `Staff` class, create these three objects and test every method:

```python
staff1 = Staff("Emeka Obi", 34, "Baker", "Production", 85000)
staff2 = Staff("Ngozi Eze", 28, "Driver", "Distribution", 60000)
staff3 = Staff("Chidi Nwosu", 41, "Manager", "Operations", 150000)
```

### What to Call on Each Object

```python
# Test display_info() — should print both Person info and Staff info
staff1.display_info()
staff2.display_info()
staff3.display_info()

# Test give_raise()
staff1.give_raise(10000)
staff2.give_raise(5000)
staff3.give_raise(20000)

# Test that set_age() still works — inherited from Person
staff1.set_age(16)    # should fail
staff1.set_age(35)    # should succeed
```

### Expected Output for `Staff`

```
  Name       : Emeka Obi
  Age        : 34
  Role       : Baker
  Department : Production
  Salary     : ₦85,000

  Name       : Ngozi Eze
  Age        : 28
  Role       : Driver
  Department : Distribution
  Salary     : ₦60,000

  Name       : Chidi Nwosu
  Age        : 41
  Role       : Manager
  Department : Operations
  Salary     : ₦150,000

  ✔ Emeka Obi received a raise of ₦10,000. New salary: ₦95,000
  ✔ Ngozi Eze received a raise of ₦5,000. New salary: ₦65,000
  ✔ Chidi Nwosu received a raise of ₦20,000. New salary: ₦170,000

  ✖ Error: Age must be 18 or above. Age not updated.
  ✔ Emeka Obi's age updated to 35
```

---

## Class 3: `Expense`

### Purpose
Represents one recorded expense anywhere in the bakery. Every naira that leaves the business must be captured as an `Expense` object.

### Attributes
- `description` — what the money was spent on
- `amount` — how much was spent in Naira
- `category` — the type of expense

### Methods

| Method | What It Must Do |
|---|---|
| `display_expense()` | Prints description, amount formatted with ₦ and commas, and category |
| `update_amount(new_amount)` | Replaces current amount with new value and prints a confirmation |

---

### Test Objects for `Expense`

After you write the `Expense` class, create these four objects and test every method:

```python
expense1 = Expense("Flour Purchase", 45000, "Raw Material")
expense2 = Expense("Van Maintenance", 25000, "Maintenance")
expense3 = Expense("Generator Fuel", 18000, "Utility")
expense4 = Expense("Yeast Purchase", 12000, "Raw Material")
```

### What to Call on Each Object

```python
# Test display_expense() on all four
expense1.display_expense()
expense2.display_expense()
expense3.display_expense()
expense4.display_expense()

# Test update_amount() — simulating a correction
expense1.update_amount(48000)
expense4.update_amount(14000)

# Display again after update to confirm the change
expense1.display_expense()
expense4.display_expense()
```

### Expected Output for `Expense`

```
  Description : Flour Purchase
  Amount      : ₦45,000
  Category    : Raw Material

  Description : Van Maintenance
  Amount      : ₦25,000
  Category    : Maintenance

  Description : Generator Fuel
  Amount      : ₦18,000
  Category    : Utility

  Description : Yeast Purchase
  Amount      : ₦12,000
  Category    : Raw Material

  ✔ Flour Purchase updated to ₦48,000
  ✔ Yeast Purchase updated to ₦14,000

  Description : Flour Purchase
  Amount      : ₦48,000
  Category    : Raw Material

  Description : Yeast Purchase
  Amount      : ₦14,000
  Category    : Raw Material
```

---

## Class 4: `Department`

### Purpose
The financial engine of the system. Each department tracks its own staff, expenses, and income independently, then reports whether it is making a profit or bleeding money. This is what gives David the answer he needs.

### Attributes
- `department_name` — name of the section
- `expenses` — empty list, will hold `Expense` objects
- `staff_list` — empty list, will hold `Staff` objects
- `income` — starts at zero

### Methods

| Method | What It Must Do |
|---|---|
| `add_expense(expense_object)` | Adds an `Expense` object to `self.expenses`. Prints confirmation with description and amount |
| `add_income(amount)` | Adds amount to `self.income`. Prints amount added and new running total |
| `add_staff(staff_object)` | Adds `Staff` object to `self.staff_list`. Automatically creates a new `Expense` from the staff member's salary and appends it to `self.expenses`. Prints confirmation |
| `calculate_profit()` | Loops through all expenses, totals them, subtracts from income, prints full department summary, returns the result |

---

### Test Objects for `Department`

After you write the `Department` class, create these three objects. You will reuse the `Staff` and `Expense` objects you already created above:

```python
dept1 = Department("Production")
dept2 = Department("Distribution")
dept3 = Department("Operations")
```

### What to Call on Each Object

```python
# Add staff to their departments
# add_staff() automatically records their salary as an expense
dept1.add_staff(staff1)      # Emeka → Production
dept2.add_staff(staff2)      # Ngozi → Distribution
dept3.add_staff(staff3)      # Chidi → Operations

# Add expenses to their departments
dept1.add_expense(expense1)  # Flour → Production
dept2.add_expense(expense2)  # Van Maintenance → Distribution
dept3.add_expense(expense3)  # Generator Fuel → Operations

# Record income for each department
dept1.add_income(320000)
dept2.add_income(180000)
dept3.add_income(0)

# Calculate profit or loss for each department
dept1.calculate_profit()
dept2.calculate_profit()
dept3.calculate_profit()
```

### Expected Output for `Department`

```
  ✔ Emeka Obi added to Production
  ✔ Salary expense recorded: Emeka Obi — ₦85,000

  ✔ Ngozi Eze added to Distribution
  ✔ Salary expense recorded: Ngozi Eze — ₦60,000

  ✔ Chidi Nwosu added to Operations
  ✔ Salary expense recorded: Chidi Nwosu — ₦150,000

  ✔ Expense added to Production: Flour Purchase — ₦45,000
  ✔ Expense added to Distribution: Van Maintenance — ₦25,000
  ✔ Expense added to Operations: Generator Fuel — ₦18,000

  ✔ Income recorded: ₦320,000 | Production total income: ₦320,000
  ✔ Income recorded: ₦180,000 | Distribution total income: ₦180,000
  ✔ Income recorded: ₦0 | Operations total income: ₦0

  ─────────────────────────────────────
  Department  : Production
  Income      : ₦320,000
  Expenses    : ₦130,000
  ─────────────────────────────────────
  ✔ PROFIT    : ₦190,000
  ─────────────────────────────────────

  ─────────────────────────────────────
  Department  : Distribution
  Income      : ₦180,000
  Expenses    : ₦85,000
  ─────────────────────────────────────
  ✔ PROFIT    : ₦95,000
  ─────────────────────────────────────

  ─────────────────────────────────────
  Department  : Operations
  Income      : ₦0
  Expenses    : ₦168,000
  ─────────────────────────────────────
  ✖ LOSS      : ₦168,000
  ─────────────────────────────────────
```

---

## Final Step: The Complete Financial Report

After all four classes are working and all individual tests pass, write one final block of code at the very bottom of your file that prints the complete bakery report. This is what David reads to make his business decision.

```python
print("\n" + "═"*45)
print("   DAVID'S BAKERY — FINAL FINANCIAL REPORT")
print("═"*45)

dept1.calculate_profit()
dept2.calculate_profit()
dept3.calculate_profit()

total_income   = dept1.income + dept2.income + dept3.income
total_expenses = sum(e.amount for e in dept1.expenses) + \
                 sum(e.amount for e in dept2.expenses) + \
                 sum(e.amount for e in dept3.expenses)
net_profit     = total_income - total_expenses

print("═"*45)
print(f"  Total Income   : ₦{total_income:,.0f}")
print(f"  Total Expenses : ₦{total_expenses:,.0f}")
print(f"  NET PROFIT     : ₦{net_profit:,.0f}")
print("═"*45)
```

### Final Expected Output

```
═════════════════════════════════════════════
   DAVID'S BAKERY — FINAL FINANCIAL REPORT
═════════════════════════════════════════════

  ─────────────────────────────────────
  Department  : Production
  Income      : ₦320,000
  Expenses    : ₦130,000
  ─────────────────────────────────────
  ✔ PROFIT    : ₦190,000
  ─────────────────────────────────────

  ─────────────────────────────────────
  Department  : Distribution
  Income      : ₦180,000
  Expenses    : ₦85,000
  ─────────────────────────────────────
  ✔ PROFIT    : ₦95,000
  ─────────────────────────────────────

  ─────────────────────────────────────
  Department  : Operations
  Income      : ₦0
  Expenses    : ₦168,000
  ─────────────────────────────────────
  ✖ LOSS      : ₦168,000
  ─────────────────────────────────────

═════════════════════════════════════════════
  Total Income   : ₦500,000
  Total Expenses : ₦383,000
  NET PROFIT     : ₦117,000
═════════════════════════════════════════════
```

---

## Business Conclusion

The report gives David three things he can act on immediately:

**Production and Distribution are healthy.** Both departments are earning more than they spend. The core business — baking bread and delivering it — is working correctly.

**Operations is the crisis department.** It recorded zero income this month while spending ₦168,000. Chidi's salary alone is ₦150,000. David must now ask one serious question: what is the Operations department producing that justifies this cost? If a department earns nothing, every naira it spends is a direct cut from the overall profit.

**The bakery's survival margin is thin.** ₦117,000 net profit on ₦500,000 income is 23.4%. That is fragile. One bad month in Distribution or one unexpected expense in Production wipes out the entire profit. The system has shown David that he is not losing money to theft or magic — he is losing it to an unproductive department that nobody was watching.

**David's decision:** Restructure Operations. Either assign it a revenue-generating function, redistribute its costs across Production and Distribution where they actually belong, or reduce the management cost. Without this system, David would have kept staring at an empty account wondering why. Now he knows exactly where to look.

---

## OOP Concepts Demonstrated

| Concept | Where It Appears |
|---|---|
| Classes and objects | All four classes |
| Constructors | All four classes |
| Encapsulation | `__name` and `__age` in `Person`; getters and setters |
| Inheritance | `Staff` inheriting from `Person` |
| Method overriding | `display_info()` redefined in `Staff` |
| `super()` | `Staff.__init__()` and `Staff.display_info()` |
| Composition | `Department` owns lists of `Expense` and `Staff` objects |
| Cross-object interaction | `add_staff()` reads a `Staff` object to create an `Expense` automatically |
| Loops over objects | `calculate_profit()` loops through the expenses list |
| Financial logic | Real profit and loss calculation from real business data |
