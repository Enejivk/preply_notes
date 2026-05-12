# Python Inheritance — Complete Student Notes

> **How to use these notes:** Read the explanation carefully, study the code examples, then attempt every task on your own before checking solutions. Tasks marked 🔥 are challenging — they are designed to push your thinking.

---

## Table of Contents

1. [Introduction to Inheritance](#1-introduction-to-inheritance)
2. [Prerequisites Before Learning Inheritance](#2-prerequisites-before-learning-inheritance)
3. [Basic Inheritance Syntax](#3-basic-inheritance-syntax)
4. [Understanding Parent and Child Classes](#4-understanding-parent-and-child-classes)
5. [Inheriting Attributes](#5-inheriting-attributes)
6. [Inheriting Methods](#6-inheriting-methods)
7. [Constructor Inheritance](#7-constructor-inheritance)
8. [The `super()` Function](#8-the-super-function)
9. [Method Overriding](#9-method-overriding)
10. [Extending Parent Methods](#10-extending-parent-methods)
11. [Types of Inheritance](#11-types-of-inheritance)
12. [Multiple Inheritance Deep Dive](#12-multiple-inheritance-deep-dive)
13. [Method Resolution Order (MRO)](#13-method-resolution-order-mro)
14. [The Diamond Problem](#14-the-diamond-problem)
15. [`isinstance()` and `issubclass()`](#15-isinstance-and-issubclass)
16. [Protected and Private Members in Inheritance](#16-protected-and-private-members-in-inheritance)
17. [Polymorphism and Inheritance](#17-polymorphism-and-inheritance)
18. [Abstract Classes and Inheritance](#18-abstract-classes-and-inheritance)
19. [Inheritance vs Composition](#19-inheritance-vs-composition)
20. [Common Mistakes in Inheritance](#20-common-mistakes-in-inheritance)
21. [Best Practices](#21-best-practices)
22. [Advanced Concepts](#22-advanced-concepts)
23. [Real-World Practice Projects](#23-real-world-practice-projects)
24. [Debugging Inheritance](#24-debugging-inheritance)
25. [Final Mastery Topics](#25-final-mastery-topics)

---

## 1. Introduction to Inheritance

### Explanation

**Inheritance** is one of the four pillars of Object-Oriented Programming (OOP). It is a mechanism that allows a new class (child/subclass) to **acquire the properties and behaviors** of an existing class (parent/superclass).

Think of it this way: A `Dog` is an `Animal`. A `Car` is a `Vehicle`. A `SavingsAccount` is a `BankAccount`. The child class **"is a"** specialised version of the parent class — this is known as the **"is-a" relationship**.

**Why does inheritance exist?**
- **Code reusability** — write shared logic once in the parent; all children benefit automatically.
- **Extensibility** — add new behavior in the child without touching the parent.
- **Maintainability** — fix a bug in the parent and all children are fixed.
- **Logical hierarchy** — model real-world relationships naturally in code.

**Real-world analogy:**
Imagine a general blueprint for a `Smartphone`. It defines things all smartphones share — a screen, a battery, the ability to make calls. Now `iPhone` and `AndroidPhone` are specialised blueprints that inherit everything from `Smartphone` and then add their own unique features. Neither `iPhone` nor `AndroidPhone` needs to redefine "make a call" — they inherit it.

**Inheritance vs Composition (briefly):**
- **Inheritance (is-a):** `Dog` IS AN `Animal`.
- **Composition (has-a):** `Car` HAS AN `Engine`.

We will cover this distinction deeply in Section 19.

```python
# Without inheritance — repeated code
class Dog:
    def breathe(self):
        print("Breathing...")
    def bark(self):
        print("Woof!")

class Cat:
    def breathe(self):       # Same method repeated!
        print("Breathing...")
    def meow(self):
        print("Meow!")

# With inheritance — DRY (Don't Repeat Yourself)
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

d = Dog()
d.breathe()  # Inherited from Animal
d.bark()
```

---

### Tasks — Introduction to Inheritance

1. In your own words, explain what inheritance is and why it is useful. Write at least five sentences.
2. Give three real-world examples of an "is-a" relationship (different from the notes). For each, name the parent and child.
3. Give three real-world examples of a "has-a" relationship. For each, name what owns what.
4. Why would a programmer prefer inheritance over copy-pasting the same method into two different classes?
5. Without writing any code, draw a simple hierarchy diagram for: `LivingThing → Animal → Mammal → Dog → GoldenRetriever`.
6. What is the difference between a **base class** and a **derived class**? Write a definition for each.
7. Explain the concept of **code reusability** in the context of inheritance with your own example.
8. Imagine you are building a game. You have `Warrior`, `Mage`, and `Archer` characters. What common parent class would you create? What attributes and methods would that parent class have?
9. True or False (and justify your answer): Every class in Python is a child of some parent class.
10. Research: What are the four pillars of OOP? List them and write one sentence about each.
11. Look at the code in the notes above (Dog/Cat without inheritance). How many lines are saved by using inheritance? Count them.
12. 🔥 A `Rectangle` and a `Circle` are both `Shape`s. Both need an `area()` method, but the calculation is different. Describe (without code) how inheritance would help organise this.
13. 🔥 Is a `Square` a `Rectangle`? If `Square` inherits from `Rectangle`, what problems might arise? Think carefully about what makes a square unique.
14. Create a table with two columns: "Use Inheritance" and "Use Composition". Fill in at least five scenarios for each column.
15. 🔥 What would happen if there were NO concept of inheritance in programming? Describe the problems developers would face with a large application.

---

## 2. Prerequisites Before Learning Inheritance

### Explanation

Before studying inheritance, you must be comfortable with the fundamentals of Python classes. Below is a complete refresher.

**Classes and Objects:**
A **class** is a blueprint. An **object** is an instance of that blueprint.

**Instance Attributes:**
Variables that belong to a specific object. Defined inside `__init__` using `self`.

**Methods:**
Functions defined inside a class that describe behavior.

**The `__init__` Constructor:**
A special method that runs automatically when an object is created. It initialises the object's attributes.

**The `self` keyword:**
Refers to the current instance of the class. It must be the first parameter of every instance method.

```python
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age      # instance attribute

    # Instance method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # Another instance method
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age}.")

# Creating objects
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

# Accessing attributes
print(p1.name)   # Alice
print(p2.age)    # 25

# Calling methods
p1.greet()
p2.have_birthday()
```

---

### Tasks — Prerequisites

1. Create a class called `Book` with attributes `title`, `author`, and `pages`. Add a method `describe()` that prints all three attributes in a sentence.
2. Create two objects of your `Book` class with different data and call `describe()` on both.
3. Add a method `is_long()` to `Book` that returns `True` if the book has more than 300 pages, otherwise `False`. Test it.
4. Create a class `Rectangle` with attributes `width` and `height`. Add a method `area()` that returns the area, and `perimeter()` that returns the perimeter.
5. Add a method `is_square()` to `Rectangle` that returns `True` if width equals height.
6. Create a class `BankAccount` with attribute `balance` (default `0`). Add methods `deposit(amount)` and `withdraw(amount)`. Make sure withdrawal doesn't go below zero.
7. What happens if you forget the `self` keyword in a method definition? Test it and note the error.
8. What is the difference between a **class attribute** and an **instance attribute**? Show an example of each.
9. Create a class `Counter` with a class attribute `count = 0`. Every time an object is created, `count` should increase by 1. Print the count after creating three objects.
10. Create a class `Student` with attributes `name` and `grades` (a list). Add methods `add_grade(grade)`, `average()`, and `highest()`.
11. What does `__init__` stand for and why does it start and end with double underscores?
12. 🔥 Create a class `Temperature` that stores a value in Celsius. Add methods `to_fahrenheit()` and `to_kelvin()`.
13. 🔥 Create a class `Stack` that uses a list internally. Add methods `push(item)`, `pop()`, `peek()` (view top without removing), and `is_empty()`.
14. Demonstrate that two different objects of the same class have independent instance attributes.
15. 🔥 What is a **dunder method** (magic method)? List at least five dunder methods Python provides and describe what each does.

---

## 3. Basic Inheritance Syntax

### Explanation

Creating a child class in Python is straightforward. You place the parent class name inside parentheses after the child class name.

```python
class Parent:
    pass

class Child(Parent):
    pass
```

The child class immediately gains access to everything the parent defines (attributes and methods), without any extra code.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")


# Cat inherits from Animal
class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")


# Instantiate
d = Dog("Rex")
d.breathe()   # Inherited from Animal
d.sleep()     # Inherited from Animal
d.bark()      # Defined in Dog

c = Cat("Whiskers")
c.breathe()   # Inherited from Animal
c.meow()      # Defined in Cat
```

**Key rules:**
- The child class can use all public methods and attributes of the parent.
- The child class can define its own additional methods.
- The child class can also override parent methods (covered in Section 9).

---

### Tasks — Basic Inheritance Syntax

1. Create a `Vehicle` class with a method `move()` that prints `"Vehicle is moving."`. Then create a `Car` class that inherits from `Vehicle` and add a method `honk()`. Instantiate `Car` and call both `move()` and `honk()`.
2. Create a `Shape` class with a method `describe()` that prints `"I am a shape."`. Create `Circle` and `Triangle` subclasses, each with their own additional method. Instantiate both and test.
3. What is the output of `class Child(Parent): pass` — does the child have any methods? Investigate using `dir(Child)`.
4. Create a parent class `Appliance` with a method `power_on()`. Create three subclasses: `WashingMachine`, `Refrigerator`, and `Microwave`. Each subclass should have one unique method. Test all of them.
5. Can a child class exist without any body at all (just `pass`)? Try it and explain what happens.
6. Create a `Person` class with `__init__(name, age)` and a `greet()` method. Create an `Employee` class that inherits from `Person` and adds a `work()` method. Instantiate `Employee` and call both `greet()` and `work()`.
7. Check the type of an object from question 6. What does `type(employee_object)` return? What does `type(person_object)` return?
8. Create a `Bird` class with a method `fly()`. Create a `Penguin` class that inherits from `Bird`. Should `Penguin` really be able to call `fly()`? What does this tell you about the limits of inheritance?
9. Write a class `Furniture` with attributes `material` and `color`. Create subclasses `Chair` and `Table`. Instantiate each with specific values and print their attributes.
10. Create a `Computer` parent class with a method `compute()`. Create subclasses `Laptop` and `Desktop`, each with an additional unique method. Show that all instances can call `compute()`.
11. How many classes can a single parent have as children? Is there a limit? Test with at least four child classes.
12. 🔥 Without using `__init__` in the child class, create a child whose parent has an `__init__` method with two parameters. Instantiate the child — what arguments does it require?
13. 🔥 Create a three-level simple hierarchy: `LivingThing → Animal → Dog`. Verify that a `Dog` object can call methods defined in `LivingThing`.
14. Explore `dir()` on a child class object. How many methods does it have that come from the parent? How many come from Python's built-in `object` class?
15. 🔥 What happens if you define the same method name in both parent and child? Who wins? Test and explain.

---

## 4. Understanding Parent and Child Classes

### Explanation

**Terminology:**

| Term | Also Called | Meaning |
|---|---|---|
| Parent class | Base class / Superclass | The class being inherited from |
| Child class | Derived class / Subclass | The class that inherits |

**Shared vs Specialised Behavior:**
- The parent holds **shared** behavior — things all children have in common.
- Each child holds **specialised** behavior — what makes it unique.

**Visualising a hierarchy:**

```
         Animal
        /      \
      Dog       Cat
     /   \
  Poodle Bulldog
```

In code:

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def fetch(self):
        print(f"{self.name} is fetching the ball!")


class Cat(Animal):
    def purr(self):
        print(f"{self.name} is purring...")


class Poodle(Dog):
    def style_hair(self):
        print(f"{self.name} is getting a poodle haircut!")


# Poodle can call methods from Animal, Dog, and its own
p = Poodle("Fifi", 3)
p.eat()         # From Animal
p.sleep()       # From Animal
p.fetch()       # From Dog
p.style_hair()  # From Poodle
```

---

### Tasks — Understanding Parent and Child Classes

1. Define the terms: superclass, subclass, base class, derived class. Give one example of each.
2. Draw a hierarchy diagram for the following: `Vehicle → Car → ElectricCar`, `Vehicle → Truck`, `Vehicle → Motorcycle`. Show which methods belong at which level.
3. Create the `Vehicle` hierarchy from Task 2 in Python. Assign at least two methods to each level.
4. At which level in a hierarchy should the `eat()` method live: `LivingThing`, `Animal`, `Dog`, or `Poodle`? Justify your answer.
5. In the hierarchy `Animal → Dog → GuideDog`, what is `Dog` relative to `Animal`? What is `Dog` relative to `GuideDog`?
6. Can a class be both a parent AND a child at the same time? Explain and give an example.
7. Create a class hierarchy for an e-commerce app: `Product` as the parent, with children `Electronics`, `Clothing`, and `Food`. Add appropriate attributes and methods to each level.
8. What does "specialisation" mean in the context of class hierarchies? Give an example from your hierarchy in Task 7.
9. Create a `SchoolMember` class and make `Teacher` and `Student` inherit from it. What attributes should live in the parent? What should be unique to each child?
10. Identify the "shared" and "specialised" behavior in the following scenario: a `SportsPlayer` parent with children `Footballer` and `Basketballer`.
11. 🔥 Is it always obvious what should go in the parent class? Design a hierarchy for `Animal → Bird → Parrot`. At what level should `fly()` go? What about `talk()`?
12. Create a five-level hierarchy of your own choice. Implement it in Python with at least one method at every level. Demonstrate the deepest child calling methods from all levels.
13. 🔥 Why is it bad practice to have very deep inheritance hierarchies (e.g., 10+ levels)? List three specific problems.
14. What is the `object` class in Python? Every class inherits from it — verify this using `issubclass(MyClass, object)`.
15. 🔥 Create a `GameCharacter` parent with children `Warrior`, `Mage`, and `Ranger`. Design shared attributes (name, health, level) and specialised attributes and methods for each subclass. Implement a `status()` method in the parent that prints all shared attributes.

---

## 5. Inheriting Attributes

### Explanation

When a child class inherits from a parent, it gains access to all **instance attributes** set on the parent's `self`.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True   # Default attribute

class Dog(Animal):
    def show_info(self):
        # Accessing parent's attributes directly
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Alive: {self.is_alive}")

d = Dog("Buddy", "Canis lupus familiaris")
d.show_info()
print(d.name)    # Directly accessible
```

**Adding new child attributes:**
The child can define additional attributes on top of what the parent provides.

```python
class Dog(Animal):
    def __init__(self, name, species, breed):
        # First, call the parent's __init__ to set up name and species
        super().__init__(name, species)
        # Now add the child-specific attribute
        self.breed = breed

    def show_info(self):
        print(f"Name: {self.name}, Species: {self.species}, Breed: {self.breed}")

d = Dog("Max", "Canis lupus", "Labrador")
d.show_info()
```

**Modifying inherited attributes:**
A child object can freely change values of inherited attributes.

```python
d = Dog("Rex", "Canis lupus", "Poodle")
print(d.is_alive)   # True (from parent)
d.is_alive = False  # Modified on this specific object
print(d.is_alive)   # False
```

---

### Tasks — Inheriting Attributes

1. Create a `Vehicle` class with attributes `make`, `model`, and `year`. Create a `Car` class that inherits from `Vehicle` (without its own `__init__`). Instantiate `Car` and print all three attributes.
2. Add an attribute `is_running = False` to `Vehicle`. In the `Car` class, add a method `start()` that sets `is_running` to `True` and prints `"Car started."`. Test it.
3. Create a `Person` class with `name` and `age`. Create an `Employee` class that adds `company` and `salary` as extra attributes (use `super()`). Print all four attributes.
4. Modify an inherited attribute on a child object. Verify that modifying it on one object does not affect another object of the same class.
5. Create a `Product` class with `name` and `price`. Create a `DiscountedProduct` class that adds a `discount_percent` attribute and a method `discounted_price()` that returns the reduced price.
6. What happens if you try to access an attribute that exists in the child but not the parent — on a parent object? Test and explain.
7. What happens if you try to access an attribute that exists in the parent but not the child — on a child object? Test and explain.
8. Create a `BankAccount` class with `owner` and `balance`. Create `SavingsAccount` with an additional `interest_rate`. Add a method `apply_interest()` that increases balance by the interest rate percentage.
9. Create a `Laptop` class inheriting from `Computer`. `Computer` has `brand` and `ram`. `Laptop` adds `battery_life`. Show that a `Laptop` object has all three attributes.
10. Can a class attribute (not instance attribute) also be inherited? Create a parent with a class attribute and verify on a child object.
11. 🔥 Create a `Vehicle` with `speed = 0` as an instance attribute. Create a `Car` with methods `accelerate(amount)` and `brake(amount)`. Ensure speed never goes below 0.
12. 🔥 If both parent and child `__init__` set an attribute with the same name but different values, which one wins? Test it and explain why.
13. Create a `Game` class with attributes `title`, `genre`, and `rating`. Create a `MultiplayerGame` class that adds `max_players` and `is_online`. Test all attributes.
14. 🔥 Create a class where the child's `__init__` does NOT call `super().__init__()`. What happens to the parent's attributes? How do you fix it?
15. 🔥 Create a `House` class with a class attribute `num_rooms = 4`. Create a `Villa(House)` that sets `num_rooms = 10`. Show how class attribute inheritance and overriding works at the class vs instance level.

---

## 6. Inheriting Methods

### Explanation

When a child class inherits from a parent, it can call any **public method** defined in the parent directly, as if the method were defined in the child itself.

**How Python finds methods (Method Lookup Process):**
1. Python first looks in the **child class** for the method.
2. If not found, it looks in the **parent class**.
3. If not found, it continues up the hierarchy.
4. If never found, it raises `AttributeError`.

```python
class Animal:
    def breathe(self):
        print("Inhaling and exhaling...")

    def eat(self, food):
        print(f"Eating {food}.")

    def sleep(self):
        print("Sleeping... ZZZ.")


class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

    def fetch(self, item):
        print(f"Fetching the {item}!")


d = Dog()
d.breathe()          # Found in Animal → runs
d.eat("bone")        # Found in Animal → runs
d.sleep()            # Found in Animal → runs
d.bark()             # Found in Dog → runs
d.fetch("stick")     # Found in Dog → runs
# d.purr()           # AttributeError — not in Dog or Animal
```

**Reusing parent logic in a child method:**

```python
class Animal:
    def describe(self):
        return "I am an animal."

class Dog(Animal):
    def describe(self):
        parent_desc = super().describe()  # Reuse parent logic
        return parent_desc + " Specifically, I am a dog."

d = Dog()
print(d.describe())  # I am an animal. Specifically, I am a dog.
```

---

### Tasks — Inheriting Methods

1. Create a `Machine` class with methods `start()`, `stop()`, and `status()`. Create a `Robot` class that inherits from `Machine` and adds `perform_task(task_name)`. Verify all methods work on a `Robot` object.
2. Call a parent method from within a child method (without using `super()`). Show how this works.
3. Create an `Employee` class with methods `work()`, `take_break()`, and `clock_out()`. Create a `Manager` class that adds `hold_meeting()`. Call all methods on a `Manager` object.
4. What error does Python raise when you call a method that does not exist in the class or any of its parents? Demonstrate this.
5. Trace the method lookup manually: given `class C(B): pass` and `class B(A): pass`, if `C().hello()` is called and only `A` has `hello()`, describe step by step how Python finds it.
6. Create a `Printer` class with `print_document(filename)` and `check_ink()` methods. Create a `LaserPrinter` that inherits these and adds `warm_up()`.
7. Can a child class call a parent method even if the child has its own method with the same name? Demonstrate using `super()`.
8. 🔥 Create a `Logger` class with a `log(message)` method that prints `"[LOG]: message"`. Create `FileLogger` and `DatabaseLogger` subclasses that each inherit `log()` and also have their own `save()` method (with different behavior for each).
9. Show that a parent object CANNOT call methods defined only in the child class. What error appears?
10. Create a class `Authenticator` with `validate_username(username)` and `validate_password(password)`. Create `AdminAuthenticator` that adds `validate_admin_code(code)`. Test all three on an `AdminAuthenticator` object.
11. 🔥 Create a class hierarchy where a method in a grandchild calls a method that only exists in the grandparent. Show that this works.
12. Create a `TextProcessor` parent with methods `to_uppercase(text)` and `to_lowercase(text)`. Create a `AdvancedProcessor` child that adds `reverse(text)` and `word_count(text)`.
13. 🔥 What is the difference between calling a method as `ParentClass.method(self)` vs `super().method()`? When would you use each?
14. Write code that demonstrates the exact sequence Python uses to find a method in a three-level hierarchy. Use print statements inside each class's version of the method to show which one runs.
15. 🔥 Create a `MathHelper` class with methods `add(a, b)`, `subtract(a, b)`, and `multiply(a, b)`. Create `AdvancedMath` that inherits these and adds `power(base, exp)` and `average(*nums)`. Show all methods in use.

---

## 7. Constructor Inheritance

### Explanation

The constructor `__init__` is a method like any other — it follows the same inheritance rules.

**Case 1: Child has NO `__init__`**
Python automatically uses the parent's `__init__`.

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal __init__ called for {self.name}")

class Dog(Animal):
    pass  # No __init__

d = Dog("Rex")   # Parent's __init__ runs
print(d.name)    # Rex — attribute is available
```

**Case 2: Child HAS its own `__init__` (without `super()`)**
The parent's `__init__` is completely replaced. Parent attributes are NOT set.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed   # Parent's __init__ NOT called

d = Dog("Poodle")
print(d.breed)  # Poodle
# print(d.name)  # AttributeError! name was never set
```

**Case 3: Child HAS its own `__init__` (WITH `super()`)**
The correct approach — parent's `__init__` runs first, then child adds more.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Runs Animal's __init__
        self.breed = breed       # Then adds Dog-specific attribute

d = Dog("Rex", "Poodle")
print(d.name)    # Rex  (set by Animal)
print(d.breed)   # Poodle (set by Dog)
```

---

### Tasks — Constructor Inheritance

1. Create a `Vehicle` class with `__init__(make, model)`. Create a `Car` class with no `__init__`. Instantiate `Car` with two arguments and print `make` and `model`.
2. Create a `Person` class with `__init__(name, age)`. Create an `Employee` class with `__init__(name, age, company)` that calls `super().__init__(name, age)`. Verify all three attributes exist.
3. What happens if a child has `__init__` but does NOT call `super().__init__()`? Show this breaking and explain why.
4. Create a three-level hierarchy `LivingThing → Animal → Dog`. Each class should have its own `__init__` and call `super()`. Trace the chain of constructor calls using print statements.
5. Create a `BankAccount` with `__init__(owner, balance=0)`. Create `SavingsAccount` with `__init__(owner, balance=0, interest_rate=0.05)`. Use `super()` correctly.
6. What are default parameter values in `__init__`? Show an example in a parent class and verify child inherits that default behavior.
7. Create a `Product` class with `__init__(name, price)`. Create `DiscountedProduct` with `__init__(name, price, discount)`. Use `super()`. Add a method `final_price()`.
8. 🔥 Create `Shape → Polygon → Triangle`. Each level adds attributes (e.g., Shape: `color`; Polygon: `num_sides`; Triangle: `side_a, side_b, side_c`). Chain all constructors correctly.
9. Demonstrate that without calling `super().__init__()`, a parent method that uses `self.parent_attribute` will crash. Fix it.
10. Create a `User` class with `__init__(username, email)`. Create `AdminUser` with an extra `admin_level` attribute. Add a method `admin_info()` that prints all three.
11. 🔥 What happens to default arguments in a parent's `__init__` when the child calls `super()`? Can the child override those defaults? Show with an example.
12. Create a `Gadget` class and a `SmartGadget` subclass. In `SmartGadget.__init__`, call `super()` in the middle (after setting some attributes). What happens? What is the recommended order?
13. Demonstrate **constructor chaining** across four levels of inheritance. Every level should print something so you can see the order of execution.
14. 🔥 What is a **keyword-only argument** in `__init__`? Create a parent and child that use `*` to enforce keyword-only arguments and chain them with `super()`.
15. 🔥 A child class has `__init__(self, *args, **kwargs)`. It passes everything to `super().__init__(*args, **kwargs)`. When is this pattern useful? Create an example.

---

## 8. The `super()` Function

### Explanation

`super()` is a built-in Python function that gives you access to the **parent class** (or next in MRO). It is most commonly used to:
1. Call the parent's `__init__` from the child's `__init__`.
2. Call an overridden parent method from the child.

**Syntax:**
```python
super().method_name(arguments)
```

**Why `super()` instead of calling the parent directly?**

You could write `Animal.__init__(self, name)` directly, but `super()` is better because:
- It respects the **MRO** (Method Resolution Order) — critical in multiple inheritance.
- If you rename the parent class, you don't need to update every `super()` call.
- It enables **cooperative multiple inheritance**.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"I am {self.name}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # Calls Animal.__init__
        self.breed = breed

    def describe(self):
        base = super().describe()  # Calls Animal.describe
        return f"{base}, a {self.breed}"


d = Dog("Rex", "Labrador")
print(d.describe())   # I am Rex, a Labrador
```

**`super()` vs direct parent call:**

```python
# Option 1 — Direct parent call (less flexible)
Animal.__init__(self, name)

# Option 2 — super() (preferred)
super().__init__(name)
```

---

### Tasks — The `super()` Function

1. Create a `Vehicle` and `Car` class. In `Car.__init__`, use `super()` to call `Vehicle.__init__`. Add a print statement in each `__init__` to trace execution order.
2. Override a method in a child class and use `super()` inside it to call the parent's version. Show the combined output.
3. Without using `super()`, call the parent class method directly using `ParentClass.method(self)`. Does it work? Compare it with `super()`.
4. Create a three-level hierarchy and use `super()` in each level's `__init__`. Add print statements to trace the exact execution order.
5. What happens if you call `super()` in a class that has no parent (other than `object`)? Test it.
6. Create a `Logger` class with `log()` that prints `"[LOG]"`. Create `TimedLogger` that uses `super().log()` and adds a timestamp before the message.
7. Use `super()` to call a method that is NOT `__init__`. Create an example where a child enhances a parent method using `super()`.
8. 🔥 What does `super(Dog, self)` (the explicit form) mean? When would you use the explicit form over the simple `super()`?
9. Demonstrate that using `super()` correctly in multiple inheritance gives different results than calling the parent directly by class name.
10. Create a `Formatter` base class with `format(text)` that wraps text in asterisks. Create `BoldFormatter` that uses `super()` and also wraps in underscores. Create `ItalicFormatter` that uses `super()` and wraps in slashes.
11. 🔥 Is it possible to call `super()` outside of a class method? Try it and note what happens.
12. 🔥 What is "cooperative multiple inheritance" and why does `super()` enable it? Explain with an example.
13. Create a chain of decorators (classes) for a text string: each class adds something (e.g., prefix, suffix, uppercase) and uses `super()` to build on the previous.
14. 🔥 What happens if one class in a multiple inheritance chain does NOT call `super().__init__()`? Which parent's `__init__` gets skipped? Demonstrate.
15. 🔥 Research and explain the difference between `super()` in Python 2 vs Python 3. Why did Python 3 simplify it?

---

## 9. Method Overriding

### Explanation

**Method overriding** occurs when a child class defines a method with the **same name** as a method in the parent class. The child's version replaces (overrides) the parent's version for child objects.

```python
class Animal:
    def sound(self):
        print("Some generic animal sound.")

    def describe(self):
        print("I am an animal.")


class Dog(Animal):
    # Override sound()
    def sound(self):
        print("Woof! Woof!")


class Cat(Animal):
    # Override sound()
    def sound(self):
        print("Meow!")


# Parent object uses parent method
a = Animal()
a.sound()    # Some generic animal sound.

# Child objects use their own overridden method
d = Dog()
d.sound()    # Woof! Woof!

c = Cat()
c.sound()    # Meow!

# Non-overridden method is still inherited
d.describe()   # I am an animal.
c.describe()   # I am an animal.
```

**Calling the overridden parent method from inside the override:**

```python
class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        super().sound()        # Call parent's version first
        print("Then: Woof!")   # Then add own behavior

d = Dog()
d.sound()
# Animal makes a sound.
# Then: Woof!
```

**Practical use cases:**
- Customising generic behavior for specific classes
- Enforcing a different implementation in a subclass
- Extending parent logic rather than replacing it completely

---

### Tasks — Method Overriding

1. Create an `Animal` class with a `speak()` method. Create four subclasses (`Dog`, `Cat`, `Cow`, `Duck`) each overriding `speak()` with their own sound. Test all.
2. Demonstrate that overriding a method in the child does NOT affect the parent's version. Show a parent object and child object calling the same method name.
3. Create a `Shape` class with `area()` that returns 0. Override `area()` in `Circle` and `Rectangle` with correct formulas. Test all three classes.
4. Use `super()` inside an overridden method to call the parent's version and then add extra behavior.
5. Create a `Notification` class with `send(message)` that prints `"Sending: message"`. Override in `EmailNotification` and `SMSNotification` to add channel-specific prefixes.
6. Create an `Employee` class with `calculate_pay()` that returns a flat salary. Create `SalesEmployee` that overrides it to add commission. Create `Manager` that overrides it to add a bonus.
7. What is the purpose of overriding `__str__()` in a class? Override it in a `Product` class so that `print(product)` shows a nicely formatted string.
8. Override `__repr__()` in a class and explain the difference between `__str__` and `__repr__`.
9. 🔥 Create a `Validator` class with `validate(value)` that always returns `True`. Create `AgeValidator` and `EmailValidator` subclasses that override `validate()` with specific rules.
10. 🔥 Override `__eq__()` in a `Student` class so two students are considered equal if they have the same student ID. Test it.
11. 🔥 Override `__lt__()` and `__gt__()` in a `Temperature` class so that temperature objects can be compared. Test with `sorted()`.
12. Create a game `Character` with an `attack()` method. Create `Warrior`, `Mage`, and `Archer` that override `attack()` with unique behavior, but all call `super().attack()` first.
13. 🔥 Is it possible to override a method and make it do something completely unrelated to the parent method? Is this a good practice? Explain.
14. Create a `Report` class with `generate()`. Create `PDFReport` and `HTMLReport` that each override `generate()` to output in their respective formats.
15. 🔥 Create a `Payment` class with `process(amount)` that logs the transaction. Override it in `CreditCardPayment` and `PayPalPayment` — both should call `super().process(amount)` and then add their own specific processing steps.

---

## 10. Extending Parent Methods

### Explanation

**Extending** means keeping the parent's method logic and **adding more** on top, rather than replacing it entirely. This is done using `super()`.

```python
class Vehicle:
    def start(self):
        print("Turning on ignition...")
        print("Engine started.")

class ElectricCar(Vehicle):
    def start(self):
        super().start()                    # All of Vehicle's start logic
        print("Battery system activated.") # Additional ElectricCar logic
        print("Silent electric motor ON.")

e = ElectricCar()
e.start()
# Turning on ignition...
# Engine started.
# Battery system activated.
# Silent electric motor ON.
```

**Position of `super()` call matters:**

```python
class Base:
    def greet(self):
        print("Hello from Base")

class Child(Base):
    def greet(self):
        print("Starting Child greet")
        super().greet()              # Parent logic in the middle
        print("Finishing Child greet")

c = Child()
c.greet()
# Starting Child greet
# Hello from Base
# Finishing Child greet
```

**Real-world use case — logging:**

```python
class DatabaseConnector:
    def connect(self):
        print("Connecting to database...")
        # actual connection code

class LoggedConnector(DatabaseConnector):
    def connect(self):
        print("[LOG] Connection attempt started.")
        super().connect()
        print("[LOG] Connection successful.")
```

---

### Tasks — Extending Parent Methods

1. Create a `User` class with `register()` that prints `"User registered."`. Create `PremiumUser` that extends `register()` to also print `"Premium features activated."`.
2. Create a `Logger` with `log(message)`. Extend it in `TimestampLogger` to prepend the current date and time to every message.
3. Demonstrate three different positions for `super()` call in an extended method: before, after, and in the middle. Show the output difference.
4. Create a `Cake` class with `bake()` that describes standard baking steps. Create `ChocolateCake` that extends `bake()` with chocolate-specific steps.
5. Create a `Form` class with `submit()` that validates and saves data. Create `ContactForm` that extends `submit()` to also send an email notification.
6. Create a `Game` class with `start()` that prints basic startup info. Create `MultiplayerGame` that extends `start()` to also connect to a server.
7. 🔥 Create four levels of a hierarchy where each level extends the same method name. The final output when the deepest child calls the method should show contributions from all four levels.
8. Create a `Sale` class with `apply_discount(price)` that applies 10% off. Extend in `SeasonalSale` to apply an additional 5% off after the base discount.
9. 🔥 Is there a difference between calling `super().method()` at the START vs END of an overridden method? Create a case where the order matters (produce different results).
10. Create a `Report` class with `generate()` that produces a basic report. Extend in `DetailedReport` to add more sections. Extend `DetailedReport` in `AuditReport` to add audit-specific sections.
11. Create a `Pizza` class with `prepare()` that lists standard preparation steps. Create `VeganPizza` that extends `prepare()` to substitute non-vegan ingredients.
12. 🔥 Create a mixin-like pattern: a class `Timestamps` with `save()` that records created/updated time. Extend it in `DatabaseRecord` to actually save to a (simulated) database.
13. Can you call `super()` more than once in the same method? Try it. What happens? Is it a good practice?
14. 🔥 Create a `Security` class with `authenticate(password)` that checks a password hash. Extend in `TwoFactorAuth` to also verify a one-time code after the password passes.
15. 🔥 Describe the "Template Method Pattern". How does it relate to extending parent methods? Implement a simple example (e.g., a `DataProcessor` with `process()` that calls abstract steps defined in subclasses).

---

## 11. Types of Inheritance

### Explanation

Python supports five types of inheritance:

---

### a. Single Inheritance
One parent → one child. The simplest and most common form.

```python
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):
    def bark(self):
        print("Woof!")
```

---

### b. Multilevel Inheritance
Grandparent → Parent → Child. A chain of inheritance.

```python
class LivingThing:
    def grow(self):
        print("Growing...")

class Animal(LivingThing):
    def breathe(self):
        print("Breathing...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog()
d.grow()     # From LivingThing
d.breathe()  # From Animal
d.bark()     # From Dog
```

---

### c. Hierarchical Inheritance
One parent → multiple children.

```python
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):
    def bark(self): print("Woof!")

class Cat(Animal):
    def meow(self): print("Meow!")

class Bird(Animal):
    def chirp(self): print("Tweet!")
```

---

### d. Multiple Inheritance
One child inherits from multiple parents.

```python
class Flyable:
    def fly(self):
        print("Flying...")

class Swimmable:
    def swim(self):
        print("Swimming...")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack!")

d = Duck()
d.fly()   # From Flyable
d.swim()  # From Swimmable
d.quack() # From Duck
```

---

### e. Hybrid Inheritance
A combination of two or more types.

```python
class A:
    pass

class B(A):   # Multilevel + hierarchical
    pass

class C(A):
    pass

class D(B, C):  # Multiple inheritance
    pass
```

---

### Tasks — Types of Inheritance

1. Write a clear definition for each of the five types of inheritance in your own words.
2. Draw a diagram for each of the five types. Label each class in the diagram.
3. Implement a single inheritance example for a `Smartphone` that inherits from `ElectronicDevice`.
4. Implement a multilevel inheritance: `LivingThing → Mammal → Human → Student`.
5. Implement hierarchical inheritance: `Shape → Circle`, `Shape → Square`, `Shape → Triangle`.
6. Implement multiple inheritance: `Printable` and `Saveable` as parents; `Document` as the child.
7. Implement hybrid inheritance combining all forms. Draw the diagram before coding.
8. Which type of inheritance is generally the safest to use? Which is the most dangerous? Justify.
9. 🔥 In multilevel inheritance with four levels, how many classes does the deepest child inherit from? List all of them.
10. Create a real-world example for each of the five types (different from the notes). For each, justify why that type of inheritance is appropriate.
11. 🔥 Create a `FlyingFish` class that inherits from both `Fish` and `Bird`. Both have a `move()` method. What happens when `FlyingFish` calls `move()`? Which one runs?
12. 🔥 What is the risk of multiple inheritance compared to single inheritance? Name three specific risks.
13. In hierarchical inheritance, if the parent class changes, how many child classes are affected? Is this good or bad?
14. 🔥 Research real-world Python frameworks or libraries that use multiple inheritance. Name two examples and explain how they use it.
15. 🔥 Build a `Character` class hierarchy for a role-playing game using at least three types of inheritance. Include classes like `Character`, `Mortal`, `Magical`, `Wizard`, `Paladin`, etc.

---

## 12. Multiple Inheritance Deep Dive

### Explanation

Multiple inheritance allows a class to inherit from more than one parent simultaneously.

```python
class Father:
    def skill(self):
        return "Engineering"

class Mother:
    def skill(self):
        return "Medicine"

class Child(Father, Mother):
    pass

c = Child()
print(c.skill())  # Engineering — Father is listed first, so it takes priority
```

**Inheriting from multiple classes with no conflict:**

```python
class JSONSerializable:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Printable:
    def display(self):
        print(self.__dict__)

class Record(JSONSerializable, Printable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

r = Record("Alice", 30)
r.display()    # From Printable
print(r.to_json())  # From JSONSerializable
```

**Constructor behavior with multiple parents:**

```python
class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B:
    def __init__(self):
        print("B init")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()

c = C()
# C init
# A init
# B init
```

---

### Tasks — Multiple Inheritance Deep Dive

1. Create `Flyable` and `Swimmable` classes with a `move()` method in each. Create `Duck(Flyable, Swimmable)`. Which `move()` runs? Change the order of parents and observe.
2. Create two parent classes with NO method conflicts. Create a child that inherits from both. Verify it has methods from both parents.
3. Use `ClassName.mro()` to check the MRO of `Duck(Flyable, Swimmable)`. List the order.
4. 🔥 Create a scenario where two parent classes share the same method name. Design a child that intelligently combines both parent methods using `super()`.
5. Create `JSONMixin` with `to_json()` and `XMLMixin` with `to_xml()`. Create `DataRecord(JSONMixin, XMLMixin)` that uses both.
6. What happens in `__init__` with multiple parents? Create `A`, `B`, and `C(A, B)` each with `__init__` and use `super()` in all. Trace the execution.
7. Create `Timestampable` with `created_at()` and `Auditable` with `last_modified_by()`. Create `Document(Timestampable, Auditable)`.
8. 🔥 Create three parent classes and one child that inherits from all three. Map the MRO before writing code, then verify.
9. 🔥 When is multiple inheritance genuinely useful vs when is it just confusing? Give one good use case and one bad use case.
10. Research: What is a **Mixin**? How does it relate to multiple inheritance? Give an example.
11. 🔥 Create `Readable` and `Writable` as parents. Create `ReadWritable(Readable, Writable)`. Then create `ReadOnly(Readable)`. Show that they behave correctly.
12. 🔥 Demonstrate the C3 Linearisation algorithm manually with a diamond class hierarchy. Map it step by step.
13. What is the difference between `class C(A, B)` and `class C(B, A)`? Does the order always matter?
14. 🔥 Create a mixin `ValidationMixin` that adds `validate()`. Apply it to `User(ValidationMixin, BaseModel)` and `Product(ValidationMixin, BaseModel)`.
15. 🔥 Some developers say "avoid multiple inheritance". Others say "use mixins freely". What is the distinction between bad multiple inheritance and a well-designed mixin? Explain with examples.

---

## 13. Method Resolution Order (MRO)

### Explanation

**MRO** (Method Resolution Order) defines the **order in which Python searches for a method or attribute** in a class hierarchy.

Python uses the **C3 Linearisation** algorithm to determine MRO, ensuring:
- A class always comes before its parents.
- The order of parents as listed is respected.
- Every class appears only once.

```python
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")

class C(A):
    def hello(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.hello()   # Hello from B — B comes before C in MRO

# Check MRO:
print(D.mro())
# [D, B, C, A, object]
```

**Reading the MRO:**
Python searches left to right in the MRO list. The first class that has the method wins.

```python
# MRO: [D, B, C, A, object]
# When d.hello() is called:
# 1. Check D — not found
# 2. Check B — found! Run it and stop.
```

**Viewing MRO:**

```python
print(MyClass.mro())         # Returns list
print(MyClass.__mro__)       # Returns tuple
help(MyClass)                # Shows MRO in output
```

---

### Tasks — MRO

1. Define MRO in your own words. Why does Python need a defined lookup order?
2. Given `class D(B, C)`, `class B(A)`, `class C(A)`, manually write out the expected MRO before running code. Then verify with `D.mro()`.
3. Print the MRO of `int`, `str`, `list`, and `dict`. What is the last class in every MRO?
4. Create a four-class hierarchy and manually predict the MRO. Verify with `.mro()`.
5. Explain why the MRO of any class always ends with `object`.
6. Create `class X(Y, Z)` where both `Y` and `Z` have a `greet()` method. Use the MRO to predict which `greet()` runs before testing.
7. 🔥 Manually apply the C3 Linearisation algorithm to: `class D(B, C)`, `class B(A)`, `class C(A)`. Show every step.
8. What error does Python raise if you create an impossible MRO? Try to create one and capture the error.
9. 🔥 Create a five-class hierarchy. Print the MRO. Walk through it and explain each class's position.
10. Show how `super()` uses the MRO. In a chain of classes all defining `greet()`, use `super()` to chain them all.
11. 🔥 Explain why `super()` is "MRO-aware" while directly calling `Parent.method(self)` is not.
12. What does `__mro__` return vs `.mro()`? How are they different (type-wise)?
13. 🔥 Create a case where changing the order of parents in `class D(B, C)` to `class D(C, B)` changes the behavior of a method call. Demonstrate.
14. What happens to MRO in single inheritance? Predict and verify.
15. 🔥 Create a class hierarchy where you intentionally want `super()` to skip a class in the chain and call a grandparent's method directly. Is this possible? What are the consequences?

---

## 14. The Diamond Problem

### Explanation

The **diamond problem** occurs when a class inherits from two classes that both inherit from the same base class. This creates a diamond shape in the hierarchy diagram.

```
       A
      / \
     B   C
      \ /
       D
```

The problem: if `D` calls a method from `A`, which path should Python take — through `B` or through `C`?

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()

class D(B, C):
    def greet(self):
        print("Hello from D")
        super().greet()

d = D()
d.greet()
# Hello from D
# Hello from B
# Hello from C
# Hello from A
```

**Python's solution:** The MRO ensures `A.greet()` is called only ONCE, even though `B` and `C` both inherit from `A`. The MRO for `D` is: `[D, B, C, A, object]`. Each class calls `super()` which follows the MRO, not the direct parent.

**What causes ambiguity:**
Without MRO, calling `D().greet()` might call `A.greet()` twice (once through `B` and once through `C`), or Python wouldn't know which `B.greet()` or `C.greet()` to prefer.

---

### Tasks — The Diamond Problem

1. Draw the diamond diagram for: `A` as top, `B(A)` and `C(A)` as middle, `D(B, C)` at the bottom.
2. Implement the exact diamond hierarchy from the notes. Verify the output.
3. Remove `super().greet()` calls from `B` and `C`. What changes in the output? Why?
4. What is the MRO for `D(B, C)` in the diamond example? Verify with `D.mro()`.
5. Change `D(B, C)` to `D(C, B)`. How does the output change? Why?
6. Explain in your own words how Python's MRO solves the diamond problem.
7. 🔥 Create a diamond problem with four levels (A → B,C → D → E). Trace the MRO manually.
8. 🔥 What if `A.greet()` keeps state (e.g., a counter of how many times it's called)? Does the diamond problem cause it to be called twice without `super()`? Test and confirm.
9. Create a diamond hierarchy where the shared base `A` has an `__init__`. Show that with `super()`, `A.__init__` is called exactly once.
10. 🔥 Research other programming languages (e.g., Java, C++). How do they handle (or avoid) the diamond problem?
11. Create your own diamond problem scenario in a real-world context: for example, `Appliance → WashingMachine`, `Appliance → Dryer`, `WasherDryer(WashingMachine, Dryer)`. Implement it.
12. 🔥 What happens in the diamond problem if only some classes in the chain call `super()`? Create this case and explain the consequences.
13. Explain the role of `object` at the top of every Python hierarchy in relation to the diamond problem.
14. 🔥 Create a diamond hierarchy and add a class attribute with the same name in both `B` and `C`. Which one does `D` inherit? Use MRO to explain.
15. 🔥 Design a "safe" diamond hierarchy that properly uses `super()` at every level so each method runs exactly once. Use print statements to verify.

---

## 15. `isinstance()` and `issubclass()`

### Explanation

These two built-in functions let you **inspect and verify object relationships** at runtime.

**`isinstance(object, class)`** — checks if an object is an instance of a class OR its subclasses.

```python
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()

print(isinstance(d, Dog))     # True — d is a Dog
print(isinstance(d, Animal))  # True — d is also an Animal (via inheritance)
print(isinstance(d, str))     # False — d is not a string
```

**`issubclass(subclass, superclass)`** — checks if one class is a subclass of another.

```python
print(issubclass(Dog, Animal))   # True
print(issubclass(Animal, Dog))   # False — reversed
print(issubclass(Dog, Dog))      # True — a class is a subclass of itself
print(issubclass(Dog, object))   # True — every class is a subclass of object
```

**Checking against a tuple of types:**

```python
print(isinstance(d, (Dog, Cat, Bird)))  # True if d is ANY of these
print(issubclass(Dog, (Animal, Vehicle)))  # True if Dog is subclass of ANY of these
```

**Practical use — input validation:**

```python
def process_animal(a):
    if not isinstance(a, Animal):
        raise TypeError(f"Expected Animal, got {type(a).__name__}")
    print(f"Processing {type(a).__name__}")

process_animal(d)        # Works
process_animal("hello")  # Raises TypeError
```

---

### Tasks — `isinstance()` and `issubclass()`

1. Create a three-level hierarchy. Use `isinstance()` to check an object of the deepest class against every class in the hierarchy. Note the results.
2. Use `issubclass()` to check all possible subclass relationships in a hierarchy of four classes.
3. What does `isinstance(d, object)` return for any object `d`? Why?
4. Demonstrate that `isinstance()` returns `True` for parent classes, not just the direct class.
5. Create a function `describe(shape)` that uses `isinstance()` to detect the actual type and calls the appropriate method (e.g., `area()` for `Circle` or `perimeter()` for `Rectangle`).
6. Create a list of mixed objects (Dogs, Cats, Strings, Integers). Use `isinstance()` to filter only `Animal` instances.
7. Is `isinstance(Dog, type)` `True`? Test it and explain what `type` means here.
8. What is the difference between `type(obj) == Dog` and `isinstance(obj, Dog)` when inheritance is involved? Demonstrate.
9. 🔥 Why is `isinstance()` generally preferred over `type() ==` for type checking in Python?
10. Create a `validate(value, expected_type)` utility function that raises a `TypeError` with a descriptive message if the value is not the expected type.
11. 🔥 Use `isinstance()` with a tuple of types. Create `is_number(x)` that returns `True` if `x` is `int`, `float`, or `complex`.
12. 🔥 Create a class `MultiType` that registers multiple parent classes using `ABC` or a custom `__instancecheck__`. Explore how Python allows customising `isinstance()` behavior.
13. `issubclass(bool, int)` — is this `True`? Why? What does this tell you about Python's class hierarchy?
14. 🔥 Create a decorator that uses `isinstance()` to enforce type checking on function arguments.
15. 🔥 What is the `__class__` attribute? How does it relate to `isinstance()`? Explore with an example.

---

## 16. Protected and Private Members in Inheritance

### Explanation

Python uses naming conventions to indicate access levels for attributes and methods.

| Access Level | Convention | Example | Accessible From |
|---|---|---|---|
| Public | No prefix | `self.name` | Anywhere |
| Protected | Single underscore | `self._name` | Class & subclasses (by convention) |
| Private | Double underscore | `self.__name` | Only within the defining class |

**Public attributes** — accessible everywhere.

```python
class Animal:
    def __init__(self):
        self.name = "Generic"  # Public
```

**Protected attributes** — intended for use within the class and subclasses. The single underscore is a *convention*, not enforcement.

```python
class Animal:
    def __init__(self):
        self._health = 100  # Protected by convention

class Dog(Animal):
    def take_damage(self, amount):
        self._health -= amount  # OK — child accessing protected attribute
        print(f"Health: {self._health}")
```

**Private attributes — name mangling:**
Double underscore causes Python to rename the attribute to `_ClassName__attribute`. This prevents accidental overriding in subclasses.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private — name mangled to _BankAccount__balance

    def get_balance(self):
        return self.__balance       # Accessible within the class

class SavingsAccount(BankAccount):
    def show(self):
        # print(self.__balance)    # AttributeError! Mangled name is different
        print(self._BankAccount__balance)  # Technically works but bad practice

acc = BankAccount(1000)
# print(acc.__balance)   # AttributeError
print(acc._BankAccount__balance)   # Works — but breaks encapsulation
```

---

### Tasks — Protected and Private Members in Inheritance

1. Create an `Employee` class with a public attribute `name`, a protected attribute `_salary`, and a private attribute `__id`. Print all three from inside the class.
2. Try to access `__id` from outside the class. What error do you get?
3. Try to access `_salary` from outside the class. Does it work? What does this tell you about the single underscore?
4. Create a `Vehicle` class with `_speed` (protected). Create `Car` that modifies `_speed` in a method. Verify this works from the child class.
5. Try to access a parent's `__private` attribute directly in a child class. What happens? How do you access it using the mangled name?
6. 🔥 What is **name mangling**? Explain why Python does it (hint: what problem does it solve in inheritance?).
7. Create a class with both a protected method `_validate()` and a public method `save()` that calls `_validate()` internally. Create a subclass that overrides `_validate()`.
8. Create a `Person` class with `__ssn` (private). Add a `get_ssn()` and `set_ssn()` method (getter/setter). Show that this is the correct way to expose private data.
9. 🔥 Create a `BankAccount` class with `__balance`. Create `SavingsAccount` that needs to access the balance. Show the correct (using getter methods) and incorrect (direct access) approaches.
10. 🔥 Demonstrate that name mangling prevents a child class from accidentally overriding a parent's private attribute. Create a scenario where both parent and child define `__value` — show they are different attributes.
11. Create a class hierarchy where the protected attribute `_status` is modified at each level of the hierarchy. Print `_status` at each level to trace how it changes.
12. 🔥 Python's single underscore is "by convention only". Write code that proves you can still access `_protected` from outside the class. Then explain why you shouldn't.
13. 🔥 What is a **property** (`@property`)? Create a class with a private attribute `__age` and expose it using `@property` getter and setter with validation.
14. Research: How do other languages (Java, C++) enforce access control? How is Python's approach different?
15. 🔥 Create a `Config` class that stores sensitive settings in private attributes. Create a `DevelopmentConfig(Config)` subclass that overrides some settings. Use name mangling correctly so parent and child don't clash.

---

## 17. Polymorphism and Inheritance

### Explanation

**Polymorphism** means "many forms." In OOP, it means that the same method name can produce different behavior depending on the object that calls it.

Inheritance is the primary mechanism through which polymorphism is achieved.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Duck(Animal):
    def speak(self):
        print("Quack!")

# Polymorphism in action
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    animal.speak()   # Each calls its own speak() — same name, different behavior
# Woof!
# Meow!
# Quack!
```

**Duck Typing:**
Python allows polymorphism without inheritance. If an object has the right method, it can be used — regardless of its class.

```python
class Car:
    def fuel_up(self):
        print("Adding petrol...")

class ElectricCar:
    def fuel_up(self):
        print("Charging battery...")

# Neither inherits from a common base, yet they work the same way
for vehicle in [Car(), ElectricCar()]:
    vehicle.fuel_up()
```

**Runtime method resolution:**
Python decides which `speak()` to call at runtime, based on the actual type of the object.

---

### Tasks — Polymorphism and Inheritance

1. Create a `Shape` hierarchy with `Circle`, `Square`, and `Triangle`. Each has an `area()` method. Write a function `print_area(shape)` that calls `shape.area()` polymorphically.
2. Demonstrate polymorphism with a list of different shape objects. Loop and call `area()` on each.
3. What is duck typing? Create an example with two unrelated classes that have the same method name. Show they can be used interchangeably.
4. Create a `Payment` hierarchy: `CreditCard`, `PayPal`, and `Crypto`. Each has `process(amount)`. Loop through a list and process all payments.
5. Create a `Renderer` class with `render()`. Create `HTMLRenderer` and `PDFRenderer`. Write code that switches between them based on a condition.
6. 🔥 What is the difference between **compile-time polymorphism** and **runtime polymorphism**? Which type does Python use?
7. Create a `Vehicle` base class and a function `start_all(vehicles)` that calls `start()` on every vehicle in a list. Test with `Car`, `Bike`, and `Truck`.
8. 🔥 Can Python have two methods with the same name but different parameters in the same class (method overloading)? What happens if you try? How do you simulate it?
9. Create a `Discount` hierarchy: `NoDiscount`, `TenPercent`, `Seasonal`. Each has `apply(price)`. Write code that applies discounts polymorphically.
10. 🔥 What is the "Liskov Substitution Principle" (LSP)? Explain it in simple terms with an example. Why is it important for polymorphism?
11. 🔥 Violate the Liskov Substitution Principle. Show code where a subclass breaks the expected behavior of a parent. Then fix it.
12. Create a `Sorter` class with `sort(data)`. Create `BubbleSorter`, `QuickSorter`, and `MergeSorter` that each implement their own `sort()`. Test them polymorphically.
13. 🔥 Explain the difference between **polymorphism via inheritance** and **polymorphism via interfaces (abstract classes)**. Give an example of each.
14. Demonstrate that Python's `len()` function is polymorphic — it works on lists, strings, tuples, and dicts. What magic method makes this possible?
15. 🔥 Create a complete polymorphic system: `Notification(Email, SMS, Push)`. A `NotificationService` takes any `Notification` object and calls `send()`. Add a `log()` method in the base class that is shared. Test all three types.

---

## 18. Abstract Classes and Inheritance

### Explanation

An **abstract class** is a class that cannot be instantiated directly. It is designed to be a blueprint that other classes must follow. Abstract classes define a contract — methods that every subclass MUST implement.

Python provides the `abc` module (Abstract Base Classes) for this purpose.

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass   # No implementation — subclasses must provide one

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):   # Concrete method — NOT abstract
        print(f"I am a shape with area {self.area()}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


# Shape()  # TypeError: Can't instantiate abstract class Shape
c = Circle(5)
c.describe()        # Concrete method from Shape
print(c.area())     # Implemented in Circle
```

**Key rules:**
- Inherit from `ABC` (or `ABCMeta`).
- Use `@abstractmethod` decorator on methods that must be overridden.
- Any subclass that does not implement ALL abstract methods cannot be instantiated.

---

### Tasks — Abstract Classes and Inheritance

1. Create an abstract class `Animal` with abstract methods `speak()` and `move()`. Create two concrete subclasses and implement both methods.
2. Try to instantiate an abstract class. What error does Python raise? Document it.
3. What happens if a subclass only implements ONE of two abstract methods? Test and explain.
4. Create an abstract class `Vehicle` with abstract methods `start()` and `stop()`, and a concrete method `fuel_type()`. Create `Car` and `Boat` as subclasses.
5. Can an abstract class have a constructor? Create one with `__init__` and verify it runs when a concrete subclass is instantiated.
6. 🔥 Create an abstract class `DataStore` with abstract methods `read(key)` and `write(key, value)`. Implement `InMemoryStore` and `FileStore` as concrete classes.
7. What is the difference between an abstract class and a regular class? List at least five differences.
8. Can an abstract class inherit from another abstract class? Test and explain.
9. 🔥 Create a fully abstract class `Serializer` with `serialize(data)` and `deserialize(data)`. Create `JSONSerializer` and `XMLSerializer` implementations.
10. Demonstrate that you can have both abstract and concrete methods in the same abstract class. Show a concrete method being inherited and used by subclasses.
11. 🔥 What is the difference between an abstract class and an interface? Python doesn't have interfaces — how do you simulate them?
12. 🔥 Create an abstract class `Plugin` with an abstract `execute()` method. Create three plugins: `LogPlugin`, `CachePlugin`, and `AuthPlugin`. Then create a `PluginRunner` that runs them all.
13. 🔥 What is `ABCMeta`? How is `class MyABC(metaclass=ABCMeta)` different from `class MyABC(ABC)`?
14. Create an abstract class `ReportGenerator` with abstract methods `fetch_data()`, `format_data()`, and `output()`. Implement `CSVReport` and `HTMLReport`.
15. 🔥 Research and explain how Python's built-in abstract base classes (`collections.abc.Sequence`, `collections.abc.Mapping`, etc.) work. Create a custom class that satisfies `collections.abc.Sequence`.

---

## 19. Inheritance vs Composition

### Explanation

Inheritance ("is-a") and Composition ("has-a") are the two primary code-reuse strategies in OOP.

**When to use Inheritance:**
Use it when a genuine "is-a" relationship exists. A `Dog` IS AN `Animal`. A `SavingsAccount` IS A `BankAccount`.

**When to use Composition:**
Use it when a "has-a" relationship exists. A `Car` HAS AN `Engine`. A `Person` HAS AN `Address`.

```python
# Inheritance example (is-a)
class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):   # A Dog IS AN Animal
    def bark(self):
        print("Woof!")


# Composition example (has-a)
class Engine:
    def start(self):
        print("Engine starting...")

class Car:           # A Car HAS AN Engine
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        self.engine.start()     # Delegate to Engine
        print("Car is ready.")
```

**Problems with over-using inheritance:**
- Tight coupling — child breaks when parent changes.
- "Fragile base class" problem.
- Deep chains become hard to understand and maintain.
- Forced "is-a" relationships that don't really fit.

**Favour composition when:**
- You want to change behavior at runtime (swap out components).
- The relationship is flexible or optional.
- You want to combine behaviors from multiple unrelated classes.

```python
# Composition allows swapping behavior at runtime
class Logger:
    def log(self, msg):
        print(f"[LOG]: {msg}")

class FileLogger:
    def log(self, msg):
        print(f"[FILE]: {msg}")

class App:
    def __init__(self, logger):
        self.logger = logger  # Inject any logger

    def run(self):
        self.logger.log("App is running.")

App(Logger()).run()
App(FileLogger()).run()
```

---

### Tasks — Inheritance vs Composition

1. Define "is-a" and "has-a" in your own words. Give two examples of each.
2. Classify each relationship as inheritance or composition: (a) `Dog` and `Animal`, (b) `Car` and `Wheel`, (c) `Teacher` and `Person`, (d) `House` and `Room`, (e) `ElectricCar` and `Car`.
3. Create a composition example: `Library` HAS many `Book` objects. `Library` should have `add_book()`, `remove_book()`, and `list_books()` methods.
4. Rewrite the following using composition instead of inheritance: `class SportsCar(Car): ...` — extract behavior into components.
5. 🔥 What is the "fragile base class" problem? Create an example where changing the parent class breaks the child unexpectedly.
6. Create a `Robot` class using composition: it HAS a `MotorSystem`, `SensorSystem`, and `AIBrain`. Each component has its own methods. `Robot` delegates to them.
7. 🔥 Create the same example twice: once using inheritance and once using composition. Compare the readability, flexibility, and coupling.
8. 🔥 What is the "favour composition over inheritance" principle (from the Gang of Four)? Explain it with an example.
9. Create a `GameCharacter` using composition: it HAS a `Weapon`, `Armor`, and `Skill`. Allow swapping weapons at runtime.
10. When does inheritance genuinely make sense? Give five real scenarios where inheritance is clearly the right choice.
11. 🔥 Create a strategy pattern using composition: `Sorter` class that takes a `SortStrategy` object (`BubbleSort`, `QuickSort`). The strategy can be swapped at runtime.
12. 🔥 Does Python's mixin pattern blur the line between inheritance and composition? Explain.
13. Create a `Report` class that uses composition to plug in a `DataFetcher` and a `Formatter`. The `Report` class doesn't care about the specific implementations.
14. 🔥 Research the SOLID principles. Which principle directly relates to the preference for composition over inheritance?
15. 🔥 Take any inheritance hierarchy you built earlier in these notes and refactor it using composition. Compare: which version is better, and why?

---

## 20. Common Mistakes in Inheritance

### Explanation

Even experienced developers make mistakes with inheritance. Knowing these pitfalls will save you hours of debugging.

**Mistake 1: Forgetting `super()`**
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # Forgot super()! self.name is never set
        self.breed = breed

d = Dog("Rex", "Poodle")
# print(d.name)  # AttributeError
```

**Mistake 2: Overriding methods improperly**
```python
class Animal:
    def speak(self):
        print("Animal speaking...")
        self._make_sound()  # Expects subclass to define this

class Dog(Animal):
    def speak(self):  # Completely replaces parent's logic — _make_sound never called
        print("Woof!")
```

**Mistake 3: Deep inheritance chains**
Long chains (5+ levels) become extremely hard to follow and debug.

**Mistake 4: Misusing inheritance for code reuse**
```python
# Bad — using inheritance just to reuse a method
class JSONHelper:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(JSONHelper):   # User is NOT a JSONHelper — this is wrong
    ...

# Better — use composition or a standalone function
```

**Mistake 5: Tight coupling**
The child depends too heavily on parent implementation details, breaking when the parent changes.

---

### Tasks — Common Mistakes in Inheritance

1. Reproduce the "forgetting `super()`" mistake. Show the exact error and then fix it.
2. Create a class hierarchy where a child completely overrides a parent method, accidentally discarding important logic. Show the bug, then fix it using `super()`.
3. 🔥 What does "tight coupling" mean in the context of inheritance? Create an example and show how a change in the parent breaks the child.
4. Reproduce an error caused by a deep inheritance chain (5 levels). Trace the bug through the chain.
5. Create an example of misusing inheritance for code reuse (use-a not is-a). Then refactor it using composition.
6. What happens if you call `super().__init__()` multiple times in a class? Is it dangerous?
7. 🔥 Create a case where a child class changes the signature (parameters) of an overridden method. Show how this can break code that uses the parent type polymorphically.
8. Demonstrate the mistake of accessing a parent's private attribute from a child directly. Show the error and the correct fix.
9. 🔥 What is the "Liskov Substitution Principle" violation? Create an example (e.g., a `Square` that breaks `Rectangle` behavior) and explain why it's a mistake.
10. Show what happens when you forget to call `super().__init__()` in a multiple inheritance chain. Which parent's constructor gets missed?
11. Create a "god class" parent that has too many responsibilities. Show how it leads to bad inheritance. Refactor it.
12. 🔥 What is the "fragile base class" problem? Create a scenario where the parent is refactored, breaking a child unexpectedly.
13. Demonstrate incorrect method overriding where the child's method returns a different type than the parent's. Why is this a problem?
14. 🔥 Create an example of circular inheritance (A inherits from B, B inherits from A). What error does Python raise?
15. 🔥 Create a checklist of at least ten questions to ask yourself before using inheritance in your code.

---

## 21. Best Practices

### Explanation

Follow these principles to write clean, maintainable inheritance code.

1. **Keep inheritance shallow** — prefer 2-3 levels max. Deep chains are hard to follow.
2. **Use meaningful class hierarchies** — only inherit when a real "is-a" relationship exists.
3. **Prefer composition when suitable** — when in doubt, compose rather than inherit.
4. **Override responsibly** — don't discard parent logic unnecessarily. Use `super()`.
5. **Keep parent classes generic** — parents should be general blueprints, not too specific.
6. **Follow SOLID principles:**
   - **S** — Single Responsibility: each class does one thing.
   - **O** — Open/Closed: open for extension, closed for modification.
   - **L** — Liskov Substitution: subclasses should be replaceable for parents.
   - **I** — Interface Segregation: don't force clients to depend on unused methods.
   - **D** — Dependency Inversion: depend on abstractions, not concrete classes.

```python
# Good practice example
class Animal(ABC):
    """Generic, abstract parent."""
    @abstractmethod
    def speak(self): pass

class Dog(Animal):
    """Concrete, specialised child."""
    def speak(self):
        return "Woof!"

# Only 2 levels, clear relationship, specific child, abstract parent
```

---

### Tasks — Best Practices

1. List the six best practices from the notes and explain each one in your own words.
2. Explain each letter of the SOLID principles with your own example.
3. Take any hierarchy you built earlier and evaluate it against all six best practices. Does it comply? Improve it where needed.
4. Create a "bad" inheritance example that violates at least three best practices. Then refactor it to follow them.
5. 🔥 What does "Open/Closed Principle" mean? Create a `Shape` example that is open for extension (new shapes) but closed for modification (existing code never changes).
6. What is the maximum recommended depth for an inheritance hierarchy? Justify your answer.
7. 🔥 Create a class hierarchy that satisfies ALL SOLID principles. Use at least five classes.
8. 🔥 What is the "Single Responsibility Principle" violation in inheritance? Create a parent class that does too much, then split it.
9. Research a Python open-source project (e.g., Django, Flask). Find an example of inheritance in their codebase. Does it follow best practices?
10. 🔥 Create a hierarchy that violates the Liskov Substitution Principle. Then refactor it to comply.
11. 🔥 What is "programming to an interface" and how does Python's `ABC` support it?
12. Compare two inheritance hierarchies: one shallow (2 levels) and one deep (5 levels). Which is easier to understand, test, and maintain?
13. 🔥 The "Dependency Inversion Principle" says to depend on abstractions. Create a `NotificationService` that depends on an abstract `Notifier`, not a concrete `EmailNotifier`.
14. 🔥 What is the "Interface Segregation Principle"? Show how a single large abstract class can be split into smaller, more focused abstract classes.
15. 🔥 Write a one-page design document (in code comments or docstrings) for a class hierarchy of your choosing, explicitly addressing every best practice before writing a single line of class code.

---

## 22. Advanced Concepts

### Explanation

**Cooperative Multiple Inheritance:**
When all classes in a chain properly use `super()`, they cooperate to ensure every class in the MRO gets a chance to run.

```python
class A:
    def process(self):
        print("A processing")

class B(A):
    def process(self):
        print("B processing")
        super().process()

class C(A):
    def process(self):
        print("C processing")
        super().process()

class D(B, C):
    def process(self):
        print("D processing")
        super().process()

D().process()
# D processing → B processing → C processing → A processing
```

**Mixins:**
Mixins are small classes designed to add a specific feature via multiple inheritance. They are not meant to be standalone classes.

```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class TimestampMixin:
    def timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()

class User(JSONMixin, TimestampMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

u = User("Alice", "alice@example.com")
print(u.to_json())
print(u.timestamp())
```

**Dynamic Inheritance:**
Python allows creating classes dynamically at runtime using `type()`.

```python
# Dynamically create a class
MyClass = type("MyClass", (Animal,), {"sound": lambda self: "Dynamic!"})
obj = MyClass()
print(obj.sound())
```

---

### Tasks — Advanced Concepts

1. Implement cooperative multiple inheritance with three classes all defining the same method, all using `super()`. Trace the full output.
2. Create a `LogMixin` that adds a `log(msg)` method. Apply it to two unrelated classes: `User` and `Order`.
3. Create a `ValidationMixin` with `validate()` that checks all instance attributes are not empty. Apply it to `Product` and `Customer`.
4. 🔥 What makes a class a "proper" mixin vs a regular class? List the conventions/rules.
5. 🔥 Create a `SingletonMixin` that ensures only one instance of a class can exist. Apply it to a `Config` class.
6. 🔥 Create a `RepresentationMixin` that automatically generates `__repr__` and `__str__` from `self.__dict__`. Apply it to three different classes.
7. Create a `SerializableMixin` with `to_dict()` and `from_dict()`. Apply to `User` and `Product`.
8. 🔥 Use `type()` to dynamically create a subclass at runtime. Pass methods as a dictionary. Instantiate and call a method.
9. 🔥 What is a **metaclass** in Python? How does it relate to inheritance? Create a simple metaclass that adds a class attribute to every class that uses it.
10. 🔥 Explore `__init_subclass__`. What does it do? Create an example where a parent uses `__init_subclass__` to automatically register all subclasses.
11. Create a mixin `EquatableMixin` that implements `__eq__` and `__hash__` based on a `primary_key` attribute defined in the subclass.
12. 🔥 Research and implement the **Observer pattern** using inheritance. Create `Observable` as a base class and multiple `Observer` subclasses.
13. 🔥 How does Django's Model class use inheritance behind the scenes? Research and explain.
14. 🔥 Implement a **plugin system** using `__init_subclass__`: a `Plugin` base class that automatically tracks all registered plugins in a class-level list.
15. 🔥 What is the `__class_getitem__` method? How is it used in Python's generic types? Create a simple generic container class using it.

---

## 23. Real-World Practice Projects

### Explanation

The best way to master inheritance is to build complete systems. Below are project ideas with starter guidance.

**Example: Animal Management System (starter)**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    @abstractmethod
    def speak(self):
        pass

    def describe(self):
        print(f"{self.name} ({self.species}), age {self.age}")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Canis lupus familiaris")
        self.breed = breed

    def speak(self):
        print(f"{self.name}: Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name}: Meow!")
```

---

### Tasks — Real-World Practice Projects

> **Build each project fully** — not just the classes, but also test code that creates objects, calls methods, and demonstrates the inheritance in action.

1. **Animal Management System:** Create `Animal` (abstract), `Dog`, `Cat`, `Bird`, `Fish`. Include attributes like `name`, `age`, `diet`. Add methods `speak()`, `move()`, and `describe()`. Create a shelter that holds multiple animals.

2. **School Management System:** Create `Person` as base, then `Student` and `Teacher`. `Student` has grades and GPA logic. `Teacher` has subjects and schedule. Create a `School` class that manages both.

3. **Banking Application:** Create `BankAccount` with `deposit()`, `withdraw()`, and `balance`. Create `SavingsAccount` (with interest), `CheckingAccount` (with overdraft limit), and `FixedDeposit` (can't withdraw until maturity).

4. **Vehicle Hierarchy:** Create `Vehicle → MotorVehicle → Car/Truck/Motorcycle` and `Vehicle → NonMotorVehicle → Bicycle/Skateboard`. Each has appropriate attributes and methods.

5. **Employee Management System:** Create `Employee` with `name`, `salary`, `department`. Create `FullTimeEmployee`, `PartTimeEmployee`, `Contractor`. Add `calculate_pay()` and `generate_report()` methods.

6. **Game Character Hierarchy:** Create `Character` with `name`, `health`, `level`. Create `Warrior`, `Mage`, `Archer`. Each has unique attack/defense methods. Create a simple battle simulation.

7. **GUI Component System:** Create abstract `Widget` with `render()` and `handle_click()`. Create `Button`, `TextBox`, `Label`, `Checkbox`. Each renders and handles events differently.

8. **E-Commerce Product System:** Create `Product` base, then `PhysicalProduct` (has weight/dimensions), `DigitalProduct` (has download link), `ServiceProduct` (has duration).

9. **Notification System:** Create abstract `Notification` with `send(message)`. Create `EmailNotification`, `SMSNotification`, `PushNotification`. Create a `NotificationManager` that sends to multiple channels.

10. **Restaurant Ordering System:** Create `MenuItem` base, then `Food`, `Drink`, and `Combo`. Create `Order` that holds multiple items. Add `calculate_total()`, `apply_discount()`, and `generate_receipt()`.

11. **Library Management System:** Create `LibraryItem` base, then `Book`, `Magazine`, `DVD`. Track `checked_out` status. Create `Member` and `LibraryCard`. Implement `checkout()` and `return_item()`.

12. **Social Media Post System:** Create `Post` base, then `TextPost`, `ImagePost`, `VideoPost`. Add `like()`, `comment()`, and `share()`. Create a `Feed` that manages posts.

13. **Transport Booking System:** Create `Transport` base, then `Flight`, `Train`, `Bus`. Each has different seat classes and booking rules. Create a `Booking` system.

14. 🔥 **Plugin System:** Create a `Plugin` abstract base class with `execute()`. Create at least five plugins. Create a `PluginManager` that loads and runs them dynamically.

15. 🔥 **ORM (Object-Relational Mapper) Mini-Project:** Create a `Model` base class with `save()`, `delete()`, and `find()` methods that simulate database operations. Create `User`, `Post`, and `Comment` models that inherit from `Model`. Store data in a dictionary to simulate a database.

---

## 24. Debugging Inheritance

### Explanation

Debugging inheritance issues requires systematic tools and techniques.

**Using `dir()`** — lists all attributes and methods of an object.
```python
class Animal:
    def breathe(self): pass

class Dog(Animal):
    def bark(self): pass

d = Dog()
print(dir(d))   # All methods including inherited ones and dunder methods
```

**Using `__class__` and `type()`** — identify the actual class of an object.
```python
print(type(d))         # <class '__main__.Dog'>
print(d.__class__)     # <class '__main__.Dog'>
print(d.__class__.__name__)   # Dog
```

**Inspecting MRO** — understand the method lookup order.
```python
print(Dog.mro())
print(Dog.__mro__)
```

**Using `vars()`** — shows only instance attributes (not methods).
```python
d = Dog("Rex", "Poodle")
print(vars(d))   # {'name': 'Rex', 'breed': 'Poodle'}
```

**Using `inspect` module:**
```python
import inspect
print(inspect.getmembers(Dog, predicate=inspect.isfunction))
print(inspect.getmro(Dog))
```

---

### Tasks — Debugging Inheritance

1. Create a three-level hierarchy and use `dir()` on the deepest child. Categorise the output into: (a) inherited from grandparent, (b) inherited from parent, (c) defined in child, (d) from `object`.
2. Use `type()` and `__class__` on objects from different levels of your hierarchy. Compare the outputs.
3. Create a bug where a child's method name accidentally shadows a parent's method (same name, different purpose). Use debugging tools to identify and fix it.
4. Use `vars()` on an object and explain what it shows vs what `dir()` shows.
5. Use the `inspect` module to list only the methods defined directly in a class (not inherited). How do you distinguish them?
6. 🔥 Create a scenario where `AttributeError` occurs due to a missing `super().__init__()` call. Use `vars()` to diagnose the problem.
7. Use `inspect.getmro()` to inspect the MRO of a class with multiple inheritance. Compare it to `ClassName.mro()`.
8. Create a class with a method that calls `super()` incorrectly. Trace the error through the stack trace.
9. 🔥 Write a debugging utility function `inspect_hierarchy(cls)` that prints the full MRO, all methods at each level, and which level each method belongs to.
10. 🔥 Create a `trace_method` decorator that prints `"Calling [ClassName].[method_name]"` every time an inherited method is called. Apply it to a hierarchy.
11. Use `hasattr()` and `getattr()` to safely access attributes on objects of unknown types. Create an example where this is useful.
12. 🔥 Create a scenario where a method from a mixin accidentally overrides a method from a main parent. Use MRO inspection to identify and fix it.
13. 🔥 Explore `__dict__` at the class level vs the instance level. What is the difference? How does it help in debugging?
14. Create a utility `print_method_origin(obj, method_name)` that tells you which class in the hierarchy actually defines a given method.
15. 🔥 Simulate a complex multiple inheritance bug where the wrong method is called. Document your full debugging process: tools used, findings, fix applied.

---

## 25. Final Mastery Topics

### Explanation

This final section covers advanced design thinking, interview preparation, and reading real-world code.

**Designing scalable hierarchies:**
- Start with the most general abstraction.
- Add specificity as you go deeper.
- Evaluate every new class: should it extend or compose?

**Reading framework code:**
Major Python frameworks use inheritance extensively:
- **Django:** `Model`, `View`, `Form` all use inheritance.
- **Flask:** `Blueprint` uses inheritance for extension.
- **unittest:** `TestCase` is a base class for all test classes.

```python
# Example — Django model (simplified)
class Model:
    def save(self): ...
    def delete(self): ...

class User(Model):     # Inherits save, delete
    username = ...
    email = ...

# Example — unittest
import unittest

class MyTest(unittest.TestCase):   # Inherits setUp, tearDown, assert methods
    def test_something(self):
        self.assertEqual(1 + 1, 2)
```

**Common interview questions on inheritance:**

1. What is the difference between `override` and `overload`?
2. Can you call the parent's `__init__` without `super()`?
3. What is MRO and how does C3 Linearisation work?
4. What is the diamond problem and how does Python solve it?
5. When would you use composition instead of inheritance?

---

### Tasks — Final Mastery

1. Design (on paper or in comments) a scalable class hierarchy for a hospital management system. Include: `Person`, `Patient`, `Doctor`, `Nurse`, `Staff`. Justify every design decision.
2. Implement the hospital management system from Task 1 in Python. Test every class.
3. 🔥 Read the source code of `unittest.TestCase`. Identify which methods are designed to be inherited, which are designed to be overridden, and which are abstract-like.
4. 🔥 Read Django's `Model` class documentation. List five examples of inheritance being used by Django's ORM.
5. Answer these interview questions in writing (3-5 sentences each): (a) What is inheritance? (b) What is MRO? (c) What is the diamond problem? (d) What is method overriding? (e) When should you use composition?
6. 🔥 Refactor an inheritance hierarchy from earlier in these notes to be more scalable. Document every change and the reason for it.
7. 🔥 Create a complete test suite (using `unittest`) for a class hierarchy. Test: attribute inheritance, method inheritance, overriding, `isinstance`, `issubclass`.
8. 🔥 Research Python's `dataclasses`. How do they interact with inheritance? Create an example of inheriting a dataclass.
9. 🔥 Research `__slots__`. How do `__slots__` affect inheritance? Create an example and explain.
10. 🔥 Read about Protocol (from `typing`). How is `Protocol` different from `ABC`? When would you use each?
11. 🔥 Create a mini-framework (like a tiny version of Django) that uses inheritance for its core: a `Model` class, a `View` class, and a `Controller` class.
12. 🔥 What is "monkey patching"? How does it relate to inheritance? Create an example and explain the risks.
13. 🔥 Compare Python's inheritance to inheritance in Java or C++. List five similarities and five differences.
14. 🔥 Create a quiz application (as a class hierarchy) that tests another student's knowledge of inheritance. Include at least 10 questions of different types.
15. 🔥 **Capstone Project:** Design and implement a complete application of your choosing that demonstrates EVERY major concept from these notes: single inheritance, multilevel, hierarchical, multiple inheritance, MRO, `super()`, method overriding, abstract classes, polymorphism, and mixins. Write a brief report explaining how each concept is used.

---

## Quick Reference

### Key Syntax

```python
# Basic inheritance
class Child(Parent):
    pass

# super() in __init__
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

# Abstract class
from abc import ABC, abstractmethod
class Abstract(ABC):
    @abstractmethod
    def method(self): pass

# Multiple inheritance
class Child(Parent1, Parent2):
    pass

# Check MRO
print(ClassName.mro())

# isinstance / issubclass
isinstance(obj, ClassName)
issubclass(ChildClass, ParentClass)
```

### Key Terms Glossary

| Term | Definition |
|---|---|
| Inheritance | A mechanism where a class acquires attributes and methods from another class |
| Superclass | The parent class being inherited from |
| Subclass | The child class that inherits |
| `super()` | Built-in function to access parent class methods |
| Method Overriding | Redefining a parent method in a child class |
| MRO | Method Resolution Order — the search order for methods in a hierarchy |
| Diamond Problem | Ambiguity when a class inherits from two classes with a common ancestor |
| Polymorphism | Same method name, different behavior depending on the object |
| Abstract Class | A class that cannot be instantiated; defines required methods for subclasses |
| Mixin | A small class designed to add specific functionality via multiple inheritance |
| Composition | Building a class by including instances of other classes ("has-a") |
| Duck Typing | Using objects based on their behavior rather than their type |
| Name Mangling | Python's transformation of `__attr` to `_ClassName__attr` |

---

*End of Notes — Python Inheritance*

> **Tip for students:** Don't rush. Read each section twice, then attempt the tasks without looking at the notes. Only look back when you are genuinely stuck. The tasks are designed to be challenging — that difficulty is where learning happens.