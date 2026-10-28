# NumPy Teaching Notes (for Eneji)

Read this before class. It follows the slide order. Every code sample has its expected output so you can check yourself. Run everything once in a notebook first.

**Setup:** `pip install numpy`, then `import numpy as np` (the `np` alias is universal).

---

## 1. Getting Started

### What NumPy is
NumPy gives Python one main object, the **ndarray**: a grid of items that all share one data type, stored in one continuous block of memory. That is the whole secret of its speed. A Python list stores pointers to separate objects scattered in memory. An array stores the raw numbers side by side, and the maths loops run in compiled C instead of Python.

### List vs array
```python
nums = [1, 2, 3]
print(nums * 2)            # [1, 2, 3, 1, 2, 3]  <- repeats the list!
print(np.array(nums) * 2)  # [2 4 6]             <- maths on each item
```
**Teaching point:** `*` on a list repeats it; `*` on an array multiplies. Students are often surprised, so use it as your hook.

**Timing demo (optional, impressive):**
```python
import time
big = list(range(5_000_000)); arr = np.arange(5_000_000)
t=time.time(); [x*2 for x in big]; print(time.time()-t)   # roughly 0.2-0.5 s
t=time.time(); arr*2;             print(time.time()-t)   # roughly 0.01 s
```
Your exact times will differ. Arrays are usually 10-100x faster.

---

## 2. Array Basics

### Creating from data
```python
b = np.array([[1, 2, 3], [4, 5, 6]])
```
- 1D = a row of numbers, 2D = a table, 3D = a stack of tables.
- All rows must be the same length, otherwise you get an error or an object array.
- **Upcasting:** `np.array([1, 2.5])` gives `[1. 2.5]`. Mixing numbers and strings turns everything into strings.

### Attributes
| Attribute | Meaning | For `b` above |
|---|---|---|
| `shape` | size per dimension | `(2, 3)` |
| `ndim` | number of dimensions | `2` |
| `size` | total items | `6` |
| `dtype` | item type | `int64` |

Note: `shape` is a **tuple**; a 1D array of 3 items has shape `(3,)` with the trailing comma. On Windows the default int may be `int32`.

### dtypes
Common ones: `int32`, `int64`, `float32`, `float64`, `bool`. Why care? Memory: a float32 array uses half the space of float64. Precision: float32 keeps about 7 digits, float64 about 15.
```python
y = np.array([1.9, 2.7])
print(y.astype(int))   # [1 2]  truncates, does not round
```
`astype` always returns a **new** array.

---

## 3. Creating Arrays

| Function | Example | Result |
|---|---|---|
| `zeros` | `np.zeros((2,3))` | 2x3 of 0.0 |
| `ones` | `np.ones(3)` | `[1. 1. 1.]` |
| `full` | `np.full((2,2), 7)` | 2x2 of 7 |
| `arange` | `np.arange(0,10,2)` | `[0 2 4 6 8]` |
| `linspace` | `np.linspace(0,1,5)` | `[0. 0.25 0.5 0.75 1.]` |
| `eye` | `np.eye(3)` | identity matrix |

**arange vs linspace:** `arange(start, stop, step)` excludes stop and you choose the step. `linspace(start, stop, count)` **includes** stop and you choose how many points. With float steps, `linspace` is safer because `arange` can be off by one item from rounding.

### Random numbers
Use the modern generator API (the old `np.random.seed` still works but is considered legacy):
```python
rng = np.random.default_rng(42)
rng.integers(1, 7, size=5)   # five dice rolls (high end excluded)
rng.random(3)                # floats in [0, 1)
rng.normal(0, 1, 3)          # mean 0, std 1
rng.choice([10, 20, 30])     # random pick
```
Same seed means the same numbers every run. That matters for marking and for reproducible examples. Printed values can differ across NumPy versions, so tell students to compare logic, not digits.

---

## 4. Indexing and Slicing

### Basics
```python
a = np.array([10, 20, 30, 40, 50])
a[1]      # 20
a[-1]     # 50
a[1:4]    # [20 30 40]   stop is excluded
a[::2]    # [10 30 50]
```
### 2D
```python
m = np.array([[1,2,3],[4,5,6]])
m[1, 2]    # 6      (row 1, col 2)
m[:, 1]    # [2 5]  whole column 1
m[0, :]    # [1 2 3] whole row 0
```
NumPy uses `m[row, col]`, not `m[row][col]` (the second works but is slower and clumsier).

### Boolean masks
```python
a = np.array([5, 12, 8, 20, 3])
a > 7                    # [False  True  True  True False]
a[a > 7]                 # [12  8 20]
a[(a > 7) & (a < 15)]    # [12  8]
```
**Common mistake:** `a > 7 and a < 15` raises *"truth value of an array is ambiguous"*. Use `&`, `|`, `~` and wrap each condition in brackets, because `&` binds tighter than `>`.

### Fancy indexing
`a[[0, 3]]` gives `[5 20]`. Unlike slices, fancy indexing and masks return **copies**.

---

## 5. Shape Manipulation

```python
a = np.arange(6)         # [0 1 2 3 4 5]
m = a.reshape(2, 3)      # [[0 1 2],[3 4 5]]
a.reshape(3, -1).shape   # (3, 2)   -1 = infer
m.T.shape                # (3, 2)
m.flatten()              # [0 1 2 3 4 5]  (copy)
m.ravel()                # same values, usually a view
```
Rule: the new shape must hold the same number of items. `a.reshape(4, 2)` fails because 8 is not 6.

### Joining and splitting
```python
a = np.array([1, 2]); b = np.array([3, 4])
np.concatenate([a, b])   # [1 2 3 4]
np.vstack([a, b])        # [[1 2],[3 4]]
np.hstack([a, b])        # [1 2 3 4]
np.split(np.arange(6), 3)  # [array([0,1]), array([2,3]), array([4,5])]
```

---

## 6. Operations

### Vectorisation and ufuncs
Operators work item by item: `a + b`, `a * b`, `a ** 2`. **Universal functions** (ufuncs) such as `np.sqrt`, `np.exp`, `np.log`, `np.sin`, `np.abs` also apply to every item.

Important: `a * b` is element-wise. It is **not** matrix multiplication (use `@`).

### Broadcasting
Broadcasting lets arrays of different shapes work together.

**The rule:** line up the shapes from the **right**. Each pair of sizes must be equal, or one of them must be 1 (or missing).

| Shapes | Result |
|---|---|
| `(2,3)` + `(3,)` | works, gives `(2,3)` |
| `(2,3)` + `(2,1)` | works, gives `(2,3)` |
| `(2,3)` + `(2,)` | **error**, 3 vs 2 |

```python
m = np.array([[1,2,3],[4,5,6]])
m + np.array([100,200,300])   # [[101 202 303],[104 205 306]]
```
Fix for the error case: `m + np.array([10, 20])[:, None]` turns shape `(2,)` into `(2,1)` and adds 10 to row 0, 20 to row 1.

---

## 7. Statistics and the axis argument

Main functions: `sum`, `mean`, `median`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, `cumsum`.

```python
m = np.array([[1,2,3],[4,5,6]])
m.sum()          # 21
m.sum(axis=0)    # [5 7 9]   collapse the rows -> one value per column
m.sum(axis=1)    # [ 6 15]   collapse the columns -> one value per row
m.mean()         # 3.5
m.argmax()       # 5  (index in the flattened array)
```
**Memory trick:** the axis you name is the axis that **disappears**. For shape `(4,5)`, `axis=0` gives shape `(5,)` and `axis=1` gives `(4,)`.

`np.std` uses the population formula by default (`ddof=0`). Pass `ddof=1` for the sample standard deviation.

---

## 8. Linear Algebra

```python
A = np.array([[1,2],[3,4]]); B = np.array([[0,1],[1,0]])
A @ B                    # [[2 1],[4 3]]
np.linalg.det(A)         # about -2.0 (tiny float error is normal)
np.linalg.inv(A)         # [[-2.   1. ],[ 1.5 -0.5]]
np.linalg.solve(A, [5, 6])   # [-4.   4.5]
```
- `@` needs matching inner sizes: `(m,n) @ (n,p)` gives `(m,p)`.
- Prefer `solve(A, b)` over `inv(A) @ b`: it is faster and more accurate.
- A singular matrix (det = 0) has no inverse and raises `LinAlgError`.

---

## 9. Useful Tools

```python
a = np.array([3, 1, 2, 3, 1])
np.sort(a)                          # [1 1 2 3 3]
np.argsort(a)                       # [1 4 2 0 3]
np.unique(a, return_counts=True)    # (array([1,2,3]), array([2,1,2]))
np.where(a > 1, "big", "small")     # ['big' 'small' 'big' 'big' 'small']
np.isin(a, [1, 2])                  # [False True True False True]
```
`np.where(cond)` with only the condition returns the **indices** where it is True.

### Missing values (NaN)
```python
a = np.array([1.0, np.nan, 3.0])
a.sum()           # nan
np.nansum(a)      # 4.0
np.nanmean(a)     # 2.0
a[~np.isnan(a)]   # [1. 3.]
```
`np.nan == np.nan` is **False**, so always use `np.isnan`. NaN only exists in float arrays; integer arrays cannot hold it.

---

## 10. Memory and Files

### Views vs copies
Slices share memory with the original:
```python
a = np.array([1,2,3,4]); s = a[:2]; s[0] = 99
print(a)    # [99  2  3  4]
```
Use `.copy()` when you need independence. Check with `np.shares_memory(a, s)`.

### Saving
```python
np.save("data.npy", a);       b = np.load("data.npy")
np.savetxt("data.csv", m, delimiter=",", fmt="%d")
m2 = np.loadtxt("data.csv", delimiter=",")
```
`.npy` keeps dtype and shape exactly. CSV is human readable but everything comes back as float unless you set `dtype`. For files with headers or messy data, move to Pandas.

---

## 11. Mini project: Student scores

```python
s = np.array([[60,70,80],[40,45,50],[90,85,95]])
avg = s.mean(axis=1)             # [70. 45. 90.]
test_avg = s.mean(axis=0)        # [63.33 66.67 75.  ]
avg >= 50                        # [ True False  True]
np.minimum(s + 5, 100)           # curved marks, capped at 100
s.argmax(axis=0)                 # [2 2 2]  top student per test
```
Have students predict each output before you run it.

---

## Common mistakes to watch for
1. Using `and`/`or` instead of `&`/`|` on arrays.
2. Forgetting a slice is a view, then wondering why the original changed.
3. Mixing up `axis=0` and `axis=1`.
4. Expecting `*` to do matrix multiplication.
5. Using `==` to test for NaN.
6. Assuming `astype(int)` rounds.
7. Reshaping to an incompatible size.

## Suggested pacing (about 90 minutes)
| Block | Slides | Minutes |
|---|---|---|
| Intro, basics, dtypes | 1-5 | 15 |
| Creation, random | 6-7 | 10 |
| Indexing, masks | 8-9 | 15 |
| Reshape, join | 10-11 | 10 |
| Maths, broadcasting | 12-13 | 15 |
| axis, linear algebra | 14-15 | 10 |
| where/NaN, views, project | 16-19 | 15 |
