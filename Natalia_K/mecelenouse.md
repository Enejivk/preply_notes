# Object-Oriented Programming: Miscellaneous Topics
### A Beginner-Friendly Guide for Python Students

> **How to use this note:** Each topic builds on the previous one. Read through in order, run every code example yourself, and attempt the exercises before looking at solutions. The goal is not just to understand the syntax — it's to understand *why* these features exist.

---

## Table of Contents

1. [Multiple Inheritance](#1-multiple-inheritance)
2. [Method Resolution Order (MRO)](#2-method-resolution-order-mro)
3. [Method Overriding](#3-method-overriding)
4. [Polymorphism](#4-polymorphism)
5. [Method Overloading](#5-method-overloading)
6. [Operator Overloading](#6-operator-overloading)
7. [Static Methods](#7-static-methods)
8. [Class Methods](#8-class-methods)
9. [Abstraction](#9-abstraction)

---

## 1. Multiple Inheritance

### What Is It?

**Multiple Inheritance** is when a class inherits from **more than one parent class** at the same time.

In regular inheritance, one child class gets features from one parent. Multiple inheritance lets a child class combine features from two or more parents.

### Why Does It Exist?

Sometimes a concept in the real world naturally belongs to more than one category. Instead of copying code between classes, multiple inheritance lets you reuse existing classes and combine their behaviours cleanly.

### Real-World Analogy

Think of a **SmartTV**. It behaves like a **Television** (it has a screen, shows content) and also like a **Computer** (it has apps, a browser, Wi-Fi). A SmartTV *inherits* from both worlds. You wouldn't want to rewrite all the TV logic inside the SmartTV — you just bring both sets of features together.

### Syntax

```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):  # inherits from both
    pass
```

### Example 1: A Simple Combination

```python
class Flyable:
    def fly(self):
        print("I can fly!")

class Swimmable:
    def swim(self):
        print("I can swim!")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack!")

donald = Duck()
donald.fly()    # I can fly!
donald.swim()   # I can swim!
donald.quack()  # Quack!
```

**Step-by-step explanation:**
- `Flyable` defines the ability to fly.
- `Swimmable` defines the ability to swim.
- `Duck` inherits from both, so it gets both `fly()` and `swim()` for free.
- `donald` is an instance of `Duck` and can call all three methods.

### Example 2: A More Realistic Scenario

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working.")

class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying.")

class InternStudent(Employee, Student):
    def __init__(self, name):
        self.name = name  # shared attribute

    def introduce(self):
        print(f"Hi, I'm {self.name}. I work AND study.")

intern = InternStudent("Amaka")
intern.work()       # Amaka is working.
intern.study()      # Amaka is studying.
intern.introduce()  # Hi, I'm Amaka. I work AND study.
```

**Step-by-step explanation:**
- Both `Employee` and `Student` have an `__init__` that sets `self.name`.
- `InternStudent` defines its own `__init__` to avoid conflicts.
- It inherits `work()` from `Employee` and `study()` from `Student`.

### Common Mistakes Students Make

| Mistake | What Happens |
|---|---|
| Forgetting to call `super().__init__()` properly | Parent attributes don't get initialized |
| Two parents having a method with the **same name** | Python uses MRO to decide which one runs (see Section 2) |
| Inheriting from too many classes | Code becomes hard to read and maintain |

### Best Practices

- Keep each parent class focused on **one responsibility**.
- Use multiple inheritance for **mixing in** small, independent abilities (these are called **Mixins**).
- Prefer composition (has-a) over inheritance (is-a) when things get complex.

### Interview Questions

1. What is multiple inheritance? How is it different from single inheritance?
2. What problem can arise when two parent classes have a method with the same name?
3. What is a Mixin, and how does it relate to multiple inheritance?

### Exercises

1. Create a class `Printable` with a method `print_info()` and a class `Saveable` with a method `save()`. Create a class `Document` that inherits from both.
2. Create classes `ElectricPowered` and `GasPowered`, each with a `start()` method that prints a different message. Create a `HybridCar` that inherits from both. Which `start()` runs? (Hint: read the next section to find out.)

---

## 2. Method Resolution Order (MRO)

### What Is It?

**Method Resolution Order (MRO)** is the rule Python uses to decide **which class's method to call** when the same method name exists in multiple parent classes.

Think of it as Python's lookup checklist: "If I call `fly()` on this object, which class should I look in first? Second? Third?"

### Why Does It Exist?

With multiple inheritance, conflicts are inevitable. Without a clear rule, Python wouldn't know which parent's method to use. MRO gives it a deterministic, predictable answer every time.

### The Diamond Problem

The **diamond problem** is a classic dilemma in multiple inheritance. It gets its name from the shape of the inheritance diagram:

```
        A
       / \
      B   C
       \ /
        D
```

- `B` inherits from `A`
- `C` inherits from `A`
- `D` inherits from both `B` and `C`
- If both `B` and `C` define a method `greet()`, and `D` calls `greet()` — which version runs?

```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()  # Which greet() runs?
```

**Output:**
```
Hello from B
```

Python resolves this using the **C3 Linearization Algorithm**, which produces the MRO.

### How to See the MRO

```python
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Or more readable:
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```

**Python's lookup order for `D`:**
```
D → B → C → A → object
```

It goes left to right through the parents, and depth-first — but it never visits a class until all classes that inherit from it have been checked first.

### Understanding `super()`

`super()` is a built-in that lets you call the **next class in the MRO**, not just your immediate parent. This is powerful in multiple inheritance because it ensures all parent `__init__` methods get called in the correct order.

#### Without `super()` — the broken way:

```python
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        A.__init__(self)  # hard-coded — breaks with multiple inheritance
        print("B init")

class C(A):
    def __init__(self):
        A.__init__(self)  # A gets called twice!
        print("C init")

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print("D init")

D()
```

**Output (broken — A runs twice):**
```
A init
B init
A init
C init
D init
```

#### With `super()` — the correct way:

```python
class A:
    def __init__(self):
        print("A init")
        super().__init__()

class B(A):
    def __init__(self):
        print("B init")
        super().__init__()

class C(A):
    def __init__(self):
        print("C init")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D init")
        super().__init__()

D()
```

**Output (correct — A runs only once):**
```
D init
B init
C init
A init
```

**Step-by-step explanation:**
- `D.__init__` calls `super().__init__()`, which follows the MRO: next is `B`.
- `B.__init__` calls `super().__init__()`, which follows the MRO: next is `C`.
- `C.__init__` calls `super().__init__()`, which follows the MRO: next is `A`.
- `A.__init__` calls `super().__init__()`, which hits `object` — the base of everything. Done.
- Each class runs exactly once. No duplication.

### Example: MRO in a Real Scenario

```python
class Vehicle:
    def describe(self):
        print("I am a vehicle.")

class Car(Vehicle):
    def describe(self):
        print("I am a car.")
        super().describe()

class ElectricMixin:
    def describe(self):
        print("I run on electricity.")
        super().describe()

class ElectricCar(ElectricMixin, Car):
    pass

tesla = ElectricCar()
tesla.describe()
print(ElectricCar.mro())
```

**Output:**
```
I run on electricity.
I am a car.
I am a vehicle.
[ElectricCar, ElectricMixin, Car, Vehicle, object]
```

**Step-by-step explanation:**
- MRO is: `ElectricCar → ElectricMixin → Car → Vehicle → object`
- `ElectricMixin.describe()` runs first, then calls `super()` which goes to `Car.describe()`, which calls `super()` going to `Vehicle.describe()`.
- Each level in the chain runs, in MRO order.

### Common Mistakes Students Make

- Calling parent class methods directly by name (e.g. `A.__init__(self)`) instead of using `super()`.
- Assuming `super()` always calls the immediate parent — it calls the **next in MRO**, which may be a sibling class.
- Not calling `super().__init__()` in every class in the chain, which breaks the cooperative call chain.

### Best Practices

- Always use `super()` instead of hard-coding parent class names.
- Make sure every class in a cooperative hierarchy calls `super()`.
- Check `ClassName.mro()` whenever you're unsure about the lookup order.

### Interview Questions

1. What is the MRO and why is it important?
2. Explain the diamond problem with an example.
3. What does `super()` actually do? Is it always calling the immediate parent?
4. What algorithm does Python use to compute the MRO?

### Exercises

1. Create a 4-class diamond hierarchy (`A`, `B`, `C`, `D`) where every class has a `greet()` method. Use `super()` so that all four versions of `greet()` are called when `D().greet()` is invoked.
2. Call `.mro()` on a class with three levels of inheritance. Write out the order manually before running it, then verify.

---

## 3. Method Overriding

### What Is It?

**Method Overriding** is when a child class defines a method with the **same name** as a method in its parent class. When you call that method on the child, the child's version runs — not the parent's.

### Why Does It Exist?

Inheritance gives you a starting point — you get the parent's behaviour for free. But sometimes the child class needs to do the same thing *differently*. Method overriding lets the child say: "I know my parent has a `speak()` method, but I want my own version."

### Real-World Analogy

Your company has a general **Employee** contract that says employees must submit a monthly report. But **Managers** have a different kind of report than regular **Developers**. Both submit reports, but the format is different. Overriding is how each class customises the shared behaviour.

### Syntax

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):          # same name — this overrides the parent version
        print("Hello from Child")

obj = Child()
obj.greet()  # Hello from Child
```

### Example 1: Basic Override

```python
class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.speak()
```

**Output:**
```
Some generic sound
Woof!
Meow!
```

**Step-by-step explanation:**
- `Dog` and `Cat` both inherit from `Animal` but override the `speak()` method.
- When we loop through the list, each object calls its own version of `speak()`.
- This is the foundation of **polymorphism** (coming up next).

### Example 2: Calling the Parent Method Too

Sometimes you want to override *and* still include the parent's logic. Use `super()`:

```python
class Shape:
    def draw(self):
        print("Drawing a shape...")

class Circle(Shape):
    def draw(self):
        super().draw()              # call the parent's draw first
        print("...specifically, a circle.")

c = Circle()
c.draw()
```

**Output:**
```
Drawing a shape...
...specifically, a circle.
```

**Step-by-step explanation:**
- `Circle.draw()` calls `super().draw()` first to run the parent's version.
- Then it adds its own circle-specific output.
- This is useful when the parent does some setup and the child adds to it.

### Example 3: Overriding `__init__`

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)   # reuse parent's __init__
        self.company = company

    def info(self):
        super().info()                # reuse parent's info()
        print(f"Company: {self.company}")

emp = Employee("Victor", 28, "JustiGuide")
emp.info()
```

**Output:**
```
Name: Victor, Age: 28
Company: JustiGuide
```

**Step-by-step explanation:**
- `Employee.__init__` calls `super().__init__()` so the `name` and `age` attributes are still set.
- Then it adds `self.company` on top.
- `Employee.info()` calls `super().info()` to print the base info, then adds company info.

### Common Mistakes Students Make

- Forgetting to call `super().__init__()` when overriding `__init__`, so parent attributes are lost.
- Using the wrong method name (a typo means you've added a *new* method, not overridden anything).
- Overriding when you didn't intend to, by accidentally reusing a parent's method name.

### Best Practices

- Always call `super()` when the parent method does useful setup.
- Keep overrides focused — if you're changing more than one thing, consider whether the design is correct.
- Use method overriding deliberately, not by accident.

### Interview Questions

1. What is the difference between method overriding and method overloading?
2. How do you call the parent's version of a method from inside an overriding method?
3. Can you override `__init__`? What should you remember when you do?

### Exercises

1. Create a `Vehicle` class with a `fuel_type()` method that prints "Petrol". Create `ElectricCar` that overrides it to print "Electric". Create `HybridCar` that calls both the parent method and prints "Also Electric".
2. Create a `BankAccount` class with a `withdraw()` method. Create a `SavingsAccount` subclass that overrides `withdraw()` to block any withdrawal that would leave the balance below ₦5000.

---

## 4. Polymorphism

### What Is It?

**Polymorphism** means "many forms." In OOP, it means that different classes can have methods with the **same name**, and Python will call the right version depending on the object.

You've already seen this in action with method overriding. Polymorphism is the broader principle — method overriding is just one way to achieve it.

### Why Does It Exist?

Without polymorphism, you'd write code like:

```python
if type(animal) == Dog:
    animal.bark()
elif type(animal) == Cat:
    animal.meow()
```

This is messy and doesn't scale. Polymorphism lets you just write `animal.speak()` and trust that the right thing happens, no matter what type of animal it is.

### Real-World Analogy

Think of a **payment terminal**. It has one button: "Pay". Whether you tap your card, insert a chip card, or scan your phone — the terminal calls the same action. Each *payment method* handles it differently, but the interface is the same.

### Example 1: Polymorphism with a Common Interface

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Parrot:
    def speak(self):
        return "Squawk!"

animals = [Dog(), Cat(), Parrot()]

for animal in animals:
    print(animal.speak())
```

**Output:**
```
Woof!
Meow!
Squawk!
```

**Step-by-step explanation:**
- `Dog`, `Cat`, and `Parrot` are completely separate classes.
- They all have a `speak()` method with different implementations.
- The loop doesn't care what type each object is — it just calls `speak()` and polymorphism takes care of the rest.

### Example 2: Polymorphism Through Inheritance

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

def print_area(shape):
    print(f"Area: {shape.area():.2f}")

shapes = [Rectangle(4, 5), Circle(3), Rectangle(10, 2)]

for s in shapes:
    print_area(s)
```

**Output:**
```
Area: 20.00
Area: 28.27
Area: 20.00
```

**Step-by-step explanation:**
- `print_area()` accepts any `Shape` (or anything with an `area()` method).
- It doesn't know or care if it's a `Rectangle` or `Circle`.
- Python figures out which `area()` to call based on the actual object type at runtime. This is called **runtime polymorphism**.

### Example 3: Duck Typing (Python's Special Flavour)

Python has a philosophy: *"If it walks like a duck and quacks like a duck, it's a duck."* This means Python doesn't require a shared base class — as long as an object has the method, it works.

```python
class Printer:
    def print_document(self):
        print("Printing from Printer...")

class Scanner:
    def print_document(self):
        print("Printing scan preview...")

class PDFRenderer:
    def print_document(self):
        print("Rendering PDF to screen...")

devices = [Printer(), Scanner(), PDFRenderer()]

for device in devices:
    device.print_document()
```

**Step-by-step explanation:**
- None of these classes inherit from each other.
- But they all have `print_document()`, so the same code works for all of them.
- Python checks for the method at runtime — not the class hierarchy. This is duck typing.

### Common Mistakes Students Make

- Confusing polymorphism with inheritance — polymorphism can exist without inheritance (duck typing).
- Writing `if isinstance(obj, Dog)` style checks when polymorphism would make it cleaner.
- Thinking polymorphism is a separate feature you "turn on" — it's a natural result of having the same method name.

### Best Practices

- Design methods with consistent names across related classes.
- Rely on polymorphism instead of `if/elif type(x) ==` checks.
- Use abstract base classes (Section 9) to enforce that all subclasses define the same method.

### Interview Questions

1. What is polymorphism? Give a real-world example.
2. What is duck typing in Python?
3. How does polymorphism improve code maintainability?
4. What is the difference between compile-time and runtime polymorphism? (Python only supports runtime.)

### Exercises

1. Create three classes: `Circle`, `Triangle`, and `Square` — each with an `area()` method. Write a function `total_area(shapes)` that takes a list of shapes and returns the sum of all their areas.
2. Create a `Notification` base concept (no inheritance needed) with three classes: `EmailNotification`, `SMSNotification`, and `PushNotification` — each with a `send(message)` method. Write code that sends the same message through all three using a loop.

---

## 5. Method Overloading

### What Is It?

**Method Overloading** is when a class has multiple methods with the **same name but different parameters**. In Python, this is handled differently than in languages like Java or C++.

**The honest truth:** Python does **not** support traditional method overloading. If you define the same method name twice, the second definition **replaces** the first.

### Why Does the Concept Exist?

The need is real: sometimes you want a method to behave differently depending on how many arguments are passed (e.g., `add(2)` vs `add(2, 3)` vs `add(2, 3, 4)`). Python solves this elegantly with **default arguments** and **`*args`**.

### Real-World Analogy

Think of the word "book". You can *book a flight*, *book a table*, or *book a meeting*. One word, different contexts. Python achieves something similar — one method name that handles multiple input scenarios.

### What Happens Without Careful Handling

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):   # This REPLACES the one above
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       # TypeError! add() requires 3 arguments now
```

### Python's Approach 1: Default Arguments

```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       # 5  (c defaults to 0)
print(calc.add(2, 3, 4))    # 9
```

**Step-by-step explanation:**
- `c=0` makes the third argument optional.
- If you pass two values, `c` is `0`. If you pass three, `c` takes the third value.
- One method definition handles both cases cleanly.

### Python's Approach 2: Using `*args`

```python
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(2, 3))           # 5
print(calc.add(2, 3, 4))        # 9
print(calc.add(1, 2, 3, 4, 5))  # 15
```

**Step-by-step explanation:**
- `*args` collects all positional arguments into a tuple.
- `sum(args)` adds them all up, no matter how many there are.
- This is extremely flexible — any number of arguments works.

### Python's Approach 3: Using `isinstance()` for Different Types

```python
class Formatter:
    def display(self, value):
        if isinstance(value, int):
            print(f"Integer: {value}")
        elif isinstance(value, float):
            print(f"Float: {value:.2f}")
        elif isinstance(value, str):
            print(f"String: '{value}'")

f = Formatter()
f.display(42)       # Integer: 42
f.display(3.14159)  # Float: 3.14
f.display("hello")  # String: 'hello'
```

**Step-by-step explanation:**
- One `display()` method handles integers, floats, and strings.
- `isinstance()` checks the type and routes to the appropriate logic.
- This mimics overloading by type, which is common in other languages.

### Common Mistakes Students Make

- Defining the same method name twice and wondering why only one works.
- Overcomplicating logic inside a single method instead of refactoring properly.
- Forgetting that `*args` receives a **tuple**, not individual values.

### Best Practices

- Use default arguments for methods where some parameters are optional.
- Use `*args` and `**kwargs` when the number of inputs is genuinely variable.
- Don't jam too many behaviours into one method — if the logic branches too much, consider separate methods.

### Interview Questions

1. Does Python support method overloading? How is it typically achieved?
2. What is the difference between `*args` and default arguments?
3. How would you write a method that can accept either one or two arguments?

### Exercises

1. Write a `Greeting` class with a `say_hello()` method that prints "Hello!" if no name is given, "Hello, [name]!" if a name is given, and "Hello, [name]! You are [age] years old." if both name and age are given.
2. Write a `Stats` class with a `calculate()` method that accepts any number of numbers and returns their average.

---

## 6. Operator Overloading

### What Is It?

**Operator Overloading** lets you define what standard Python operators (`+`, `-`, `*`, `==`, `len()`, `str()`, etc.) do when used on objects of your custom class.

By default, Python doesn't know how to add two `Student` objects together. But with operator overloading, you can define exactly what `student1 + student2` means.

### Why Does It Exist?

It makes custom objects behave naturally and intuitively. Instead of writing `student1.combine(student2)`, you can write `student1 + student2` if that makes logical sense in your domain.

### Real-World Analogy

A **mixing board** in a music studio. When a sound engineer "adds" two audio tracks, they get a combined track. The "+" concept is being applied to audio tracks, not numbers. Operator overloading is how you teach Python what "adding" means for *your* objects.

### Magic Methods (Dunder Methods)

These are special methods with **double underscores** on both sides: `__add__`, `__str__`, etc. They're called "dunder" (short for double underscore) methods or "magic methods."

Python calls them automatically when you use operators.

| Operator / Function | Dunder Method |
|---|---|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `==` | `__eq__` |
| `<` | `__lt__` |
| `str(obj)` or `print(obj)` | `__str__` |
| `len(obj)` | `__len__` |
| `repr(obj)` | `__repr__` |

### Example 1: `__str__` — Custom String Representation

Without `__str__`, printing an object shows something like `<__main__.Student object at 0x...>`. With it, you control what displays.

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student({self.name}, Grade: {self.grade})"

s = Student("Ngozi", 85)
print(s)        # Student(Ngozi, Grade: 85)
print(str(s))   # Student(Ngozi, Grade: 85)
```

**Step-by-step explanation:**
- Without `__str__`, `print(s)` would show memory address garbage.
- With `__str__`, Python calls it automatically whenever `str()` or `print()` is used on the object.
- Always define `__str__` for any class you create — it makes debugging much easier.

### Example 2: `__add__` — Combining Objects

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2   # Python calls v1.__add__(v2)

print(v3)  # Vector(4, 6)
```

**Step-by-step explanation:**
- `v1 + v2` triggers `v1.__add__(v2)`.
- Inside `__add__`, `self` is `v1` and `other` is `v2`.
- A new `Vector` is returned with the summed `x` and `y` values.
- The result is a brand new object — `v1` and `v2` are unchanged.

### Example 3: `__len__` — Custom Length

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' with {len(self)} songs"

playlist = Playlist("Afrobeats Mix")
playlist.add_song("Essence")
playlist.add_song("Peru")
playlist.add_song("Sungba")

print(len(playlist))  # 3
print(playlist)       # Playlist 'Afrobeats Mix' with 3 songs
```

**Step-by-step explanation:**
- `len(playlist)` triggers `playlist.__len__()`.
- We return the length of the internal `songs` list.
- Inside `__str__`, we call `len(self)` to reuse our own `__len__` method.

### Example 4: `__eq__` — Custom Equality Check

```python
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def __eq__(self, other):
        return self.isbn == other.isbn   # two books are equal if same ISBN

    def __str__(self):
        return f"Book('{self.title}', ISBN: {self.isbn})"

book1 = Book("Clean Code", "978-0132350884")
book2 = Book("Clean Code", "978-0132350884")  # same ISBN
book3 = Book("The Pragmatic Programmer", "978-0135957059")

print(book1 == book2)   # True  (same ISBN)
print(book1 == book3)   # False (different ISBN)
```

**Step-by-step explanation:**
- By default, `==` checks if two variables point to the **same object in memory**.
- `__eq__` lets you redefine equality based on meaningful attributes.
- Here, two different `Book` objects with the same ISBN are considered equal — which makes logical sense.

### Common Mistakes Students Make

- Forgetting to return a new object from `__add__` (and returning `None` instead).
- Confusing `__str__` (human-readable) with `__repr__` (developer/debug representation).
- Modifying `self` inside `__add__` — the original object should stay unchanged.

### Best Practices

- Always define `__str__` for any class.
- Make `__add__` and similar methods return a **new object** of the same type.
- Only overload operators when it makes **intuitive sense** for your domain.
- If you define `__eq__`, consider also defining `__hash__` (or setting `__hash__ = None` if the object is mutable).

### Interview Questions

1. What are dunder/magic methods? Give three examples.
2. What is the difference between `__str__` and `__repr__`?
3. What happens if you define `__add__` but not `__radd__`? (Research this.)
4. Why is it important that `__add__` returns a new object?

### Exercises

1. Create a `ShoppingCart` class. Implement `__len__` to return the number of items, `__str__` to show a summary, and `__add__` to combine two carts into one.
2. Create a `Temperature` class that stores a value in Celsius. Implement `__add__`, `__sub__`, `__eq__`, and `__str__`. Make `Temperature(30) + Temperature(5)` return `Temperature(35)`.

---

## 7. Static Methods

### What Is It?

A **static method** is a method that belongs to the class but **doesn't have access to the instance (`self`) or the class (`cls`)**. It's essentially a regular function that lives inside a class for organisational purposes.

### Why Does It Exist?

Sometimes a method is logically related to a class, but doesn't need to access any instance data or class data. Putting it inside the class keeps the code organised without forcing it to receive `self` or `cls`.

### Real-World Analogy

A **calculator app** on your phone. The calculator doesn't need to know anything about you (your name, your account) — it just performs calculations. It's related to the app but doesn't depend on any specific "instance" of you. Static methods are like that calculator: utility functions with no state.

### Syntax

Use the `@staticmethod` decorator:

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```

### Example 1: A Utility Method

```python
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

# Call on the class — no instance needed
print(TemperatureConverter.celsius_to_fahrenheit(100))  # 212.0
print(TemperatureConverter.fahrenheit_to_celsius(32))   # 0.0

# Can also call on an instance (but there's usually no reason to)
converter = TemperatureConverter()
print(converter.celsius_to_fahrenheit(37))  # 98.6
```

**Step-by-step explanation:**
- No `self` or `cls` parameter in the method signature.
- You can call it on the class directly: `TemperatureConverter.celsius_to_fahrenheit(100)`.
- It doesn't rely on any object state — it's a pure utility function.

### Example 2: A Validation Utility

```python
class User:
    def __init__(self, username, email):
        if not User.is_valid_email(email):
            raise ValueError("Invalid email address")
        self.username = username
        self.email = email

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    def __str__(self):
        return f"User({self.username}, {self.email})"

# Using the validator before creating an object
print(User.is_valid_email("user@example.com"))  # True
print(User.is_valid_email("notanemail"))         # False

u = User("victor", "victor@example.com")
print(u)  # User(victor, victor@example.com)
```

**Step-by-step explanation:**
- `is_valid_email` is a standalone utility — it doesn't need `self` or any instance data.
- It's called inside `__init__` to validate before storing the email.
- It's also callable from outside the class as `User.is_valid_email(...)`.

### Common Mistakes Students Make

- Adding `self` to a static method when it isn't needed (it just becomes a regular method).
- Using a static method when you actually need to access `self` — in that case, use a regular instance method.
- Confusing `@staticmethod` with `@classmethod` (see the next section).

### Best Practices

- Use static methods for utility/helper functions logically related to the class.
- If the method needs the class itself, use `@classmethod` instead.
- If the method needs instance data, use a regular method.

### Interview Questions

1. What is a static method? How is it different from a regular instance method?
2. Can a static method access `self` or `cls`?
3. When would you use a static method instead of just a module-level function?

### Exercises

1. Create a `StringUtils` class with static methods: `is_palindrome(s)`, `word_count(s)`, and `reverse(s)`.
2. Add a static method `validate_age(age)` to a `Person` class that returns `True` if the age is between 0 and 150.

---

## 8. Class Methods

### What Is It?

A **class method** is a method that receives the **class itself** as its first argument (named `cls` by convention) instead of an instance. It can access and modify **class-level data** — attributes shared across all instances.

### Why Does It Exist?

Sometimes you need a method that works at the class level, not the instance level. The most common use case is creating **alternative constructors** — different ways to create an object.

### Real-World Analogy

A **bakery** keeps track of how many loaves have been baked in total (class-level data). Individual loaves have their own properties (weight, flavour — instance data). The total count belongs to the bakery as a whole, not to any one loaf. A class method updates and reads that shared count.

### Syntax

Use the `@classmethod` decorator. The first parameter is always `cls`:

```python
class MyClass:
    @classmethod
    def my_class_method(cls):
        print(cls)
```

### Example 1: Tracking a Shared Counter

```python
class Employee:
    employee_count = 0   # class attribute — shared by all instances

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def get_count(cls):
        return cls.employee_count

    def __str__(self):
        return f"Employee({self.name})"

e1 = Employee("Amaka")
e2 = Employee("Tunde")
e3 = Employee("Sola")

print(Employee.get_count())  # 3
```

**Step-by-step explanation:**
- `employee_count` is a class attribute — it lives on the class, not on any instance.
- Every time `__init__` runs, it increments the count.
- `get_count()` is a class method — it uses `cls.employee_count` to access the shared data.
- You call it on the class: `Employee.get_count()`.

### Example 2: Alternative Constructors (The Most Important Use Case)

This is where class methods really shine. Suppose you want to create a `Date` object, but sometimes the input is a string like `"2024-07-15"` rather than three separate numbers.

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)   # calls Date(year, month, day)

    @classmethod
    def today(cls):
        import datetime
        today = datetime.date.today()
        return cls(today.year, today.month, today.day)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

# Standard creation
d1 = Date(2024, 7, 15)
print(d1)  # 2024-07-15

# From a string — alternative constructor
d2 = Date.from_string("2024-12-25")
print(d2)  # 2024-12-25

# Today's date
d3 = Date.today()
print(d3)
```

**Step-by-step explanation:**
- `from_string` is a class method that parses a string and returns a new `Date` object.
- `cls(year, month, day)` calls the regular `__init__` — it's like writing `Date(year, month, day)`.
- Using `cls` instead of the class name directly makes it work correctly with subclasses too.
- This pattern (alternative constructors via class methods) is used extensively in Python's standard library.

### Comparing the Three Method Types

```python
class Demo:
    class_var = "I belong to the class"

    def instance_method(self):
        print(f"Access instance: {self}")
        print(f"Access class: {self.__class__}")

    @classmethod
    def class_method(cls):
        print(f"Access class: {cls}")
        print(f"Class var: {cls.class_var}")

    @staticmethod
    def static_method():
        print("No access to self or cls")

d = Demo()
d.instance_method()   # has access to self and class
Demo.class_method()   # has access to class only
Demo.static_method()  # has access to neither
```

| | Instance Method | Class Method | Static Method |
|---|---|---|---|
| First param | `self` (instance) | `cls` (class) | nothing |
| Access instance data? | ✅ Yes | ❌ No | ❌ No |
| Access class data? | ✅ Yes | ✅ Yes | ❌ No |
| Called on instance? | ✅ | ✅ | ✅ |
| Called on class? | ❌ | ✅ | ✅ |

### Common Mistakes Students Make

- Naming the first parameter `self` instead of `cls` in a class method (it works, but it's confusing).
- Using `@classmethod` when `@staticmethod` would be more appropriate (the method doesn't need `cls`).
- Calling `ClassName(...)` directly inside a class method instead of `cls(...)` — this breaks subclass compatibility.

### Best Practices

- Always use `cls` as the first parameter name in class methods.
- Use class methods when you need alternative constructors or need to read/modify class attributes.
- Use `cls(...)` instead of `ClassName(...)` inside class methods.

### Interview Questions

1. What is a class method? How is it different from a static method?
2. What is an alternative constructor pattern? Show an example.
3. Why is it better to use `cls(...)` instead of `ClassName(...)` inside a class method?

### Exercises

1. Create a `Circle` class. Add a class method `from_diameter(cls, diameter)` that creates a `Circle` from a diameter value (radius = diameter / 2).
2. Create a `Person` class with a class attribute `species = "Human"`. Add a class method `get_species()` that returns it, and a class method `change_species(cls, new_species)` that updates it.

---

## 9. Abstraction

### What Is It?

**Abstraction** means hiding complex internal details and showing only what is necessary. An **abstract class** is a class that defines *what* methods must exist, without providing the *how*. It's a blueprint that cannot be used directly — subclasses must fill in the details.

An **abstract method** is a method declared in the abstract class with no implementation. Every subclass is *required* to provide its own implementation.

### Why Does It Exist?

Abstraction enforces a **contract**. If you're designing a system where multiple classes (e.g., `PDFReport`, `ExcelReport`, `HTMLReport`) must all have a `generate()` method, abstract classes guarantee they all provide it. If a subclass forgets, Python raises an error immediately.

It also separates *interface* (what it does) from *implementation* (how it does it).

### Real-World Analogy

A **job description** is an abstraction. It says: "This role must: write code, attend standups, review PRs." It doesn't say *how* the person will write code — that's up to the individual hired. Abstract classes are job descriptions for code.

### Python's `abc` Module

Python provides the `abc` (Abstract Base Classes) module for this:

```python
from abc import ABC, abstractmethod
```

- `ABC` — inherit from this to make your class abstract.
- `@abstractmethod` — use this decorator to mark a method as abstract (must be overridden).

### Syntax

```python
from abc import ABC, abstractmethod

class AbstractAnimal(ABC):

    @abstractmethod
    def speak(self):
        pass   # no implementation here

    @abstractmethod
    def move(self):
        pass
```

### Example 1: Enforcing a Contract

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"I am a shape with area {self.area():.2f} and perimeter {self.perimeter():.2f}")

# Can we create a Shape directly?
# s = Shape()  # TypeError: Can't instantiate abstract class Shape!
```

**Step-by-step explanation:**
- `Shape` inherits from `ABC`, making it abstract.
- `area()` and `perimeter()` are marked `@abstractmethod`.
- You **cannot** create a `Shape` object directly.
- Any class that inherits from `Shape` **must** define `area()` and `perimeter()`.
- `describe()` is a regular method — it's provided by the abstract class and subclasses inherit it.

### Example 2: Concrete Subclasses Fulfilling the Contract

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [Rectangle(4, 6), Circle(5), Triangle(3, 4, 5)]

for shape in shapes:
    shape.describe()
```

**Output:**
```
Area: 24.00, Perimeter: 20.00
Area: 78.54, Perimeter: 31.42
Area: 6.00, Perimeter: 12.00
```

**Step-by-step explanation:**
- `Rectangle`, `Circle`, and `Triangle` each provide their own `area()` and `perimeter()`.
- They inherit `describe()` from `Shape` — no need to redefine it.
- The loop demonstrates polymorphism — the same `describe()` call works on all three types.

### Example 3: What Happens If You Forget to Implement an Abstract Method

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Fish(Animal):
    pass   # forgot to implement speak()

d = Dog()
print(d.speak())   # Works fine: Woof!

f = Fish()         # TypeError: Can't instantiate abstract class Fish
                   # with abstract method speak
```

**Step-by-step explanation:**
- `Dog` properly implements `speak()` — works.
- `Fish` doesn't implement `speak()` — Python catches this immediately when you try to create a `Fish` object.
- This is the power of abstraction: errors are caught early, not buried in runtime surprises.

### Example 4: Abstract Class in a Real-World System

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def charge(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

    def process_payment(self, amount):
        self.connect()
        self.charge(amount)
        print(f"Payment of ₦{amount:,.2f} processed.")


class PaystackProcessor(PaymentProcessor):
    def connect(self):
        print("Connecting to Paystack API...")

    def charge(self, amount):
        print(f"Charging ₦{amount:,.2f} via Paystack...")

    def refund(self, amount):
        print(f"Refunding ₦{amount:,.2f} via Paystack...")


class FlutterwaveProcessor(PaymentProcessor):
    def connect(self):
        print("Connecting to Flutterwave API...")

    def charge(self, amount):
        print(f"Charging ₦{amount:,.2f} via Flutterwave...")

    def refund(self, amount):
        print(f"Refunding ₦{amount:,.2f} via Flutterwave...")


# The calling code doesn't need to know which processor is used
def run_checkout(processor: PaymentProcessor, amount: float):
    processor.process_payment(amount)

run_checkout(PaystackProcessor(), 5000)
print()
run_checkout(FlutterwaveProcessor(), 12000)
```

**Output:**
```
Connecting to Paystack API...
Charging ₦5,000.00 via Paystack...
Payment of ₦5,000.00 processed.

Connecting to Flutterwave API...
Charging ₦12,000.00 via Flutterwave...
Payment of ₦12,000.00 processed.
```

**Step-by-step explanation:**
- `PaymentProcessor` is the abstract contract. It says: all payment processors must have `connect`, `charge`, and `refund`.
- `process_payment` is a concrete template method — it defines the overall flow and relies on the abstract methods.
- `PaystackProcessor` and `FlutterwaveProcessor` are concrete implementations.
- `run_checkout()` works with any `PaymentProcessor` — you can swap out the payment provider without changing the calling code. This is the power of abstraction.

### Abstraction vs Encapsulation (Quick Distinction)

These two are often confused:

| | Abstraction | Encapsulation |
|---|---|---|
| **What it is** | Hiding *complexity* (the how) | Hiding *data* (the what) |
| **Goal** | Show only what's necessary | Protect internal state |
| **How achieved** | Abstract classes, interfaces | Private attributes, getters/setters |
| **Example** | You press "Start" without knowing the engine | `self.__balance` can't be accessed directly |

### Common Mistakes Students Make

- Trying to instantiate an abstract class directly.
- Subclassing an abstract class but forgetting to implement one of the abstract methods.
- Putting business logic in abstract methods (they should be empty or raise `NotImplementedError`).
- Confusing abstraction with encapsulation.

### Best Practices

- Use abstract classes when you want to **enforce a contract** across multiple subclasses.
- Provide non-abstract (concrete) methods in abstract classes when the logic is shared across all subclasses.
- Name abstract classes clearly — many teams prefix them with `Abstract` or `Base` (e.g., `BaseProcessor`).
- Always import from `abc`: `from abc import ABC, abstractmethod`.

### Interview Questions

1. What is an abstract class? Can you instantiate it directly?
2. What is the difference between an abstract method and a regular method?
3. What does the `abc` module provide in Python?
4. What is the difference between abstraction and encapsulation?
5. Why would you use an abstract base class instead of just a regular base class?

### Exercises

1. Create an abstract class `DatabaseConnector` with abstract methods: `connect()`, `execute(query)`, and `disconnect()`. Implement two concrete classes: `MySQLConnector` and `PostgreSQLConnector`.
2. Create an abstract class `Notification` with an abstract method `send(message)`. Implement `EmailNotification`, `SMSNotification`, and `SlackNotification`. Write a function `broadcast(notification, message)` that works for all three.

---

## Putting It All Together

Here's how all nine concepts connect:

```
Multiple Inheritance → MRO (solves the conflicts multiple inheritance creates)
     ↓
Method Overriding → Polymorphism (overriding is HOW; polymorphism is the RESULT)
     ↓
Method Overloading → flexibility within a single class
     ↓
Operator Overloading → makes custom objects feel like built-in types
     ↓
Static Methods → class-level utilities with no state
Class Methods → class-level operations + alternative constructors
     ↓
Abstraction → enforces that subclasses implement the right methods
             (uses everything above: inheritance, overriding, polymorphism)
```

### Final Capstone Exercise

Build a mini **Library Management System** using all the concepts:

1. Create an **abstract class** `LibraryItem` with abstract methods `checkout()`, `return_item()`, and `get_info()`.
2. Create `Book` and `AudioBook` that inherit from `LibraryItem` — implement all abstract methods.
3. Use **operator overloading** (`__str__`, `__eq__`) on `Book` and `AudioBook`.
4. Use **class methods** to track how many items are in the library.
5. Use **static methods** to validate item IDs.
6. Demonstrate **polymorphism** by writing a function `display_all(items)` that works on a mixed list of `Book` and `AudioBook` objects.

---

## Quick Reference Card

| Concept | Keyword/Decorator | Key Point |
|---|---|---|
| Multiple Inheritance | `class Child(A, B)` | Inherit from multiple parents |
| MRO | `.mro()`, `super()` | Python's lookup order; use `super()` always |
| Method Overriding | Same method name in child | Child's version replaces parent's |
| Polymorphism | Same method name, different classes | One interface, many behaviours |
| Method Overloading | `*args`, default params | Python's way of handling variable inputs |
| Operator Overloading | `__add__`, `__str__`, etc. | Dunder methods for operators |
| Static Methods | `@staticmethod` | No `self` or `cls`; pure utility |
| Class Methods | `@classmethod` | Receives `cls`; good for alt constructors |
| Abstraction | `ABC`, `@abstractmethod` | Enforce contract; can't instantiate directly |

---

*Notes prepared for Python OOP — Intermediate Level*
*Author: Eneji Victor*
