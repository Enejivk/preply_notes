# Introduction to JavaScript

## What is JavaScript?

JavaScript is a programming language that makes web pages interactive and dynamic. Before JavaScript existed, websites were mostly static — you could read content on them, but they could not respond to what you did. JavaScript changed all of that.

Today, JavaScript is one of the three core technologies of the web, working alongside HTML and CSS. Here is a simple way to think about the three of them:

- **HTML** is the structure — it defines what is on the page (headings, paragraphs, buttons, images).
- **CSS** is the style — it controls how things look (colors, fonts, spacing, layout).
- **JavaScript** is the behavior — it controls what happens when a user does something (clicks a button, submits a form, scrolls the page).

JavaScript was originally created in 1995 by Brendan Eich and took only 10 days to build. It was designed to run inside web browsers, and for many years that was its only home. Today, JavaScript also runs on servers (thanks to a platform called Node.js), in mobile apps, and even in hardware devices. But we will start where it all began — the browser.

---

## How JavaScript Runs in the Browser

When you open a web page, your browser does several things behind the scenes. It downloads the HTML file, reads it top to bottom, builds the page structure, applies the styles, and then executes any JavaScript it finds.

Every modern browser — Chrome, Firefox, Edge, Safari — comes with a built-in **JavaScript engine**. Chrome uses an engine called **V8**. Firefox uses one called **SpiderMonkey**. These engines are responsible for reading your JavaScript code and executing it.

JavaScript is an **interpreted language**, which means the browser reads and runs it line by line, in real time. You do not need to compile it before running it — you write the code, load the page, and it runs immediately. This makes JavaScript very quick to test and experiment with, which is great for learning.

Here is what happens when the browser encounters JavaScript:

1. The browser reads the HTML file from top to bottom.
2. When it finds a `<script>` tag, it pauses reading the HTML.
3. It downloads and executes the JavaScript code.
4. Once done, it continues reading the rest of the HTML.

This is why the placement of your `<script>` tag matters — something we will talk about shortly.

---

## Linking JavaScript to HTML

Just like you link a CSS file to your HTML, you need to connect your JavaScript file to your HTML page. There are a few ways to do this.

### Method 1 — Inline JavaScript (not recommended for large projects)

You can write JavaScript directly inside your HTML file using the `<script>` tag:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello, World!</h1>

    <script>
      alert("Welcome to my page!");
    </script>
  </body>
</html>
```

This works perfectly fine, but mixing JavaScript and HTML in the same file becomes messy as your code grows.

### Method 2 — External JavaScript File (recommended)

The better approach is to write your JavaScript in a separate `.js` file and link it to your HTML:

**index.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Page</title>
  </head>
  <body>
    <h1>Hello, World!</h1>

    <script src="script.js"></script>
  </body>
</html>
```

**script.js**
```javascript
alert("Welcome to my page!");
```

Notice the `<script>` tag is placed just before the closing `</body>` tag. This is intentional. If you put it in the `<head>`, the JavaScript might try to interact with HTML elements that have not loaded yet. Placing it at the bottom ensures the entire page is loaded before your script runs.

Alternatively, you can place the script in the `<head>` and use the `defer` attribute, which tells the browser to wait until the page is fully loaded before executing the script:

```html
<head>
  <script src="script.js" defer></script>
</head>
```

Both approaches are valid. Many modern developers prefer the `defer` approach because it keeps all linked resources in the `<head>` for organization.

---

## The Console — Your Most Important Tool

The browser console is where JavaScript communicates with you as a developer. It is not visible to regular users of your website — it is a tool designed specifically for developers to inspect, debug, and test code.

### Opening the Console

You can open the browser console in a few ways:

- Press **F12** on Windows/Linux, or **Cmd + Option + I** on Mac
- Right-click anywhere on a web page and select **Inspect**, then click the **Console** tab
- In Chrome: go to the three-dot menu → More tools → Developer Tools → Console

### Using `console.log()`

The most common thing you will do in the console is print values using `console.log()`. Think of it as JavaScript's way of talking back to you.

```javascript
console.log("Hello, class!");
console.log(42);
console.log(10 + 5);
```

**Output in console:**
```
Hello, class!
42
15
```

You can pass multiple values at once:

```javascript
let name = "Ada";
let age = 20;
console.log("Name:", name, "| Age:", age);
```

**Output:**
```
Name: Ada | Age: 20
```

### Other Useful Console Methods

| Method | What It Does |
|---|---|
| `console.log()` | Prints a regular message |
| `console.warn()` | Prints a warning (shown in yellow) |
| `console.error()` | Prints an error message (shown in red) |
| `console.table()` | Displays data in a neat table format |
| `console.clear()` | Clears all previous output from the console |

**Example:**

```javascript
console.log("This is a normal message");
console.warn("Careful — this might cause a problem");
console.error("Something went wrong!");
```

### Basic Debugging with the Console

Debugging is the process of finding and fixing errors in your code. When something is not working the way you expect, `console.log()` is your first weapon. Place it at different points in your code to see what values your variables hold at any given moment.

```javascript
let price = 100;
let discount = 20;
let finalPrice = price - discount;

console.log("Price:", price);
console.log("Discount:", discount);
console.log("Final Price:", finalPrice);
```

This kind of step-by-step logging helps you trace where your logic is going wrong.

You will also encounter **errors** in the console. Do not panic when you see them — read them carefully. The console tells you what went wrong and on which line of your file. For example:

```
Uncaught ReferenceError: myVariable is not defined
    at script.js:5
```

This tells you that on line 5 of `script.js`, you tried to use a variable that does not exist. Learning to read error messages is one of the most important skills you will develop as a programmer.

---

## A Complete Working Example

Here is a simple example that brings everything together:

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>JavaScript Demo</title>
    <script src="script.js" defer></script>
  </head>
  <body>
    <h1>Open the console to see the magic!</h1>
  </body>
</html>
```

**script.js**
```javascript
console.log("JavaScript is now linked and running!");
console.log("The page has fully loaded.");
console.warn("This is just a warning — everything is fine.");
```

Open this in your browser, press F12, and you will see all three messages appear in the console.

---

## Key Takeaways

- JavaScript is the programming language that adds interactivity and behavior to web pages.
- Browsers run JavaScript using built-in engines — you do not need to install anything extra.
- Always link your JavaScript using an external `.js` file for clean, organized code.
- Place your `<script>` tag before `</body>`, or use the `defer` attribute in `<head>`.
- The browser console is your debugging workspace — use `console.log()` constantly while learning.
- Error messages in the console are helpful, not scary — read them and trace the issue.

---

## Coding Tasks

Work through these tasks on your own. Each one is designed to reinforce what you have learned in this note. Do not rush — take your time to understand what each line of code is doing and why.

---

**Task 1**
Create an HTML file called `index.html` and a JavaScript file called `script.js`. Link the two files together correctly. In your `script.js`, write a `console.log()` that prints your full name. Open the file in your browser and confirm the output appears in the console.

---

**Task 2**
In your `script.js`, use `console.log()` to print the result of the following calculations without storing them in variables first:
- 250 plus 175
- 1000 minus 437
- 18 multiplied by 6
- 144 divided by 12

---

**Task 3**
Write a script that prints five different messages to the console — one using `console.log()`, one using `console.warn()`, one using `console.error()`, and two using `console.log()` with multiple values separated by commas. Open the browser and observe how each type of message looks different.

---

**Task 4**
Intentionally break your script by referencing a variable that does not exist, like this:

```javascript
console.log(studentName);
```

Open the console and read the error message carefully. Write a comment in your code (using `//`) that explains in your own words what the error message is telling you.

---

**Task 5**
Create a new HTML file. In the `<head>` section, link your JavaScript file using the `defer` attribute. Then remove `defer` and move the `<script>` tag to just before the closing `</body>` tag. Both should work. Write a comment in your code explaining the difference between these two approaches.

---

**Task 6**
Write a script that uses `console.log()` to print a simple "story" — at least five sentences — about your favourite hobby or interest. Each sentence should be on a separate `console.log()` line.

---

**Task 7**
Use `console.table()` to display the following information as a table in the console:

| Name | Age | Course |
|---|---|---|
| Chidi | 21 | Computer Science |
| Ngozi | 20 | Information Technology |
| Emeka | 22 | Software Engineering |

Research how `console.table()` works with arrays of objects and implement it.

---

**Task 8**
Write a script that performs the following steps in order, using a `console.log()` after each step so you can trace the flow:
1. Print "Starting calculation..."
2. Add 500 and 300 and print the result
3. Multiply that result by 2 and print the new result
4. Subtract 150 from the latest result and print the final answer
5. Print "Calculation complete."

---

**Task 9**
You have been given this broken HTML file. Find and fix **all three errors** in it:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Broken Page</title>
  </head>
  <body>
    <h1>Hello!</h1>
  <script src="main.js">
</html>
```

List the three errors in comments inside your corrected file.

---

**Task 10**
Create a script that simulates a simple "system check." Print the following to the console in this order:
- A log message: "System check started."
- A warning message: "Memory usage is at 80%."
- A log message: "Network connection: OK."
- An error message: "Disk space critically low — 95% full."
- A log message: "System check complete."

---

**Task 11**
Write a JavaScript file where you use `console.log()` to print the phrase `"JavaScript is fun!"` exactly **ten times** — but you are only allowed to write the `console.log()` statement **once** in your code. Think carefully about how to do this.

---

**Task 12**
Open any website of your choice in your browser. Open the console and type the following directly into the console (not in a file):

```javascript
document.title = "I changed this!";
```

Observe what happens to the browser tab title. Then type:

```javascript
console.log(document.title);
```

Write a short comment in a `.js` file explaining what `document.title` is and what happened when you changed it.

---

**Task 13**
Create two separate HTML pages — `page1.html` and `page2.html`. Both should link to the **same** `script.js` file. In `script.js`, print a message that includes the phrase: `"This script is shared between pages."` Open both pages and confirm the same script runs on both.

---

**Task 14**
Modify your `script.js` so that when it runs, it prints the current date and time to the console using:

```javascript
console.log(new Date());
```

Reload the page several times and observe the output. Write a comment explaining what `new Date()` appears to do based on what you observe.

---

**Task 15**
Write a script that has a deliberate logic error — something that runs without throwing an error but gives a wrong result. For example, if you want to calculate a 10% discount on 500 but accidentally calculate the wrong thing. Use `console.log()` to trace through the values step by step and catch where the wrong result is produced. Fix it and print the correct answer.

---

**Task 16**
Use `console.log()` to print a simple multiplication table for the number **7** — from 7 × 1 all the way to 7 × 10. Each line should read like: `"7 x 1 = 7"`, `"7 x 2 = 14"`, and so on. Do not hardcode the answers — calculate them using the `*` operator.

---

**Task 17**
Create an HTML page with a button element:

```html
<button id="myBtn">Click Me</button>
```

Link a script that uses `console.log()` to print `"Button was clicked!"` every time the button is clicked. You will need to look up how to use `document.getElementById()` and `.addEventListener()` to accomplish this — this is intentionally a research task.

---

**Task 18**
Write a script that prints the following pattern to the console using only `console.log()`:

```
*
**
***
****
*****
```

You may not hardcode each line as a string. Instead, build each line programmatically.

---

**Task 19**
Create a JavaScript file that does the following:
1. Prints `"Hello"` to the console.
2. Then prints an intentional error: call a function that does not exist, like `greetUser()`.
3. Notice that after the error, any `console.log()` statements that come after it do **not** run.

Explain this behavior in a comment — what does this tell you about how JavaScript handles runtime errors?

---

**Task 20**
Write a script that uses `console.log()` to display a simple ASCII-art drawing of any object or animal of your choice — at least 5 lines tall. Be creative. Each row of the drawing should be its own `console.log()` statement.