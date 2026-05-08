# Object-Oriented Programming in Python
## Comprehensive Lecture Notes — Encapsulation & Class Design

---

> **Course:** Object-Oriented Programming with Python
> **Topic Series:** Encapsulation, Access Control, Properties, and Class Structure

---

## Table of Contents

1. [Introduction to Encapsulation](#1-introduction-to-encapsulation)
2. [Public Attributes and Methods](#2-public-attributes-and-methods)
3. [Protected Attributes and Methods](#3-protected-attributes-and-methods)
4. [Private Attributes and Methods](#4-private-attributes-and-methods)
5. [Access Modifiers in Python](#5-access-modifiers-in-python)
6. [Getters and Setters](#6-getters-and-setters)
7. [Properties in Python](#7-properties-in-python)
8. [Static Attributes (Class Attributes)](#8-static-attributes-class-attributes)
9. [Static Methods](#9-static-methods)
10. [Comparing Different Types of Methods](#10-comparing-different-types-of-methods)
11. [Combining Everything in One Class](#11-combining-everything-in-one-class)
12. [Best Practices and Common Mistakes](#12-best-practices-and-common-mistakes)

---

## 1. Introduction to Encapsulation

### What is Encapsulation?

Encapsulation is one of the four core principles of Object-Oriented Programming (OOP). It refers to the practice of **bundling data (attributes) and the methods (functions) that operate on that data together inside a single unit — the class** — while also **controlling how that data is accessed or modified from outside the class**.

Think of it like a capsule (a medicine pill). The ingredients inside the capsule are hidden and protected. You take the pill as a whole; you do not reach inside and adjust the ingredients yourself.

In programming, encapsulation means:
- The internal state (data) of an object is hidden from the outside world.
- The outside world can only interact with that data through controlled, well-defined interfaces (methods).

### Why Do We Hide and Control Data?

There are several important reasons to hide and control data in OOP:

**1. Data Integrity**
If any part of your program could freely change an object's internal data, errors and bugs become very hard to track. Encapsulation ensures data is only changed in controlled and validated ways.

**2. Security**
Some data is sensitive (e.g., passwords, bank balances). Hiding it prevents unintended or malicious access.

**3. Flexibility and Maintainability**
If you later decide to change how data is stored internally, code that uses your class does not need to change, as long as the public interface stays the same.

**4. Reduced Complexity**
Users of a class only need to know *what* it does, not *how* it does it. This reduces cognitive overhead.

### Direct Access vs Controlled Access

**Direct Access** — Anyone can read or change the data:

```python
class BankAccount:
    def __init__(self):
        self.balance = 1000  # Directly accessible

account = BankAccount()
account.balance = -500  # No check! This is dangerous.
print(account.balance)  # -500
```

**Controlled Access** — Data is accessed and modified through methods:

```python
class BankAccount:
    def __init__(self):
        self.__balance = 1000  # Hidden

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(500)
print(account.get_balance())  # 1500
# account.__balance = -500  # This will NOT work as expected
```

Controlled access gives you a gatekeeper — the methods — that can validate, log, or transform data before it is stored or returned.

---

### 📝 Tasks — Lesson 1

**Task 1:** In your own words, define encapsulation and explain why it is useful in software development. Give a real-world analogy (not the pill example used above).

**Task 2:** Look at the code below. Identify the problem with direct access and explain what could go wrong:
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Alice", 20)
s.age = -5
print(s.age)
```

**Task 3:** Rewrite the `Student` class above so that the `age` attribute is protected from invalid values like negative numbers. Use a method called `set_age()` to control how age is assigned.

**Task 4:** A `Car` class has an attribute `speed`. Write a version with direct access and a version with controlled access. In the controlled version, make sure speed cannot be set to a value greater than 200 or less than 0.

**Task 5:** List three real-world systems (software or physical) where encapsulation is used. For each, identify: (a) what data is hidden, (b) what the controlled interface is.

---

## 2. Public Attributes and Methods

### What Are Public Members?

In Python, **public attributes and methods** are accessible from anywhere — inside the class, outside the class, and inside subclasses. They are the default in Python; if you do not use any special prefix, the member is public.

### Creating Public Attributes

```python
class Person:
    def __init__(self, name, age):
        self.name = name   # public attribute
        self.age = age     # public attribute
```

### Creating Public Methods

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):           # public method
        return f"Hello, my name is {self.name}."

    def birthday(self):        # public method
        self.age += 1
```

### Accessing and Modifying Attributes Directly

```python
p = Person("Alice", 25)

# Accessing
print(p.name)        # Alice
print(p.age)         # 25

# Modifying
p.name = "Bob"
p.age = 30
print(p.name)        # Bob
print(p.age)         # 30
```

### Calling Public Methods

```python
print(p.greet())     # Hello, my name is Bob.
p.birthday()
print(p.age)         # 31
```

### When Are Public Members Useful?

Public members are appropriate when:
- The data does not require validation or protection.
- The attribute is genuinely meant to be read and changed freely.
- You are writing a simple, internal script where strict access control is not necessary.
- The attribute is a constant or a label (like a name or title) with no harmful side effects if changed.

> **Note:** In Python, there is no true "forced" access control at the language level. All access modifiers in Python are **conventions**. Python trusts developers to follow the rules.

---

### 📝 Tasks — Lesson 2

**Task 1:** Create a `Book` class with public attributes: `title`, `author`, and `pages`. Write a method `summary()` that returns a string describing the book. Create an object and call the method.

**Task 2:** Create a `Rectangle` class with public attributes `width` and `height`. Add a public method `area()` that returns the area and a method `perimeter()` that returns the perimeter. Test your class by creating two rectangle objects with different dimensions.

**Task 3:** Given the following class, write code that: (a) creates an object, (b) accesses and prints each attribute, (c) changes the `brand` attribute, and (d) calls the `describe()` method:
```python
class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def describe(self):
        return f"{self.brand} | RAM: {self.ram}GB | Storage: {self.storage}GB"
```

**Task 4:** Create a `Counter` class with a public attribute `count` starting at 0. Add three methods: `increment()`, `decrement()`, and `reset()`. Demonstrate using the counter to count from 0 to 5, then back to 3, then reset.

**Task 5:** Discuss: When is it a bad idea to make all attributes public? Give two specific scenarios where unrestricted public access to an attribute could lead to a bug or a security problem.

---

## 3. Protected Attributes and Methods

### What Are Protected Members?

In Python, **protected members** are indicated by a **single leading underscore** (`_attribute` or `_method`). This is a **convention** that signals to other developers: *"This member is intended for internal use within the class and its subclasses. Please do not access it from outside unless you know what you are doing."*

Python does **not** enforce this restriction technically — you can still access `_attribute` from outside — but it is considered bad practice to do so.

### Using Single Underscore `_attribute`

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name           # public
        self._salary = salary      # protected

    def _calculate_bonus(self):    # protected method
        return self._salary * 0.10

    def get_info(self):
        bonus = self._calculate_bonus()
        return f"{self.name} | Salary: {self._salary} | Bonus: {bonus}"
```

### Accessing Protected Members in Subclasses

The primary legitimate use of protected members is **within subclasses**:

```python
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def manager_info(self):
        # Accessing protected attribute from parent class — acceptable
        return f"Manager: {self.name} | Dept: {self.department} | Salary: {self._salary}"

m = Manager("John", 80000, "Engineering")
print(m.manager_info())
# Manager: John | Dept: Engineering | Salary: 80000
```

### Accessing Protected Members from Outside (Technically Possible but Not Recommended)

```python
e = Employee("Alice", 60000)
print(e._salary)          # Works, but you should not do this
e._salary = 999999        # Modifiable, but violates convention
```

### Python Convention for Protected Members

| What It Means | What It Does NOT Mean |
|---|---|
| Intended for internal or subclass use | The attribute is locked or inaccessible |
| A signal to other developers | A hard enforcement by Python |
| Should not be accessed from outside code | Cannot be accessed from outside code |

---

### 📝 Tasks — Lesson 3

**Task 1:** Create an `Animal` class with a protected attribute `_species` and a protected method `_make_sound()`. Then create a `Dog` subclass that inherits from `Animal` and calls `_make_sound()` inside a public method `speak()`. Demonstrate creating a `Dog` object and calling `speak()`.

**Task 2:** A `BankAccount` class has a protected attribute `_balance`. Create a `SavingsAccount` subclass that adds a method `apply_interest()` which increases `_balance` by 5%. Create a savings account with balance 1000 and apply interest twice, printing the balance each time.

**Task 3:** What is the output of the following code? Explain each line:
```python
class Vehicle:
    def __init__(self, speed):
        self._speed = speed

    def _display_speed(self):
        return f"Speed: {self._speed} km/h"

class Car(Vehicle):
    def show(self):
        return self._display_speed()

c = Car(120)
print(c.show())
print(c._speed)
```

**Task 4:** Explain the difference between accessing a protected member from within a subclass versus accessing it from completely outside the class hierarchy. Why is one acceptable and the other discouraged?

**Task 5:** Create a `School` class with protected attributes `_school_name` and `_principal_name`. Create a `Teacher` subclass and a `Student` subclass. Each subclass should have a method that uses the protected attributes to print their school details. Demonstrate creating objects of both subclasses.

---

## 4. Private Attributes and Methods

### What Are Private Members?

In Python, **private members** are indicated by a **double leading underscore** (`__attribute` or `__method`). Unlike protected members, Python does apply a technical mechanism here called **name mangling**.

### Using Double Underscore `__attribute`

```python
class Person:
    def __init__(self, name, password):
        self.name = name
        self.__password = password    # private

    def __validate(self):             # private method
        return len(self.__password) >= 8

    def check_password(self, entered):
        if entered == self.__password:
            return "Access granted."
        return "Access denied."
```

### Name Mangling in Python

When you use `__attribute`, Python automatically renames it internally to `_ClassName__attribute`. This means:

```python
p = Person("Alice", "secret123")

# Direct access fails:
# print(p.__password)   # AttributeError

# But name mangling exposes it like this (avoid this in real code):
print(p._Person__password)   # secret123 — technically accessible but strongly discouraged
```

Name mangling is not true privacy — it is a safety mechanism that makes accidental access harder, and signals intent very strongly.

### Why Private Members Are Important

- They enforce a clear contract: "Only this class should touch this data."
- They prevent subclasses from accidentally overriding internal attributes.
- They are ideal for sensitive data (passwords, PINs, tokens).

### Hiding Sensitive Data

```python
class UserAccount:
    def __init__(self, username, pin):
        self.username = username
        self.__pin = pin            # Hidden from outside

    def verify_pin(self, entered_pin):
        return entered_pin == self.__pin

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            if len(str(new_pin)) == 4:
                self.__pin = new_pin
                return "PIN updated successfully."
            return "PIN must be 4 digits."
        return "Old PIN is incorrect."

user = UserAccount("alice99", 1234)
print(user.verify_pin(1234))          # True
print(user.change_pin(1234, 5678))    # PIN updated successfully.
print(user.verify_pin(1234))          # False
```

---

### 📝 Tasks — Lesson 4

**Task 1:** Create a `CreditCard` class with a private attribute `__card_number`. Add a method `get_masked_number()` that returns only the last 4 digits (e.g., `"**** **** **** 4321"`). Demonstrate that direct access to `__card_number` raises an error.

**Task 2:** Explain name mangling with an example. What does Python rename `__secret` to in a class called `Config`? Write code to prove it.

**Task 3:** A `Student` class has a private attribute `__gpa`. Write the class so that: (a) GPA cannot be accessed directly, (b) a method `is_honor_student()` returns `True` if GPA ≥ 3.5, and (c) a method `update_gpa(new_gpa)` validates that the new GPA is between 0.0 and 4.0 before updating.

**Task 4:** What is the difference between `_attr` (single underscore) and `__attr` (double underscore) in Python? Write a table comparing: convention vs enforcement, accessibility from subclass, accessibility from outside, and name mangling.

**Task 5:** Create a `Hospital` class with a private attribute `__patient_records` (a dictionary). Add methods to: (a) add a patient record (name → diagnosis), (b) retrieve a record by name, and (c) delete a record. Ensure the dictionary itself cannot be accessed directly from outside the class.

---

## 5. Access Modifiers in Python

### Overview of All Three Levels

Python has three access levels, all enforced by convention (with name mangling for private):

| Level | Syntax | Convention | Accessible From |
|---|---|---|---|
| Public | `attribute` | No underscore | Everywhere |
| Protected | `_attribute` | Single underscore | Class + Subclasses (by convention) |
| Private | `__attribute` | Double underscore | Only within the class |

### Public Members

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius       # Public

    def area(self):                # Public
        return 3.14159 * self.radius ** 2
```

### Protected Members

```python
class Shape:
    def __init__(self, color):
        self._color = color        # Protected

    def _describe(self):           # Protected
        return f"A {self._color} shape"
```

### Private Members

```python
class Vault:
    def __init__(self, code):
        self.__code = code         # Private

    def unlock(self, entered):     # Public interface to private data
        return entered == self.__code
```

### All Three in One Class

```python
class Employee:
    def __init__(self, name, department, salary):
        self.name = name               # public
        self._department = department  # protected
        self.__salary = salary         # private

    def get_summary(self):             # public
        return f"{self.name} - {self._department}"

    def _calculate_tax(self):          # protected
        return self.__salary * 0.2

    def __apply_raise(self, percent):  # private
        self.__salary += self.__salary * (percent / 100)

    def give_raise(self, percent):     # public interface to private method
        self.__apply_raise(percent)
        return f"New salary: {self.__salary}"
```

### Differences and Choosing the Right Level

**Choose Public when:**
- The attribute is genuinely part of the class's public interface.
- It is safe and reasonable for external code to read and modify.

**Choose Protected when:**
- The attribute is an internal implementation detail, but subclasses may need it.
- You want to signal "internal use" without hard enforcement.

**Choose Private when:**
- The attribute is sensitive (passwords, IDs, financial data).
- You do not want subclasses or outside code to touch it.
- You want name mangling to prevent accidental access.

---

### 📝 Tasks — Lesson 5

**Task 1:** For each of the following attributes, decide whether it should be public, protected, or private. Justify each decision:
- A `username` in a social media profile
- A `__encryption_key` in a security system
- A `_base_salary` in an `Employee` class where subclasses like `Manager` need to compute bonuses
- A `title` of a blog post
- A `__session_token` in a web authentication class

**Task 2:** Create a `University` class with:
- A public attribute: `name`
- A protected attribute: `_ranking`
- A private attribute: `__funding_amount`

Add appropriate public methods to access and display all three values. Demonstrate creating an object and calling those methods.

**Task 3:** Write a `Vehicle` class and a `Truck` subclass. In `Vehicle`, create one attribute of each type (public, protected, private). In the `Truck` subclass, try to access all three from within a method. Describe and demonstrate what happens with each.

**Task 4:** Create a `Config` class that stores application settings. Some settings are public (theme, language), some are protected (server_url), and one is private (api_key). Demonstrate proper access patterns for each type.

**Task 5:** Why does Python use conventions rather than hard enforcement for access control? Write a short paragraph discussing the philosophy of "we are all consenting adults" in Python design and whether you think hard enforcement (like in Java) would be better or worse for Python programs.

---

## 6. Getters and Setters

### Why Are Getters and Setters Needed?

Even though Python allows direct access to public attributes, there are situations where you need to:
- **Validate** data before it is stored.
- **Compute** a value before returning it.
- **Log** or **notify** when data changes.
- **Hide** the internal structure of data.

Getters and setters are methods that provide this controlled access.

### Creating Getter Methods

A **getter** retrieves the value of a private or protected attribute:

```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_celsius(self):           # Getter
        return self.__celsius

    def get_fahrenheit(self):        # Computed getter
        return (self.__celsius * 9/5) + 32

t = Temperature(100)
print(t.get_celsius())      # 100
print(t.get_fahrenheit())   # 212.0
```

### Creating Setter Methods

A **setter** allows controlled modification of a private or protected attribute:

```python
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_celsius(self):
        return self.__celsius

    def set_celsius(self, value):    # Setter
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self.__celsius = value

t = Temperature(25)
t.set_celsius(100)
print(t.get_celsius())   # 100

# t.set_celsius(-300)    # Raises ValueError
```

### Data Validation Using Setters

```python
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)       # Use setter in __init__ for validation

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.__name = name

    def set_age(self, age):
        if not isinstance(age, int) or age < 5 or age > 120:
            raise ValueError("Age must be an integer between 5 and 120.")
        self.__age = age

s = Student("Alice", 20)
print(s.get_name())   # Alice
print(s.get_age())    # 20

s.set_age(25)
print(s.get_age())    # 25

# s.set_age(-1)       # ValueError
```

### Preventing Invalid Data Assignment

The key benefit of setters is acting as a **gatekeeper**:

```python
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = round(price, 2)

p = Product("Laptop", 999.999)
print(p.get_price())   # 1000.0
```

---

### 📝 Tasks — Lesson 6

**Task 1:** Create a `Circle` class with a private attribute `__radius`. Add a getter `get_radius()` and a setter `set_radius()` that ensures the radius is a positive number. Also add a getter `get_area()` that computes and returns the area.

**Task 2:** Create a `Person` class where `__age` is private. The setter `set_age()` should reject values less than 0 or greater than 150. The getter `get_age()` should return the age. In `__init__`, call the setter to validate age at creation.

**Task 3:** A `Rectangle` class has private `__width` and `__height`. Write getters and setters for both, ensuring neither can be zero or negative. Add a `get_area()` method. Demonstrate creating a rectangle, changing one dimension with a setter, and printing the area.

**Task 4:** What is the output of the following code? Trace through it step by step:
```python
class Counter:
    def __init__(self):
        self.__count = 0

    def get_count(self):
        return self.__count

    def set_count(self, value):
        if value < 0:
            print("Count cannot be negative. Setting to 0.")
            self.__count = 0
        else:
            self.__count = value

c = Counter()
c.set_count(5)
print(c.get_count())
c.set_count(-3)
print(c.get_count())
c.set_count(10)
print(c.get_count())
```

**Task 5:** Create a `UserProfile` class with private attributes: `__username`, `__email`, and `__age`. Write getters and setters for all three with the following validations:
- `username`: must be at least 3 characters, no spaces
- `email`: must contain `@` and `.`
- `age`: must be between 13 and 99

---

## 7. Properties in Python

### The Problem with Traditional Getters and Setters

Traditional getters and setters work, but they make code verbose and un-Pythonic:

```python
# Traditional (verbose):
student.set_age(21)
print(student.get_age())

# With properties (clean and Pythonic):
student.age = 21
print(student.age)
```

Properties let you use simple attribute syntax while still running getter/setter logic behind the scenes.

### Introduction to `@property`

The `@property` decorator turns a method into a "getter" that can be accessed like an attribute:

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):            # Getter — accessed as c.radius
        return self.__radius
```

```python
c = Circle(5)
print(c.radius)    # 5 — looks like attribute access, but calls the method
```

### Read-Only Properties

If you define only `@property` without a setter, the attribute becomes **read-only**:

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def area(self):                    # Computed read-only property
        return 3.14159 * self.__radius ** 2

c = Circle(7)
print(c.radius)    # 7
print(c.area)      # 153.938...

# c.radius = 10   # AttributeError: can't set attribute
```

### Writable Properties and Property Setters

To allow assignment, add a setter using `@property_name.setter`:

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):           # Setter
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self.__radius = value

c = Circle(5)
c.radius = 10        # Calls the setter
print(c.radius)      # 10

# c.radius = -3     # ValueError
```

### Full Example — Properties in Action

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius         # Calls the setter via @property

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self.__celsius = value

    @property
    def fahrenheit(self):              # Read-only computed property
        return (self.__celsius * 9/5) + 32

t = Temperature(100)
print(t.celsius)       # 100
print(t.fahrenheit)    # 212.0
t.celsius = 0
print(t.fahrenheit)    # 32.0
```

### Comparison: Traditional vs Property Approach

```python
# Traditional:
class OldStyle:
    def get_name(self): return self.__name
    def set_name(self, v): self.__name = v

obj.set_name("Alice")
print(obj.get_name())

# Pythonic with @property:
class NewStyle:
    @property
    def name(self): return self.__name
    @name.setter
    def name(self, v): self.__name = v

obj.name = "Alice"
print(obj.name)
```

---

### 📝 Tasks — Lesson 7

**Task 1:** Convert the following traditional getter/setter class to use Python `@property`:
```python
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self): return self.__width
    def set_width(self, w):
        if w > 0: self.__width = w
    def get_height(self): return self.__height
    def set_height(self, h):
        if h > 0: self.__height = h
    def get_area(self): return self.__width * self.__height
```

**Task 2:** Create a `Person` class with a `name` property (read-write, must be a non-empty string) and an `age` property (read-write, must be between 0 and 150). Add a `birth_year` **read-only** property that computes the birth year based on the current year (assume current year is 2025).

**Task 3:** What is the output of this code? Explain what happens at each step:
```python
class Speed:
    def __init__(self, kmh):
        self.kmh = kmh

    @property
    def kmh(self):
        return self.__kmh

    @kmh.setter
    def kmh(self, value):
        if value < 0:
            self.__kmh = 0
        else:
            self.__kmh = value

    @property
    def mph(self):
        return self.__kmh * 0.621371

s = Speed(100)
print(s.kmh)
print(s.mph)
s.kmh = -50
print(s.kmh)
```

**Task 4:** Create a `Password` class. The password should be stored privately and never returned directly. Add:
- A write-only setter property `password` that hashes the password (just reverse the string for simulation).
- A method `check_password(entered)` that checks if the reversed version of `entered` matches.

**Task 5:** Create a `BankAccount` class using properties:
- `balance` property: readable but not directly settable
- `deposit(amount)` method: validates and increases balance
- `withdraw(amount)` method: validates and decreases balance (cannot go below 0)
Demonstrate depositing and withdrawing money, and trying to set balance directly.

---

## 8. Static Attributes (Class Attributes)

### Instance Attributes vs Class Attributes

So far, every attribute we created was an **instance attribute** — each object gets its own separate copy.

A **class attribute** (also called a static attribute) is defined directly in the class body and **shared across all instances** of that class.

```python
class Dog:
    species = "Canis lupus familiaris"   # Class attribute — shared

    def __init__(self, name):
        self.name = name                  # Instance attribute — unique per object

d1 = Dog("Rex")
d2 = Dog("Buddy")

print(d1.species)   # Canis lupus familiaris
print(d2.species)   # Canis lupus familiaris
print(d1.name)      # Rex
print(d2.name)      # Buddy
```

### How Class Attributes Are Shared

```python
class Counter:
    count = 0          # Shared class attribute

    def __init__(self):
        Counter.count += 1    # Increments the shared counter

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.count)   # 3
print(c1.count)        # 3 — all instances see the same value
```

### Modifying Class Attributes

Always modify class attributes using the **class name**, not an instance:

```python
class Settings:
    theme = "light"

# Correct:
Settings.theme = "dark"

# Risky — this creates an instance attribute that shadows the class attribute:
s = Settings()
s.theme = "blue"          # Creates s.theme, does NOT change Settings.theme
print(Settings.theme)     # "dark" — unchanged
print(s.theme)            # "blue" — instance-level shadow
```

### Accessing Class Attributes

```python
class Circle:
    pi = 3.14159         # Class attribute

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2   # Best: via class name
        # return self.pi * ...                # Also works, but less clear

c = Circle(5)
print(Circle.pi)       # 3.14159
print(c.pi)            # 3.14159 — accessing via instance (allowed but less clear)
print(c.area())        # 78.53975
```

### Practical Use Case

```python
class Employee:
    company_name = "TechCorp"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    def get_info(self):
        return f"{self.name} works at {Employee.company_name}"

e1 = Employee("Alice")
e2 = Employee("Bob")

print(Employee.employee_count)   # 2
print(e1.get_info())             # Alice works at TechCorp
```

---

### 📝 Tasks — Lesson 8

**Task 1:** Create a `Book` class with a class attribute `library_name = "City Library"` and instance attributes `title` and `author`. Create three book objects and print the library name using the class name, and using one of the instances.

**Task 2:** Write a `Vehicle` class that tracks how many vehicles have been created using a class attribute `total_vehicles`. Each time a new object is created, increment the counter. Create 4 vehicles and print the total count.

**Task 3:** What is the output of the following code? Explain why:
```python
class Config:
    debug = False

c1 = Config()
c2 = Config()

Config.debug = True
print(c1.debug)
print(c2.debug)

c1.debug = False
print(c1.debug)
print(c2.debug)
print(Config.debug)
```

**Task 4:** Create a `Student` class with a class attribute `school = "Python Academy"` and instance attributes `name` and `grade`. Demonstrate:
- Changing the school for all students at once by modifying the class attribute.
- Creating a special student with a different school by assigning to the instance.
- Show that other students are unaffected by the instance-level override.

**Task 5:** Explain the difference between modifying a class attribute through the class (`ClassName.attr = ...`) versus through an instance (`obj.attr = ...`). When would each approach be used?

---

## 9. Static Methods

### What Are Static Methods?

A **static method** is a method defined inside a class but that does **not** have access to the instance (`self`) or the class (`cls`). It is essentially a regular function that lives inside a class for organizational purposes.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtils.add(3, 5))        # 8
print(MathUtils.multiply(4, 6))   # 24
```

### Using `@staticmethod`

The `@staticmethod` decorator tells Python this method does not need `self` or `cls`:

```python
class Validator:
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    @staticmethod
    def is_strong_password(password):
        return len(password) >= 8

print(Validator.is_valid_email("user@example.com"))   # True
print(Validator.is_valid_email("not-an-email"))       # False
print(Validator.is_strong_password("abc"))            # False
```

### Difference Between Instance Methods and Static Methods

```python
class Example:
    def instance_method(self):       # Needs self — accesses instance data
        return f"Called on: {self}"

    @staticmethod
    def static_method():             # No self — independent of instance
        return "I am a static method"

e = Example()
print(e.instance_method())     # Called on: <Example object>
print(e.static_method())       # I am a static method
print(Example.static_method()) # Can also call on the class directly
```

| Feature | Instance Method | Static Method |
|---|---|---|
| Has `self` parameter | Yes | No |
| Accesses instance attributes | Yes | No |
| Accesses class attributes | Via `self` or class name | Via class name only |
| Called on instance | Yes | Yes |
| Called on class | No (normally) | Yes |

### Utility / Helper Methods

Static methods are great for helper or utility logic related to the class:

```python
class DateHelper:
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_in_month(month, year):
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        if month == 2 and DateHelper.is_leap_year(year):
            return 29
        return days[month - 1]

print(DateHelper.is_leap_year(2024))        # True
print(DateHelper.days_in_month(2, 2024))    # 29
```

---

### 📝 Tasks — Lesson 9

**Task 1:** Create a `StringUtils` class with the following static methods:
- `reverse(s)`: returns the reverse of a string
- `is_palindrome(s)`: returns True if the string is a palindrome
- `capitalize_words(s)`: returns the string with each word capitalized
Test each method with at least two examples.

**Task 2:** Create a `TemperatureConverter` class with static methods:
- `celsius_to_fahrenheit(c)`
- `fahrenheit_to_celsius(f)`
- `celsius_to_kelvin(c)`
Demonstrate converting 0°C, 100°C, and -40°C using each method.

**Task 3:** Why would you use a static method inside a class instead of just a regular module-level function? Give two situations where placing utility logic as a static method inside a class makes more sense.

**Task 4:** What is the output of the following code? Explain:
```python
class Calc:
    result = 0

    def add_to_result(self, n):
        Calc.result += n

    @staticmethod
    def square(n):
        return n * n

c1 = Calc()
c2 = Calc()

c1.add_to_result(5)
c2.add_to_result(3)

print(Calc.result)
print(Calc.square(4))
print(c1.square(7))
```

**Task 5:** Create a `PasswordGenerator` class with a static method `generate(length)` that returns a random password string of the given length (use letters and digits). Also add a static method `strength(password)` that returns `"Weak"`, `"Medium"`, or `"Strong"` based on the length.

---

## 10. Comparing Different Types of Methods

### Three Types of Methods in Python

Python classes support three types of methods, each with different access and purpose:

```python
class MyClass:
    class_attr = "shared"

    def __init__(self, value):
        self.value = value

    # 1. Instance method — needs self
    def instance_method(self):
        return f"Instance value: {self.value}"

    # 2. Class method — needs cls
    @classmethod
    def class_method(cls):
        return f"Class attribute: {cls.class_attr}"

    # 3. Static method — needs neither
    @staticmethod
    def static_method():
        return "I am independent of instance and class."
```

### Instance Methods

- Have access to `self` — the specific object.
- Can read and modify instance attributes.
- Can access class attributes through `self` or the class name.
- Most common type of method.

```python
obj = MyClass("hello")
print(obj.instance_method())   # Instance value: hello
```

### Static Methods

- No `self`, no `cls`.
- Cannot access or modify instance or class state.
- Used for utility logic that logically belongs in the class.

```python
print(MyClass.static_method())   # I am independent of instance and class.
```

### Class Methods

- Have access to `cls` — the class itself (not a specific instance).
- Can modify class-level state.
- Commonly used as **alternative constructors**.

```python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):       # Alternative constructor
        day, month, year = map(int, date_string.split("-"))
        return cls(day, month, year)

    def display(self):
        return f"{self.day}/{self.month}/{self.year}"

d = Date.from_string("15-08-2025")
print(d.display())   # 15/8/2025
```

### Summary Comparison Table

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| First parameter | `self` | `cls` | None |
| Access instance attributes | Yes | No | No |
| Access class attributes | Yes | Yes | No (directly) |
| Modify instance state | Yes | No | No |
| Modify class state | Via class name | Yes | No |
| Called on instance | Yes | Yes | Yes |
| Called on class | No | Yes | Yes |
| Common use | Object behavior | Alt constructors | Utility/helper |

---

### 📝 Tasks — Lesson 10

**Task 1:** Create a `Person` class with all three types of methods:
- `greet()` — instance method that says hello using the person's name
- `count_people()` — class method that returns the total number of `Person` objects created
- `is_adult(age)` — static method that returns True if age ≥ 18
Test all three from both the class and an instance.

**Task 2:** When should you use a class method versus a static method? Give a concrete scenario for each that justifies the choice.

**Task 3:** The `Date` class above uses a class method as an alternative constructor. Create a `Temperature` class with:
- `__init__(self, celsius)` — standard constructor
- `from_fahrenheit(cls, f)` — class method that creates a Temperature from Fahrenheit
- `from_kelvin(cls, k)` — class method that creates a Temperature from Kelvin
- `display()` — instance method that shows Celsius value

**Task 4:** What is wrong with the following code? Fix it:
```python
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def area(self):
        return Circle.pi * self.radius ** 2

c = Circle(5)
print(c.area())
```

**Task 5:** Create a `Logger` class that:
- Has a class attribute `log_count = 0`
- Has an instance method `log(message)` that prints the message and increments `log_count`
- Has a class method `get_log_count(cls)` that returns the total number of logs made
- Has a static method `format_message(message)` that returns the message in uppercase with `[LOG]` prepended
Demonstrate using all three types.

---

## 11. Combining Everything in One Class

### Building a Complete, Real-World Class

The following example brings together every concept covered: access modifiers, getters/setters (via properties), static attributes, static methods, instance methods, and class methods.

```python
class BankAccount:
    """
    A complete BankAccount class demonstrating:
    - Public, protected, and private attributes
    - Properties with validation
    - Static attributes and methods
    - Instance and class methods
    """

    bank_name = "PyBank"           # Class (static) attribute
    _interest_rate = 0.05          # Protected class attribute
    __total_accounts = 0           # Private class attribute

    def __init__(self, owner, initial_balance=0):
        self.owner = owner                    # Public instance attribute
        self._account_type = "Standard"       # Protected instance attribute
        self.__balance = 0                    # Private instance attribute

        self.deposit(initial_balance)         # Use method for validation at init
        BankAccount.__total_accounts += 1

    # ── Properties ──────────────────────────────────────────

    @property
    def balance(self):
        return self.__balance

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        valid_types = ["Standard", "Premium", "Student"]
        if value not in valid_types:
            raise ValueError(f"Account type must be one of {valid_types}")
        self._account_type = value

    # ── Instance Methods ─────────────────────────────────────

    def deposit(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__balance += amount
        return f"Deposited {amount}. New balance: {self.__balance}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        return f"Withdrew {amount}. New balance: {self.__balance}"

    def apply_interest(self):
        interest = self.__balance * BankAccount._interest_rate
        self.__balance += interest
        return f"Interest applied: {interest:.2f}. New balance: {self.__balance:.2f}"

    def get_summary(self):
        return (f"Account: {self.owner} | "
                f"Type: {self._account_type} | "
                f"Balance: {self.__balance:.2f} | "
                f"Bank: {BankAccount.bank_name}")

    # ── Class Methods ─────────────────────────────────────────

    @classmethod
    def get_total_accounts(cls):
        return f"Total accounts at {cls.bank_name}: {cls.__total_accounts}"

    @classmethod
    def set_interest_rate(cls, rate):
        if not (0 < rate < 1):
            raise ValueError("Interest rate must be between 0 and 1.")
        cls._interest_rate = rate

    # ── Static Methods ────────────────────────────────────────

    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def currency_format(amount):
        return f"${amount:,.2f}"
```

### Using the Complete Class

```python
# Create accounts
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

# Use properties
print(acc1.balance)               # 1000
acc1.account_type = "Premium"
print(acc1.account_type)          # Premium

# Instance methods
print(acc1.deposit(200))          # Deposited 200. New balance: 1200
print(acc1.withdraw(100))         # Withdrew 100. New balance: 1100
print(acc1.apply_interest())      # Interest applied: 55.00. New balance: 1155.00

# Class methods
print(BankAccount.get_total_accounts())   # Total accounts at PyBank: 2
BankAccount.set_interest_rate(0.03)

# Static methods
print(BankAccount.validate_amount(500))             # True
print(BankAccount.currency_format(acc1.balance))    # $1,155.00

# Full summary
print(acc1.get_summary())
print(acc2.get_summary())
```

---

### 📝 Tasks — Lesson 11

**Task 1:** Create a `Library` class that combines:
- A class attribute `library_name`
- A private class attribute `__total_books`
- A private instance attribute `__books` (a list)
- Properties for `book_count`
- An `add_book(title)` method
- A `remove_book(title)` method
- A class method `get_total_books()`
- A static method `validate_title(title)` (must be non-empty string)

**Task 2:** Extend the `BankAccount` class above with a `transaction_history` feature. Every deposit and withdrawal should be recorded in a private list `__transactions`. Add a property `transaction_history` that returns a copy of the list (not the list itself, to protect encapsulation).

**Task 3:** Design a `Hospital` class from scratch that uses:
- Public: `hospital_name`, `location`
- Protected: `_patient_count`
- Private: `__patient_records` (dictionary)
- A property: `patient_count`
- Methods: `admit_patient()`, `discharge_patient()`, `get_patient_info()`
- A static method: `validate_patient_name(name)`
- A class method: `get_hospital_info()`

**Task 4:** Create a `GameCharacter` class with:
- `name` (public)
- `_level` (protected, property with validation: 1-100)
- `__health` (private, property with validation: 0-100)
- `__xp` (private)
- Static attribute: `max_level = 100`
- `attack(target)` instance method
- `level_up()` instance method that increases level if enough XP
- Static method: `calculate_damage(attacker_level, defender_level)`

**Task 5:** Reflect on the `BankAccount` class example. Identify: (a) two decisions where a different access level could have been used and explain the trade-off, (b) one thing you would add to make the class more complete, and (c) one thing that might be over-engineered for a simple use case.

---

## 12. Best Practices and Common Mistakes

### Best Practice 1: Avoid Unnecessary Getters and Setters

In many languages (Java, C#), you write getters and setters for every attribute by default. In Python, this is not necessary.

```python
# ❌ Over-engineered (Java style in Python):
class Person:
    def get_name(self): return self.__name
    def set_name(self, n): self.__name = n

# ✅ Clean and Pythonic:
class Person:
    def __init__(self, name):
        self.name = name   # Just use a public attribute if no validation needed
```

Only add getters/setters (or properties) when there is a **reason** to control access — validation, computation, logging, etc.

### Best Practice 2: Prefer Properties in Python

When you do need controlled access, prefer `@property` over manual getter/setter methods:

```python
# ❌ Traditional (verbose):
class Temperature:
    def get_celsius(self): return self.__celsius
    def set_celsius(self, c): self.__celsius = c if c >= -273.15 else -273.15

# ✅ Pythonic:
class Temperature:
    @property
    def celsius(self): return self.__celsius
    @celsius.setter
    def celsius(self, c): self.__celsius = max(c, -273.15)
```

### Best Practice 3: Proper Use of Private Members

Use private (`__`) only when you truly need to prevent accidental access or subclass interference:

```python
# ❌ Over-privatizing:
class Point:
    def __init__(self, x, y):
        self.__x = x    # Why? Nothing sensitive here.
        self.__y = y

# ✅ Appropriate:
class Point:
    def __init__(self, x, y):
        self.x = x      # Fine as public — no validation needed
        self.y = y
```

### Best Practice 4: Avoid Modifying Class Attributes Through Instances

```python
# ❌ Dangerous — creates instance shadow, doesn't change class attribute:
Dog.count = 0
d = Dog()
d.count = 5       # Only changes this instance's shadow, not Dog.count

# ✅ Correct:
Dog.count = 5     # Explicitly modifies the class attribute
```

### Best Practice 5: Writing Clean and Maintainable Classes

- Keep classes focused — one class, one responsibility.
- Document your classes with docstrings.
- Use `__init__` to define all instance attributes (don't create them in random methods later).
- Call setters/properties from `__init__` to ensure validation from the start.
- Avoid putting too much logic in `__init__`.

```python
class Product:
    """Represents a product in the store inventory."""

    def __init__(self, name, price, quantity):
        self.name = name          # Call setter for validation
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self.__quantity = value

    def total_value(self):
        """Returns the total inventory value of this product."""
        return self.__price * self.__quantity

    def __str__(self):
        return f"{self.name} | ${self.__price:.2f} x {self.__quantity} units"
```

### Common Mistakes Summary Table

| Mistake | Problem | Fix |
|---|---|---|
| Using `__` for everything | Unnecessary complexity, harder inheritance | Use `__` only for truly sensitive data |
| Manual getters/setters in Python | Verbose, un-Pythonic | Use `@property` instead |
| Modifying class attribute via instance | Creates a shadow; confusing behavior | Always use `ClassName.attr = value` |
| Not validating in `__init__` | Object created in invalid state | Call setters from `__init__` |
| Overly large classes | Hard to maintain, violates Single Responsibility | Split into smaller, focused classes |
| Direct access after defining properties | Bypasses validation | Always use the property interface |

---

### 📝 Tasks — Lesson 12

**Task 1:** Review the following class and identify at least three best practice violations. Then rewrite the class following Python best practices:
```python
class User:
    total = 0
    def __init__(self, n, a, p):
        self.__n = n
        self.__a = a
        self.__p = p
        User.total += 1

    def get_n(self): return self.__n
    def set_n(self, n): self.__n = n
    def get_a(self): return self.__a
    def set_a(self, a): self.__a = a
    def get_p(self): return self.__p
    def set_p(self, p): self.__p = p
```

**Task 2:** A student wrote the following code. Explain what went wrong and how to fix it:
```python
class Dog:
    breed_count = 0

d1 = Dog()
d2 = Dog()
d1.breed_count = 5
print(Dog.breed_count)   # Student expected 5, got 0
```

**Task 3:** Write a `clean` version of a `Library` class that follows all the best practices discussed. Include a docstring, use `@property`, avoid unnecessary private members, and demonstrate it working correctly.

**Task 4:** Read the following design and decide for each attribute whether it should be public, protected, or private. Justify each:
- A `Flight` class with: `flight_number`, `departure_city`, `arrival_city`, `_fuel_level`, `__passenger_manifest`, `__cockpit_code`
- A `Game` class with: `player_name`, `current_level`, `_enemy_list`, `__save_data`, `high_score`

**Task 5 (Capstone):** Design a complete `SmartPhone` class from scratch that demonstrates every concept from this course:
- Public, protected, and private attributes
- At least two `@property` definitions (one read-only, one read-write)
- At least one class attribute
- At least one static method
- At least one class method
- At least one instance method with validation
- Docstring for the class and each method
- Demonstrate creating two phone objects and calling all methods

---

## Quick Reference Sheet

### Access Modifier Syntax

```python
self.name       # Public    — accessible everywhere
self._name      # Protected — convention: class + subclasses
self.__name     # Private   — name mangled to _ClassName__name
```

### Property Template

```python
@property
def attribute(self):
    return self.__attribute

@attribute.setter
def attribute(self, value):
    # validate value
    self.__attribute = value
```

### Method Types at a Glance

```python
def method(self):         # Instance method — accesses object
@classmethod
def method(cls):          # Class method — accesses class
@staticmethod
def method():             # Static method — accesses neither
```

### Class vs Instance Attribute

```python
class MyClass:
    class_attr = "shared"    # Class attribute

    def __init__(self):
        self.inst_attr = "unique"   # Instance attribute
```

---

*End of Lecture Notes — Object-Oriented Programming in Python*

# what is higher order fuction
# 1. Take a funtion as argument
# 2. return a function
# 3. Do both

#HOF
# def greet(func):
#   name = func()
#   return "hello " + name


# def get_name():
#   return "Victor"


# print(greet(get_name))

# callinng the function
# Mini calculator
# take a function, and two numbers
# apply the function to the two and return the result

# def add(func, a, b):
#   result = func(a, b)
#   return result

# def operate(num1, num2):
#   return num1 + num2

# print(add(operate, 1, 3))

# FUNCTION THAT RETURNS A FUNCTION
# def outer():
#   def inner():
#     print("this is comming from the inner function")
#   return inner


# inner = outer()
# inner()



# def greet(func):
#   def inner():
#     name = func()
#     print("this is from the inner function")
#     print("this was the result of the function that was passed", name)

#   return inner


# def get_name():
#   return "Natalia"
# inner = greet(get_name)
# inner()




# BUILTING PYTHON HIGER ORDER FUNCTION
# 1. map
# 2. filter



# def square_numbers(nums):
#   squares = []
#   for num in nums:
#     squares.append(num ** 2)
#   return squares

# new_list = square_numbers(nums)
# print(new_list)





# how map works
#square(1)
#square(2)
#square(3)

# Use map() to convert all strings to uppercase
# name = ['Tara', 'Perry', 'Jo', 'Luke']
# print(list(map(uppercase, name)))
# def uppercase(name):
#   return name.upper()

# def square(num):
#   return num ** 2


# nums = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda x : x ** 2, nums)))

# name = ['Tara', 'Perry', 'Jo', 'Luke']
# print(list(map(lambda x : x.upper(), name)))



# def even(num):
#   if num % 2 == 0:
#     return True
#   return False

# def even_list_func(nums):
#   even_list = []
#   for num in nums:
#     if even(num):
#       even_list.append(num)
#   return even_list

# print(even_list_func(nums))

# print(list(filter(lambda x : x % 2 == 0, nums)))


# from functools import reduce
# nums = [0, 1, 2, 3, 4, 5, 6]

# def add_two(num1, num2):
#   return num1 + num2

# print(reduce(add_two, nums))


# nums = [1, 2, 3, 4, 5]
# total = reduce(lambda acc, n: acc + n, nums)
# print(total) 


# HOF
# 1. take a function as an argument
# 2. returns a function
# 3. do the both

# closure

# decorator
# def greet(func):
  
#   def lauder():
#     name = func()
#     print("Hello", name.upper())
    
#   return lauder

# def get_name():
#   return "victor"


# func = greet(get_name)
# func()



# inner = modify(add)
# print(inner(1,2))
# from datetime import datetime
# start = datetime.now()

# import time
# def time_taken(func):
#   def wrapper(a, b):
#     start_time = datetime.now()
#     result = func(a, b)
#     end_time = datetime.now()
#     time_taken = end_time - start_time
#     print("time taken is", time_taken)
#     return result
    
#   return wrapper
    


# def power(a, b):
#   return a ** b

# # print(power(2, 3))

# wrapper_inner = time_taken(power)
# #print(wrapper_inner(2, 3))



# def uppercase(func):
#   def wrapper(name):
#     result = func(name).upper()
#     return result
  
#   return wrapper
  
# @uppercase
# def shout(name):
#   return "Hey " + name

# print(shout('Natalia'))

# # inner = uppercase(shout)
# # print(inner('Natalia'))






# def shout(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper


# @shout
# def greet():
#     return "hello"

# print(greet())

# inner = shout(greet)
# print(inner())


# inner = modify(add)
# print(inner(1,2))


# from datetime import datetime

# import time
# def time_taken(func):
#   def wrapper(*args, **kwags):
#     start_time = datetime.now()
#     result = func(*args, **kwags)
#     end_time = datetime.now()
#     time_taken = end_time - start_time
#     print("time taken is", time_taken)
#     return result
    
#   return wrapper

# @time_taken
# def multiply(*args, **kwags):
#   time.sleep(3)
#   num1, num2 = args
#   return num1 * num2
  
# print(multiply(4,5, sum=20))


# def square()
# @time_taken
# def out():
#   time.sleep(2)
#   return 'hello'

# print(out())


# *args

# def variable_arg(*args, **kwargs):
#   num1, num2 = args
#   print("num1", num1)
#   print("num2", num2)


# variable_arg(1, 2, age=10)

# payment
# deposite


# bal = 900
# def logger(func):
#   def wrapper(*args, **kwargs):
#     amount, user_name = args
#     print(f"amount: {amount}, user: {user_name} time: {date}")
#   return wrapper


# @logger
# def deposite(amount, user_name):
#   bal = bal + amount

# @logger
# def withdraw(amount, user_nam):
#   bal = bal - amount


# withdraw(500, 'hj')

#Quesition 1
# Write a function called `apply_twice(func, value)` that applies `func` to
#`value` twice. For example, `apply_twice(double, 3)` should return `12`.


# def apply_twice(func, value):
#   value1 = func(value)
#   value2 = func(value1)
#   print(value2)

# def double(num1):
#   return num1 * 2

# apply_twice(double, 4)


# Write a function `get_operation(op_name)` that accepts a string (`'add'`, `'subtract'`, `'multiply'`, `'divide'`) 
# and returns the corresponding math function. Then use it: `op = get_operation('multiply'); print(op(4, 5))`.

# **Expected Output:** `get_operation('add')(3,4) → 7` | `get_operation('multiply')(4,5) → 20`


# def get_operation(op_name):
#   if op_name == 'add':
#     return lambda x, y : x + y
#   elif op_name == 'subtract':
#     return lambda x, y : x - y
#   elif op_name == 'multiply':
#     return lambda x, y : x * y
#   elif op_name == 'divide':
#     return lambda x, y : x / y
#   else:
#     print('Not an operation')

# op = get_operation("add")
# print(op(2, 4))



# Write a function `build_pipeline(*funcs)` that accepts any number of functions and returns a 
# NEW function. The new function should apply all the input functions in sequence to a given value.
# Example: `pipeline = build_pipeline(double, square, str)` then `pipeline(3)` should 
# compute `str(square(double(3))) = '36'`.

# > **Hint:** Use a loop inside the returned function to apply each `func` in order. 
# Look up `*args` syntax if you haven't seen it yet.
# > 

# **Expected Output:** `build_pipeline(double, square, str)(3) → '36'` | `build_pipeline(abs, double)(-5) → 10`


# def build_pipeline(*funcs):
#   def new_function(value):
#     result = value
#     for func in funcs:
#       result = func(result)
#     return result
#   return new_function
  
# double = lambda x : x * 2
# square = lambda x : x ** 2
# to_str = lambda x : str(x)
# triple = lambda x : x * 3


# new_func = build_pipeline(double, square, triple, to_str)
# print(new_func(1))



# Given a list of Celsius temperatures `[0, 15, 22, 37, 100]`, use `map()` to convert them all to Fahrenheit.
# Formula: `F = (C * 9/5) + 32`
# > **Hint:** Pass a lambda or a named function to `map()`.
# **Expected Output:** `[32.0, 59.0, 71.6, 98.6, 212.0]`


# temp = [0, 15, 22, 37, 100]

# temp_f = list(map(lambda c : c * 9/5 + 32, temp))
# # print(temp_f)

# # values_less_than_50 = list(filter(lambda x : x < 50, temp_f))
# # print(values_less_than_50)

# less_than_50 = list(filter(lambda x : x < 50, map(lambda c : c * 9/5 + 32, temp)))
# # map(lambda c : c * 9/5 + 32, temp)

# print(less_than_50)



### 2.2 (Medium) Word Length Filter & Sort

# Given `words = ['python', 'is', 'a', 'beautiful', 'language', 'hi']`, use `filter()` 
# to keep words longer than 3 characters, then use `sorted()` with a key to sort them by length (shortest first).

# > **Hint:** Chain `filter()`— you can wrap one inside the other.
# > 

# **Expected Output:** `['python', 'beautiful', 'language', 'hi'] → ['python', 'language', 'beautiful']`

words = ['python', 'is', 'a', 'beautiful', 'language', 'hi', "adamuuuuu"]

sorted_words = sorted(list(filter(lambda x : len(x) > 3 , words)), key = len)
print(sorted_words)
