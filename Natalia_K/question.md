You are right, I played it too safe. Let me put the financial tracking back in but keep it structured so it is teachable. Here is the redesigned question:

---

# David's Bakery — Staff, Expense & Financial Tracker

## Background

David owns a bakery in Calabar. After returning from Lagos, his financial analyst gave him one clear instruction:

> *"David, you cannot fix what you cannot see. Start by tracking your people, your money, and your departments."*

So David decides to build a Python program that tracks three things:

1. The **staff** who work in his bakery
2. The **expenses** the bakery records every day
3. The **departments** and whether each one is making a profit or a loss

---

## The Class Structure

```
Person          ←  base class (encapsulation lives here)
   │
   └──  Staff   ←  inherits from Person (adds salary + department)

Expense         ←  standalone class (tracks one expense)

Department      ←  standalone class (holds expenses, calculates profit/loss)
```

Four classes total. Each one has a clear job.

---

## Class 1: `Person`

This is the base class. It holds basic information about any person connected to the bakery.

### Attributes

| Attribute | Description | Example |
|---|---|---|
| `__name` | Private. The person's full name | `"Emeka Obi"` |
| `__age` | Private. The person's age | `34` |
| `role` | Public. Their role in the bakery | `"Baker"` |

> **Why private?** An employee's personal details should not be freely editable from anywhere in the program. The double underscore forces every part of the code to go through your controlled methods to read or change the data. This is **encapsulation** in practice.

### Methods

**`__init__(self, name, age, role)`**
Stores name and age as private attributes (`self.__name`, `self.__age`) and role as public.

**`get_name(self)`**
Returns `self.__name`. This is a getter — the only way to read the private name from outside the class.

**`get_age(self)`**
Returns `self.__age`. Same concept — controlled read access.

**`set_age(self, new_age)`**
This is a setter. Before updating, check: if `new_age` is less than 18, print an error and do not update. Otherwise update `self.__age` and confirm. This shows why encapsulation matters — you control how data is changed, not just whether it can be seen.

**`display_info(self)`**
Prints the person's name, age, and role in a clean readable format. Must use `get_name()` and `get_age()` internally to access the private attributes.

---

## Class 2: `Staff` (inherits from `Person`)

Represents a bakery employee. Inherits everything from `Person` and adds what is specific to staff.

> **Why inheritance?** Every staff member is a person, but not every person is staff. A supplier is a Person but has no salary or department. Inheritance means you build on what already exists instead of rewriting it.

### Additional Attributes

| Attribute | Description | Example |
|---|---|---|
| `department` | Which department they work in | `"Production"` |
| `salary` | Monthly salary in Naira | `85000` |

### Methods

**`__init__(self, name, age, role, department, salary)`**
Calls `super().__init__(name, age, role)` first to handle the inherited attributes, then sets `department` and `salary`.

**`display_info(self)`**
Overrides the parent version. Calls `super().display_info()` first to print the basic person info, then prints department and salary below. This is **method overriding** — the child customises what it inherited.

**`give_raise(self, amount)`**
Adds `amount` to `self.salary`. Prints the staff member's name (using `get_name()`), the raise amount, and the new salary after the raise.

---

## Class 3: `Expense`

Represents one business expense anywhere in the bakery.

### Attributes

| Attribute | Description | Example |
|---|---|---|
| `description` | What the expense is for | `"Flour Purchase"` |
| `amount` | How much was spent in Naira | `45000` |
| `category` | Type of expense | `"Raw Material"` |

### Methods

**`__init__(self, description, amount, category)`**
Sets up the three attributes.

**`display_expense(self)`**
Prints the description, amount formatted as ₦45,000, and category clearly.

**`update_amount(self, new_amount)`**
Replaces the current amount with `new_amount` and prints a confirmation. Used when an expense was recorded incorrectly.

---

## Class 4: `Department`

This is where the financial tracking lives. Each department independently tracks its own expenses and income, then reports whether it is profitable or bleeding money. This is exactly how David's analyst told him to think about his business.

### Attributes

| Attribute | Description | Example |
|---|---|---|
| `department_name` | Name of this department | `"Production"` |
| `expenses` | A list of `Expense` objects belonging to this department. Starts empty | `[]` |
| `income` | Total income recorded for this department. Starts at zero | `0` |

### Methods

**`__init__(self, department_name)`**
Sets `department_name`, initialises `expenses` as an empty list, and `income` as zero.

**`add_expense(expense_object)`**
Takes an `Expense` object and adds it to the `expenses` list. Prints a confirmation showing the expense description and amount. This is **composition** — a Department object owns and manages a collection of Expense objects.

**`add_income(self, amount)`**
Adds `amount` to `self.income`. Prints the amount added and the new running total income for this department.

**`add_staff(self, staff_object)`**
Takes a `Staff` object and automatically adds that staff member's salary as an expense into this department's `expenses` list. It should create a new `Expense` object internally using the staff member's name, salary, and category `"Salary"`, then append it to `self.expenses`. Print a confirmation. This is where `Staff` and `Department` connect — adding a staff member to a department automatically registers their salary as a cost.

**`calculate_profit(self)`**
Loops through every `Expense` object in `self.expenses`, adds up all the amounts to get total expenses, then subtracts from `self.income`. Prints a clear summary:
- Department name
- Total income
- Total expenses
- Whether the result is a PROFIT or a LOSS and by how much

Returns the profit or loss value.

---

## Sample Data to Use When Testing

### Staff Members

| Name | Age | Role | Department | Salary |
|---|---|---|---|---|
| Emeka Obi | 34 | Baker | Production | ₦85,000 |
| Ngozi Eze | 28 | Driver | Distribution | ₦60,000 |
| Chidi Nwosu | 41 | Manager | Operations | ₦150,000 |

### Expenses

| Description | Amount | Category | Belongs To |
|---|---|---|---|
| Flour Purchase | ₦45,000 | Raw Material | Production |
| Generator Fuel | ₦18,000 | Utility | Operations |
| Van Maintenance | ₦25,000 | Maintenance | Distribution |

### Income Per Department

| Department | Income This Month |
|---|---|
| Production | ₦320,000 |
| Distribution | ₦180,000 |
| Operations | ₦0 |

---

## What Your Test Code Must Do

Write this at the bottom of your file in this exact order:

```
1. Create three Staff objects using the sample data above
2. Call display_info() on each staff member
3. Test set_age() with a valid age and then with an age below 18
4. Give Emeka a raise of ₦10,000
5. Create three Department objects: Production, Distribution, Operations
6. Add each staff member to their correct department using add_staff()
7. Create the three Expense objects and add each to its correct department
8. Record the income for each department using add_income()
9. Call calculate_profit() on each department and observe the results
10. Update the flour expense to ₦48,000 and call calculate_profit() 
    on Production again to see how the number changes
```

Step 10 is the most important one. It shows students that when an expense object changes, the department's financial result changes too — because the department holds a reference to the real object, not a copy.

---

## Final Expected Output Summary

| Department | Income | Expenses | Result |
|---|---|---|---|
| Production | ₦320,000 | ₦133,000 (Emeka salary + flour) | **PROFIT ₦187,000** |
| Distribution | ₦180,000 | ₦85,000 (Ngozi salary + van maintenance) | **PROFIT ₦95,000** |
| Operations | ₦0 | ₦168,000 (Chidi salary + generator fuel) | **LOSS ₦168,000** |

Operations has zero income and high staff costs. That is the conversation starter — *why is the Operations department recording no income? Where is that money going?* That is the real-world problem this system is designed to surface.

---

## OOP Concepts Covered

| Concept | Where It Appears |
|---|---|
| Classes and objects | All four classes |
| Constructors | All four classes |
| Encapsulation | `__name` and `__age` in `Person`, getters and setters |
| Inheritance | `Staff` inheriting from `Person` |
| Method overriding | `display_info()` in `Staff` |
| `super()` | `Staff.__init__()` and `Staff.display_info()` |
| Composition | `Department` owns a list of `Expense` objects |
| Cross-object interaction | `add_staff()` reads a `Staff` object to create an `Expense` |

---

## A Note on Static and Class Methods

They do not appear in this task because there is no honest place for them yet. They will appear in the next task where you need a method that counts how many `Department` objects have been created across the entire program — at that point a `@classmethod` earns its place naturally. Forcing it here would teach bad habits.

---

This covers encapsulation, inheritance, composition, cross-object interaction, and real financial logic — all connected to David's actual problem. The story arc is intact: David cannot find his profit, the system surfaces that Operations is losing money, and the students see exactly why.
