# BeautifulSoup4 — Complete Beginner Notes
> Based on the official documentation: Beautiful Soup 4.14.3 | https://www.crummy.com/software/BeautifulSoup/bs4/doc/

---

## Table of Contents
1. [What is BeautifulSoup?](#1-what-is-beautifulsoup)
2. [Installation](#2-installation)
3. [Parsers](#3-parsers)
4. [Making the Soup (Parsing a Document)](#4-making-the-soup)
5. [The Four Kinds of Objects](#5-the-four-kinds-of-objects)
6. [Navigating the Tree](#6-navigating-the-tree)
7. [Searching the Tree](#7-searching-the-tree)
8. [CSS Selectors](#8-css-selectors)
9. [Modifying the Tree](#9-modifying-the-tree)
10. [Extracting Data (Common Patterns)](#10-extracting-data-common-patterns)
11. [Output](#11-output)
12. [Common Gotchas](#12-common-gotchas)
13. [Quick Reference Cheat Sheet](#13-quick-reference-cheat-sheet)

---

## 1. What is BeautifulSoup?

BeautifulSoup is a Python library for **pulling data out of HTML and XML files**. It turns a raw HTML string (or file) into a Python object you can navigate and search — like a tree of elements. It's the go-to tool for web scraping.

**What it does NOT do:**
- It does not fetch web pages. You need `requests` or `httpx` for that.
- It is not a browser. JavaScript-rendered content is invisible to it.

**Typical workflow:**
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")
# Now extract whatever you need from soup
```

---

## 2. Installation

```bash
pip install beautifulsoup4
```

> ⚠️ The package name on PyPI is `beautifulsoup4`, NOT `BeautifulSoup`. If you accidentally install `BeautifulSoup`, that's the old, unsupported version 3. Delete it and install `beautifulsoup4`.

**Verify it works:**
```python
from bs4 import BeautifulSoup
print("Installed!")
```

---

## 3. Parsers

BeautifulSoup doesn't parse HTML itself — it delegates to a **parser**. You must tell it which one to use. You always pass the parser as the **second argument** to `BeautifulSoup()`.

| Parser | How to use | Install | When to use |
|--------|-----------|---------|-------------|
| `html.parser` | `"html.parser"` | Built-in (no install needed) | Good default for beginners |
| `lxml` | `"lxml"` | `pip install lxml` | Fastest option |
| `html5lib` | `"html5lib"` | `pip install html5lib` | Most lenient; parses like a browser |
| `lxml-xml` | `"lxml-xml"` or `"xml"` | `pip install lxml` | Only option for XML files |

**For beginners:** just use `"html.parser"` — it's built in and works fine. If speed matters later, switch to `"lxml"`.

```python
# Good default
soup = BeautifulSoup(html_string, "html.parser")

# Faster, needs: pip install lxml
soup = BeautifulSoup(html_string, "lxml")
```

> ⚠️ Always specify a parser explicitly. If you don't, BeautifulSoup will pick one for you and print a warning — and different machines may pick different parsers, giving you different results.

---

## 4. Making the Soup

"Making the soup" means parsing your HTML/XML into a BeautifulSoup object.

**From a string:**
```python
from bs4 import BeautifulSoup

html = "<html><body><p>Hello world</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
```

**From a file:**
```python
with open("page.html") as f:
    soup = BeautifulSoup(f, "html.parser")
```

**From a URL (using requests):**
```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, "html.parser")
```

BeautifulSoup automatically:
- Converts the document to Unicode
- Converts HTML entities (e.g. `&amp;` → `&`)
- Fixes some malformed/broken HTML

---

## 5. The Four Kinds of Objects

BeautifulSoup turns your HTML into a tree of Python objects. You'll only deal with **4 types**:

### 5.1 `Tag`
Corresponds to an HTML tag like `<p>`, `<a>`, `<div>`, etc.

```python
soup = BeautifulSoup('<b class="boldest">Hello</b>', "html.parser")
tag = soup.b
print(type(tag))   # <class 'bs4.element.Tag'>
print(tag.name)    # 'b'
```

**Accessing attributes** — treat the tag like a dictionary:
```python
tag = BeautifulSoup('<a href="https://google.com" id="link1">Go</a>', "html.parser").a

tag["href"]        # 'https://google.com'
tag["id"]          # 'link1'
tag.attrs          # {'href': 'https://google.com', 'id': 'link1'}
tag.get("href")    # 'https://google.com' (safe — returns None if missing)
tag.get("missing") # None
```

**Modifying attributes:**
```python
tag["id"] = "new-id"    # change
del tag["id"]           # delete
tag["new-attr"] = "val" # add
```

**Multi-valued attributes (like `class`):**
The `class` attribute can hold multiple CSS classes, so BS4 returns it as a **list**:
```python
soup = BeautifulSoup('<p class="title bold">Hi</p>', "html.parser")
soup.p["class"]  # ['title', 'bold']  ← a list, not a string!
```

---

### 5.2 `NavigableString`
The **text content** inside a tag. It's like a Python string but also knows its position in the tree.

```python
soup = BeautifulSoup('<b>Hello</b>', "html.parser")
tag = soup.b
print(tag.string)        # 'Hello'
print(type(tag.string))  # <class 'bs4.element.NavigableString'>

# Convert to a plain Python string:
plain = str(tag.string)  # 'Hello'
```

You can't edit a NavigableString in place, but you can replace it:
```python
tag.string.replace_with("Goodbye")
print(tag)  # <b>Goodbye</b>
```

---

### 5.3 `BeautifulSoup` object
The object that represents the **entire parsed document**. It behaves like a Tag in most ways, but its `.name` is `"[document]"` and it has no attributes.

```python
print(soup.name)    # '[document]'
print(soup.parent)  # None
```

---

### 5.4 `Comment`
An HTML comment (`<!-- like this -->`). It's a special type of NavigableString.

```python
markup = "<b><!-- This is a comment --></b>"
soup = BeautifulSoup(markup, "html.parser")
comment = soup.b.string
print(type(comment))  # <class 'bs4.element.Comment'>
print(comment)        # 'This is a comment'
```

---

## 6. Navigating the Tree

Once you have a soup object, you can move around the document tree in multiple ways.

### 6.1 Navigating by Tag Name (dot notation)

Just type `soup.tagname` to grab the **first** matching tag:

```python
soup.head    # <head>...</head>
soup.title   # <title>The Dormouse's story</title>
soup.p       # first <p> tag only
soup.a       # first <a> tag only
soup.body.b  # first <b> inside <body>
```

---

### 6.2 Going Down (into children)

**`.contents`** — returns a tag's direct children as a **list**:
```python
head_tag = soup.head
head_tag.contents  # [<title>The Dormouse's story</title>]

# Access by index:
head_tag.contents[0]  # <title>The Dormouse's story</title>
```

**`.children`** — like `.contents` but returns a **generator** (better for looping):
```python
for child in soup.body.children:
    print(child)
```

**`.descendants`** — iterates over **all** nested children, recursively (not just direct children):
```python
for child in soup.head.descendants:
    print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story
```

**`.string`** — the text content, but only works if a tag has exactly **one** child string:
```python
soup.title.string   # "The Dormouse's story"
soup.html.string    # None  ← has multiple children, so None
```

**`.strings`** — generator of all strings inside a tag (including nested ones):
```python
for s in soup.strings:
    print(repr(s))
```

**`.stripped_strings`** — same as `.strings` but strips whitespace and ignores blank strings:
```python
for s in soup.stripped_strings:
    print(repr(s))
```

---

### 6.3 Going Up (to parents)

**`.parent`** — the tag that directly contains this element:
```python
soup.title.parent        # <head>...</head>
soup.title.string.parent # <title>...</title>
soup.html.parent         # <BeautifulSoup object>  (the soup itself)
```

**`.parents`** — iterate up through all ancestors:
```python
for parent in soup.a.parents:
    print(parent.name)
# p → body → html → [document]
```

---

### 6.4 Going Sideways (siblings)

Tags at the same level of nesting are called **siblings**.

**`.next_sibling` / `.previous_sibling`** — the element immediately before/after:
```python
# Given: <b>text1</b><c>text2</c>
soup.b.next_sibling     # <c>text2</c>
soup.c.previous_sibling # <b>text1</b>
```

> ⚠️ **Gotcha:** In real documents, siblings often include whitespace text nodes (newlines, spaces). Don't be surprised if `.next_sibling` returns `'\n'` instead of the next tag.

**`.next_siblings` / `.previous_siblings`** — iterate through all siblings:
```python
for sibling in soup.a.next_siblings:
    print(repr(sibling))
```

---

### 6.5 Going Back and Forth (document order)

**`.next_element` / `.previous_element`** — what comes immediately after/before in the order the parser saw things (different from siblings):
```python
last_a = soup.find("a", id="link3")
last_a.next_element       # 'Tillie'  (the text inside the tag)
last_a.next_sibling       # '; and they lived...'  (after the tag)
```

**`.next_elements` / `.previous_elements`** — iterate in document order:
```python
for element in last_a.next_elements:
    print(repr(element))
```

---

## 7. Searching the Tree

This is the most important section. The two main methods are `find()` and `find_all()`.

### 7.1 `find_all()`

Returns a **list** of all matching tags.

```python
soup.find_all("a")         # all <a> tags
soup.find_all(["a", "b"]) # all <a> and <b> tags
```

**Signature:**
```python
find_all(name, attrs, recursive, string, limit, **kwargs)
```

---

### 7.2 `find()`

Returns the **first** match only (or `None` if nothing found):
```python
soup.find("p")
soup.find(id="link1")
```

`find(x)` is basically `find_all(x, limit=1)[0]` — but safer, since it returns `None` instead of raising an error.

---

### 7.3 Filters — What You Can Pass In

Both `find()` and `find_all()` accept these filter types:

**A string (tag name):**
```python
soup.find_all("b")  # all <b> tags
```

**A list of strings:**
```python
soup.find_all(["a", "p"])  # all <a> and <p> tags
```

**`True` (matches everything):**
```python
soup.find_all(True)  # every single tag in the document
```

**A regular expression:**
```python
import re
soup.find_all(re.compile("^b"))  # tags whose name starts with "b": <b>, <body>
soup.find_all(re.compile("t"))   # tags containing "t": <title>, <html>, etc.
```

**A function (custom filter):**
```python
def has_class_but_no_id(tag):
    return tag.has_attr("class") and not tag.has_attr("id")

soup.find_all(has_class_but_no_id)
```

---

### 7.4 Filtering by Attributes (keyword arguments)

Pass attributes as keyword arguments. Use `class_` (with underscore) for CSS class since `class` is a Python reserved word.

```python
soup.find_all("a", class_="sister")     # <a> tags with class "sister"
soup.find_all(id="link2")               # any tag with id="link2"
soup.find_all("p", id="myid")           # <p> with that id
soup.find_all(href="http://example.com/elsie")  # match exact href
soup.find_all(href=re.compile("elsie")) # href matching a regex
soup.find_all(attrs={"data-foo": "bar"}) # use attrs dict for non-standard attributes
```

**Finding by CSS class (important):**
```python
# Any of these work to find <p class="title">:
soup.find_all("p", class_="title")
soup.find_all("p", "title")     # shorthand: second positional arg = class
```

If a tag has multiple classes, searching for one is enough:
```python
# <p class="body strikeout">
soup.find_all("p", class_="strikeout")  # still finds it
```

---

### 7.5 Filtering by String Content

Use the `string` argument to find tags by their text content:

```python
soup.find_all(string="Elsie")           # exact match
soup.find_all(string=re.compile("Dormouse"))  # regex match
soup.find_all("a", string="Elsie")      # <a> tag containing exactly "Elsie"
```

---

### 7.6 The `limit` Argument

Stop after finding N results:
```python
soup.find_all("a", limit=2)  # first 2 <a> tags only
```

---

### 7.7 The `recursive` Argument

By default, `find_all()` searches all descendants. Set `recursive=False` to search only direct children:

```python
soup.html.find_all("title")                  # finds it (recursive)
soup.html.find_all("title", recursive=False) # doesn't find it (not a direct child)
```

---

### 7.8 Other Search Methods

| Method | What it does |
|--------|-------------|
| `find_all()` | Returns list of all matches |
| `find()` | Returns first match (or None) |
| `find_parents()` | Search up through ancestors |
| `find_parent()` | First matching ancestor |
| `find_next_siblings()` | All matching next siblings |
| `find_next_sibling()` | First matching next sibling |
| `find_previous_siblings()` | All matching previous siblings |
| `find_previous_sibling()` | First matching previous sibling |
| `find_all_next()` | All matching elements after this one |
| `find_next()` | First matching element after this one |
| `find_all_previous()` | All matching elements before this one |
| `find_previous()` | First matching element before this one |

```python
# Find all <a> tags that come after the first <b> tag:
first_b = soup.find("b")
first_b.find_all_next("a")

# Find the first <p> that is a parent of this link:
soup.a.find_parent("p")
```

---

## 8. CSS Selectors

BeautifulSoup supports CSS selectors via `.select()` and `.select_one()`. Under the hood, this uses the **SoupSieve** library (bundled with BS4).

```python
# select() → returns a list
soup.select("p")               # all <p> tags
soup.select("p.title")         # <p> with class "title"
soup.select("p > b")           # <b> that is a direct child of <p>
soup.select("a[href]")         # <a> tags that have an href attribute
soup.select("a[href='http://example.com/elsie']")  # exact attribute match
soup.select("#link1")          # tag with id="link1"
soup.select(".sister")         # tags with class="sister"
soup.select("p .sister")       # .sister elements inside a <p>

# select_one() → returns the first match (or None)
soup.select_one("p.title")
```

**When to use CSS selectors vs find_all():**
- CSS selectors are great if you already know CSS and the selector is straightforward.
- `find_all()` is more Pythonic and handles complex filters (functions, regex) more easily.
- Both are fine — pick whichever you're comfortable with.

---

## 9. Modifying the Tree

BS4 lets you change the document — add, remove, replace, or move elements.

### 9.1 Changing Tag Name and Attributes

```python
tag = soup.b
tag.name = "blockquote"         # rename the tag
tag["class"] = "new-class"      # add/change attribute
tag["id"] = "my-id"
del tag["class"]                # remove attribute
```

### 9.2 Changing String Content

```python
tag.string = "New text"                    # replace the string
tag.string.replace_with("Replaced text")   # also replaces string content
```

### 9.3 `append()` and `insert()`

```python
soup.a.append(" (extra text)")    # add to end of tag's contents
new_tag = soup.new_tag("a", href="https://example.com")
new_tag.string = "Click here"
soup.p.append(new_tag)            # add new tag to end of <p>

soup.p.insert(1, new_tag)         # insert at position 1
soup.p.insert_before(new_tag)     # insert before this tag in the tree
soup.p.insert_after(new_tag)      # insert after this tag
```

### 9.4 `clear()`, `decompose()`, `extract()`

```python
tag.clear()      # removes all of a tag's children (tag stays)
tag.decompose()  # removes tag from tree AND destroys it entirely
tag.extract()    # removes tag from tree and RETURNS it (you can reuse it)
```

### 9.5 `replace_with()`

```python
tag.replace_with(new_tag)       # replace tag with another
tag.string.replace_with("New")  # replace string content
```

### 9.6 `wrap()` and `unwrap()`

```python
# wrap: put a tag inside a new tag
soup.p.string.wrap(soup.new_tag("b"))
# result: <p><b>original text</b></p>

# unwrap: remove a tag but keep its contents
soup.a.unwrap()  # removes <a> tags but keeps the text inside
```

### 9.7 Creating New Tags and Strings

```python
new_tag = soup.new_tag("a", href="https://example.com")
new_tag.string = "Link text"

from bs4 import NavigableString
new_string = NavigableString("Some text")
soup.p.append(new_string)
```

---

## 10. Extracting Data (Common Patterns)

### Get all links on a page
```python
for a in soup.find_all("a"):
    print(a.get("href"))
    print(a.string)
```

### Get all text from a page
```python
print(soup.get_text())

# With separator and stripped whitespace:
print(soup.get_text(separator="\n", strip=True))
```

### Get all images
```python
for img in soup.find_all("img"):
    print(img.get("src"))
    print(img.get("alt"))
```

### Scrape a table
```python
table = soup.find("table")
rows = table.find_all("tr")

for row in rows:
    cells = row.find_all(["td", "th"])
    data = [cell.get_text(strip=True) for cell in cells]
    print(data)
```

### Scrape specific text with a class
```python
price = soup.find("span", class_="price").get_text(strip=True)
title = soup.find("h1", class_="product-title").string
```

### Check if an attribute exists
```python
if tag.has_attr("class"):
    print(tag["class"])
```

### Safely get text (handles None)
```python
element = soup.find("p", class_="price")
text = element.get_text(strip=True) if element else "Not found"
```

---

## 11. Output

### Pretty-print the HTML
```python
print(soup.prettify())
# Nicely indented HTML
```

### Get the raw HTML string of an element
```python
str(soup.p)       # '<p class="title"><b>The Dormouse's story</b></p>'
str(soup.p.b)     # '<b>The Dormouse's story</b>'
```

### Get just the text (no tags)
```python
soup.get_text()                        # all text, concatenated
soup.get_text(separator=" ")           # joined with a space
soup.get_text(separator="\n", strip=True)  # stripped and newline-separated

tag.string      # text if tag has one child string, else None
tag.get_text()  # text always, even if nested
```

---

## 12. Common Gotchas

**1. `soup.a` only gives you the first `<a>`**
Use `soup.find_all("a")` to get all of them.

**2. `class` attribute returns a list**
`soup.p["class"]` gives `['title']` not `'title'`. Use `soup.p["class"][0]` to get the string.

**3. `.next_sibling` may be whitespace**
Real HTML has newlines between tags. `soup.p.next_sibling` might be `'\n'`, not a tag. Skip whitespace-only strings when looping.

**4. `.string` is `None` for tags with multiple children**
Use `.get_text()` instead — it always returns a string.

**5. Always specify your parser**
Don't call `BeautifulSoup(html)` without a parser argument. Always include `"html.parser"` (or `"lxml"` etc.).

**6. `class_` not `class`**
In Python, `class` is a reserved keyword. BS4 uses `class_` in keyword arguments:
```python
soup.find_all("p", class_="title")  # ✅ correct
soup.find_all("p", class="title")   # ❌ SyntaxError
```

**7. Don't modify `.contents` directly**
If you want to add/remove children, use the proper methods (`append()`, `extract()`, etc.) instead of editing the list.

**8. `find()` returns `None` if not found**
Always check before accessing attributes:
```python
result = soup.find("div", id="missing")
if result:
    print(result.string)
```

---

## 13. Quick Reference Cheat Sheet

### Setup
```python
pip install beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_string, "html.parser")
```

### Navigate
```python
soup.title              # first <title> tag
soup.title.name         # 'title'
soup.title.string       # text content
soup.title.parent       # parent tag
soup.p["class"]         # attribute value (returns list for class!)
soup.p.get("class")     # safe attribute access

# Down
tag.contents            # list of direct children
tag.children            # generator of direct children
tag.descendants         # generator of ALL nested children
tag.string              # text if single child, else None
tag.strings             # all descendant strings
tag.stripped_strings    # all descendant strings, whitespace removed

# Up
tag.parent
tag.parents             # all ancestors

# Sideways
tag.next_sibling
tag.previous_sibling
tag.next_siblings
tag.previous_siblings
```

### Search
```python
soup.find("a")                         # first <a>
soup.find("a", id="link1")             # first <a> with id
soup.find_all("a")                     # all <a> tags
soup.find_all("a", class_="sister")    # by class
soup.find_all("a", limit=2)            # max 2 results
soup.find_all(string="Elsie")          # by text content
soup.find_all(re.compile("^b"))        # by regex on tag name
soup.select("p.title")                 # CSS selector (returns list)
soup.select_one("p.title")             # CSS selector (first match)
```

### Extract
```python
tag.get_text()                  # all text, no tags
tag.get_text(strip=True)        # stripped
tag.get("href")                 # safe attribute get
tag.has_attr("class")           # check if attr exists
str(tag)                        # render to HTML string
```

### Modify
```python
tag.name = "div"                  # rename
tag["id"] = "new"                 # set attribute
del tag["id"]                     # delete attribute
tag.string = "New text"           # replace text
tag.append(new_tag)               # add child at end
tag.insert(0, new_tag)            # add child at position
tag.extract()                     # remove + return
tag.decompose()                   # remove + destroy
tag.replace_with(other)           # swap
soup.new_tag("a", href="...")     # create new tag
soup.prettify()                   # pretty-print output
```

---

*Official docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/*
*Current version: 4.14.3*