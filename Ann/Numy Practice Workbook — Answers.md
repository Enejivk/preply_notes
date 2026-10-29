# NumPy Practice Workbook — Answers

Oct 29, 2026 · @Associate2TrioEdX

## How to use the answers

Each answer gives runnable code and a short explanation of why it works. Run the code and compare with the expected output in the questions doc (all outputs were produced on NumPy 2.5). Question numbers match the questions doc.

- Attempt the question first; only open the answer to check or when stuck for more than ten minutes.
- Every code block assumes `import numpy as np`. Where a topic has shared setup, it is shown once at the top of that topic.
- Many questions have more than one correct answer. If your output matches, your solution is right even if it looks different.
- When teaching, the explanation line is usually the part worth saying out loud.

## Topic 1: Creating arrays

**Q1.1**

```python
a = np.arange(10)
print(a)
```

`arange(stop)` starts at 0 and stops *before* `stop`, just like Python's `range`.

**Q1.2**

```python
a = np.linspace(0, 1, 5)
print(a)
```

`linspace(start, stop, num)` includes the endpoint by default and you choose *how many* points, not the step.

**Q1.3**

```python
a = np.zeros((3, 4), dtype=int)
print(a)
print(a.dtype)
```

`np.zeros` defaults to `float64`; passing `dtype=int` changes that. Note the shape is passed as one tuple.

**Q1.4**

```python
print(np.eye(3))
print(np.full((2, 3), 7))
```

`np.eye(n)` gives floats on the diagonal. `np.full(shape, value)` takes its dtype from `value` (an int here).

**Q1.5**

```python
a = np.arange(10, -11, -2)
print(a)
```

With a negative step the stop must be *past* -10, so -11. Students often write `-10` and lose the last value.

**Q1.6**

```python
print(np.arange(0, 1, 0.25))
print(np.linspace(0, 1, 4, endpoint=False))
```

`endpoint=False` makes `linspace` behave like a half-open range. For float steps, `linspace` is safer because `arange` can gain or lose a point through rounding.

**Q1.7**

```python
a = np.ones((5, 5), dtype=int)
a[1:-1, 1:-1] = 0
print(a)
```

Start with all ones, then overwrite the interior slice `1:-1` on both axes.

**Q1.8**

```python
lst = [[1, 2, 3], [4, 5, 6]]
a = np.array(lst)
b = np.ones_like(a, dtype=float)
print(b)
```

`ones_like`, `zeros_like` and `full_like` copy the shape (and by default the dtype) of an existing array.

**Q1.9**

```python
print(np.diag([1, 2, 3, 4]))
print(np.eye(4, k=1, dtype=int))
```

`np.diag(list)` builds a diagonal matrix. `np.eye(n, k=1)` shifts the ones one place to the right (k=-1 shifts left/down).

**Q1.10**

```python
a = np.fromfunction(lambda i, j: 10 * i + j, (3, 4), dtype=int)
print(a)
```

`fromfunction` calls your function once with whole arrays of row indices and column indices, so the formula is vectorized.

**Q1.11**

```python
board = np.zeros((8, 8), dtype=int)
board[0::2, 1::2] = 1
board[1::2, 0::2] = 1
print(board)
```

Two strided slices: even rows/odd columns and odd rows/even columns. Alternative: `np.indices((8,8)).sum(axis=0) % 2`, or `np.tile([[0,1],[1,0]], (4,4))`.

**Q1.12**

```python
print(np.zeros((2, 2)))
```

`np.empty` only reserves memory; whatever bytes were there remain, so its values are unpredictable. Use it only when you will overwrite every element.

## Topic 2: Attributes and data types

**Q2.1**

```python
a = np.arange(24).reshape(2, 3, 4)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
```

`ndim` = number of axes, `shape` = length of each axis, `size` = total elements (2×3×4).

**Q2.2**

```python
a = np.zeros(100, dtype=np.float64)
b = np.zeros(100, dtype=np.float32)
print(a.itemsize, a.nbytes)
print(b.itemsize, b.nbytes)
```

`itemsize` is bytes per element; `nbytes = itemsize * size`. Choosing float32 halves memory.

**Q2.3**

```python
x = np.array([1.7, -2.3, 3.9])
print(x.astype(int))
```

`astype(int)` **truncates toward zero** (1.7→1, -2.3→-2). Use `np.round(x).astype(int)` to round.

**Q2.4**

```python
a = np.array([1, 2.5, '3'])
print(a)
print(a.dtype)
```

An array has one dtype. When a string is mixed in, everything is converted to a Unicode string type (`<U32`). Arithmetic on it will now fail.

**Q2.5**

```python
a = np.array([250], dtype=np.uint8)
print(a + 10)
```

uint8 holds 0–255. 260 wraps around to 260 − 256 = 4, silently. This *overflow* is a classic data bug.

**Q2.6**

```python
flags = np.array([True, False, True, True])
print(flags.sum())
print(flags.astype(int))
```

True counts as 1 and False as 0, so `sum()` counts Trues.

**Q2.7**

```python
a = np.array([7, 8, 9])
print(a / 2, (a / 2).dtype)
print(a // 2, (a // 2).dtype)
```

`/` always gives float; `//` keeps integers when both sides are integers.

**Q2.8**

```python
info = np.iinfo(np.int16)
print(info.min, info.max)
print(np.finfo(np.float32).eps)
```

`np.iinfo` describes integer types and `np.finfo` describes float types. eps is the gap between 1.0 and the next representable float.

**Q2.9**

```python
a = np.arange(1, 6, dtype=np.float32)
print(a.dtype)
print(a.astype(np.int8))
```

Most constructors take `dtype=`. `astype` always returns a new array.

## Topic 3: Indexing and slicing

Every solution below assumes this setup has been run:

```python
a = np.arange(1, 26).reshape(5, 5)
```

**Q3.1**

```python
print(a)
print(a[2, 3])
```

Use `a[row, col]`; `a[2][3]` also works but makes two indexing steps.

**Q3.2**

```python
print(a[-1])
print(a[:, -1])
```

`:` means 'all rows'. The column comes back as a 1-D array, not a column shape.

**Q3.3**

```python
print(a[-2:, -2:])
```

Negative starts count from the end; omitting the stop goes to the end.

**Q3.4**

```python
print(a[::2, ::2])
```

`start:stop:step` works per axis.

**Q3.5**

```python
print(a[::-1])
print(a[::-1, ::-1])
```

A step of -1 walks backwards. `np.flipud` / `np.flip` do the same.

**Q3.6**

```python
print(a[1:-1, 1:-1])
```

Same pattern as the border question in Topic 1, now used to read rather than write.

**Q3.7**

```python
x = np.arange(10)
print(x[7::-2])
```

Start at index 7 and step backwards by 2 until the start of the array.

**Q3.8**

```python
b = np.arange(24).reshape(2, 3, 4)
print(b[1, :, 2])
print(b[:, 1, :])
print(b[..., -1])
```

`...` (Ellipsis) means 'all the axes I didn't mention'. Shapes: (3,), (2, 4), (2, 3).

**Q3.9**

```python
print(a[1].shape)
print(a[1:2].shape)
print(a[:, 1].shape)
print(a[:, [1]].shape)
```

An integer index *removes* that axis; a slice or a list *keeps* it. This matters for broadcasting later.

**Q3.10**

```python
c = a.copy()
c[:, 0] = 0
c[0] = -1
print(c)
```

Assigning a scalar to a slice broadcasts it to every element. Order matters: row 0 is set last, so its first element is -1.

**Q3.11**

```python
print(np.diag(a))
print(np.diag(np.fliplr(a)))
```

`np.diag` on a 2-D array extracts the diagonal. Flipping left-right turns the anti-diagonal into the main one.

## Topic 4: Boolean masks and fancy indexing

Every solution below assumes this setup has been run:

```python
data = np.array([12, -5, 7, 0, 23, -18, 4, 9, -1, 15])
```

**Q4.1**

```python
print(data[data > 0])
```

`data > 0` is a boolean array; indexing with it keeps the True positions.

**Q4.2**

```python
print(((data >= 0) & (data <= 10)).sum())
```

Use `&` (not `and`) and wrap each condition in parentheses because `&` binds more tightly than `>=`.

**Q4.3**

```python
d = data.copy()
d[d < 0] = 0
print(d)
```

Mask assignment changes values in place, so copy first if you need the original.

**Q4.4**

```python
print(data[(data % 2 == 0) | (data > 20)])
```

`|` is element-wise OR. `~` is element-wise NOT.

**Q4.5**

```python
print(data[[0, 4, 9]])
print(data[[9, 0, 4]])
```

A list of indices returns elements in exactly the order you list them; repeats are allowed too.

**Q4.6**

```python
m = np.arange(12).reshape(3, 4)
print(m[[0, 1, 2], [1, 3, 0]])
```

Two index lists are paired up position by position: (0,1), (1,3), (2,0).

**Q4.7**

```python
m = np.arange(12).reshape(3, 4)
print(m[np.ix_([0, 2], [1, 3])])
print(m[[0, 2], [1, 3]])
```

`np.ix_` builds a grid (every row with every column). Plain paired lists give only the points (0,1) and (2,3).

**Q4.8**

```python
print(np.nonzero(data > 10)[0])
```

`np.nonzero` returns a tuple with one index array per axis, so take `[0]` for 1-D.

**Q4.9**

```python
names = np.array(['Ada', 'Ben', 'Cy', 'Di', 'Eve'])
scores = np.array([88, 92, 79, 95, 60])
print(names[scores > scores.mean()])
```

A mask built from one array can index another array of the same length; this is how you 'join' parallel columns.

**Q4.10**

```python
m = np.arange(12).reshape(3, 4)
print(m[m.sum(axis=1) > 15])
```

`m.sum(axis=1)` gives one number per row; a 1-D mask on axis 0 selects whole rows.

**Q4.11**

```python
g = np.array([[3, 0, 5], [1, 2, 4], [0, 0, 7]])
print(np.any(g == 0, axis=1))
print(np.all(g > 0, axis=1))
```

`np.any` / `np.all` reduce booleans along an axis.

**Q4.12**

```python
m = np.arange(12).reshape(3, 4)
m[m % 3 == 0] = -1
print(m)
```

`m[mask] = value` is a single assignment that writes into `m`. But `m[mask]` on its own makes a **copy**, so `m[mask][0] = 100` changes only that temporary copy.

## Topic 5: Reshaping, stacking and splitting

**Q5.1**

```python
a = np.arange(12)
print(a.reshape(3, 4))
print(a.reshape(2, -1))
```

`-1` means 'whatever length makes the total size fit'. Only one axis may be -1.

**Q5.2**

```python
a = np.arange(12).reshape(3, 4)
print(a.T)
print(a.ravel())
print(a.ravel(order='F'))
```

Default order 'C' reads row by row; 'F' (Fortran) reads column by column.

**Q5.3**

```python
x = np.array([1, 2, 3])
print(x[:, np.newaxis].shape)
print(x[np.newaxis, :].shape)
print(np.expand_dims(x, 0).shape)
```

`np.newaxis` (same as `None`) inserts a length-1 axis. This is how you turn a vector into a column for broadcasting.

**Q5.4**

```python
print(np.zeros((1, 3, 1)).squeeze().shape)
```

`squeeze` removes every axis of length 1.

**Q5.5**

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a, b)))
print(np.hstack((a, b)))
print(np.column_stack((a, b)))
```

vstack stacks as rows, hstack joins end to end, column\_stack treats each 1-D array as a column.

**Q5.6**

```python
p = np.array([[1, 2], [3, 4]])
q2 = np.array([[5, 6], [7, 8]])
print(np.concatenate((p, q2), axis=0))
print(np.concatenate((p, q2), axis=1))
```

`concatenate` joins along an *existing* axis; the other axes must match.

**Q5.7**

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.stack((a, b), axis=0).shape)
print(np.stack((a, b), axis=1).shape)
```

`stack` creates a *new* axis at the position you give, unlike `concatenate`.

**Q5.8**

```python
x = np.arange(10)
print(np.split(x, 5))
print(np.array_split(x, 3))
```

`np.split` raises an error if the split isn't even; `array_split` allows uneven parts.

**Q5.9**

```python
left, right = np.hsplit(np.arange(16).reshape(4, 4), 2)
print(left)
print(right)
```

`hsplit` splits along columns (axis 1); `vsplit` along rows.

**Q5.10**

```python
b = np.arange(24).reshape(2, 3, 4)
print(b.transpose(1, 0, 2).shape)
print(np.swapaxes(b, 0, 2).shape)
print(np.moveaxis(b, -1, 0).shape)
```

`transpose` takes the new order of all axes; `swapaxes` swaps two; `moveaxis` moves one axis to a new position.

**Q5.11**

```python
print(np.tile([1, 2], 3))
print(np.repeat([1, 2], 3))
print(np.repeat([[1, 2], [3, 4]], 2, axis=0))
```

`tile` repeats the whole block; `repeat` repeats each element.

**Q5.12**

```python
try:
    np.arange(10).reshape(3, 4)
except ValueError as e:
    print(e)
```

Reshape never adds or drops elements: 10 values cannot fill 3×4 = 12 slots.

## Topic 6: Vectorized arithmetic and ufuncs

**Q6.1**

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
print(a + b)
print(a * b)
print(a ** 2)
```

Operators act element by element on arrays of the same shape.

**Q6.2**

```python
c = np.array([-10, 0, 25, 37.5, 100])
print(c * 9 / 5 + 32)
```

A whole formula applies to the whole array at once.

**Q6.3**

```python
x = np.array([1, 4, 9])
print(np.round(np.sqrt(x), 3))
print(np.round(np.exp(x), 3))
print(np.round(np.log(x), 3))
```

`np.log` is the natural log; use `np.log10` or `np.log2` for other bases. The exp line prints in scientific notation because its values span a wide range (2.7 to 8103); `np.set_printoptions(suppress=True)` turns that off.

**Q6.4**

```python
xs = np.array([3, 6, 5])
ys = np.array([4, 8, 12])
print(np.sqrt(xs**2 + ys**2))
```

`np.hypot(xs, ys)` does the same in one call.

**Q6.5**

```python
v = np.array([-7, -2, 0, 3, 8])
print(np.abs(v))
print(np.sign(v))
print(v % 3)
```

Python-style modulo: the result takes the sign of the divisor, so -7 % 3 is 2, not -1.

**Q6.6**

```python
a = np.array([1, 5, 3])
b = np.array([4, 2, 6])
print(np.maximum(a, b))
print(np.max(a))
```

`np.maximum` compares two arrays element by element; `np.max` reduces one array to a single value.

**Q6.7**

```python
x = np.array([1, 2, 3, 4, 5])
print(np.cumsum(x))
print(np.cumprod(x))
print(np.diff(x**2))
```

`diff` returns one fewer element: each value minus the one before it.

**Q6.8**

```python
print(0.1 + 0.2 == 0.3)
print(np.isclose(0.1 + 0.2, 0.3))
```

Floats are stored in binary, so 0.1 + 0.2 is 0.30000000000000004. Always compare floats with a tolerance.

**Q6.9**

```python
print(np.multiply.outer(np.arange(1, 5), np.arange(1, 6)))
print(np.add.reduce([1, 2, 3, 4]))
print(np.add.accumulate([1, 2, 3, 4]))
```

Every binary ufunc has `.reduce`, `.accumulate` and `.outer`. `np.sum` is really `np.add.reduce`.

**Q6.10**

```python
p = np.array([100, 105, 102, 110, 99])
print(np.round(np.diff(p) / p[:-1] * 100, 2))
```

Divide each difference by the *earlier* price, which is `p[:-1]`. Off-by-one slicing is the usual mistake here.

**Q6.11**

```python
with np.errstate(divide='ignore', invalid='ignore'):
    print(np.array([1.0, 0.0, -1.0]) / 0)
```

NumPy returns inf, nan and -inf instead of raising like plain Python. `errstate` controls the warnings.

**Q6.12**

```python
x = np.array([1.5, 2.5, 3.5, -1.5])
print(np.round(x))
print(np.floor(x))
print(np.ceil(x))
print(np.trunc(x))
```

`np.round` uses *round half to even* (banker's rounding): 2.5 → 2, 3.5 → 4. Students expect 3.

## Topic 7: Broadcasting

**Q7.1**

```python
col = np.array([[0], [10], [20]])
row = np.array([1, 2, 3, 4])
r = col + row
print(r)
print(r.shape)
```

(3,1) and (4,) → (3,4): each length-1 axis is stretched to match.

**Q7.2**

```python
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(M - M.mean(axis=0))
```

`M.mean(axis=0)` has shape (3,), which lines up with the last axis of M.

**Q7.3**

```python
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.round(M / M.sum(axis=1, keepdims=True), 3))
```

Row sums have shape (3,); without `keepdims=True` (giving (3,1)) they would line up with columns — a silent bug.

**Q7.4**

```python
pairs = [((3, 4), (4,)), ((3, 4), (3,)), ((3, 1), (1, 4)), ((2, 3, 4), (3, 1))]
for s1, s2 in pairs:
    try:
        print(s1, s2, '->', np.broadcast_shapes(s1, s2))
    except ValueError:
        print(s1, s2, '-> error')
```

(3,4)&(3,) fails because the last axes are 4 and 3. Fix it by reshaping the second to (3,1).

**Q7.5**

```python
n = np.arange(1, 6)
print(n[:, None] * n)
```

A column times a row gives every pairwise product.

**Q7.6**

```python
p = np.array([0, 3, 7, 10])
print(np.abs(p[:, None] - p[None, :]))
```

The same column-minus-row trick. The diagonal is 0 and the matrix is symmetric.

**Q7.7**

```python
pts = np.array([[0, 0], [3, 4], [6, 8]])
diff = pts[:, None, :] - pts[None, :, :]
print(np.round(np.sqrt((diff ** 2).sum(axis=-1)), 2))
```

Shapes: (3,1,2) − (1,3,2) → (3,3,2). Sum the squared differences over the last axis.

**Q7.8**

```python
D = np.array([[10, 200, 3], [20, 400, 9], [15, 300, 6]])
mn = D.min(axis=0)
mx = D.max(axis=0)
print(np.round((D - mn) / (mx - mn), 2))
```

Column statistics (axis=0) broadcast across rows automatically.

**Q7.9**

```python
qty = np.array([[2, 0, 5, 1], [4, 3, 0, 2], [1, 1, 1, 1]])
price = np.array([2.5, 10.0, 1.0, 4.0])
print((qty * price).sum(axis=1))
```

Shapes (3,4) × (4,) broadcast. Equivalent: `qty @ price`.

**Q7.10**

```python
print((np.ones((3, 4)) + np.ones((3,))[:, None]).shape)
```

Broadcasting aligns from the **right**: 4 vs 3 conflict. Turning (3,) into (3,1) aligns it with the rows.

## Topic 8: Aggregations and the axis argument

Every solution below assumes this setup has been run:

```python
sales = np.array([[120,  95, 130, 110],
                  [ 80, 105,  90, 125],
                  [150, 140, 160, 135]])  # rows = stores A, B, C; columns = Q1..Q4
```

**Q8.1**

```python
print(sales.sum())
print(sales.sum(axis=1))
print(sales.sum(axis=0))
```

Per store means 'across the columns', so axis=1.

**Q8.2**

```python
print(np.round(sales.mean(axis=1), 2))
print(np.round(sales.std(axis=0), 2))
```

`std` defaults to population std (ddof=0). Use `ddof=1` for the sample std.

**Q8.3**

```python
print(sales.argmax(axis=1))
print(sales.argmax(axis=0))
```

`argmax` returns positions, not values.

**Q8.4**

```python
print(sales.sum(axis=1).shape)
print(sales.sum(axis=1, keepdims=True).shape)
```

`keepdims=True` keeps the collapsed axis with length 1, which is ready for broadcasting back.

**Q8.5**

```python
print(np.median(sales))
print(np.percentile(sales, [25, 75]))
```

With no axis, statistics work on the flattened array.

**Q8.6**

```python
print(sales.cumsum(axis=1))
```

Cumulative functions keep the shape and accumulate along the axis.

**Q8.7**

```python
growth = sales[:, -1] - sales[:, 0]
i = growth.argmax()
print('ABC'[i], growth[i])
```

Slice the first and last columns, subtract, then argmax.

**Q8.8**

```python
print((sales > 100).sum(axis=1))
```

Summing a boolean mask along an axis counts per row.

**Q8.9**

```python
print(np.round(sales / sales.sum(axis=1, keepdims=True) * 100, 1))
```

This combines aggregation with broadcasting, the single most common NumPy pattern.

**Q8.10**

```python
a = np.arange(24).reshape(2, 3, 4)
print(a.sum(axis=0).shape)
print(a.sum(axis=(1, 2)))
```

You can collapse several axes at once with a tuple.

**Q8.11**

```python
print(np.average([70, 85, 90], weights=[0.2, 0.3, 0.5]))
```

`np.mean` has no weights; `np.average` does.

**Q8.12**

```python
i = np.unravel_index(sales.argmax(), sales.shape)
print(sales.max(), int(i[0]), int(i[1]))
```

Without an axis, `argmax` indexes the flattened array; `unravel_index` converts that back to (row, col).

## Topic 9: Sorting, searching and set operations

**Q9.1**

```python
x = np.array([5, 2, 9, 1, 7])
print(np.sort(x))
print(x)
x.sort()
print(x)
```

`np.sort` returns a sorted copy; the method `.sort()` sorts in place and returns None.

**Q9.2**

```python
names = np.array(['Ada', 'Ben', 'Cy', 'Di', 'Eve'])
scores = np.array([88, 92, 79, 95, 60])
order = np.argsort(scores)[::-1]
print(names[order])
```

`argsort` gives the positions that would sort the array; reverse it for descending, then use it to index the names.

**Q9.3**

```python
m = np.array([[3, 1, 2], [9, 7, 8], [6, 5, 4]])
print(np.sort(m, axis=0))
print(np.sort(m, axis=1))
```

axis=0 sorts each column independently; axis=1 (the default) sorts each row. Rows do not stay together.

**Q9.4**

```python
votes = np.array(['red', 'blue', 'red', 'green', 'blue', 'red'])
vals, counts = np.unique(votes, return_counts=True)
print(vals)
print(counts)
```

`np.unique` also sorts. `return_index` and `return_inverse` give more information.

**Q9.5**

```python
s = np.array([10, 20, 30, 40])
print(np.searchsorted(s, [25, 10, 45]))
```

`searchsorted` uses binary search; by default it returns the leftmost valid position.

**Q9.6**

```python
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7])
print(np.intersect1d(a, b))
print(np.union1d(a, b))
print(np.setdiff1d(a, b))
print(np.setxor1d(a, b))
print(np.isin(a, b))
```

`isin` returns a mask the same length as `a` — very handy for filtering.

**Q9.7**

```python
x = np.array([14, 3, 27, 8, 19, 30, 1])
print(np.sort(x)[-3:][::-1])
```

For huge arrays, `np.partition(x, -3)[-3:]` finds the top 3 without fully sorting.

**Q9.8**

```python
x = np.array([40, 10, 30, 20])
print(x.argsort().argsort())
```

`argsort` tells you which element goes in each position; argsorting that again tells you each element's position.

**Q9.9**

```python
m = np.array([[1, 9], [2, 3], [3, 7], [4, 1]])
print(m[m[:, 1].argsort()])
```

Argsort one column, then use the order to index whole rows, so rows stay together.

**Q9.10**

```python
ids = np.array([101, 102, 103, 104, 105])
cls = np.array([2, 1, 2, 1, 1])
score = np.array([70, 90, 85, 60, 75])
order = np.lexsort((score, cls))
print(ids[order])
```

`lexsort((secondary, primary))`: the last key is the primary sort key.

**Q9.11**

```python
x = np.array([4, 12, 18, 9, 21])
print(np.argmax(x > 15))
```

`argmax` returns the first True. Careful: if nothing is True it returns 0, so check `.any()` first.

## Topic 10: Copies vs views

**Q10.1**

```python
a = np.arange(5)
b = a[1:4]
b[0] = 99
print(a)
```

A slice is a view; changing it changes `a`.

**Q10.2**

```python
a = np.arange(5)
b = a[1:4].copy()
b[0] = 99
print(a)
```

`.copy()` makes independent memory.

**Q10.3**

```python
a = np.arange(5)
c = a[[1, 2, 3]]
c[0] = 99
print(a)
```

Fancy indexing always returns a copy.

**Q10.4**

```python
a = np.arange(12).reshape(3, 4)
for x in [a.reshape(4, 3), a.ravel(), a.flatten(), a.T, a[::2], a[a > 5]]:
    print(np.shares_memory(a, x))
```

`flatten` always copies; `ravel` returns a view when it can. Boolean indexing copies.

**Q10.5**

```python
a = np.array([1, 2, 3])
b = a
b[0] = 100
print(a)
print(b is a)
```

Plain assignment does not copy at all: both names point to the same object.

**Q10.6**

```python
a = np.arange(6)
b = a[1:4]
b[:] = b * 10
c = a[[0, 5]]
c[:] = -1
print(a)
```

`b` is a view, so its change lands in `a`; `c` is a copy, so its change does not.

**Q10.7**

```python
a = np.arange(6)
print(a[2:].base is a)
print(a[[2, 3]].base is a)
```

`.base` points at the array a view borrows its memory from; a copy owns its memory.

**Q10.8**

```python
a = np.arange(6)
a[a > 2] = 0
print(a)
a = np.arange(6)
b = a[a > 2]
b[:] = 0
print(a)
```

Indexed *assignment* writes into `a`. Indexing on the right-hand side creates a copy first.

**Q10.9**

```python
def inplace(x):
    x += 1

def rebind(x):
    x = x + 1

a = np.array([1, 2, 3])
inplace(a)
print(a)
a = np.array([1, 2, 3])
rebind(a)
print(a)
```

`+=` modifies the same array in place; `x = x + 1` builds a new array and only rebinds the local name.

## Topic 11: where, select, clip and NaN handling

**Q11.1**

```python
scores = np.array([45, 78, 50, 32, 91])
print(np.where(scores >= 50, 'pass', 'fail'))
```

`np.where(cond, if_true, if_false)` is a vectorized if/else.

**Q11.2**

```python
scores = np.array([45, 78, 50, 32, 91])
print(np.select([scores >= 80, scores >= 60], ['A', 'B'], default='C'))
```

Conditions are checked in order, so the first match wins. Nested `np.where` works but gets hard to read.

**Q11.3**

```python
v = np.array([-20, 5, 50, 130, 99])
print(np.clip(v, 0, 100))
```

Values below the lower bound become 0; above the upper become 100.

**Q11.4**

```python
arr = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
print(np.mean(arr))
print(np.nanmean(arr))
print(np.isnan(arr).sum())
```

Any NaN poisons a normal aggregate. The `nan*` versions skip them.

**Q11.5**

```python
print(np.nan == np.nan)
print(np.isnan(np.nan))
```

NaN is not equal to anything, including itself, so `== np.nan` never finds missing values.

**Q11.6**

```python
X = np.array([[1.0, np.nan, 3.0], [4.0, 5.0, np.nan], [7.0, 8.0, 9.0]])
col_means = np.nanmean(X, axis=0)
X2 = np.where(np.isnan(X), col_means, X)
print(X2)
```

`col_means` (shape (3,)) broadcasts across the rows inside `np.where`.

**Q11.7**

```python
X = np.array([[1.0, np.nan, 3.0], [4.0, 5.0, np.nan], [7.0, 8.0, 9.0]])
print(X[~np.isnan(X).any(axis=1)])
```

Build 'row has any NaN', invert it with `~`, use it as a row mask.

**Q11.8**

```python
bmi = np.array([17.2, 22.0, 27.5, 31.1, 24.9])
print(np.select([bmi < 18.5, bmi < 25, bmi < 30], ['under', 'normal', 'over'], default='obese'))
```

Ordered conditions mean you only need upper bounds.

**Q11.9**

```python
arr = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
print(np.nanmax(arr), np.nanmin(arr), np.nansum(arr))
print(np.nan_to_num(arr))
```

`nan_to_num` also replaces inf with very large finite numbers.

**Q11.10**

```python
a = np.array([1, 2, 3])
try:
    a[0] = np.nan
except ValueError as e:
    print(e)
b = a.astype(float)
b[0] = np.nan
print(b)
```

NaN is a floating-point value. Integer arrays have no slot for 'missing'.

## Topic 12: Random numbers

**Q12.1**

```python
rng = np.random.default_rng(42)
print(rng.integers(1, 7, size=10))
```

The upper bound of `integers` is exclusive, so use 7 for a die.

**Q12.2**

```python
rng = np.random.default_rng(42)
print(np.round(rng.random(5), 3))
```

`rng.random` samples uniformly from \[0, 1).

**Q12.3**

```python
rng = np.random.default_rng(42)
print(np.round(rng.normal(50, 10, size=5), 2))
```

`normal(loc, scale, size)`: loc is the mean, scale the standard deviation.

**Q12.4**

```python
names = np.array(['Ada', 'Ben', 'Cy', 'Di', 'Eve'])
rng = np.random.default_rng(42)
print(rng.choice(names, size=3, replace=False))
```

`replace=False` guarantees no repeats; also accepts `p=` for weighted choices.

**Q12.5**

```python
rng = np.random.default_rng(42)
print(rng.permutation(8))
```

`permutation` returns a shuffled copy; `rng.shuffle(arr)` shuffles in place.

**Q12.6**

```python
r1 = np.random.default_rng(7)
r2 = np.random.default_rng(7)
print(np.array_equal(r1.random(3), r2.random(3)))
```

Same seed → same stream. That is what makes experiments reproducible.

**Q12.7**

```python
rng = np.random.default_rng(0)
flips = rng.integers(0, 2, size=10_000)
print(round(flips.mean(), 3))
```

The mean of 0/1 values is the proportion of 1s. It should be close to 0.5.

**Q12.8**

```python
rng = np.random.default_rng(1)
pts = rng.random((100_000, 2))
inside = (pts ** 2).sum(axis=1) <= 1
print(round(4 * inside.mean(), 3))
```

A classic Monte Carlo exercise: the quarter-circle area is π/4.

**Q12.9**

```python
rng = np.random.default_rng(3)
totals = rng.integers(1, 7, size=(10_000, 2)).sum(axis=1)
vals, counts = np.unique(totals, return_counts=True)
print(vals[counts.argmax()], counts.max())
```

Generate a (10000, 2) array in one go, sum across axis 1, then count. The answer should be 7.

**Q12.10**

```python
rng = np.random.default_rng(5)
print(rng.integers(10, 100, size=(3, 4)))
```

`size` can be a tuple for multi-dimensional results.

## Topic 13: Linear algebra

Every solution below assumes this setup has been run:

```python
A = np.array([[2, 1], [1, 3]])
B = np.array([[1, 2], [3, 4]])
```

**Q13.1**

```python
print(A @ B)
print(A * B)
```

`@` is matrix multiplication (rows × columns); `*` multiplies matching elements.

**Q13.2**

```python
print(B.T)
print(np.trace(B))
print(round(np.linalg.det(B), 2))
```

det(B) = 1×4 − 2×3 = −2. The float result is slightly off, hence the rounding.

**Q13.3**

```python
Ainv = np.linalg.inv(A)
print(np.round(Ainv, 3))
print(np.allclose(A @ Ainv, np.eye(2)))
```

Never test float matrices with `==`; use `allclose`.

**Q13.4**

```python
x = np.linalg.solve(A, np.array([5, 10]))
print(x)
```

`solve` is faster and more accurate than `inv(A) @ b`. Note the coefficient matrix is exactly `A`.

**Q13.5**

```python
u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
print(np.dot(u, v))
print(round(np.linalg.norm(u), 3))
print(np.cross(u, v))
```

dot = 1·4 + 2·5 + 3·6 = 32. norm = √14.

**Q13.6**

```python
w, vecs = np.linalg.eig(np.array([[4, 1], [2, 3]]))
print(np.round(np.sort(w.real), 2))
```

`eig` returns eigenvalues and eigenvectors (as columns). The order isn't guaranteed, so sort. This NumPy version may return them as complex numbers (`5.+0.j`); `.real` keeps the real part. For symmetric matrices use `np.linalg.eigh`, which always returns real values.

**Q13.7**

```python
F = np.linalg.matrix_power(np.array([[1, 1], [1, 0]]), 10)
print(F)
print(F[0, 1])
```

`A ** 10` would raise each element to the 10th power — not the same thing.

**Q13.8**

```python
x = np.array([0, 1, 2, 3, 4], dtype=float)
y = np.array([1.1, 2.9, 5.2, 7.1, 8.8])
X = np.column_stack((x, np.ones_like(x)))
(m, c), *_ = np.linalg.lstsq(X, y)
print(round(m, 3), round(c, 3))
```

Build a design matrix with a column of ones for the intercept. `np.polyfit(x, y, 1)` gives the same answer.

**Q13.9**

```python
print(np.linalg.matrix_rank(np.array([[1, 2, 3], [2, 4, 6], [1, 0, 1]])))
```

Row 2 is exactly 2 × row 1, so only two rows are independent.

**Q13.10**

```python
M = np.array([[1, 1, 1], [0, 2, 5], [2, 5, -1]])
b = np.array([6, -4, 27])
print(np.linalg.solve(M, b))
```

Each equation is a row of coefficients. The answer is x = 5, y = 3, z = −2.

## Topic 14: Saving and loading

**Q14.1**

```python
a = np.arange(10)
np.save('data.npy', a)
b = np.load('data.npy')
print(np.array_equal(a, b))
```

`.npy` keeps dtype and shape exactly. `np.save` adds the extension if you leave it off.

**Q14.2**

```python
np.savez('bundle.npz', x=np.arange(3), y=np.ones((2, 2)))
z = np.load('bundle.npz')
print(sorted(z.files))
print(z['y'])
```

An `.npz` file behaves like a dictionary of arrays. Use `savez_compressed` for big data.

**Q14.3**

```python
marks = np.array([[70, 65], [88, 92], [54, 61]])
np.savetxt('marks.csv', marks, delimiter=',', fmt='%d', header='math,physics', comments='')
with open('marks.csv') as f:
    print(f.read())
```

`comments=''` stops NumPy putting ` #  ` in front of the header line.

**Q14.4**

```python
m = np.loadtxt('marks.csv', delimiter=',', skiprows=1)
print(m)
print(m.mean(axis=0))
```

`loadtxt` gives floats by default. Use `dtype=int` if you need integers.

**Q14.5**

```python
text = 'a,b,c\n1,2,3\n4,,6\n7,8,\n'
with open('gaps.csv', 'w') as f:
    f.write(text)
g = np.genfromtxt('gaps.csv', delimiter=',', skip_header=1)
print(g)
print(np.round(np.nanmean(g, axis=0), 2))
```

`loadtxt` would crash on the blanks; `genfromtxt` fills them with NaN.

## Topic 15: Mixed challenge problems

**Q15.1**

```python
p = np.array([10, 12, 11, 15, 18, 17, 20])
print(np.round(np.convolve(p, np.ones(3) / 3, mode='valid'), 2))
```

`mode='valid'` keeps only windows that fit fully, giving len(p) − 2 values. Alternative: `np.lib.stride_tricks.sliding_window_view(p, 3).mean(axis=1)`.

**Q15.2**

```python
x = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
c = np.bincount(x)
print(c.argmax(), c.max())
```

`bincount` counts each non-negative integer. It only works for non-negative ints; use `np.unique` otherwise.

**Q15.3**

```python
Z = np.arange(1, 10).reshape(3, 3)
print(np.round((Z - Z.mean()) / Z.std(), 2))
```

The result has mean 0 and standard deviation 1.

**Q15.4**

```python
R = np.array([[3, 8, 1], [7, 2, 9], [4, 6, 5]])
R2 = R.copy()
R2[np.arange(len(R2)), R2.argmax(axis=1)] = 0
print(R2)
```

Pair each row index with that row's argmax column using fancy indexing.

**Q15.5**

```python
x = np.array([1.5, 4.0, 6.0, 7.2, 9.9])
print(x[np.abs(x - 6.3).argmin()])
```

Absolute difference, then argmin.

**Q15.6**

```python
labels = np.array([2, 0, 1, 2])
print(np.eye(3, dtype=int)[labels])
```

Each row of the identity matrix is a one-hot vector; fancy indexing picks the right one per label.

**Q15.7**

```python
img = np.arange(16).reshape(4, 4)
print(img.reshape(2, 2, 2, 2).mean(axis=(1, 3)))
```

Reshape to (block\_row, row\_in\_block, block\_col, col\_in\_block), then average over the two inner axes. This is 'average pooling'.

**Q15.8**

```python
x = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(np.maximum.accumulate(x))
```

Any binary ufunc can `accumulate`.

**Q15.9**

```python
S = np.arange(9).reshape(3, 3)
S[[0, 2]] = S[[2, 0]]
print(S)
```

The right side is a copy, so there's no overwrite problem. The Python-style swap `S[0], S[2] = S[2], S[0]` goes wrong: the right side holds views, so both rows end up as `[6 7 8]`.

**Q15.10**

```python
G = np.array([[55, 70, 62], [90, 85, 95], [40, 58, 61], [72, 66, 80]])
w = np.array([0.3, 0.3, 0.4])
final = G @ w
print(final)
print(final >= 60)
print(np.argsort(final)[::-1])
```

A weighted sum per row is a matrix–vector product.

**Q15.11**

```python
d0 = np.datetime64('2026-10-29')
print(np.datetime64('2026-12-25') - d0)
print(np.arange(d0, d0 + np.timedelta64(7, 'D')))
```

`datetime64` supports subtraction (giving `timedelta64`) and `arange`.

**Q15.12**

```python
inc = np.array([8_000, 25_000, 40_000, 75_000])
tax = 0.10 * np.clip(inc - 10_000, 0, 30_000) + 0.20 * np.clip(inc - 40_000, 0, None)
print(tax)
```

`clip` measures how much of each income falls in each band.

**Q15.13**

```python
s = np.array([3, 5, -2, -4, 6, 1, -7])
print(np.count_nonzero(np.diff(np.sign(s))))
```

Take the sign of each value, then count where consecutive signs differ.

**Q15.14**

```python
grid = np.arange(25).reshape(5, 5)
print(grid[1:4, 1:4].sum() - grid[2, 2])
```

Take the 3×3 window around the cell and subtract the cell itself. This is the core of Conway's Game of Life.

**Q15.15**

```python
V = np.array([[3.0, 4.0], [1.0, 1.0], [0.0, 2.0]])
U = V / np.linalg.norm(V, axis=1, keepdims=True)
print(np.round(U, 3))
print(np.linalg.norm(U, axis=1))
```

`norm(..., axis=1, keepdims=True)` returns a (n,1) column that broadcasts over each row.
