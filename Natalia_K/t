# Pandas Deep Dive — Columns, Rows, Filtering & Aggregation

This note covers things people *think* are simple in pandas — adding a column, adding a row, filtering data, aggregating it — but which are actually full of sharp edges. Every example below was run against **pandas 3.0** to confirm current behavior (some old StackOverflow advice is now flat-out broken).

---

## Part 1: Adding a Column

### Method 1 — Direct assignment (`df['col'] = ...`)

This is the bracket-assignment method. It's the most common way and it's fine *most* of the time.

```python
import pandas as pd

df = pd.DataFrame({'name': ['Ada', 'Linus'], 'age': [36, 55]})

df['country'] = ['UK', 'Finland']   # new column, list of matching length
df['active'] = True                 # scalar broadcasts to every row
df['age_plus_10'] = df['age'] + 10  # derived from existing column
```

**Nuance #1 — length must match exactly, or be a scalar.**

```python
df['x'] = [1, 2]   # ValueError: Length of values (2) does not match length of index (3)
```

If your list is shorter or longer than the DataFrame, pandas raises `ValueError: Length of values (N) does not match length of index (M)`. It will **not** silently pad or truncate. A scalar (`df['x'] = 7`) is the one exception — that broadcasts to all rows.

**Nuance #2 — order of operations with brand-new columns.**

```python
df['bonus'] = df['age'] * 0.1   # fine — 'age' already exists
df['total'] = df['salary'] + df['bonus']  # KeyError if 'salary' doesn't exist yet
```

You can't reference a column on the right-hand side that doesn't exist yet. Obvious once you say it, but it's a very common copy-paste mistake when reordering cells in a notebook.

**Nuance #3 — this method *mutates the DataFrame in place*.**
Unlike `.assign()` (below), `df['col'] = ...` modifies `df` directly. There is no "new object" returned. This matters a lot if `df` is something you got as a slice or view of another DataFrame — more on that in the "Chained Assignment" landmine section.

---

### Method 2 — `.assign()`

```python
df2 = df.assign(age_squared=lambda d: d['age'] ** 2)
```

`.assign()` returns a **new** DataFrame and leaves the original untouched. I verified this directly:

```python
df2 = pd.DataFrame({'x': [1, 2, 3]})
df3 = df2.assign(y=lambda d: d['x'] * 2)
# df2 is STILL just column x. df3 has x and y.
```

**Why use this over bracket assignment?**
- It's chainable: `df.assign(a=...).assign(b=...).query('a > 5')` reads nicely in a pipeline.
- It avoids mutating shared state — valuable if other code holds a reference to the same DataFrame and you don't want side effects.
- The lambda form (`lambda d: ...`) lets you reference a column you're creating *in the same call* in a later kwarg, in left-to-right order, which bracket assignment can't do in one line.

**The catch:** you must use `=` keyword arguments, so the new column name has to be a valid Python identifier. `df.assign(my-column=...)` is a `SyntaxError`. If you need a name with spaces or dashes, you're back to `df['my column'] = ...`.

---

### Method 3 — `.insert()` — controlling *where* the column goes

Both methods above always tack the new column onto the far right. If you need it at a specific position:

```python
df = pd.DataFrame({'a': [1, 2], 'c': [3, 4]})
df.insert(1, 'b', [99, 100])   # args: position, column name, values
```

Result:
```
   a    b  c
0  1   99  3
1  2  100  4
```

**Nuance — `.insert()` mutates in place and returns `None`.** This trips people up constantly:

```python
df = df.insert(1, 'b', [99, 100])   # WRONG — df is now None!
```

Don't assign the result. Just call it as a statement.

**Nuance — duplicate column names are blocked by default.**

```python
df.insert(1, 'a', [1, 1])
# ValueError: cannot insert a, already exists
```

I confirmed this raises a `ValueError`. There's an `allow_duplicates=True` parameter if you genuinely want two columns with the same name (rare, and usually a sign something else has gone wrong upstream — duplicate column names make later selection ambiguous, since `df['a']` would return a DataFrame instead of a Series).

---

### Method 4 — `pd.concat(axis=1)` for adding multiple columns from another DataFrame

```python
extra = pd.DataFrame({'city': ['London', 'Helsinki'], 'verified': [True, False]})
combined = pd.concat([df, extra], axis=1)
```

This is the right tool when you're merging in *several* columns at once from a separate DataFrame, rather than building them one at a time. The critical thing to get right is the **index alignment** — `concat(axis=1)` lines rows up by index label, not by position. If `df` and `extra` have different indexes, you'll get `NaN`s where they don't match, even if both have "the same number of rows." Reset both indexes (`.reset_index(drop=True)`) first if you're not certain they're aligned.

---

### The Landmine: Chained Assignment and Copy-on-Write

This is the single most misunderstood area of adding columns, and it changed meaningfully in pandas 2.x → 3.0.

The old, infamous warning was `SettingWithCopyWarning`, triggered by code like:

```python
subset = df[df['age'] > 40]
subset['flag'] = True   # used to warn: "you might be modifying a view, not a copy"
```

The ambiguity was always: is `subset` a *view* into `df`'s memory, or an independent *copy*? If it was a view, your assignment would silently change the original `df` too — a classic source of "spooky action at a distance" bugs.

**As of pandas 3.0, Copy-on-Write (CoW) is the default and permanent behavior.** I tested this directly:

```python
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
sub = df[df['a'] > 1]
sub['c'] = 99          # no warning, no error
```

Result: `sub` gets the new column `c`. The original `df` is **completely unaffected** — confirmed by printing it afterward, still just columns `a` and `b`. Under the hood, `sub` now behaves as if it always was an independent copy; any write to it triggers an actual physical copy at that moment rather than mutating shared memory.

**What this means practically:**
- The old `SettingWithCopyWarning` panic is mostly gone, because the ambiguous "did I just silently corrupt my original data?" scenario can no longer happen.
- **But** don't treat this as permission to write sloppy chained code. `subset['flag'] = True` still only ever affects `subset`. If your actual intent was to flag those rows back in the original `df`, CoW means it silently *won't* — you get no error, just a result that quietly isn't what you expected. The bug changed shape: it used to be "I might be accidentally mutating the original," now it's "I assumed I was mutating the original, but I wasn't."
- The fix is the same as it's always been: be explicit. If you want to modify rows of the original, use `.loc` on the original directly:
  ```python
  df.loc[df['age'] > 40, 'flag'] = True
  ```
  This is correct in every pandas version, CoW or not, because there's no intermediate object — you're addressing `df` itself.

---

## Part 2: Adding a Row

This is where things get genuinely more involved, because pandas removed the method most tutorials used to teach.

### `.append()` is gone. Not deprecated — removed.

```python
df.append({'a': 3, 'b': 4}, ignore_index=True)
```

I ran this against pandas 3.0 and got:

```
AttributeError: 'DataFrame' object has no attribute 'append'
```

If you're following any tutorial, course, or old StackOverflow answer that uses `.append()` for rows, it is **outdated and will crash** on any reasonably current pandas install. This is the single most common "why doesn't my code work" issue for people learning from older material. `.append()` was deprecated back in pandas 1.4 and was fully removed by pandas 2.0. There is no flag to bring it back — you must switch methods.

The reason it was removed isn't arbitrary: row-by-row `.append()` in a loop is **O(n²)** — every call reallocates and copies the entire underlying array, because DataFrames are column-oriented and not built for incremental row growth. People used it in loops anyway, got terrible performance on anything beyond a few hundred rows, and didn't understand why. Removing it forces a better pattern.

---

### Method 1 — `pd.concat()` (the current standard way)

```python
df = pd.DataFrame({'a': [1], 'b': [2]})
new_row = pd.DataFrame({'a': [3], 'b': [4]})
df = pd.concat([df, new_row], ignore_index=True)
```

**Critical detail: the new row must be wrapped as a DataFrame, not a plain dict**, and it must be a *list of one row*, i.e. `{'a': [3]}` not `{'a': 3}`. If you write `pd.DataFrame({'a': 3, 'b': 4})` without the list brackets, pandas raises an error because it doesn't know how many rows you mean.

**`ignore_index=True` is almost always what you want.** Without it:

```python
df = pd.concat([df, new_row])   # no ignore_index
```

both rows will independently carry index `0` (since `new_row` was created fresh with its own default index), giving you a DataFrame with a **duplicate index**. This doesn't error — pandas allows duplicate index labels — but it will absolutely bite you the next time you do `df.loc[0]`, because that now returns *two* rows instead of one, and any code expecting a single Series back will break in a confusing way three steps later, far from where the actual mistake was made.

**Performance nuance:** `pd.concat()` in a loop has the *exact same* O(n²) problem `.append()` had — each call still copies everything. If you're adding many rows, the correct pattern is:

```python
rows = []
for item in source_data:
    rows.append({'a': item.a, 'b': item.b})   # plain list of dicts, cheap
df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)  # ONE concat at the end
```

Collect everything in a plain Python list first (cheap — Python lists grow efficiently), then build the DataFrame and concat **once**. This is the most common mistake people carry over from `.append()`-style thinking: they replace `df.append(...)` with `df = pd.concat([df, ...])` inside the same loop, which "works" but keeps the same quadratic blowup the removal was meant to discourage.

---

### Method 2 — `.loc[]` for adding a single row by label

```python
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]}, index=['x', 'y'])
df.loc['z'] = [5, 6]
```

This appends a new row at label `'z'`. I confirmed it works cleanly when `'z'` doesn't already exist.

**The landmine:** if the label *does* already exist, `.loc[]` doesn't add a row — it **overwrites** the existing one.

```python
df.loc['x'] = [100, 200]   # 'x' already existed -> original row x is replaced, not duplicated
```

Confirmed directly: the row at index `'x'` silently changes from `[1, 3]` to `[100, 200]`; no new row appears, no warning is raised. If you're adding rows in a loop using `df.loc[i] = ...` with an integer counter `i`, and that counter ever repeats or resets, you will silently overwrite data instead of appending it. This is an easy bug to introduce when refactoring a loop and forgetting to carry the counter across iterations.

If you want to *guarantee* a new row regardless of existing labels, the safe pattern is:

```python
df.loc[len(df)] = [5, 6]
```

`len(df)` as the next integer label only works cleanly if your DataFrame has a clean default `0..n-1` RangeIndex with no gaps or duplicates. If you've previously deleted rows or done custom indexing, `len(df)` is not guaranteed to be an index value that doesn't already exist — verify with `.reset_index(drop=True)` first if you're unsure.

---

### Method 3 — Inserting a row in the *middle* (not at the end)

Neither `.loc[]` nor `pd.concat()` directly inserts "between" two existing rows — they both append. To genuinely insert at a specific position, you slice and reassemble:

```python
df = pd.DataFrame({'a': [1, 2, 4, 5], 'b': ['w', 'x', 'z', 'y']})

new_row = pd.DataFrame({'a': [3], 'b': ['y']})
top = df.iloc[:2]      # rows before the insertion point
bottom = df.iloc[2:]   # rows from the insertion point onward
result = pd.concat([top, new_row, bottom], ignore_index=True)
```

I verified this produces the correctly ordered result with the new row sitting exactly between index 1 and what was index 2. This slice-concat-slice pattern is the standard way to do positional row insertion — there's no single built-in "insert row at position N" method the way `.insert()` exists for columns. That asymmetry surprises people: pandas has a clean column-insert-at-position method but no equivalent for rows, precisely because rows are expensive to insert mid-structure in a column-oriented data layout.

There's an older "hack" floating around using fractional index values (`df.loc[1.5] = [...]` then `.sort_index()`), which does work — I tested it and it produces the correct order — but it's fragile (relies on float index labels, needs an explicit re-sort and `reset_index` afterward) and most pandas style guides now consider the slice-concat approach clearer and less surprising to the next person reading the code.

---

## Part 3: Filtering

Filtering in pandas means producing a smaller DataFrame based on a condition. There are several mechanisms, and the differences between them matter more than they first appear.

### Method 1 — Boolean masking (the fundamental mechanism)

```python
df = pd.DataFrame({
    'name': ['Ada', 'Linus', 'Grace', 'Alan'],
    'age':  [36, 55, 85, 41],
    'dept': ['eng', 'eng', 'math', 'math']
})

older = df[df['age'] > 40]
```

`df['age'] > 40` doesn't return filtered rows — it returns a **Series of booleans**, the same length as `df`, aligned by index. `df[that_series]` then keeps only the rows where the boolean is `True`. Every other filtering method in pandas is really just generating this boolean mask for you in a more convenient syntax. Understanding this is the key to debugging *any* filtering problem, because you can always drop back to inspecting the raw mask:

```python
mask = df['age'] > 40
print(mask)   # see exactly which rows are True/False before applying it
```

### Method 2 — `.query()` — readable string-based filtering

```python
df.query('age > 40 and dept == "eng"')
```

This reads closer to SQL and avoids repeating `df[...]` for every condition. Two specific things make `.query()` genuinely useful rather than just cosmetic:

**Referencing external variables with `@`:**
```python
min_age = 45
df.query('age > @min_age')
```
I confirmed this works correctly — without the `@`, pandas would look for a *column* named `min_age` and raise an error, since `.query()` parses its string in its own namespace where bare names mean column names by default.

**Column names with spaces:** `.query()` lets you wrap them in backticks — `` df.query('`first name` == "Ada"') `` — which bracket-indexing handles naturally anyway, so this advantage mostly matters for readability in long chained conditions, not capability.

### Method 3 — `.loc[]` with boolean conditions (and the callable trick)

```python
df.loc[df['age'] > 40]                       # same as df[df['age'] > 40]
df.loc[df['age'] > 40, ['name', 'salary']]    # filter rows AND select columns at once
```

The second form is the real reason to reach for `.loc` over plain bracket filtering — it lets you filter rows and pick columns in one expression instead of two.

**The callable trick**, useful inside a method chain where you don't have a variable name for the DataFrame yet:
```python
df.loc[lambda d: d['salary'] > 100]
```
I verified this works — `.loc` accepts a function that receives the DataFrame and returns a boolean mask, which means you can filter mid-chain (e.g. `df.assign(x=...).loc[lambda d: d['x'] > 0].reset_index(drop=True)`) without breaking the chain to introduce a temporary variable.

### Method 4 — `.isin()`, `.between()`, and negation

```python
df[df['dept'].isin(['eng', 'sales'])]   # membership test against a list
df[df['age'].between(40, 60)]           # inclusive range, both ends by default
df[~(df['dept'] == 'eng')]              # ~ negates the whole mask
```

`.isin()` is the right tool the moment you're checking membership against more than one or two values — it's far more readable than chaining `==` with `|`.

### The Landmine: Operator Precedence in Combined Conditions

This is the single most common filtering bug for people coming from SQL or general Python:

```python
df[df['age'] > 40 & df['dept'] == 'eng']
```

I ran this exact line and got:
```
TypeError: unsupported operand type(s) for &: 'int' and 'StringArray'
```

The problem is that Python's `&` operator binds **tighter** than `>` and `==`. So this actually gets parsed as `df['age'] > (40 & df['dept']) == 'eng'`, which is nonsense — pandas tries to bitwise-AND the integer `40` with a column of strings before the comparisons even happen, and blows up immediately.

**You must wrap every individual condition in parentheses** when combining with `&` (and) or `|` (or):

```python
df[(df['age'] > 40) & (df['dept'] == 'eng')]
```

This is non-negotiable boilerplate in pandas — unlike plain Python `and`/`or`, you can't skip the parens here, because `&`/`|` are the *elementwise* (NumPy-style) operators, not the short-circuit boolean ones. Plain `and`/`or` don't work at all on Series (`ValueError: The truth value of a Series is ambiguous`), which is precisely why pandas overloads `&`/`|` for this purpose in the first place — and why the parens become mandatory: operator precedence on these is different from what English-reading intuition expects.

`.query()` sidesteps this entirely — `df.query('age > 40 and dept == "eng"')` works with plain `and`, because `.query()` parses the string with its own evaluator that respects normal logical precedence. That's a real, practical reason to prefer `.query()` for multi-condition filters, beyond just readability.

---

## Part 4: Aggregation

Aggregation means collapsing groups of rows down to summary values. The core tool is `.groupby()`, and the depth here is almost entirely in what you do *after* the groupby.

### The basic shape

```python
df = pd.DataFrame({
    'dept':   ['eng', 'eng', 'math', 'math', 'eng'],
    'name':   ['Ada', 'Linus', 'Grace', 'Alan', 'Tim'],
    'age':    [36, 55, 85, 41, 50],
    'salary': [100, 120, 90, 95, 110]
})

df.groupby('dept')['salary'].mean()
```

`df.groupby('dept')` on its own doesn't compute anything — it returns a `DataFrameGroupBy` object, a lazy grouping plan. Nothing is calculated until you call an aggregation method on it (`.mean()`, `.sum()`, `.agg()`, etc.). This matters because `df.groupby('dept')` is cheap to create and reuse for multiple different aggregations without recomputing the grouping itself.

**Nuance — single-bracket vs double-bracket column selection changes the return type.**
```python
df.groupby('dept')['salary']        # SeriesGroupBy -> aggregations return a Series
df.groupby('dept')[['salary']]      # DataFrameGroupBy -> aggregations return a DataFrame
```
I confirmed `df.groupby('dept').salary` (attribute access, no brackets at all) is equivalent to the single-bracket form and also returns a `SeriesGroupBy`. Pick based on what shape you want downstream — a Series is easier to chain into `.reset_index()` for a tidy two-column result; a DataFrame is what you want if you're about to add more aggregated columns next to it.

### Multiple aggregations: `.agg()` with a dict, and named aggregation

```python
df.groupby('dept').agg({'salary': 'mean', 'age': 'max'})
```

This is fine for quick work but has one real weakness: if you aggregate the *same* column two different ways (e.g. both mean and max of `salary`), the dict form can't express that — a dict key can only map to one value.

**Named aggregation** solves this and is the more modern, more readable pattern:

```python
df.groupby('dept').agg(
    avg_salary=('salary', 'mean'),
    max_salary=('salary', 'max'),
    max_age=('age', 'max')
)
```

Each keyword becomes a clean output column name, and you can hit the same source column as many times as you like with different functions. I verified this produces correctly labeled columns (`avg_salary`, `max_age`, etc.) directly — no renaming step needed afterward, which the dict-based form often requires since it inherits the original column names.

**`as_index=False`** — by default the grouping column becomes the index of the result, which is awkward if you immediately want to treat the result as a flat table (e.g. to plot it or merge it back with something else):

```python
df.groupby('dept', as_index=False)['salary'].mean()
```

This keeps `dept` as a normal column instead of promoting it to the index — equivalent to chaining `.reset_index()` afterward, just in one step.

### Aggregating into a list — a common "advanced" need

A frequent real-world ask: collapse each group's values into a Python list rather than a single number.

```python
df.groupby('dept')['name'].agg(list)
```

```
dept
eng     [Ada, Linus, Tim]
math        [Grace, Alan]
```

I confirmed `list` (the built-in, passed bare — not `'list'` as a string) works directly as an aggregation function, and it composes with everything else `.agg()` supports:

```python
df.groupby('dept').agg(names=('name', list), avg_salary=('salary', 'mean'))
```

This gives you a list-of-names column sitting right next to a numeric aggregation in the same call — useful for building summary tables where one column needs "show me everyone" and another needs "show me the average."

### `transform` vs `apply` vs `agg` vs `filter` — the part people genuinely confuse

These four look similar but return fundamentally different shapes, and mixing them up is the most common groupby mistake once someone is past the basics.

| Method | Output shape | Typical use |
|---|---|---|
| `.agg()` | One row per group | Summary statistics |
| `.transform()` | Same number of rows as the **original** DataFrame | Broadcasting a group statistic back onto every row of that group |
| `.apply()` | Depends on what the function returns — flexible but slower | Custom logic that doesn't fit a simple agg |
| `.filter()` | Subset of the **original rows**, groups either kept whole or dropped whole | Keep/drop entire groups based on a group-level condition |

**`.transform()` in action** — adding each row's department average right alongside its own row, without collapsing anything:
```python
df['dept_avg_salary'] = df.groupby('dept')['salary'].transform('mean')
```
I confirmed this produces a column the same length as `df`, where every `eng` row shows `110.0` and every `math` row shows `92.5` — the group statistic is broadcast back, row for row. This is the standard way to compare an individual row against its group's average (e.g. "how far above/below the department average is this person's salary") without doing a separate groupby-then-merge.

**`.filter()` in action** — keeping or dropping entire groups based on a group-level test:
```python
df.groupby('dept').filter(lambda x: x['salary'].mean() > 100)
```
I confirmed this returns only the rows belonging to departments whose *average* salary exceeds 100 — here, all the `eng` rows survive and all the `math` rows are dropped, because it's evaluated per-group, not per-row. This is genuinely different from `df[df['salary'] > 100]`, which would evaluate row by row and could keep some rows from a "low" department and drop some from a "high" one.

**`.apply()` is the flexible fallback**, and also the slowest — it calls your function once per group and pandas tries to figure out how to stitch the results back together based on what you returned:
```python
df.groupby('dept')['salary'].apply(lambda x: x.max() - x.min())
```
This returns one value per group (range of salaries), so here it behaves like `.agg()` would. The danger is that `.apply()`'s output shape is inferred dynamically — if your function sometimes returns a scalar and sometimes returns a Series depending on the group's data, you can get an inconsistent, hard-to-predict result shape. If a built-in or a simple `.agg()`/`.transform()` can do the job, prefer it — reserve `.apply()` for logic that genuinely can't be expressed as one of the others.

### Multi-column groupby and reshaping with `.unstack()`

```python
df2 = pd.DataFrame({
    'dept':  ['eng', 'eng', 'math', 'math'],
    'level': ['jr', 'sr', 'jr', 'sr'],
    'salary':[80, 120, 70, 110]
})

df2.groupby(['dept', 'level'])['salary'].mean()
```

Grouping by a list of columns produces a result indexed by a **MultiIndex** — a tuple-like index combining `dept` and `level`. This is correct but often not the shape you actually want to look at or export. `.unstack()` pivots the innermost index level into columns:

```python
df2.groupby(['dept', 'level'])['salary'].mean().unstack()
```

```
level    jr     sr
dept
eng    80.0  120.0
math   70.0  110.0
```

I confirmed this transformation directly — it's functionally equivalent to using `.pivot_table()` with `index='dept', columns='level', values='salary'`, just arrived at via groupby instead. Knowing both paths matters because `.unstack()` is the natural next step when you're *already* mid-chain on a groupby result, whereas `.pivot_table()` is more direct when you're starting fresh from the raw DataFrame.

### `.pivot_table()` with multiple aggregation functions at once

```python
df.pivot_table(index='dept', values='salary', aggfunc=['mean', 'sum', 'count'])
```

I confirmed passing a *list* to `aggfunc` produces a result with multi-level columns — one top level per function (`mean`, `sum`, `count`), each containing the aggregated `salary` values. This is a fast way to get several summary angles on the same column without writing three separate `.groupby()` calls.

### The Landmine: `NaN` Group Keys Are Silently Dropped

This is the most dangerous aggregation bug in this entire note, because it produces **no error and no warning** — it just quietly loses data.

```python
df = pd.DataFrame({'dept': ['eng', 'eng', np.nan, 'math'], 'salary': [100, 120, 90, 95]})
df.groupby('dept')['salary'].sum()
```

```
dept
eng     220
math     95
```

Look closely: the original DataFrame has **4 rows** totaling `100 + 120 + 90 + 95 = 405`, but the groupby result only sums to `315`. The row where `dept` is `NaN` simply vanished — by default, **pandas excludes any row whose group key is `NaN` from the grouping entirely**, with zero indication that anything was dropped.

I confirmed the fix is the `dropna=False` parameter:
```python
df.groupby('dept', dropna=False)['salary'].sum()
```
```
dept
eng     220
math     95
NaN      90
```

Now the missing row shows up as its own `NaN` group, and the totals reconcile. **Whenever you're aggregating real-world data with any chance of missing values in the grouping column(s), get in the habit of checking `df['col'].isna().sum()` before you groupby, or just default to `dropna=False` and consciously decide whether to drop the `NaN` group afterward** — rather than letting pandas make that decision for you silently. This single default has caused more quietly-wrong dashboards and reports than almost any other pandas behavior, precisely because the code runs without complaint and the numbers just look "a little off" instead of obviously broken.

---

## Quick Reference Table

| Goal | Use | Avoid |
|---|---|---|
| Add one column, simple case | `df['col'] = values` | — |
| Add column without mutating original | `df.assign(col=...)` | — |
| Add column at a specific position | `df.insert(pos, 'col', values)` | Assigning its return value (`None`) |
| Add several columns from another DataFrame | `pd.concat([df1, df2], axis=1)` | Assuming positional alignment — it's index-based |
| Add one row at the end | `pd.concat([df, new_row_df], ignore_index=True)` | `.append()` — **removed**, will raise `AttributeError` |
| Add one row by a known new label | `df.loc[new_label] = [...]` | Reusing a label that already exists (silently overwrites) |
| Add many rows efficiently | Collect as list of dicts → one `pd.DataFrame()` → one `concat` | Calling `concat`/`append` inside the loop itself |
| Insert a row mid-DataFrame | Slice with `.iloc[]`, concat three pieces, `ignore_index=True` | Expecting an `.insert()`-style method for rows — none exists |
| Filter rows on one condition | `df[df['col'] > x]` or `df.query('col > x')` | — |
| Filter rows on multiple conditions | `df[(cond1) & (cond2)]` — **parens mandatory** | Bare `&`/`|` without parentheses; plain `and`/`or` on a Series |
| Filter with an external variable | `df.query('col > @my_var')` | Forgetting the `@`, which pandas reads as a column name |
| Filter mid-chain without a variable name | `df.loc[lambda d: d['col'] > x]` | — |
| Membership test against several values | `df[df['col'].isin([...])]` | Chains of `\|`-joined `==` comparisons |
| One summary value per group | `.groupby(...).agg(...)` or named agg | — |
| Broadcast a group stat back onto every row | `.groupby(...).transform(...)` | Manually merging a groupby result back onto the original |
| Keep/drop whole groups by a group-level test | `.groupby(...).filter(...)` | Row-level filtering when you actually meant group-level |
| Collapse a group's values into a list | `.groupby(...).agg(list)` | — |
| Aggregating data with missing group keys | `.groupby(..., dropna=False)` | Trusting the default — it silently drops `NaN` groups |

---

## The Core Mental Model

Everything above comes down to one underlying fact: **pandas DataFrames are stored column-by-column internally (built on NumPy arrays per column), not row-by-row.** This explains nearly every asymmetry in this guide:

- Adding a *column* is cheap and has a dedicated positional method (`.insert()`) because you're just attaching one more contiguous array.
- Adding a *row* is expensive and has no dedicated positional method, because conceptually you're touching a small slice of *every single column's* underlying array at once, and growing all of them is what eventually killed off `.append()` in favor of explicit, batched `concat()` calls.
- *Filtering* is fast and natural because a boolean mask is itself just another column-shaped array — pandas is built around exactly this operation.
- *Aggregation* (`groupby`) is the one operation that temporarily works against the grain — it has to gather scattered rows belonging to the same group, which is why the API gives you so many specialized exits (`agg`, `transform`, `filter`) depending on whether you want to collapse rows, broadcast a value back onto them, or keep/drop them wholesale.

Keep that model in your head — column-oriented storage, and grouping as the one operation that cuts across it — and almost every "why is this slow," "why doesn't this method exist," or "why did my data silently change shape" question about pandas answers itself.
