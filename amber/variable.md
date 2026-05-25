# Variables and Data Types in JavaScript

## What is a Variable?

A variable is a named container that holds a value. Think of it like a labelled box — you give the box a name, and you put something inside it. Later, whenever you need that thing, you just refer to the box by its name.

In programming, variables allow you to store data so you can use it, change it, and refer to it throughout your code without having to repeat the same value over and over again.

For example, instead of writing `"Chidi"` everywhere you need a student's name, you store it once in a variable called `studentName` and use that variable everywhere else. If the name ever needs to change, you only update it in one place.

---

## Declaring Variables — `var`, `let`, and `const`

JavaScript gives you three keywords for declaring variables: `var`, `let`, and `const`. They all create variables, but they behave differently, and knowing when to use each one is important.

### `var` — The Old Way

`var` was the original way to declare variables in JavaScript, used before 2015. It still works, but it has some quirky behaviors that can cause bugs, especially in larger programs. Modern JavaScript rarely uses `var` anymore, but you will see it in older code and tutorials, so you need to understand it.

```javascript
var schoolName = "Tech Academy";
console.log(schoolName); // Tech Academy

var schoolName = "Code Institute"; // You can re-declare var without any error
console.log(schoolName); // Code Institute
```

One major issue with `var` is that it can be **re-declared** (defined again with `var` in the same scope) without throwing any error. This can silently overwrite values and lead to confusing bugs.

### `let` — The Modern Standard

`let` was introduced in ES6 (2015) and is the standard choice for declaring variables whose values will change over time. Unlike `var`, `let` cannot be re-declared in the same scope.

```javascript
let studentAge = 20;
console.log(studentAge); // 20

studentAge = 21; // Reassigning is fine
console.log(studentAge); // 21

let studentAge = 22; // ERROR — you cannot re-declare with let
```

Use `let` when you know the value of a variable is going to change at some point — for example, a score in a game, a counter, or a user's input that gets updated.

### `const` — For Values That Do Not Change

`const` is also from ES6. It is used when the value should **never be reassigned** after it is first set. If you try to reassign a `const` variable, JavaScript will throw an error.

```javascript
const PI = 3.14159;
console.log(PI); // 3.14159

PI = 3.14; // ERROR — cannot reassign a const variable
```

`const` does not mean the value is permanently frozen in every situation — objects and arrays declared with `const` can still have their contents modified. But the variable itself cannot be pointed to a different value. We will explore this more when we get to objects and arrays.

### Choosing Between `var`, `let`, and `const`

Here is a simple rule to follow as a beginner:

- **Default to `const`** — use it whenever you know the value will not change.
- **Use `let`** — when you know the value will need to change later.
- **Avoid `var`** — unless you are reading or maintaining older code.

| Keyword | Can be re-declared? | Can be reassigned? | When to use |
|---|---|---|---|
| `var` | Yes | Yes | Older code only |
| `let` | No | Yes | Values that will change |
| `const` | No | No | Values that will stay the same |

---

## Naming Rules for Variables

Naming your variables properly is not just about following rules — it is about writing code that other people (and your future self) can actually read and understand. Here are the rules JavaScript enforces, followed by conventions that experienced developers follow.

### Rules You Must Follow (JavaScript enforces these)

1. **Variable names can only contain letters, digits, underscores `_`, and dollar signs `$`.**

   ```javascript
   let firstName = "Ada";     // valid
   let _score = 100;          // valid
   let $price = 500;          // valid
   let first-name = "Ada";    // INVALID — hyphens are not allowed
   let first name = "Ada";    // INVALID — spaces are not allowed
   ```

2. **Variable names cannot start with a digit.**

   ```javascript
   let score1 = 50;   // valid
   let 1score = 50;   // INVALID — cannot start with a number
   ```

3. **Variable names are case-sensitive.** `score`, `Score`, and `SCORE` are three completely different variables.

   ```javascript
   let score = 50;
   let Score = 100;
   console.log(score); // 50
   console.log(Score); // 100
   ```

4. **You cannot use JavaScript reserved words as variable names.** Words like `let`, `const`, `function`, `return`, `if`, `else`, and `new` already mean something in JavaScript — you cannot use them as variable names.

   ```javascript
   let let = 5;       // INVALID
   let return = 10;   // INVALID
   ```

### Conventions You Should Follow (Best Practice)

5. **Use camelCase for variable names.** This is the universally accepted convention in JavaScript. Start with a lowercase letter and capitalize the first letter of every subsequent word.

   ```javascript
   let studentFirstName = "Emeka";
   let totalNumberOfStudents = 30;
   let isLoggedIn = true;
   ```

6. **Give your variables meaningful, descriptive names.** A variable name should tell you exactly what it holds.

   ```javascript
   // Bad naming
   let x = 25;
   let d = "2024-01-15";

   // Good naming
   let studentAge = 25;
   let enrollmentDate = "2024-01-15";
   ```

7. **Use `UPPER_SNAKE_CASE` for constants that represent fixed values across your whole program**, like configuration values or mathematical constants.

   ```javascript
   const MAX_STUDENTS_PER_CLASS = 40;
   const TAX_RATE = 0.075;
   ```

---

## Primitive Data Types

A **data type** tells JavaScript what kind of value a variable holds. JavaScript has several built-in data types, and the most fundamental ones are called **primitive data types**. There are five you need to know right now.

### 1. String

A string is a sequence of characters — text. Strings are always wrapped in quotation marks. You can use single quotes `'...'`, double quotes `"..."`, or backticks `` `...` `` (backtick strings are called template literals and have extra powers we will explore soon).

```javascript
let firstName = "Ngozi";
let greeting = 'Good morning, class!';
let sentence = `JavaScript is the language of the web.`;

console.log(firstName);  // Ngozi
console.log(greeting);   // Good morning, class!
```

You can join (concatenate) strings using the `+` operator:

```javascript
let firstName = "Ngozi";
let lastName = "Obi";
let fullName = firstName + " " + lastName;
console.log(fullName); // Ngozi Obi
```

Or using template literals, which is more readable:

```javascript
let fullName = `${firstName} ${lastName}`;
console.log(fullName); // Ngozi Obi
```

### 2. Number

Numbers in JavaScript cover both whole numbers (integers) and decimal numbers (floats). There is no separate "integer" and "float" type — they are all just `Number`.

```javascript
let age = 21;
let price = 4999.99;
let temperature = -5;
let percentage = 0.85;

console.log(age + 9);       // 30
console.log(price * 2);     // 9999.98
console.log(100 - age);     // 79
console.log(10 / 4);        // 2.5
console.log(10 % 3);        // 1 (remainder/modulus)
```

JavaScript also has two special number values worth knowing:

```javascript
console.log(10 / 0);   // Infinity
console.log("abc" * 2); // NaN (Not a Number — result of an invalid math operation)
```

`NaN` stands for "Not a Number" and appears when you attempt a mathematical operation that does not make sense.

### 3. Boolean

A boolean can hold only one of two values: `true` or `false`. Booleans are the backbone of logic in programming — they are used to make decisions, control what code runs, and represent the state of something.

```javascript
let isLoggedIn = true;
let hasPaid = false;
let isAdult = true;

console.log(isLoggedIn); // true
console.log(hasPaid);    // false
```

Booleans often come from comparisons:

```javascript
let age = 18;
console.log(age >= 18); // true
console.log(age > 25);  // false
console.log(age === 18); // true
```

### 4. Null

`null` is a special value that represents the **intentional absence of a value**. When you set a variable to `null`, you are deliberately saying: "this variable exists, but it currently has nothing in it."

```javascript
let selectedStudent = null; // No student has been selected yet
console.log(selectedStudent); // null
```

You would typically use `null` as a starting value when a variable will eventually hold something, but it does not have that thing yet.

### 5. Undefined

`undefined` means a variable has been declared but has **not been assigned any value**. JavaScript assigns `undefined` automatically when you create a variable without giving it a value.

```javascript
let score;
console.log(score); // undefined
```

It also appears when you try to access something that does not exist:

```javascript
let student = { name: "Ada" };
console.log(student.age); // undefined — the age property does not exist
```

### `null` vs `undefined` — What is the Difference?

This is a common source of confusion. Here is the clearest way to think about it:

- **`undefined`** — the variable exists but was never given a value. JavaScript set it to `undefined` automatically.
- **`null`** — the variable exists and a programmer deliberately set it to "nothing" on purpose.

```javascript
let a;              // undefined — no value assigned
let b = null;       // null — deliberately set to nothing

console.log(a);     // undefined
console.log(b);     // null
```

---

## Type Checking with `typeof`

As you work with variables, you will sometimes need to know what type of data a variable holds — especially when you are debugging or writing code that behaves differently based on what it receives. JavaScript provides the `typeof` operator for this.

```javascript
typeof value
```

It returns a **string** that tells you the type of the value.

```javascript
let name = "Chidi";
let age = 22;
let isActive = true;
let score;
let nothing = null;

console.log(typeof name);     // "string"
console.log(typeof age);      // "number"
console.log(typeof isActive); // "boolean"
console.log(typeof score);    // "undefined"
console.log(typeof nothing);  // "object" ← famous JavaScript quirk!
```

Wait — why does `typeof null` return `"object"`? This is a well-known bug in JavaScript that has existed since the language was first created in 1995. It was never fixed because fixing it would break millions of existing web pages that relied on that behavior. So `typeof null === "object"` is simply something every JavaScript developer learns to remember.

### Practical Use of `typeof`

```javascript
let userInput = "42";

console.log(typeof userInput); // "string"

// Convert it to a number
let converted = Number(userInput);
console.log(typeof converted); // "number"
console.log(converted + 8);   // 50
```

`typeof` is especially useful when you receive data from a user or an external source and you are not sure what type it is.

---

## A Full Working Example

Here is a script that ties everything together — variable declarations, naming, data types, and type checking:

```javascript
// Student profile
const studentId = "STU-2024-001";
let studentName = "Adaeze Nwosu";
let studentAge = 20;
let isEnrolled = true;
let assignmentScore = null; // Score not yet assigned
let graduationYear;         // Not set yet — will be undefined

// Print the profile
console.log("--- Student Profile ---");
console.log("ID:", studentId);
console.log("Name:", studentName);
console.log("Age:", studentAge);
console.log("Enrolled:", isEnrolled);
console.log("Assignment Score:", assignmentScore);
console.log("Graduation Year:", graduationYear);

// Type checking
console.log("\n--- Type Checks ---");
console.log(typeof studentId);       // string
console.log(typeof studentAge);      // number
console.log(typeof isEnrolled);      // boolean
console.log(typeof assignmentScore); // object (null quirk)
console.log(typeof graduationYear);  // undefined

// Update a value
studentAge = 21;
console.log("\nUpdated Age:", studentAge); // 21
```

---

## Key Takeaways

- Variables are named containers that store data values.
- Use `const` by default, `let` when the value will change, and avoid `var` in modern code.
- Variable names must follow JavaScript's naming rules and should be descriptive and written in camelCase.
- JavaScript has five core primitive data types: `string`, `number`, `boolean`, `null`, and `undefined`.
- Use `typeof` to check what type of data a variable holds.
- `null` is intentional emptiness; `undefined` is the absence of assignment.
- `typeof null` returns `"object"` — this is a known JavaScript quirk, not a mistake you made.

---

## Coding Tasks

These tasks are designed to make you apply everything from this note with your hands — not just read and forget. Work through each one carefully and use `console.log()` to verify every result.

---

**Task 1**
Declare five variables — one using `var`, two using `let`, and two using `const`. Assign each a different type of value (string, number, boolean, null, and undefined). Print all five to the console and also print the `typeof` each one.

---

**Task 2**
Create a "student profile" using appropriate variable declarations. Include: full name, age, course of study, student ID number, whether the student is currently active, and the student's GPA (set it to `null` to indicate it has not been calculated yet). Print a formatted summary to the console.

---

**Task 3**
Declare a variable using `let`, assign it a number, then reassign it to a string, then to a boolean. After each reassignment, use `console.log(typeof variableName)` to confirm the type has changed. Write a comment explaining what this tells you about JavaScript's type system.

---

**Task 4**
Try to reassign a variable declared with `const`. Observe the error message in the console. Then try to re-declare a variable declared with `let` using the same name. Observe that error too. Write comments in your code describing both error messages in your own words.

---

**Task 5**
Declare two variables: one called `userScore` set to `null`, and one called `userName` with no value assigned (leave it undefined). Print both to the console. Then use `typeof` on both and print those results too. In a comment, explain the difference between what you see.

---

**Task 6**
You have been given these variable names. For each one, write whether it is **valid** or **invalid** as a JavaScript variable name, and if invalid, explain why — then write a corrected version:

- `2ndPlace`
- `first_name`
- `let`
- `studentAge`
- `total price`
- `_count`
- `$revenue`
- `class`
- `myVariable123`
- `hello-world`

---

**Task 7**
Write a script that calculates and prints the following for a fictional shop:
- Product name (string)
- Product price (number)
- Quantity in stock (number)
- Total stock value (price × quantity, stored in a `let` variable)
- Whether the product is available (boolean — true if quantity > 0)
- Discount rate (number, e.g. 0.15 for 15%)
- Discounted price (price minus price × discount rate)

Print everything with clear labels using `console.log()`.

---

**Task 8**
JavaScript's `NaN` (Not a Number) is a special numeric value. Write a script that intentionally produces `NaN` in at least three different ways using arithmetic operations on non-numeric values. Print each result and use `console.log(typeof NaN)` to check its type — you may be surprised by the result.

---

**Task 9**
Write a script that converts data types using the built-in functions `Number()`, `String()`, and `Boolean()`. Show at least five conversions total — for example, converting the string `"50"` to a number, the number `0` to a boolean, and the boolean `true` to a string. Print the value and its type before and after each conversion.

---

**Task 10**
Create variables to represent a bank account:
- Account holder name
- Account number (use a `const`)
- Account balance
- Account type (e.g., "Savings")
- Whether the account is frozen (boolean)

Simulate two transactions by reassigning the balance:
1. Deposit 5000 (add to balance)
2. Withdraw 2000 (subtract from balance)

Print the balance after each transaction. Make sure the account number does not change.

---

**Task 11**
Write a script that demonstrates the difference between `==` (loose equality) and `===` (strict equality) by comparing the following pairs. Print the result of both comparisons for each pair and write a comment explaining why the results differ:

- `5` and `"5"`
- `0` and `false`
- `null` and `undefined`
- `""` and `false`

---

**Task 12**
Declare a variable without assigning a value. Then use an `if` statement to check if it is `undefined`, and if so, assign it the string `"Default Value"`. Print the variable before and after. This simulates a pattern you will use constantly in real JavaScript code.

---

**Task 13**
Write a script that builds a sentence using string concatenation with `+` and then rebuilds the **exact same sentence** using a template literal (backtick string). Print both results and confirm they are identical. Use at least three variables in the sentence.

---

**Task 14**
Create a constant called `TAX_RATE` set to `0.075` (7.5%). Then create variables for three different product prices. For each product, calculate the tax amount and the total price including tax. Print the results in a clear, readable format. Use `const` for values that do not change and `let` for values that do.

---

**Task 15**
Write a script that declares a variable, assigns it a string value, then uses `typeof` to confirm it is a string. Then overwrite it with a number and confirm with `typeof` again. Then overwrite it with `null` and run `typeof` one more time. In a comment, write your conclusion about how JavaScript handles types — what does this behavior tell you about how JavaScript is different from some other languages?

---

**Task 16**
A student scored marks in five subjects. Store each mark in a separate `let` variable. Then calculate:
- The total of all marks
- The average mark (total divided by 5)
- Whether the student passed (average must be 50 or above — store result as a boolean)

Print a full result summary to the console.

---

**Task 17**
Write a script that simulates a simple "login check." Create a `const` for the correct password. Create a `let` variable for the password the user entered (you can hardcode this for now). Use a boolean variable to store whether the entered password matches the correct one. Print the result.

---

**Task 18**
Experiment with JavaScript's `Infinity` value. Write a script that:
- Divides a positive number by zero and stores the result
- Divides a negative number by zero and stores the result
- Uses `typeof` on both results
- Adds a regular number to `Infinity` and prints the result
- Checks what `Infinity - Infinity` equals

Print all results with labels and write comments explaining what you observe.

---

**Task 19**
Build a "product listing" for an e-commerce site. Use appropriate variable types for:
- Product name (`const`)
- Product category (`const`)
- Original price (`const`)
- Current sale price (`let`)
- Percentage discount (calculate it from original and sale price)
- Number of items left in stock (`let`)
- Whether the product is on sale (boolean)
- Seller rating (`let`, set to `null` initially — "not yet rated")

Print all details to the console in a clean, readable format. Then simulate a sale ending by updating the sale price back to the original price and updating the boolean accordingly.

---

**Task 20**
Write a script that declares ten variables of mixed types — some strings, some numbers, some booleans, one null, one undefined. Then use a series of `console.log(typeof ...)` statements to print the type of each one. After observing the output, write a comment that lists at least two observations or surprises you noticed about how `typeof` works in JavaScript.