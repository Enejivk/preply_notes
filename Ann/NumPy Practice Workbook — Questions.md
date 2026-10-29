# NumPy Practice Workbook — Questions

Oct 29, 2026 · @Associate2TrioEdX

## How to use this workbook

Work through 15 topics in order; each question gives the task and the exact output you should get. Every expected output below was produced by running a real solution, so if yours differs, your code is the thing to check. Worked solutions with explanations are in the companion answers doc.

- **Setup:** start every session with `import numpy as np`. Questions using randomness say which seed to use.
- **Difficulty:** ★ warm-up · ★★ core skill · ★★★ challenge.
- **Rule of thumb:** no Python `for` loops unless a question allows one. The point is to think in whole arrays.
- **Printing:** outputs are shown as `print()` would show them (NumPy 2.x). Scalars may display as `np.int64(5)` in a notebook; `print` shows `5`.
- **Teaching tip:** before running anything, predict the shape of the result. Shape errors are the most common beginner mistake.

## Topic 1: Creating arrays

Every NumPy program starts by building arrays. These questions drill the main constructors and the small differences between them.

**Q1.1** ★ — Create a 1-D array of the integers 0 to 9 using `np.arange`. Print it.

Expected output:

```text
[0 1 2 3 4 5 6 7 8 9]
```

**Q1.2** ★ — Create 5 evenly spaced numbers from 0 to 1, **including** both ends. Print them.

Expected output:

```text
[0.   0.25 0.5  0.75 1.  ]
```

**Q1.3** ★ — Create a 3×4 array of zeros whose dtype is integer. Print the array, then print its dtype.

Expected output:

```text
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
int64
```

**Q1.4** ★ — Create a 3×3 identity matrix and a 2×3 array filled with the number 7. Print both.

Expected output:

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[[7 7 7]
 [7 7 7]]
```

**Q1.5** ★★ — Create the even numbers from 10 **down to** -10 inclusive, using one call to `np.arange`. Print the result.

Expected output:

```text
[ 10   8   6   4   2   0  -2  -4  -6  -8 -10]
```

**Q1.6** ★★ — Create the numbers 0, 0.25, 0.5, 0.75 two ways: once with `arange` and once with `linspace` (hint: `endpoint`). Print both.

Expected output:

```text
[0.   0.25 0.5  0.75]
[0.   0.25 0.5  0.75]
```

**Q1.7** ★★ — Create a 5×5 array that has 1s on the border and 0s inside. Do not type the values by hand. Print it.

Expected output:

```text
[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 0 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]
```

**Q1.8** ★★ — Given `lst = [[1, 2, 3], [4, 5, 6]]`, make it an array, then create an array of the **same shape** filled with ones but of float dtype. Print it.

```python
lst = [[1, 2, 3], [4, 5, 6]]
```

Expected output:

```text
[[1. 1. 1.]
 [1. 1. 1.]]
```

**Q1.9** ★★ — Build a 4×4 diagonal matrix with 1, 2, 3, 4 on the main diagonal, and a 4×4 matrix with 1s just **above** the main diagonal. Print both.

Expected output:

```text
[[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]
[[0 1 0 0]
 [0 0 1 0]
 [0 0 0 1]
 [0 0 0 0]]
```

**Q1.10** ★★ — Create a 3×4 array where the element at row `i`, column `j` equals `10*i + j`. Do it without loops (hint: `np.fromfunction` or `np.indices`).

Expected output:

```text
[[ 0  1  2  3]
 [10 11 12 13]
 [20 21 22 23]]
```

**Q1.11** ★★★ — Create an 8×8 checkerboard of 0s and 1s with a 0 in the top-left corner. No loops. Print it.

Expected output:

```text
[[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]]
```

**Q1.12** ★★★ — Create an empty-looking array with `np.empty((2, 2))`. Explain why you must **never** rely on its contents, then show a safe alternative that guarantees zeros. Print `np.zeros((2, 2))`.

Expected output:

```text
[[0. 0.]
 [0. 0.]]
```

## Topic 2: Attributes and data types

Knowing an array's shape and dtype explains most surprising results. These questions make you inspect both.

**Q2.1** ★ — For `a = np.arange(24).reshape(2, 3, 4)`, print `ndim`, `shape`, `size` and `dtype`, each on its own line.

```python
a = np.arange(24).reshape(2, 3, 4)
```

Expected output:

```text
3
(2, 3, 4)
24
int64
```

**Q2.2** ★★ — Create a float64 array and a float32 array, each holding 100 zeros. Print `itemsize` and `nbytes` for each (4 numbers in total).

Expected output:

```text
8 800
4 400
```

**Q2.3** ★ — Convert `np.array([1.7, -2.3, 3.9])` to integers with `astype`. Print the result. Is it rounding or truncating?

Expected output:

```text
[ 1 -2  3]
```

**Q2.4** ★★ — What dtype does `np.array([1, 2.5, '3'])` get? Print the array and its dtype.

Expected output:

```text
['1' '2.5' '3']
<U32
```

**Q2.5** ★★ — Create `np.array([250], dtype=np.uint8)` and add 10. Print the result and explain it.

Expected output:

```text
[4]
```

**Q2.6** ★ — Given `flags = np.array([True, False, True, True])`, print how many are True, and print the array converted to integers.

```python
flags = np.array([True, False, True, True])
```

Expected output:

```text
3
[1 0 1 1]
```

**Q2.7** ★★ — For `a = np.array([7, 8, 9])`, print `a / 2` with its dtype, then `a // 2` with its dtype.

```python
a = np.array([7, 8, 9])
```

Expected output:

```text
[3.5 4.  4.5] float64
[3 4 4] int64
```

**Q2.8** ★★★ — Print the minimum and maximum values an `int16` can hold, and the machine epsilon of `float32`.

Expected output:

```text
-32768 32767
1.1920929e-07
```

**Q2.9** ★★ — Create an array of the numbers 1 to 5 with dtype `float32` **at creation time**, then print its dtype. Then convert it to `int8` and print the new array.

Expected output:

```text
float32
[1 2 3 4 5]
```

## Topic 3: Indexing and slicing

Slicing is where most beginners stall. Every question here uses the same 5×5 array so you can check by eye.

Use this array for every question in this topic:

```python
a = np.arange(1, 26).reshape(5, 5)
```

**Q3.1** ★ — Print `a`. Then print the element in row 2, column 3 (zero-based).

Expected output:

```text
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
14
```

**Q3.2** ★ — Print the last row of `a`, then the last column.

Expected output:

```text
[21 22 23 24 25]
[ 5 10 15 20 25]
```

**Q3.3** ★ — Print the 2×2 block in the bottom-right corner.

Expected output:

```text
[[19 20]
 [24 25]]
```

**Q3.4** ★★ — Print every other row and every other column, starting from the first.

Expected output:

```text
[[ 1  3  5]
 [11 13 15]
 [21 23 25]]
```

**Q3.5** ★★ — Print `a` with its rows in reverse order. Then print `a` reversed on both axes.

Expected output:

```text
[[21 22 23 24 25]
 [16 17 18 19 20]
 [11 12 13 14 15]
 [ 6  7  8  9 10]
 [ 1  2  3  4  5]]
[[25 24 23 22 21]
 [20 19 18 17 16]
 [15 14 13 12 11]
 [10  9  8  7  6]
 [ 5  4  3  2  1]]
```

**Q3.6** ★★ — Print the middle 3×3 block (exclude the outer border).

Expected output:

```text
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]
```

**Q3.7** ★★ — Given `x = np.arange(10)`, use **one slice** to get `[7 5 3 1]`.

```python
x = np.arange(10)
```

Expected output:

```text
[7 5 3 1]
```

**Q3.8** ★★ — Given `b = np.arange(24).reshape(2, 3, 4)`, print `b[1, :, 2]`, then `b[:, 1, :]`, then `b[..., -1]`. Predict each shape first.

```python
b = np.arange(24).reshape(2, 3, 4)
```

Expected output:

```text
[14 18 22]
[[ 4  5  6  7]
 [16 17 18 19]]
[[ 3  7 11]
 [15 19 23]]
```

**Q3.9** ★★★ — Print the shapes of `a[1]`, `a[1:2]`, `a[:, 1]` and `a[:, [1]]`. Explain why they differ.

Expected output:

```text
(5,)
(1, 5)
(5,)
(5, 1)
```

**Q3.10** ★★ — Make a copy of `a` called `c`, set column 0 of `c` to 0 and row 0 of `c` to -1. Print `c`.

Expected output:

```text
[[-1 -1 -1 -1 -1]
 [ 0  7  8  9 10]
 [ 0 12 13 14 15]
 [ 0 17 18 19 20]
 [ 0 22 23 24 25]]
```

**Q3.11** ★★★ — Print the values on the main diagonal of `a`, then the values on the anti-diagonal (top-right to bottom-left). Hint: `np.diag` and `np.fliplr`.

Expected output:

```text
[ 1  7 13 19 25]
[ 5  9 13 17 21]
```

## Topic 4: Boolean masks and fancy indexing

Masks let you select by condition; fancy indexing lets you select by a list of positions. Both are central to data work.

Use this array for every question in this topic:

```python
data = np.array([12, -5, 7, 0, 23, -18, 4, 9, -1, 15])
```

**Q4.1** ★ — Print only the positive values in `data`.

Expected output:

```text
[12  7 23  4  9 15]
```

**Q4.2** ★★ — Count how many values lie between 0 and 10, inclusive.

Expected output:

```text
4
```

**Q4.3** ★★ — Make a copy of `data` where every negative value is replaced by 0. Print it.

Expected output:

```text
[12  0  7  0 23  0  4  9  0 15]
```

**Q4.4** ★★ — Print the values that are even **or** greater than 20.

Expected output:

```text
[ 12   0  23 -18   4]
```

**Q4.5** ★ — Print the elements at positions 0, 4 and 9. Then print them in the order 9, 0, 4.

Expected output:

```text
[12 23 15]
[15 12 23]
```

**Q4.6** ★★ — Given `m = np.arange(12).reshape(3, 4)`, pick the three elements at (0,1), (1,3) and (2,0) in one expression.

```python
m = np.arange(12).reshape(3, 4)
```

Expected output:

```text
[1 7 8]
```

**Q4.7** ★★★ — Using the same `m`, select the 2×2 block made of rows 0 and 2 and columns 1 and 3. Then show what `m[[0, 2], [1, 3]]` gives instead and explain the difference.

```python
m = np.arange(12).reshape(3, 4)
```

Expected output:

```text
[[ 1  3]
 [ 9 11]]
[ 1 11]
```

**Q4.8** ★★ — Print the **indices** where `data > 10`, using `np.nonzero` (or `np.where` with one argument).

Expected output:

```text
[0 4 9]
```

**Q4.9** ★★★ — Given the names and scores below, print the names of students who scored above the class mean.

```python
names = np.array(['Ada', 'Ben', 'Cy', 'Di', 'Eve'])
scores = np.array([88, 92, 79, 95, 60])
```

Expected output:

```text
['Ada' 'Ben' 'Di']
```

**Q4.10** ★★★ — Using `m = np.arange(12).reshape(3, 4)`, print only the rows whose sum is greater than 15.

```python
m = np.arange(12).reshape(3, 4)
```

Expected output:

```text
[[ 4  5  6  7]
 [ 8  9 10 11]]
```

**Q4.11** ★★ — For `g = np.array([[3, 0, 5], [1, 2, 4], [0, 0, 7]])`, print for each row whether it contains any zero, and whether all its values are positive.

```python
g = np.array([[3, 0, 5], [1, 2, 4], [0, 0, 7]])
```

Expected output:

```text
[ True False  True]
[False  True False]
```

**Q4.12** ★★★ — Using `m = np.arange(12).reshape(3, 4)`, set every element that is divisible by 3 to -1, and print `m`. Then explain why `m[m % 3 == 0][0] = 100` does **not** change `m`.

```python
m = np.arange(12).reshape(3, 4)
```

Expected output:

```text
[[-1  1  2 -1]
 [ 4  5 -1  7]
 [ 8 -1 10 11]]
```

## Topic 5: Reshaping, stacking and splitting

These questions train you to move data between shapes without changing the values.

**Q5.1** ★ — Reshape `np.arange(12)` into a 3×4 array, then into a 2-row array letting NumPy work out the columns with `-1`. Print both.

Expected output:

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
```

**Q5.2** ★★ — For `a = np.arange(12).reshape(3, 4)`, print `a.T`, then `a.ravel()`, then `a.ravel(order='F')`.

```python
a = np.arange(12).reshape(3, 4)
```

Expected output:

```text
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
[ 0  1  2  3  4  5  6  7  8  9 10 11]
[ 0  4  8  1  5  9  2  6 10  3  7 11]
```

**Q5.3** ★ — Given `x = np.array([1, 2, 3])`, print the shapes of `x[:, np.newaxis]`, `x[np.newaxis, :]` and `np.expand_dims(x, 0)`.

```python
x = np.array([1, 2, 3])
```

Expected output:

```text
(3, 1)
(1, 3)
(1, 3)
```

**Q5.4** ★ — Print the shape of `np.zeros((1, 3, 1)).squeeze()`.

Expected output:

```text
(3,)
```

**Q5.5** ★★ — Given `a = np.array([1, 2, 3])` and `b = np.array([4, 5, 6])`, print `np.vstack`, `np.hstack` and `np.column_stack` of the pair.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

Expected output:

```text
[[1 2 3]
 [4 5 6]]
[1 2 3 4 5 6]
[[1 4]
 [2 5]
 [3 6]]
```

**Q5.6** ★★ — Given the two 2×2 arrays below, concatenate them along axis 0 and along axis 1. Print both.

```python
p = np.array([[1, 2], [3, 4]])
q2 = np.array([[5, 6], [7, 8]])
```

Expected output:

```text
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
[[1 2 5 6]
 [3 4 7 8]]
```

**Q5.7** ★★ — With `a` and `b` from the vstack question, print the shapes of `np.stack((a, b), axis=0)` and `np.stack((a, b), axis=1)`.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

Expected output:

```text
(2, 3)
(3, 2)
```

**Q5.8** ★★ — Split `np.arange(10)` into 5 equal parts with `np.split`. Then split it into 3 parts with `np.array_split`. Print both results.

Expected output:

```text
[array([0, 1]), array([2, 3]), array([4, 5]), array([6, 7]), array([8, 9])]
[array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8, 9])]
```

**Q5.9** ★★ — Split `np.arange(16).reshape(4, 4)` into a left half and a right half with `np.hsplit`. Print each half.

Expected output:

```text
[[ 0  1]
 [ 4  5]
 [ 8  9]
 [12 13]]
[[ 2  3]
 [ 6  7]
 [10 11]
 [14 15]]
```

**Q5.10** ★★★ — For `b = np.arange(24).reshape(2, 3, 4)`, print the shape of `b.transpose(1, 0, 2)`, `np.swapaxes(b, 0, 2)` and `np.moveaxis(b, -1, 0)`.

```python
b = np.arange(24).reshape(2, 3, 4)
```

Expected output:

```text
(3, 2, 4)
(4, 3, 2)
(4, 2, 3)
```

**Q5.11** ★★★ — Print `np.tile([1, 2], 3)`, `np.repeat([1, 2], 3)` and `np.repeat([[1, 2], [3, 4]], 2, axis=0)`. Explain tile vs repeat in one sentence.

Expected output:

```text
[1 2 1 2 1 2]
[1 1 1 2 2 2]
[[1 2]
 [1 2]
 [3 4]
 [3 4]]
```

**Q5.12** ★★★ — Try `np.arange(10).reshape(3, 4)` inside a `try` block and print the error message. Why does it fail?

Expected output:

```text
cannot reshape array of size 10 into shape (3,4)
```

## Topic 6: Vectorized arithmetic and ufuncs

Universal functions (ufuncs) apply an operation to every element at C speed. Replace every loop you would have written with one of these.

**Q6.1** ★ — For `a = np.array([1, 2, 3, 4])` and `b = np.array([10, 20, 30, 40])`, print `a + b`, `a * b` and `a ** 2`.

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
```

Expected output:

```text
[11 22 33 44]
[ 10  40  90 160]
[ 1  4  9 16]
```

**Q6.2** ★ — Convert the Celsius temperatures `[-10, 0, 25, 37.5, 100]` to Fahrenheit (F = C × 9/5 + 32). Print the result.

Expected output:

```text
[ 14.   32.   77.   99.5 212. ]
```

**Q6.3** ★ — For `x = np.array([1, 4, 9])`, print `np.sqrt(x)`, `np.exp(x)` and `np.log(x)`, each rounded to 3 decimals.

```python
x = np.array([1, 4, 9])
```

Expected output:

```text
[1. 2. 3.]
[2.718000e+00 5.459800e+01 8.103084e+03]
[0.    1.386 2.197]
```

**Q6.4** ★★ — Points are given as x and y arrays. Print each point's distance from the origin.

```python
xs = np.array([3, 6, 5])
ys = np.array([4, 8, 12])
```

Expected output:

```text
[ 5. 10. 13.]
```

**Q6.5** ★ — For `v = np.array([-7, -2, 0, 3, 8])`, print `np.abs(v)`, `np.sign(v)` and `v % 3`.

```python
v = np.array([-7, -2, 0, 3, 8])
```

Expected output:

```text
[7 2 0 3 8]
[-1 -1  0  1  1]
[2 1 0 0 2]
```

**Q6.6** ★★ — For `a = np.array([1, 5, 3])` and `b = np.array([4, 2, 6])`, print `np.maximum(a, b)` and `np.max(a)`. What is the difference?

```python
a = np.array([1, 5, 3])
b = np.array([4, 2, 6])
```

Expected output:

```text
[4 5 6]
5
```

**Q6.7** ★★ — For `x = np.array([1, 2, 3, 4, 5])`, print `np.cumsum(x)`, `np.cumprod(x)` and `np.diff(x**2)`.

```python
x = np.array([1, 2, 3, 4, 5])
```

Expected output:

```text
[ 1  3  6 10 15]
[  1   2   6  24 120]
[3 5 7 9]
```

**Q6.8** ★★ — Print `0.1 + 0.2 == 0.3` and `np.isclose(0.1 + 0.2, 0.3)`. Explain why they differ.

Expected output:

```text
False
True
```

**Q6.9** ★★★ — Use `np.multiply.outer` to build a times table for 1–4 (rows) by 1–5 (columns). Then use `np.add.reduce` and `np.add.accumulate` on `[1, 2, 3, 4]`.

Expected output:

```text
[[ 1  2  3  4  5]
 [ 2  4  6  8 10]
 [ 3  6  9 12 15]
 [ 4  8 12 16 20]]
10
[ 1  3  6 10]
```

**Q6.10** ★★★ — Given daily prices `[100, 105, 102, 110, 99]`, print the percentage change from each day to the next, rounded to 2 decimals.

Expected output:

```text
[  5.    -2.86   7.84 -10.  ]
```

**Q6.11** ★★★ — Divide `np.array([1.0, 0.0, -1.0])` by 0 without seeing a warning (use `np.errstate`). Print the result.

Expected output:

```text
[ inf  nan -inf]
```

**Q6.12** ★★ — Round `np.array([1.5, 2.5, 3.5, -1.5])` with `np.round`, and also apply `np.floor`, `np.ceil` and `np.trunc`. Print all four.

Expected output:

```text
[ 2.  2.  4. -2.]
[ 1.  2.  3. -2.]
[ 2.  3.  4. -1.]
[ 1.  2.  3. -1.]
```

## Topic 7: Broadcasting

Broadcasting lets arrays of different shapes combine. The rule: compare shapes from the right; each pair of lengths must be equal or one of them must be 1.

**Q7.1** ★ — Add a column vector `np.array([[0], [10], [20]])` to the row `np.array([1, 2, 3, 4])`. Print the result and its shape.

Expected output:

```text
[[ 1  2  3  4]
 [11 12 13 14]
 [21 22 23 24]]
(3, 4)
```

**Q7.2** ★★ — Subtract each column's mean from the matrix below so every column has mean 0. Print the result.

```python
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

Expected output:

```text
[[-3. -3. -3.]
 [ 0.  0.  0.]
 [ 3.  3.  3.]]
```

**Q7.3** ★★ — Scale each **row** of `M` (from above) so it sums to 1. Print the result rounded to 3 decimals.

```python
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

Expected output:

```text
[[0.167 0.333 0.5  ]
 [0.267 0.333 0.4  ]
 [0.292 0.333 0.375]]
```

**Q7.4** ★★ — Use `np.broadcast_shapes` to print the result shape for each pair, or the error message when they don't broadcast: (3,4)&(4,), (3,4)&(3,), (3,1)&(1,4), (2,3,4)&(3,1).

Expected output:

```text
(3, 4) (4,) -> (3, 4)
(3, 4) (3,) -> error
(3, 1) (1, 4) -> (3, 4)
(2, 3, 4) (3, 1) -> (2, 3, 4)
```

**Q7.5** ★ — Build a 5×5 multiplication table using broadcasting (no `outer`).

Expected output:

```text
[[ 1  2  3  4  5]
 [ 2  4  6  8 10]
 [ 3  6  9 12 15]
 [ 4  8 12 16 20]
 [ 5 10 15 20 25]]
```

**Q7.6** ★★ — For points on a line `p = np.array([0, 3, 7, 10])`, build the 4×4 matrix of distances between every pair.

```python
p = np.array([0, 3, 7, 10])
```

Expected output:

```text
[[ 0  3  7 10]
 [ 3  0  4  7]
 [ 7  4  0  3]
 [10  7  3  0]]
```

**Q7.7** ★★★ — Given three 2-D points, compute the 3×3 matrix of Euclidean distances between every pair, rounded to 2 decimals. No loops.

```python
pts = np.array([[0, 0], [3, 4], [6, 8]])
```

Expected output:

```text
[[ 0.  5. 10.]
 [ 5.  0.  5.]
 [10.  5.  0.]]
```

**Q7.8** ★★★ — Min-max scale each **column** of the matrix below to the range \[0, 1\]. Print rounded to 2 decimals.

```python
D = np.array([[10, 200, 3], [20, 400, 9], [15, 300, 6]])
```

Expected output:

```text
[[0.  0.  0. ]
 [1.  1.  1. ]
 [0.5 0.5 0.5]]
```

**Q7.9** ★★ — Rows are stores, columns are items. Multiply quantities by unit prices, then print revenue per store.

```python
qty = np.array([[2, 0, 5, 1], [4, 3, 0, 2], [1, 1, 1, 1]])
price = np.array([2.5, 10.0, 1.0, 4.0])
```

Expected output:

```text
[14.  48.  17.5]
```

**Q7.10** ★★★ — Explain why `np.ones((3, 4)) + np.ones((3,))` fails, then fix it with `[:, None]`. Print the shape of the fixed result.

Expected output:

```text
(3, 4)
```

## Topic 8: Aggregations and the axis argument

`axis=0` collapses rows (one answer per column); `axis=1` collapses columns (one answer per row). These questions use one sales table.

Use this array for every question in this topic:

```python
sales = np.array([[120,  95, 130, 110],
                  [ 80, 105,  90, 125],
                  [150, 140, 160, 135]])  # rows = stores A, B, C; columns = Q1..Q4
```

**Q8.1** ★ — Print the grand total, the total per store and the total per quarter.

Expected output:

```text
1440
[455 400 585]
[350 340 380 370]
```

**Q8.2** ★ — Print the mean of each store, rounded to 2 decimals, and the standard deviation of each quarter, rounded to 2 decimals.

Expected output:

```text
[113.75 100.   146.25]
[28.67 19.29 28.67 10.27]
```

**Q8.3** ★★ — For each store, print the index of its best quarter. For each quarter, print the index of the best store.

Expected output:

```text
[2 3 2]
[2 2 2 2]
```

**Q8.4** ★★ — Print the shape of `sales.sum(axis=1)` and of `sales.sum(axis=1, keepdims=True)`.

Expected output:

```text
(3,)
(3, 1)
```

**Q8.5** ★★ — Print the median of all sales, and the 25th and 75th percentiles.

Expected output:

```text
122.5
[102.5  136.25]
```

**Q8.6** ★★ — Print each store's running total across quarters.

Expected output:

```text
[[120 215 345 455]
 [ 80 185 275 400]
 [150 290 450 585]]
```

**Q8.7** ★★★ — Which store grew the most from Q1 to Q4? Print the store letter and the increase.

Expected output:

```text
B 45
```

**Q8.8** ★★ — Print, for each store, how many quarters had sales above 100.

Expected output:

```text
[3 2 4]
```

**Q8.9** ★★★ — Express each value as a percentage of its store's yearly total, rounded to 1 decimal.

Expected output:

```text
[[26.4 20.9 28.6 24.2]
 [20.  26.2 22.5 31.2]
 [25.6 23.9 27.4 23.1]]
```

**Q8.10** ★★ — Using `a = np.arange(24).reshape(2, 3, 4)`, print the shape of `a.sum(axis=0)`, then print `a.sum(axis=(1, 2))`.

```python
a = np.arange(24).reshape(2, 3, 4)
```

Expected output:

```text
(3, 4)
[ 66 210]
```

**Q8.11** ★★★ — Compute a weighted average grade with `np.average`. Grades 70, 85, 90 with weights 0.2, 0.3, 0.5. Print it.

Expected output:

```text
84.5
```

**Q8.12** ★★★ — Find the single largest sale and print which store and quarter it came from, using `argmax` and `np.unravel_index`.

Expected output:

```text
160 2 2
```

## Topic 9: Sorting, searching and set operations

Sorting and its index-returning cousin `argsort` power rankings, top-N lists and de-duplication.

**Q9.1** ★ — For `x = np.array([5, 2, 9, 1, 7])`, print `np.sort(x)`, then print `x` to show it is unchanged. Then call `x.sort()` and print `x` again.

```python
x = np.array([5, 2, 9, 1, 7])
```

Expected output:

```text
[1 2 5 7 9]
[5 2 9 1 7]
[1 2 5 7 9]
```

**Q9.2** ★★ — Print the names sorted by score, highest score first.

```python
names = np.array(['Ada', 'Ben', 'Cy', 'Di', 'Eve'])
scores = np.array([88, 92, 79, 95, 60])
```

Expected output:

```text
['Di' 'Ben' 'Ada' 'Cy' 'Eve']
```

**Q9.3** ★★ — For `m = np.array([[3, 1, 2], [9, 7, 8], [6, 5, 4]])`, print `np.sort(m, axis=0)` and `np.sort(m, axis=1)`.

```python
m = np.array([[3, 1, 2], [9, 7, 8], [6, 5, 4]])
```

Expected output:

```text
[[3 1 2]
 [6 5 4]
 [9 7 8]]
[[1 2 3]
 [7 8 9]
 [4 5 6]]
```

**Q9.4** ★ — Print the unique values of `votes` and how many times each appears.

```python
votes = np.array(['red', 'blue', 'red', 'green', 'blue', 'red'])
```

Expected output:

```text
['blue' 'green' 'red']
[2 1 3]
```

**Q9.5** ★★ — Given sorted `s = np.array([10, 20, 30, 40])`, print where 25, 10 and 45 would be inserted to keep it sorted.

```python
s = np.array([10, 20, 30, 40])
```

Expected output:

```text
[2 0 4]
```

**Q9.6** ★★ — For `a = np.array([1, 2, 3, 4, 5])` and `b = np.array([4, 5, 6, 7])`, print the intersection, union, `a` minus `b`, the symmetric difference, and `np.isin(a, b)`.

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7])
```

Expected output:

```text
[4 5]
[1 2 3 4 5 6 7]
[1 2 3]
[1 2 3 6 7]
[False False False  True  True]
```

**Q9.7** ★★ — Print the 3 largest values of `x`, largest first.

```python
x = np.array([14, 3, 27, 8, 19, 30, 1])
```

Expected output:

```text
[30 27 19]
```

**Q9.8** ★★★ — Compute the rank of each element of `x` (0 = smallest) without loops.

```python
x = np.array([40, 10, 30, 20])
```

Expected output:

```text
[3 0 2 1]
```

**Q9.9** ★★ — Sort the rows of `m` by the values in its second column (ascending). Print the result.

```python
m = np.array([[1, 9], [2, 3], [3, 7], [4, 1]])
```

Expected output:

```text
[[4 1]
 [2 3]
 [3 7]
 [1 9]]
```

**Q9.10** ★★★ — Students have a class number and a score. Sort them by class, and within each class by score. Print the sorted student IDs. (Hint: `np.lexsort` sorts by the **last** key first.)

```python
ids = np.array([101, 102, 103, 104, 105])
cls = np.array([2, 1, 2, 1, 1])
score = np.array([70, 90, 85, 60, 75])
```

Expected output:

```text
[104 105 102 101 103]
```

**Q9.11** ★★ — Print the index of the first value in `x` greater than 15. (Hint: `argmax` on a boolean array.)

```python
x = np.array([4, 12, 18, 9, 21])
```

Expected output:

```text
2
```

## Topic 10: Copies vs views

Basic slices are views that share memory with the original; fancy and boolean indexing return copies. Predict each output before running it.

**Q10.1** ★ — Create `a = np.arange(5)`, take `b = a[1:4]`, set `b[0] = 99`, then print `a`.

Expected output:

```text
[ 0 99  2  3  4]
```

**Q10.2** ★ — Repeat the last question but use `b = a[1:4].copy()`. Print `a`.

Expected output:

```text
[0 1 2 3 4]
```

**Q10.3** ★★ — Create `a = np.arange(5)`, take `c = a[[1, 2, 3]]`, set `c[0] = 99`, then print `a`.

Expected output:

```text
[0 1 2 3 4]
```

**Q10.4** ★★ — For `a = np.arange(12).reshape(3, 4)`, print `np.shares_memory(a, x)` for `x` in: `a.reshape(4, 3)`, `a.ravel()`, `a.flatten()`, `a.T`, `a[::2]`, `a[a > 5]`.

```python
a = np.arange(12).reshape(3, 4)
```

Expected output:

```text
True
True
False
True
True
False
```

**Q10.5** ★ — Set `a = np.array([1, 2, 3])`, then `b = a`, then `b[0] = 100`. Print `a` and `b is a`.

Expected output:

```text
[100   2   3]
True
```

**Q10.6** ★★★ — Predict, then run: `a = np.arange(6)`, `b = a[1:4]`, `b[:] = b * 10`, `c = a[[0, 5]]`, `c[:] = -1`. Print `a`.

Expected output:

```text
[ 0 10 20 30  4  5]
```

**Q10.7** ★★ — For `a = np.arange(6)`, print `a[2:].base is a` and `a[[2, 3]].base is a`.

```python
a = np.arange(6)
```

Expected output:

```text
True
False
```

**Q10.8** ★★★ — Explain the difference: (1) `a[a > 2] = 0` and (2) `b = a[a > 2]; b[:] = 0`. Start each from `a = np.arange(6)` and print `a` after each.

Expected output:

```text
[0 1 2 0 0 0]
[0 1 2 3 4 5]
```

**Q10.9** ★★★ — Inside a function, `x += 1` and `x = x + 1` behave differently on arrays. Show this by passing `np.array([1, 2, 3])` to each version and printing the original afterwards.

Expected output:

```text
[2 3 4]
[1 2 3]
```

## Topic 11: where, select, clip and NaN handling

Conditional logic and missing data — the bread and butter of cleaning real datasets.

**Q11.1** ★ — Label each score as 'pass' (≥ 50) or 'fail' using `np.where`.

```python
scores = np.array([45, 78, 50, 32, 91])
```

Expected output:

```text
['fail' 'pass' 'pass' 'fail' 'pass']
```

**Q11.2** ★★ — Give letter grades: A for ≥ 80, B for ≥ 60, C otherwise, using `np.select`.

```python
scores = np.array([45, 78, 50, 32, 91])
```

Expected output:

```text
['C' 'B' 'C' 'C' 'A']
```

**Q11.3** ★ — Clip `v = np.array([-20, 5, 50, 130, 99])` to the range 0–100.

```python
v = np.array([-20, 5, 50, 130, 99])
```

Expected output:

```text
[  0   5  50 100  99]
```

**Q11.4** ★★ — For `arr = np.array([1.0, np.nan, 3.0, np.nan, 5.0])`, print `np.mean(arr)`, `np.nanmean(arr)` and the number of NaNs.

```python
arr = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
```

Expected output:

```text
nan
3.0
2
```

**Q11.5** ★ — Print `np.nan == np.nan` and `np.isnan(np.nan)`.

Expected output:

```text
False
True
```

**Q11.6** ★★★ — Replace each NaN in `X` with the mean of its column. Print the result.

```python
X = np.array([[1.0, np.nan, 3.0], [4.0, 5.0, np.nan], [7.0, 8.0, 9.0]])
```

Expected output:

```text
[[1.  6.5 3. ]
 [4.  5.  6. ]
 [7.  8.  9. ]]
```

**Q11.7** ★★ — Using `X` from the previous question, print only the rows that have no NaN.

```python
X = np.array([[1.0, np.nan, 3.0], [4.0, 5.0, np.nan], [7.0, 8.0, 9.0]])
```

Expected output:

```text
[[7. 8. 9.]]
```

**Q11.8** ★★ — Classify BMI values: 'under' < 18.5, 'normal' < 25, 'over' < 30, otherwise 'obese'.

```python
bmi = np.array([17.2, 22.0, 27.5, 31.1, 24.9])
```

Expected output:

```text
['under' 'normal' 'over' 'obese' 'normal']
```

**Q11.9** ★★ — Print `np.nanmax`, `np.nanmin` and `np.nansum` of `arr`, then replace NaNs with 0 using `np.nan_to_num`.

```python
arr = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
```

Expected output:

```text
5.0 1.0 9.0
[1. 0. 3. 0. 5.]
```

**Q11.10** ★★★ — Why can't you put NaN in an integer array? Try `np.array([1, 2, 3])[0] = np.nan` in a try block and print the error, then show the fix by converting to float.

Expected output:

```text
cannot convert float NaN to integer
[nan  2.  3.]
```

## Topic 12: Random numbers

Use the modern Generator API (`np.random.default_rng`). Seeding makes results repeatable, which is essential for teaching. The exact values below come from NumPy 2.x; very old versions may differ.

**Q12.1** ★ — With `rng = np.random.default_rng(42)`, roll a six-sided die 10 times.

Expected output:

```text
[1 5 4 3 3 6 1 5 2 1]
```

**Q12.2** ★ — With seed 42, print 5 uniform random floats in \[0, 1), rounded to 3 decimals.

Expected output:

```text
[0.774 0.439 0.859 0.697 0.094]
```

**Q12.3** ★★ — With seed 42, draw 5 values from a normal distribution with mean 50 and standard deviation 10. Round to 2 decimals.

Expected output:

```text
[53.05 39.6  57.5  59.41 30.49]
```

**Q12.4** ★★ — With seed 42, pick 3 different names from the list without replacement.

```python
names = np.array(['Ada', 'Ben', 'Cy', 'Di', 'Eve'])
```

Expected output:

```text
['Eve' 'Ada' 'Di']
```

**Q12.5** ★★ — With seed 42, print a random permutation of `np.arange(8)`.

Expected output:

```text
[3 4 2 7 6 1 5 0]
```

**Q12.6** ★ — Create two generators with seed 7 and check that `rng.random(3)` is identical for both. Print the comparison.

Expected output:

```text
True
```

**Q12.7** ★★★ — With seed 0, flip a fair coin 10,000 times (0 = tails, 1 = heads). Print the proportion of heads, rounded to 3 decimals.

Expected output:

```text
0.503
```

**Q12.8** ★★★ — Estimate π with seed 1: sample 100,000 points uniformly in the unit square and count those inside the quarter circle x²+y² ≤ 1. Print 4 × fraction, rounded to 3 decimals.

Expected output:

```text
3.145
```

**Q12.9** ★★★ — With seed 3, roll two dice 10,000 times. Print the most common total and how often it occurred.

Expected output:

```text
7 1673
```

**Q12.10** ★★ — With seed 5, create a 3×4 matrix of random integers between 10 and 99 inclusive.

Expected output:

```text
[[70 82 12 82]
 [52 56 66 35]
 [98 14 35 44]]
```

## Topic 13: Linear algebra

Matrix multiplication, solving systems and the `np.linalg` module.

Use these arrays for every question in this topic:

```python
A = np.array([[2, 1], [1, 3]])
B = np.array([[1, 2], [3, 4]])
```

**Q13.1** ★ — Print `A @ B` and `A * B`. Explain the difference.

Expected output:

```text
[[ 5  8]
 [10 14]]
[[ 2  2]
 [ 3 12]]
```

**Q13.2** ★ — Print the transpose of `B`, the trace of `B`, and the determinant of `B` rounded to 2 decimals.

Expected output:

```text
[[1 3]
 [2 4]]
5
-2.0
```

**Q13.3** ★★ — Compute the inverse of `A` and check that `A @ inv(A)` is the identity using `np.allclose`. Print the inverse rounded to 3 decimals and the check.

Expected output:

```text
[[ 0.6 -0.2]
 [-0.2  0.4]]
True
```

**Q13.4** ★★ — Solve the system 2x + y = 5, x + 3y = 10. Print x and y.

Expected output:

```text
[1. 3.]
```

**Q13.5** ★ — For `u = np.array([1, 2, 3])` and `v = np.array([4, 5, 6])`, print the dot product, the length (norm) of `u` rounded to 3 decimals, and the cross product.

```python
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
```

Expected output:

```text
32
3.742
[-3  6 -3]
```

**Q13.6** ★★ — Find the eigenvalues of `[[4, 1], [2, 3]]`. Print them sorted and rounded to 2 decimals.

Expected output:

```text
[2. 5.]
```

**Q13.7** ★★★ — Use `np.linalg.matrix_power` on `[[1, 1], [1, 0]]` to print the 10th Fibonacci number (top-right element of the 10th power).

Expected output:

```text
[[89 55]
 [55 34]]
55
```

**Q13.8** ★★★ — Fit a straight line y = m·x + c to the points below using `np.linalg.lstsq`. Print m and c rounded to 3 decimals.

```python
x = np.array([0, 1, 2, 3, 4], dtype=float)
y = np.array([1.1, 2.9, 5.2, 7.1, 8.8])
```

Expected output:

```text
1.96 1.1
```

**Q13.9** ★★ — Print the rank of `[[1, 2, 3], [2, 4, 6], [1, 0, 1]]`. Why isn't it 3?

Expected output:

```text
2
```

**Q13.10** ★★★ — Solve the 3×3 system: x + y + z = 6, 2y + 5z = −4, 2x + 5y − z = 27. Print the solution.

Expected output:

```text
[ 5.  3. -2.]
```

## Topic 14: Saving and loading

Moving arrays to and from disk: NumPy's own binary formats and plain text/CSV.

**Q14.1** ★ — Save `np.arange(10)` to `data.npy`, load it back and print whether it equals the original.

Expected output:

```text
True
```

**Q14.2** ★★ — Save two arrays, `x = np.arange(3)` and `y = np.ones((2, 2))`, in one `.npz` file under the names `x` and `y`. Load it and print the stored names and `y`.

Expected output:

```text
['x', 'y']
[[1. 1.]
 [1. 1.]]
```

**Q14.3** ★★ — Write the matrix below to `marks.csv` with a header `math,physics`, comma separated, integer format. Then print the file's text.

```python
marks = np.array([[70, 65], [88, 92], [54, 61]])
```

Expected output:

```text
math,physics
70,65
88,92
54,61
```

**Q14.4** ★★ — Load `marks.csv` (from the previous question) with `np.loadtxt`, skipping the header. Print the array and the mean of each column.

Expected output:

```text
[[70. 65.]
 [88. 92.]
 [54. 61.]]
[70.66666667 72.66666667]
```

**Q14.5** ★★★ — A CSV has gaps. Write the text below to `gaps.csv`, read it with `np.genfromtxt` so blanks become NaN, then print the array and the column means ignoring NaN (rounded to 2 decimals).

```python
text = 'a,b,c\n1,2,3\n4,,6\n7,8,\n'
```

Expected output:

```text
[[ 1.  2.  3.]
 [ 4. nan  6.]
 [ 7.  8. nan]]
[4.  5.  4.5]
```

## Topic 15: Mixed challenge problems

Each problem combines several topics. Try to solve each in three lines or fewer, with no loops.

**Q15.1** ★★★ — Compute the 3-day moving average of `p`. Print it rounded to 2 decimals.

```python
p = np.array([10, 12, 11, 15, 18, 17, 20])
```

Expected output:

```text
[11.   12.67 14.67 16.67 18.33]
```

**Q15.2** ★★★ — Find the most frequent value in `x` and how many times it appears (use `np.bincount`).

```python
x = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
```

Expected output:

```text
5 3
```

**Q15.3** ★★★ — Standardise `Z = np.arange(1, 10).reshape(3, 3)` as a whole (subtract the mean, divide by the std). Print rounded to 2 decimals.

Expected output:

```text
[[-1.55 -1.16 -0.77]
 [-0.39  0.    0.39]
 [ 0.77  1.16  1.55]]
```

**Q15.4** ★★★ — Replace the largest value in **each row** of `R` with 0. Print the result.

```python
R = np.array([[3, 8, 1], [7, 2, 9], [4, 6, 5]])
```

Expected output:

```text
[[3 0 1]
 [7 2 0]
 [4 0 5]]
```

**Q15.5** ★★ — Find the value in `x` closest to 6.3.

```python
x = np.array([1.5, 4.0, 6.0, 7.2, 9.9])
```

Expected output:

```text
6.0
```

**Q15.6** ★★★ — One-hot encode the labels `[2, 0, 1, 2]` (3 classes) into a 4×3 matrix of 0s and 1s.

Expected output:

```text
[[0 0 1]
 [1 0 0]
 [0 1 0]
 [0 0 1]]
```

**Q15.7** ★★★ — Down-sample the 4×4 'image' by averaging each 2×2 block (giving a 2×2 result).

```python
img = np.arange(16).reshape(4, 4)
```

Expected output:

```text
[[ 2.5  4.5]
 [10.5 12.5]]
```

**Q15.8** ★★ — Print the running maximum of `x` (the best value seen so far at each step).

```python
x = np.array([3, 1, 4, 1, 5, 9, 2, 6])
```

Expected output:

```text
[3 3 4 4 5 9 9 9]
```

**Q15.9** ★★ — Swap rows 0 and 2 of `S = np.arange(9).reshape(3, 3)`. Print the result.

Expected output:

```text
[[6 7 8]
 [3 4 5]
 [0 1 2]]
```

**Q15.10** ★★★ — Gradebook: 4 students × 3 tests, weights 30%/30%/40%. Print each final score, whether each passed (≥ 60), and the indices of students from best to worst.

```python
G = np.array([[55, 70, 62], [90, 85, 95], [40, 58, 61], [72, 66, 80]])
w = np.array([0.3, 0.3, 0.4])
```

Expected output:

```text
[62.3 90.5 53.8 73.4]
[ True  True False  True]
[1 3 0 2]
```

**Q15.11** ★★★ — Dates: print the number of days from 2026-10-29 to 2026-12-25, and the list of the next 7 dates starting 2026-10-29.

Expected output:

```text
57 days
['2026-10-29' '2026-10-30' '2026-10-31' '2026-11-01' '2026-11-02'
 '2026-11-03' '2026-11-04']
```

**Q15.12** ★★★ — Progressive tax: 0% on income up to 10,000, 10% on the part between 10,000 and 40,000, 20% above 40,000. Compute the tax for each income, no loops.

```python
inc = np.array([8_000, 25_000, 40_000, 75_000])
```

Expected output:

```text
[    0.  1500.  3000. 10000.]
```

**Q15.13** ★★★ — Count how many times the sign changes in `s` (e.g. from positive to negative).

```python
s = np.array([3, 5, -2, -4, 6, 1, -7])
```

Expected output:

```text
3
```

**Q15.14** ★★★ — Given a 5×5 grid, sum the 8 neighbours of the centre cell (2, 2) using slicing.

```python
grid = np.arange(25).reshape(5, 5)
```

Expected output:

```text
96
```

**Q15.15** ★★★ — Normalise each row vector of `V` to length 1, then print the result rounded to 3 decimals and the new row lengths.

```python
V = np.array([[3.0, 4.0], [1.0, 1.0], [0.0, 2.0]])
```

Expected output:

```text
[[0.6   0.8  ]
 [0.707 0.707]
 [0.    1.   ]]
[1. 1. 1.]
```
