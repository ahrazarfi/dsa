# DSA Full Revision Pack — Pattern-First Interview Prep

**Repo:** [ahrazarfi/dsa](https://github.com/ahrazarfi/dsa)  
**Scope:** every problem under `PROBLEMS/Arrays` as of 2026-10-02  
**Solved:** 15 · **Incomplete:** 1 (`two-sum`)  
**Includes:** 2026-10-02 push — `interesection-two-sorted-arr` (under `PROBLEMS/Arrays/`)  

---

## How to revise with this pack

1. **Cover the quiz cards first** (at the end of each problem section). Try to answer out loud before reading the Back.
2. **Then read the tip-offs + pattern + skeleton.** Ask yourself: *If I saw a new prompt with the same tip-offs, would I reach for the same pattern?*
3. **Walk the example with a blank sheet.** Cover the “state changing” column and rebuild it yourself.
4. **Do not open `solution.py` while revising.** Re-open code only after you’ve forced a skeleton from memory — and even then, compare *structure*, not keystrokes.
5. **Transfer test:** for each problem, invent one slightly different prompt (different constraint, same tip-off) and name the pattern. The quiz “variant” cards already nudge you there.
6. **Suggested sitting:** 2–3 problems deeply, or skim tip-offs across all 15 then deep-dive weak patterns. Goal is recognition under interview pressure, not finishing the file in one gulp.

**Tone reminder:** Interviewers care that you *see* the pattern and can narrate tradeoffs. Memorizing your exact Python is a trap.

---

# Part I — Solved problems (15)

---

## 1. `largest-element`

**Path:** `PROBLEMS/Arrays/largest-element/solution.py`

### What it’s asking

You’re given an array of integers. Return the single largest value in it. No sorting required; no “k-th largest” twist — just the maximum. It’s a foundation problem: one pass, one piece of state.

### Tip-offs / how you’d recognize this

- “Find the maximum / minimum / extreme value”
- Unsorted array, no index to return — just the value
- Constraints allow O(n); sorting would be overkill
- Interview variant: “maximum without using library max” → still the same scan

### Pattern name(s) + why

**Single-pass linear scan with a running maximum.**  
You only need information that can be updated from each element in isolation (compare to current best). No pairs, no order dependency beyond “seen so far.”

### Approach skeleton

1. Initialize `largest` to a sentinel smaller than any possible value (e.g. −∞), **or** to `nums[0]` if the array is guaranteed non-empty.
2. Iterate each `num` in the array.
3. If `num > largest`, replace `largest` with `num`.
4. After the loop, return `largest`.

That’s the whole algorithm. The interview skill is naming this cleanly and handling empty-array / all-negative cases when asked.

### Concrete example (state changing)

Input: `nums = [3, 1, 8, 2, 8]`

| Step | `num` | `largest` before | Action | `largest` after |
|------|-------|------------------|--------|-----------------|
| init | — | −∞ | — | −∞ |
| 1 | 3 | −∞ | 3 > −∞ → update | 3 |
| 2 | 1 | 3 | 1 ≯ 3 → keep | 3 |
| 3 | 8 | 3 | 8 > 3 → update | 8 |
| 4 | 2 | 8 | keep | 8 |
| 5 | 8 | 8 | 8 ≯ 8 → keep | 8 |

Answer: **8**

### Common pitfalls / edge cases

1. **Initializing with `0`** — fails if all elements are negative (e.g. `[-5, -1, -9]`).
2. **Empty array** — decide with interviewer: throw, return sentinel, or assume `n ≥ 1`.
3. **Ties** — multiple maxima is fine; you just need *a* largest value, not an index.
4. **Calling `sorted(nums)[-1]`** — correct but O(n log n); say you’d prefer O(n) unless asked otherwise.

### Complexity

- **Time:** O(n) — one pass  
- **Space:** O(1) — one scalar

### Quiz cards

**Front 1:** Unfamiliar prompt: “Return the hottest temperature in this list of °C readings (may be negative).” What pattern and init trick?  
**Back 1:** Single-pass running max. Init with −∞ or first reading — never hardcode 0 when negatives are possible.

**Front 2:** Why is sorting the wrong default answer for “largest element”?  
**Back 2:** Sorting costs O(n log n) and gives order you don’t need. A scan finds the extreme in O(n).

**Front 3 (variant):** “Return the *index* of the largest element (first occurrence if ties).” What changes?  
**Back 3:** Same scan, but store `best_index` and update when `nums[i] > nums[best_index]` (strict `>` keeps the first tie).

---

## 2. `second-largest-element`

**Path:** `PROBLEMS/Arrays/second-largest-element/solution.py`

### What it’s asking

Return the second-largest distinct value in the array. If there is no distinct second (all equal, or length &lt; 2 with no smaller value), return −1. Duplicates of the maximum do **not** count as second-largest.

### Tip-offs / how you’d recognize this

- “Second largest / second smallest / top-2”
- “Distinct” or “if it doesn’t exist return −1”
- Example like `[8, 8, 7, 6]` → answer 7, not 8
- Still O(n) / O(1) expected — not “sort then pick”

### Pattern name(s) + why

**Single-pass scan tracking two running extrema.**  
Same family as largest-element, but the state is a pair `(largest, second)`. The hard part is the update rules when a new max appears (demote the old max) vs when a mid-range value appears.

### Approach skeleton

1. Init `largest = −∞`, `second = −∞`.
2. For each `num`:
   - If `num > largest`: set `second = largest`, then `largest = num` (demote old champ).
   - Else if `num > second` **and** `num != largest`: set `second = num`.
3. If `second` is still −∞ → no distinct second → return −1; else return `second`.

### Concrete example (state changing)

Input: `nums = [8, 8, 7, 6, 5]`

| Step | `num` | `largest` | `second` | Rule fired |
|------|-------|-----------|----------|------------|
| init | — | −∞ | −∞ | — |
| 1 | 8 | 8 | −∞ | new max (demote −∞ → second) |
| 2 | 8 | 8 | −∞ | equal to largest → skip (must not set second=8) |
| 3 | 7 | 8 | 7 | mid-range: `second < 7 < largest` |
| 4 | 6 | 8 | 7 | 6 &lt; 7 → keep |
| 5 | 5 | 8 | 7 | keep |

Answer: **7**

### Common pitfalls / edge cases

1. **Treating a duplicate max as second** — `[8, 8]` must yield −1, not 8.
2. **Forgetting demotion** — when a new max arrives, old max becomes the candidate second.
3. **Init with 0** — same negative-array trap as largest-element.
4. **Length 1** — always −1.
5. **All equal** — −1.

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

### Quiz cards

**Front 1:** Walk `[5, 5, 5]`. What do `largest` / `second` look like at the end, and what do you return?  
**Back 1:** `largest = 5`, `second` still −∞ → return −1. Duplicates never promote into second.

**Front 2:** On seeing a new maximum, why must you assign `second = largest` *before* overwriting `largest`?  
**Back 2:** The old maximum is the best known “second” candidate so far; if you overwrite first, you lose it forever.

**Front 3 (variant):** “Return the third-largest distinct.” What’s the pattern generalization?  
**Back 3:** Track a small ordered tuple of top-k distinct values in one pass (or a size-k structure). Same “demote on new extreme” idea; more careful equality checks.

---

## 3. `sum-arr-elements`

**Path:** `PROBLEMS/Arrays/sum-arr-elements/solution.py`

### What it’s asking

Sum every element of the array and return the total. Pure accumulation — the simplest “running state” problem after max.

### Tip-offs / how you’d recognize this

- “Sum / total / aggregate all values”
- Prefix-sum *setup* interviews often start here
- Later cousins: range sum queries, running average — still built on accumulation

### Pattern name(s) + why

**Single-pass accumulator.**  
State is one number that only grows by `+= nums[i]`. No comparisons, no early exit (unless empty).

### Approach skeleton

1. Init `total = 0`.
2. For each index `i` in `0 .. n−1` (or for each value): `total += nums[i]`.
3. Return `total`.

(Your solution takes both `nums` and `n` and loops `range(n)`.)

### Concrete example (state changing)

Input: `nums = [1, 2, 3, 4]`, `n = 4`

| Step | `i` | `nums[i]` | `total` after |
|------|-----|-----------|---------------|
| init | — | — | 0 |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 2 | 3 |
| 3 | 2 | 3 | 6 |
| 4 | 3 | 4 | 10 |

Answer: **10**

### Common pitfalls / edge cases

1. **Empty array** — sum should be 0 (usually).
2. **Overflow** — in fixed-width languages (C++/Java int); Python is fine. Interviewers may ask about 64-bit.
3. **Off-by-one on `n`** — if `n` is passed separately, don’t loop past the real length.
4. **Confusing with “sum of unique” or “sum in a range”** — different problems; listen to the prompt.

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

### Quiz cards

**Front 1:** How does this problem prepare you for prefix sums?  
**Back 1:** Prefix sums = store every intermediate `total` in an array (`pref[i] = pref[i−1] + nums[i]`). Same accumulation idea, kept for range queries.

**Front 2:** Prompt: “Sum of elements at even indices only.” What changes in the skeleton?  
**Back 2:** Same accumulator; add a predicate (`if i % 2 == 0`) or step `range(0, n, 2)`. Pattern unchanged.

**Front 3:** Why might an interviewer reject `sum(nums)` in a whiteboard setting?  
**Back 3:** They want to see you can write the loop and discuss overflow / empty cases. Library use is fine in production — say so, then show the loop if asked.

---

## 4. `count-odd-arr`

**Path:** `PROBLEMS/Arrays/count-odd-arr/solution.py`

### What it’s asking

Count how many elements in the array are odd. Return that count. Classic “scan + predicate.”

### Tip-offs / how you’d recognize this

- “How many elements satisfy property P?”
- P is local (depends only on the current element): odd/even, positive, vowel, etc.
- No need to store the elements — only a counter

### Pattern name(s) + why

**Single-pass conditional counter.**  
Sibling of sum-arr-elements: instead of adding the value, you add `1` when a condition holds (`num % 2 != 0`).

### Approach skeleton

1. Init `count = 0`.
2. For each index `i` in `0 .. n−1`: if `nums[i]` is odd, `count += 1`.
3. Return `count`.

### Concrete example (state changing)

Input: `nums = [1, 2, 3, 4, 5]`, `n = 5`

| Step | `num` | Odd? | `count` |
|------|-------|------|---------|
| init | — | — | 0 |
| 1 | 1 | yes | 1 |
| 2 | 2 | no | 1 |
| 3 | 3 | yes | 2 |
| 4 | 4 | no | 2 |
| 5 | 5 | yes | 3 |

Answer: **3**

### Common pitfalls / edge cases

1. **Negative odds** — in some languages `(-3) % 2` is implementation-defined; prefer `num & 1` or `abs(num) % 2` after clarifying. Python: `(-3) % 2 == 1`, so `!= 0` works for odds.
2. **Confusing “count odds” with “sum of odds.”**
3. **Empty array** → 0.
4. **Using float division** — always use integer modulo / bit test.

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

### Quiz cards

**Front 1:** What’s the generic template this problem teaches?  
**Back 1:** `count = 0; for x in arr: if P(x): count += 1`. Swap `P` for any local property.

**Front 2:** Variant: “Count elements strictly greater than their neighbors.” Is it still the same pattern?  
**Back 2:** Mostly — still a counter — but `P` now needs neighbors, so you iterate interior indices and handle ends carefully. Same family, slightly richer predicate.

**Front 3:** Why O(1) space still holds if you later need the *list* of odds?  
**Back 3:** It doesn’t — collecting them needs O(k) output space. Counting alone is O(1) extra.

---

## 5. `linear-search`

**Path:** `PROBLEMS/Arrays/linear-search/solution.py`

### What it’s asking

Find the smallest index where `target` appears in `nums`. If missing, return −1. Unsorted array, so you can’t binary-search.

### Tip-offs / how you’d recognize this

- “First index of / find position of”
- Array not sorted (or sorting forbidden / would destroy indices)
- Early exit on success is allowed and desirable
- Contrast tip-off for binary search: *sorted* + find index/existence

### Pattern name(s) + why

**Linear search with early return.**  
Still a single pass, but the “state” is “found or not,” and you stop at the first hit to get the *smallest* index naturally.

### Approach skeleton

1. For `i` from `0` to `len(nums)−1`:
2. If `nums[i] == target`, return `i` immediately.
3. If the loop finishes, return −1.

### Concrete example (state changing)

Input: `nums = [4, 2, 7, 2]`, `target = 2`

| Step | `i` | `nums[i]` | Match? | Action |
|------|-----|-----------|--------|--------|
| 1 | 0 | 4 | no | continue |
| 2 | 1 | 2 | yes | return **1** |

(Never looks at the second `2` at index 3 — first occurrence wins.)

Missing case: `target = 9` → scan all → **−1**.

### Common pitfalls / edge cases

1. **Returning the last index** — happens if you keep scanning and overwrite; for “first index,” return immediately.
2. **Sorted array temptation** — if the prompt suddenly says sorted, binary search is better — but this problem’s contract is linear.
3. **Empty array** → −1.
4. **Target equals first/last element** — check boundaries in tests.

### Complexity

- **Time:** O(n) worst case; O(1) best if found at front  
- **Space:** O(1)

### Quiz cards

**Front 1:** Prompt says the array is sorted and you need any index of target. Do you still linear-search?  
**Back 1:** Prefer binary search O(log n). Linear search is the fallback when unsorted or when you must preserve a simple first-pass story.

**Front 2:** “Return *all* indices of target.” How does the skeleton change?  
**Back 2:** Don’t early-return; collect into a list (or count). Still linear scan; output size becomes O(k).

**Front 3:** What’s the tip-off that you want the *smallest* index without extra work?  
**Back 3:** Scanning left → right and returning on first hit *is* the smallest index. No second pass needed.

---

## 6. `check-arr-sorted-i`

**Path:** `PROBLEMS/Arrays/check-arr-sorted-i/solution.py`

### What it’s asking

Decide whether the array is sorted in non-decreasing order (each element ≤ the next). Return true/false. You’re validating an *adjacent* invariant, not computing a value.

### Tip-offs / how you’d recognize this

- “Is sorted?” / “check non-decreasing / strictly increasing”
- Decision problem; one counterexample is enough to return false
- Adjacent pairs matter (`a[i]` vs `a[i+1]`), not a global max

### Pattern name(s) + why

**Single-pass adjacent invariant check (early exit on violation).**  
You walk consecutive pairs; the first descent proves “not sorted.”

### Approach skeleton

1. For `i` from `0` to `n−2`:
2. If `arr[i] > arr[i+1]`, return `False` immediately.
3. If no violation, return `True`.

(Equal neighbors are OK for non-decreasing — use `>` not `>=`.)

### Concrete example (state changing)

Input A: `arr = [1, 2, 2, 4]`, `n = 4`

| Pair | Compare | OK? |
|------|---------|-----|
| (1,2) | 1 ≯ 2 | yes |
| (2,2) | 2 ≯ 2 | yes |
| (2,4) | 2 ≯ 4 | yes |

→ **True**

Input B: `arr = [1, 3, 2]`, `n = 3`

| Pair | Compare | OK? |
|------|---------|-----|
| (1,3) | OK | yes |
| (3,2) | 3 > 2 | **False** → return |

### Common pitfalls / edge cases

1. **Using `>=` when non-decreasing allows equals** — would reject `[1, 1]`.
2. **Strictly increasing prompts** — then equals *are* a failure (`>=` as violation).
3. **Length 0 or 1** — vacuously sorted → true.
4. **Checking only against `arr[0]`** — wrong; sortedness is pairwise adjacent (transitive for totals, but you must check every consecutive pair).

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

### Quiz cards

**Front 1:** Difference between “non-decreasing” and “strictly increasing” in the comparison?  
**Back 1:** Non-decreasing: fail on `a[i] > a[i+1]`. Strict: fail on `a[i] >= a[i+1]`.

**Front 2:** Variant: “Array is sorted *or* sorted after one rotation” (rotated sorted). Same algorithm?  
**Back 2:** No — you count how many times `a[i] > a[i+1]` (and wrap around). At most one “drop” allowed. Related tip-off, different rule.

**Front 3:** Why early-return on first violation?  
**Back 3:** One counterexample disproves sortedness; remaining pairs can’t save it. Saves average time.

---

## 7. `max-consecutive-ones`

**Path:** `PROBLEMS/Arrays/max-consecutive-ones/solution.py`

### What it’s asking

Given a binary array (only 0s and 1s), return the length of the longest contiguous run of 1s. Runs of 0s break the streak.

### Tip-offs / how you’d recognize this

- “Maximum consecutive / longest run of X”
- Binary or categorical sequence where adjacency defines a run
- Reset-on-break language in the problem statement
- Not “total count of 1s” (that’s count-odd style) — *contiguous* is the keyword

### Pattern name(s) + why

**Streak counter with reset.**  
Maintain current run length and best-so-far. On a “good” element grow the run; on a “bad” element zero it out. Classic template for many “longest consecutive …” prompts.

### Approach skeleton

1. Init `count = 0` (current streak), `ans = 0` (best streak).
2. For each `num` in `nums`:
   - If `num == 1`: `count += 1`, then `ans = max(ans, count)`.
   - Else: `count = 0`.
3. Return `ans`.

### Concrete example (state changing)

Input: `nums = [1, 1, 0, 0, 1, 1, 1, 0]`

| Step | `num` | `count` | `ans` |
|------|-------|---------|-------|
| init | — | 0 | 0 |
| 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 |
| 3 | 0 | 0 | 2 |
| 4 | 0 | 0 | 2 |
| 5 | 1 | 1 | 2 |
| 6 | 1 | 2 | 2 |
| 7 | 1 | 3 | **3** |
| 8 | 0 | 0 | 3 |

Answer: **3**

### Common pitfalls / edge cases

1. **Forgetting to update `ans` inside the success branch** — if you only update at resets, a streak that ends at the array’s end is missed (unless you flush after the loop).
2. **Not resetting on 0** — current streak bleeds across zeros.
3. **All zeros** → 0; **all ones** → `n`.
4. **Confusing with “max consecutive *after flipping at most k zeros*”** — that’s sliding window, a different pattern.

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

### Quiz cards

**Front 1:** Why update `ans` on every successful increment instead of only when you hit a 0?  
**Back 1:** The longest run might be a suffix with no trailing 0. Updating live covers that without a post-loop flush.

**Front 2:** Variant: longest consecutive *even* numbers in an int array. What changes?  
**Back 2:** Same streak template; “good” predicate becomes `num % 2 == 0`. Pattern identical.

**Front 3:** Tip-off that this is *not* a sliding window yet?  
**Back 3:** You don’t need a flexible window with a budget (e.g. “at most k zeros”). One bit of state — current streak — is enough.

---

## 8. `reverse-arr`

**Path:** `PROBLEMS/Arrays/reverse-arr/solution.py`

### What it’s asking

Reverse the array **in place**. No need to return a new array — modify the given one (your runner uses `in_place=True`).

### Tip-offs / how you’d recognize this

- “Reverse / mirror the array in place”
- O(1) extra space required
- Building a new reversed copy is correct but uses O(n) space — often not what they want
- Same pointer idea appears inside rotate-by-k

### Pattern name(s) + why

**Opposite-end two pointers.**  
Left starts at the start, right at the end; swap and move inward until they meet. Each swap places two elements into final positions.

### Approach skeleton

1. Set `left = 0`, `right = n − 1`.
2. While `left < right`:
   - Swap `arr[left]` and `arr[right]`.
   - `left += 1`, `right −= 1`.
3. Done (middle element of odd-length arrays sits still).

### Concrete example (state changing)

Input: `arr = [1, 2, 3, 4, 5]`, `n = 5`

| Iteration | `left` | `right` | Array after swap |
|-----------|--------|---------|------------------|
| start | 0 | 4 | [1, 2, 3, 4, 5] |
| 1 | 0→1 | 4→3 | [**5**, 2, 3, 4, **1**] |
| 2 | 1→2 | 3→2 | [5, **4**, 3, **2**, 1] |
| stop | 2 | 2 | `left == right` → stop |

Result: `[5, 4, 3, 2, 1]`

### Common pitfalls / edge cases

1. **Off-by-one:** `right = n` instead of `n−1` → index error.
2. **Loop condition `left <= right`** — one extra no-op swap of the middle; usually harmless but `left < right` is cleaner.
3. **Empty / single-element** — loop never runs; correctly a no-op.
4. **Allocating a new list** — fails the in-place spirit if that was required.

### Complexity

- **Time:** O(n) — about n/2 swaps  
- **Space:** O(1)

### Quiz cards

**Front 1:** Why do left and right meet in the middle rather than crossing the whole array twice?  
**Back 1:** Each swap finalizes two positions; after n/2 swaps every index is done.

**Front 2:** How does this card unlock left-rotate-by-k?  
**Back 2:** Rotate-by-k is three targeted reverses (prefix, suffix, whole). Reverse is the primitive.

**Front 3 (variant):** Reverse only a subarray `arr[l..r]`. Skeleton change?  
**Back 3:** Same while-loop, but init `left = l`, `right = r` instead of `0` and `n−1`.

---

## 9. `left-rotate-array-by-one`

**Path:** `PROBLEMS/Arrays/left-rotate-array-by-one/solution.py`

### What it’s asking

Rotate the array **one step to the left** in place: every element moves one index down, and the original first element wraps to the end. Example: `[1,2,3,4,5]` → `[2,3,4,5,1]`.

### Tip-offs / how you’d recognize this

- “Rotate left/right by one”
- In-place modification; no return value
- Special case of rotate-by-k with `k = 1`
- Tip-off for the shift approach: small fixed k, or teaching the wrap idea before the reverse trick

### Pattern name(s) + why

**In-place shift with saved head (cyclic assignment).**  
You can’t overwrite `nums[0]` until you’ve saved it; then slide everyone left by one; place the saved value at the end.

### Approach skeleton

1. Save `first = nums[0]`.
2. For `i` from `1` to `len(nums)−1`: set `nums[i−1] = nums[i]` (shift left).
3. Set `nums[-1] = first`.

### Concrete example (state changing)

Input: `nums = [1, 2, 3, 4, 5]`

| Step | Action | Array |
|------|--------|-------|
| save | `first = 1` | [1, 2, 3, 4, 5] |
| i=1 | nums[0]=2 | [2, 2, 3, 4, 5] |
| i=2 | nums[1]=3 | [2, 3, 3, 4, 5] |
| i=3 | nums[2]=4 | [2, 3, 4, 4, 5] |
| i=4 | nums[3]=5 | [2, 3, 4, 5, 5] |
| wrap | nums[4]=first | [2, 3, 4, 5, **1**] |

### Common pitfalls / edge cases

1. **Empty array / length 1** — shifting loop must not assume `n ≥ 2` blindly; length 1 is already “rotated.”
2. **Rotating right by one** — save `last`, shift rightward, put `last` at front (mirror of this).
3. **Using this for large k** — O(nk) if repeated k times; switch to reverse-based rotate.
4. **Forgetting to save `first`** — first assignment destroys it.

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

### Quiz cards

**Front 1:** If you call this routine `k` times to rotate by k, what’s the complexity?  
**Back 1:** O(nk). Fine for k=1; bad for large k — use the three-reverse method instead.

**Front 2:** Narrate why you must save `nums[0]` before the shift loop.  
**Back 2:** The shift overwrites index 0 immediately; without a temp, the head is lost and can’t wrap to the end.

**Front 3 (variant):** Rotate left by one on a *linked list*. Same idea?  
**Back 3:** Conceptually yes (move head to tail), but implementation uses pointer rewiring, not index shifts — different data-structure mechanics, same cyclic intent.

---

## 10. `left-rotate-array-by-k`

**Path:** `PROBLEMS/Arrays/left-rotate-array-by-k/solution.py`

### What it’s asking

Rotate left by an arbitrary non-negative `k`, still in place. After k left rotations, the element that was at index `k` becomes the new front. Example: `[1,2,3,4,5,6]`, `k=2` → `[3,4,5,6,1,2]`.

### Tip-offs / how you’d recognize this

- “Rotate array by k” + in-place + O(1) extra space
- Mentions that k can be larger than n (need modulo)
- Interview classic: juggling / block-swap / **reverse** methods — reverse is the one you implemented

### Pattern name(s) + why

**Reverse-based block rotation** (built on opposite-end two pointers).  
Left rotate by k = move prefix of length k to the end. Three reverses achieve that without extra arrays:
1. Reverse the prefix `[0 .. k)`  
2. Reverse the suffix `[k .. n)`  
3. Reverse the entire array  

Also: **`k %= n`** because rotation is cyclic with period n.

### Approach skeleton

1. If `n == 0`, return. Else `k = k % n`.
2. Reverse indices `[0 .. k−1]`.
3. Reverse indices `[k .. n−1]`.
4. Reverse indices `[0 .. n−1]`.

(Each reverse = the opposite-end two-pointer loop from `reverse-arr`.)

### Concrete example (state changing)

Input: `nums = [1, 2, 3, 4, 5, 6]`, `k = 2`  
Effective k = 2 % 6 = 2

| Stage | Operation | Array |
|-------|-----------|-------|
| start | — | [1, 2, 3, 4, 5, 6] |
| 1 | reverse [0..1] | [**2, 1**, 3, 4, 5, 6] |
| 2 | reverse [2..5] | [2, 1, **6, 5, 4, 3**] |
| 3 | reverse all | [**3, 4, 5, 6, 1, 2**] |

Matches the desired left rotation by 2.

### Common pitfalls / edge cases

1. **Forgetting `k %= n`** — large k → index errors or wrong answers.
2. **Mixing left vs right rotate reverse order** — right rotate by k often uses reverse-all first, then reverse parts (different order). Know which one you need.
3. **`k = 0` or multiple of n** — should leave array unchanged (all reverses of empty/full cancel correctly if you handle k=0).
4. **Empty array** — guard before modulo.
5. **Off-by-one in reverse bounds** — prefix is length k (indices `0..k-1`).

### Complexity

- **Time:** O(n) — three linear reverses  
- **Space:** O(1)

### Quiz cards

**Front 1:** Why does `k %= len(nums)` belong at the top of every rotate-by-k solution?  
**Back 1:** Rotating n times is identity; only the remainder matters. Also prevents out-of-range reverses when k ≥ n.

**Front 2:** Explain in one sentence why three reverses left-rotate.  
**Back 2:** They rearrange the two blocks (prefix k and the rest) so the old suffix becomes the new prefix — a cyclic shift without extra memory.

**Front 3 (variant):** “Rotate *right* by k in place.” What’s the usual reverse recipe?  
**Back 3:** Common approach: reverse whole array, reverse first k, reverse the rest (for right rotate) — or left-rotate by `n−k`. Same pattern family.

---

## 11. `move-zeros-end`

**Path:** `PROBLEMS/Arrays/move-zeros-end/solution.py`

### What it’s asking

Move all zeros to the end of the array **in place**, keeping the relative order of the non-zero elements. Example: `[0,1,4,0,5,2]` → `[1,4,5,2,0,0]`.

### Tip-offs / how you’d recognize this

- “Move all X to the end/front” + “preserve relative order” + “in place”
- Stable partition language
- Two-pointer / write-index tip-offs
- Not sorting (sorting would also group zeros but may reorder non-zeros depending on sort stability / comparator)

### Pattern name(s) + why

**Write/read pointer — stable partition.**  
`write` (your `written`) marks the next slot for a “keeper” (non-zero). Scan with `i`; when you see a keeper, swap it into `write` and advance `write`. Zeros naturally fill the tail as keepers are swapped forward.

(An equivalent two-pass: copy non-zeros forward, then fill the rest with zeros — also fine; your final code uses the swap form.)

### Approach skeleton

1. Init `written = 0`.
2. For `i` in `0 .. n−1`:
   - If `nums[i] != 0`: swap `nums[written]` with `nums[i]`, then `written += 1`.
3. After the loop, indices `written .. n−1` hold the zeros.

### Concrete example (state changing)

Input: `nums = [0, 1, 4, 0, 5, 2]`

| `i` | `nums[i]` | Action | `written` after | Array |
|-----|-----------|--------|-----------------|-------|
| 0 | 0 | skip | 0 | [0, 1, 4, 0, 5, 2] |
| 1 | 1 | swap with idx 0 | 1 | [1, 0, 4, 0, 5, 2] |
| 2 | 4 | swap with idx 1 | 2 | [1, 4, 0, 0, 5, 2] |
| 3 | 0 | skip | 2 | [1, 4, 0, 0, 5, 2] |
| 4 | 5 | swap with idx 2 | 3 | [1, 4, 5, 0, 0, 2] |
| 5 | 2 | swap with idx 3 | 4 | [1, 4, 5, 2, 0, 0] |

### Common pitfalls / edge cases

1. **Losing relative order** — e.g. swapping from both ends without care (that’s a different partition).
2. **Using extra arrays** when in-place was required.
3. **All zeros / no zeros / zeros already at end** — algorithm should be a no-op or near no-op.
4. **Confusing with “separate positives and negatives”** — same partition pattern, different keep-rule.

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

### Quiz cards

**Front 1:** What is the keep-rule for this problem, and where does `written` point?  
**Back 1:** Keep-rule = non-zero. `written` = next index to place a keeper; also equals the count of keepers found so far.

**Front 2:** How is this the *same pattern* as remove-duplicates-from-sorted-array?  
**Back 2:** Both maintain a write index for the next valid slot. Only the keep-rule changes (non-zero vs “not equal to last unique”).

**Front 3 (variant):** “Move all zeros to the *front*, preserve non-zero order.” Idea?  
**Back 3:** Either partition keepers to the right, or scan right-to-left with a write pointer — same family, mirrored boundary.

---

## 12. `remove-duplicates-sorted-arr`

**Path:** `PROBLEMS/Arrays/remove-duplicates-sorted-arr/solution.py`

### What it’s asking

Array is sorted non-decreasing. Remove duplicates **in place** so each distinct value appears once in the front of the array. Conceptually return `k` (count of uniques); the first `k` positions must hold those uniques in original order. (Your solution returns the unique slice `nums[:seen+1]` — same logical `k = seen+1`.)

### Tip-offs / how you’d recognize this

- Input **already sorted**
- “Remove duplicates in place” / “unique elements in-place”
- Judge only cares about the prefix of length k
- Unsorted “unique elements” would need a hash set — different tip-off

### Pattern name(s) + why

**Write pointer for unique compression on a sorted array.**  
Sorted ⇒ duplicates are adjacent ⇒ you only compare the candidate to the last kept unique. Classic slow/fast pair: `seen` (last unique index) and `i` (scanner).

### Approach skeleton

1. If empty, handle edge (k = 0). Else init `seen = 0` (first element is unique).
2. For `i` from `1` to `n−1`:
   - If `nums[i] != nums[seen]`: this is a new unique → `seen += 1`, then `nums[seen] = nums[i]`.
3. Unique count `k = seen + 1`. Return `k` (LeetCode-style) or the prefix (as in your file).

### Concrete example (state changing)

Input: `nums = [0, 0, 3, 3, 5, 6]`

| `i` | `nums[i]` | `nums[seen]` | Action | `seen` | Prefix meaning |
|-----|-----------|---------------|--------|--------|----------------|
| init | — | 0 at idx 0 | — | 0 | [0, …] |
| 1 | 0 | 0 | equal → skip | 0 | |
| 2 | 3 | 0 | new → write at 1 | 1 | [0, 3, …] |
| 3 | 3 | 3 | skip | 1 | |
| 4 | 5 | 3 | new → write at 2 | 2 | [0, 3, 5, …] |
| 5 | 6 | 5 | new → write at 3 | 3 | [0, 3, 5, 6, …] |

`k = 4`. Tail junk ignored.

### Common pitfalls / edge cases

1. **Comparing to `nums[i−1]` only when you also write carefully** — comparing to `nums[seen]` is the clean invariant.
2. **Unsorted input** — this algorithm would miss non-adjacent duplicates.
3. **Returning the whole array** when the API wants integer `k` — know the contract (interview + LeetCode want `k`).
4. **Empty / single-element** — `k = 0` or `1`.
5. **All duplicates** — `k = 1`, first slot kept.

### Complexity

- **Time:** O(n)  
- **Space:** O(1) extra

### Quiz cards

**Front 1:** Why does sortedness let you avoid a hash set?  
**Back 1:** Duplicates sit next to each other, so “same as last kept” catches every repeat in one pass.

**Front 2:** What’s the invariant at index `seen`?  
**Back 2:** `nums[0..seen]` are the unique elements found so far, in order; `seen` is the last filled unique slot.

**Front 3 (variant):** “Allow each element at most *twice*” (LeetCode 80). How does the keep-rule change?  
**Back 3:** Still a write pointer, but keep if `nums[i] != nums[write−2]` (or count frequency up to 2). Same pattern, richer rule.

---

## 13. `union-two-sorted-arr`

**Path:** `PROBLEMS/Arrays/union-two-sorted-arr/solution.py`

### What it’s asking

Given two **sorted** arrays, return a new sorted array containing the union: every distinct value that appears in either array. Shared values appear once. Example: `[1,2,3,4,5]` ∪ `[1,2,7]` → `[1,2,3,4,5,7]`.

### Tip-offs / how you’d recognize this

- Both inputs sorted; output must be sorted
- “Union” / “merge unique” / “combine without duplicates”
- Linear O(n+m) expected if you exploit sortedness
- Set union then sort works but ignores the gift of sorted inputs

### Pattern name(s) + why

**Two-pointer merge (merge-sort merge style) + dedup against the last emitted value.**  
Like merging two sorted lists, but when values are equal you emit once and advance both; always skip appending if `result[-1]` already equals the candidate (handles duplicates *inside* one array too).

### Approach skeleton

1. Init `i = 0`, `j = 0`, `result = []`.
2. While both arrays have elements left:
   - If `nums1[i] < nums2[j]`: append `nums1[i]` if not dup of `result[-1]`; `i += 1`.
   - Else if `nums1[i] > nums2[j]`: same for `nums2[j]`; `j += 1`.
   - Else (equal): append once if needed; `i += 1` and `j += 1`.
3. Drain remaining `nums1` with the same dedup guard.
4. Drain remaining `nums2` similarly.
5. Return `result`.

### Concrete example (state changing)

`nums1 = [1, 2, 3, 4, 5]`, `nums2 = [1, 2, 7]`

| `i`,`j` | Heads | Action | `result` |
|---------|-------|--------|----------|
| 0,0 | 1,1 | equal → append 1; i,j→1 | [1] |
| 1,1 | 2,2 | equal → append 2; i,j→2 | [1,2] |
| 2,2 | 3,7 | 3&lt;7 → append 3; i→3 | [1,2,3] |
| 3,2 | 4,7 | append 4; i→4 | [1,2,3,4] |
| 4,2 | 5,7 | append 5; i→5 | [1,2,3,4,5] |
| done nums1 | — | drain nums2: append 7 | [1,2,3,4,5,7] |

### Common pitfalls / edge cases

1. **Forgetting dedup vs `result[-1]`** — duplicates inside one array slip through.
2. **Forgetting the drain loops** — leftover tail never appended.
3. **One array empty** — result should just be the unique version of the other (still need dedup if that array has repeats).
4. **Using a set and sorting** — acceptable brute force; mention then upgrade to two-pointer for O(n+m) without the log factor from sorting a set.

### Complexity

- **Time:** O(n + m)  
- **Space:** O(n + m) for the output (necessary); O(1) extra besides the answer

### Quiz cards

**Front 1:** How does this differ from the merge step in merge sort?  
**Back 1:** Merge sort merge keeps duplicates and doesn’t need “distinct.” Union adds the “skip if last equal” / advance-both-on-equal rules.

**Front 2:** Variant: *intersection* of two sorted arrays. Pointer rules?  
**Back 2:** Advance the side with the smaller head; on equal, emit once and advance both. No draining leftovers into the answer.

**Front 3:** Tip-off you’re in the merge family rather than hash-set family?  
**Back 3:** Inputs already sorted + need sorted output + linear pass expected.

---

## 14. `find-missing-number`

**Path:** `PROBLEMS/Arrays/find-missing-number/solution.py`

### What it’s asking

Array of length `n` contains `n` distinct integers from the range `0 .. n` (inclusive) with **exactly one** number missing. Return that missing number. Example: `[0,2,3,1,4]` (length 5, range 0..5) → missing **5**.

### Tip-offs / how you’d recognize this

- Range given explicitly (`0..n` or `1..n`) with one hole
- Distinct values; length is one less than the full range size
- “Find the missing number” without needing to sort
- Interview follow-ups: overflow-safe version, or “find two missing,” etc.

### Pattern name(s) + why

**Expected aggregate − actual aggregate (sum formula).**  
Sum of `0..n` is known; subtract the array sum → missing.  
**Sibling pattern to know:** XOR of all indices/`0..n` with all elements → missing (avoids overflow in fixed-width ints). Your code uses the sum approach (loop form of expected sum).

### Approach skeleton

1. Let `n = len(nums)` — missing is in `0..n`, so full set has `n+1` numbers.
2. Compute `sum1 = 0 + 1 + … + n` (loop or `n(n+1)//2`).
3. Compute `sum2 = sum(nums)`.
4. Return `sum1 - sum2`.

### Concrete example (state changing)

Input: `nums = [0, 2, 3, 1, 4]` → `n = 5`, full range `0..5`

| Piece | Value |
|-------|-------|
| expected sum `0+1+2+3+4+5` | 15 |
| actual sum of nums | 0+2+3+1+4 = 10 |
| missing | 15 − 10 = **5** |

XOR sketch (same example): XOR everything in `0..5` with everything in nums → 5.

### Common pitfalls / edge cases

1. **Off-by-one on the range** — length `n` means range `0..n` (n+1 possible values), not `0..n-1`.
2. **Overflow** in 32-bit languages with `n(n+1)/2` — prefer XOR or 64-bit.
3. **Missing is 0 or n** — formula still works; don’t special-case incorrectly.
4. **Assuming sorted input** — your O(n) method doesn’t need sortedness; sorting would work but is slower.

### Complexity

- **Time:** O(n)  
- **Space:** O(1)

### Quiz cards

**Front 1:** Why is `len(nums)` equal to `n` when the range is `0..n`?  
**Back 1:** Full set has n+1 numbers; exactly one missing ⇒ array holds n numbers. The missing value is still labeled from that same `0..n` universe.

**Front 2:** Give one reason to prefer XOR over sum in an interview follow-up.  
**Back 2:** XOR stays within word size and doesn’t overflow; same O(n)/O(1).

**Front 3 (variant):** Numbers are `1..n` with one missing (array length n−1). What changes?  
**Back 3:** Expected sum becomes `n(n+1)/2` still, but now `n` is the stated upper bound, not `len(nums)`. Or XOR `1..n` with array values. Adjust the definition of n carefully.

---

---

## 15. `interesection-two-sorted-arr`

**Path:** `PROBLEMS/Arrays/interesection-two-sorted-arr/solution.py`  
**Status:** solved (real logic, not a stub)  
**Related backlog problem:** `PROBLEMS/Arrays/union-two-sorted-arr`

### What it’s asking

You’re given two arrays that are already sorted in non-decreasing order. Return a new array containing their **intersection** — the values that appear in **both** arrays.

Because the inputs can contain duplicates, the important interview question is: *with what multiplicity?* Your solution emits a value once for each time the two pointers “agree” on it, advancing both. That means each value appears in the result **`min(count_in_nums1, count_in_nums2)`** times — the classic “Intersection of Two Arrays II” / multiset intersection behavior when both sides are sorted — **not** the distinct-only set intersection.

Example from your `input.txt`:  
`[1, 2, 2, 3, 3, 3]` ∩ `[2, 3, 3, 4, 5, 7]` → `[2, 3, 3]`  
(one `2` because the second array only has one; two `3`s because both have at least two).

### Tip-offs / how you’d recognize this

- Both inputs are **sorted** (or you are allowed / expected to sort first).
- Words like **intersection**, “common elements,” “present in both.”
- Output should stay sorted (falls out naturally from the merge walk).
- Linear `O(n + m)` is expected if you exploit sortedness — hashing also works but doesn’t need sorted input.
- Contrast tip-offs:
  - **Union** → emit when in *either* array (your earlier problem).
  - **Distinct intersection** → emit each common value only once (extra skip / set).
  - **Unsorted + need indices / frequencies** → hash map of counts is often cleaner.

### Pattern name(s) + why they fit

**Primary: two-pointer merge walk on sorted arrays (intersection variant).**  
Same family as merge-sort’s merge and as your `union-two-sorted-arr`. You keep one index on each array, always advancing the side with the smaller head (that value can never match anything still ahead on the other side, because both are sorted). On equality, you’ve found a shared occurrence — record it and advance **both**.

**Why not a hash set?**  
Works for *distinct* intersection on unsorted data. For multiset intersection you’d use a frequency map. Sorted two-pointers give `O(1)` extra space (besides the output) and make the “why advance this side?” reasoning interview-friendly.

**Relationship to union (same family, opposite emit rule):**

| Situation | Union (your earlier solve) | Intersection (today) |
|-----------|----------------------------|----------------------|
| `a < b` | emit `a`, advance `i` | emit nothing, advance `i` |
| `a > b` | emit `b`, advance `j` | emit nothing, advance `j` |
| `a == b` | emit once, advance both | emit once, advance both |
| Drain leftovers | yes — leftovers are in the union | **no** — leftovers can’t be in both |

### Approach skeleton

1. Init `i = 0`, `j = 0`, and an empty `result` list.
2. While `i < len(nums1)` **and** `j < len(nums2)` (both still have candidates):
   - If `nums1[i] == nums2[j]`: append that value to `result`; `i += 1`; `j += 1`.
   - Else if `nums1[i] < nums2[j]`: this value of `nums1` can never match a future `nums2[j]` (sorted) → `i += 1`.
   - Else (`nums1[i] > nums2[j]`): symmetrically `j += 1`.
3. Stop when either pointer runs out. **Do not** drain the remainder — anything left is unique to one array.
4. Return `result`.

Optional interview polish to mention: if the prompt wants **distinct** intersection only, after a match you can skip all duplicates of that value on both sides (or guard with `if not result or result[-1] != val` before append, and still advance past duplicates).

### Concrete example — state table

**Case A** (from your input):  
`nums1 = [1, 2, 2, 3, 3, 3]`, `nums2 = [2, 3, 3, 4, 5, 7]`

| Step | `i` | `j` | Heads (`nums1[i]`, `nums2[j]`) | Rule | Action | `result` |
|------|-----|-----|--------------------------------|------|--------|----------|
| 0 | 0 | 0 | (1, 2) | 1 < 2 | advance `i` | [] |
| 1 | 1 | 0 | (2, 2) | equal | append 2; advance both | [2] |
| 2 | 2 | 1 | (2, 3) | 2 < 3 | advance `i` | [2] |
| 3 | 3 | 1 | (3, 3) | equal | append 3; advance both | [2, 3] |
| 4 | 4 | 2 | (3, 3) | equal | append 3; advance both | [2, 3, 3] |
| 5 | 5 | 3 | (3, 4) | 3 < 4 | advance `i` | [2, 3, 3] |
| 6 | 6 | 3 | — | `i` exhausted | **stop** (no drain) | **[2, 3, 3]** |

Notice: the second `2` in `nums1` never finds a partner (only one `2` in `nums2`), so multiplicity is capped by the scarcer side.

**Case B** (from your input):  
`nums1 = [1, 2, 2, 3, 5]`, `nums2 = [1, 2, 7]`

| Step | Heads | Rule | `result` |
|------|-------|------|----------|
| (1, 1) | equal → append 1 | [1] |
| (2, 2) | equal → append 2 | [1, 2] |
| (2, 7) | 2 < 7 → advance `i` | [1, 2] |
| (3, 7) | 3 < 7 → advance `i` | [1, 2] |
| (5, 7) | 5 < 7 → advance `i` | [1, 2] |
| `i` done | stop | **[1, 2]** |

`7` is never emitted — it only exists on one side. The extra `2` in `nums1` is skipped after the first match consumed `nums2`’s only `2`.

### Common pitfalls / edge cases

1. **Draining leftovers like union** — wrong for intersection. Leftovers are exclusive to one array.
2. **Confusing multiset vs distinct intersection** — clarify with the interviewer. Your code is multiset (`min` of frequencies). Distinct needs an extra “skip duplicates after emit” or a set.
3. **Advancing only one pointer on equality** — can double-count or miss pairs; equality should advance **both** (for this multiset-one-pair-at-a-time style).
4. **Assuming no duplicates** — your tests deliberately include repeats (`2`, `3`); the algorithm must handle them.
5. **Empty array** — one empty input ⇒ empty intersection immediately (while never runs).
6. **Unsorted input** — this pointer logic is incorrect unless you sort first (sorting costs `O(n log n + m log m)` then `O(n + m)` merge).
7. **Repo hygiene:** folder typo `interesection-…`; empty `expected.txt` — none change the pattern, but worth fixing so tooling and future-you stay consistent.

### Complexity

- **Time:** `O(n + m)` — each index moves at most once.  
- **Space:** `O(1)` extra besides the output list (output size ≤ `min(n, m)`).

If you sorted unsorted inputs first: `O(n log n + m log m)` dominated by sorting.

### Quiz cards

**Front 1 — Recognition**  
Cold prompt: “Both arrays are sorted. Return every value that appears in both; if 5 appears twice in each, 5 should appear twice in the answer.” What pattern, and what do you do on `a < b` vs `a == b`?

**Back 1**  
Two-pointer sorted intersection (multiset). On `a < b`, advance the left/smaller side only (no emit). On `a == b`, emit once and advance **both**. Never drain leftovers.

---

**Front 2 — Gotcha vs union**  
You already solved sorted **union**. Someone pastes your union code and deletes the appends on the `<` / `>` branches but keeps the final “drain both leftovers” loops. What’s still wrong?

**Back 2**  
The drain loops. Intersection must **not** append remaining elements of either array — those values were never matched. Also confirm equality still advances both and emits once (union did that part right).

---

**Front 3 — Transfer / variant**  
Variant A: “Return distinct common values only.” Variant B: “Arrays are unsorted; still need multiset intersection.” How does the approach change for each?

**Back 3**  
A: Stay on two pointers; after emitting `x`, skip all consecutive duplicates of `x` on both arrays (or refuse to append if `result[-1] == x`).  
B: Sorting + two pointers, **or** build a frequency map from the smaller array and scan the other while decrementing counts — hash approach no longer needs sortedness; two-pointers alone on unsorted data is wrong.

---

## Pattern cheat map (this commit only)

| Pattern | Tip-off | Problem in this commit | Complexity | Cousin in your backlog |
|--------|---------|------------------------|------------|------------------------|
| Two-pointer merge walk — **intersection** | Two sorted arrays; common elements; optionally with multiplicity | `interesection-two-sorted-arr` | O(n+m) / O(1) extra | `union-two-sorted-arr` (same walk, opposite emit + drain) |

### Mini decision tree — sorted pair problems

```
Two sorted arrays, need a combined answer?
├─ Values in EITHER  → Union      (emit on <, >, ==; drain leftovers)
├─ Values in BOTH    → Intersection
│   ├─ with multiplicity → emit on == only; advance both; NO drain
│   └─ distinct only     → same, plus skip duplicate runs after emit
└─ Need "are they disjoint / one a subset?" → same walk, boolean state
```

---

## How this fits your Arrays arc

Yesterday’s backlog trained the **merge family** via union. Today’s commit flips the emit rule and drops the drain — a small code delta, a big recognition win in interviews. If you can narrate:

> “Sorted + two arrays → two pointers. Union emits on inequality; intersection only on equality; leftovers matter only for union.”

…you’re pattern-ready for merge-interval cousins and for “intersection of multiple sorted lists” (k-pointer / heap) later.

### Suggested 15-minute revise

1. Quiz cards only (3 min).  
2. Blind state table for Case A (7 min).  
3. On paper: write union vs intersection side-by-side rule table from memory (5 min).

---

*One new problem, one deep pattern upgrade. Fill `expected.txt`, fix the folder typo when you tidy, then keep stacking.*

> **Layout note:** lives under `PROBLEMS/Arrays/interesection-two-sorted-arr/` (moved from repo root on 2026-10-02). Same pattern family as `union-two-sorted-arr` — opposite emit rule.

# Part II — Incomplete preview

---

## 16. `two-sum` *(stub — not solved yet)*

**Path:** `PROBLEMS/Arrays/two-sum/solution.py`  
**Status:** `solve` is still `pass`; `input.txt` / `expected.txt` empty. Scaffold only.

### What it will ask (standard Two Sum)

Given an array of integers and a `target`, return the **indices** of two distinct elements that add up to `target`. Classic form assumes exactly one solution.

### Tip-offs / how you’ll recognize it

- “Two numbers that sum to target” + return **indices**
- Unsorted array
- O(n) time expected (brute O(n²) nested loops is the foil)
- Complement language: “for each x, is target−x present?”

### Pattern name(s) + why (intended)

**Hash map of value → index (complement lookup).**  
While scanning, each value `x` asks whether `target − x` was already seen. The map stores previous values’ indices so you can return both positions in one pass.

*(Sorting + two pointers can find the values, but recovering original indices needs extra bookkeeping — hash map is the clean index-friendly approach.)*

### Approach skeleton (what to implement)

1. Create an empty dict `seen` (value → index).
2. For each index `i`, value `x = nums[i]`:
   - Let `need = target − x`.
   - If `need` is in `seen`, return `[seen[need], i]`.
   - Else store `seen[x] = i`.
3. If the problem guarantees a solution, you never fall off the end; otherwise decide an error behavior.

### Concrete example (state changing)

`nums = [2, 7, 11, 15]`, `target = 9`

| `i` | `x` | `need` | `seen` before | Hit? | Action |
|-----|-----|--------|---------------|------|--------|
| 0 | 2 | 7 | {} | no | store 2→0 |
| 1 | 7 | 2 | {2:0} | **yes** | return **[0, 1]** |

### Common pitfalls / edge cases (watch when you implement)

1. **Using the same element twice** — check map *before* inserting, or ensure indices differ.
2. **Returning values instead of indices.**
3. **Duplicate values** — map keeps one index; usually fine for “one valid pair.”
4. **Empty input files in your repo** — add cases when you solve (include negatives, target 0, pair at ends).

### Complexity (target)

- **Time:** O(n) average  
- **Space:** O(n) for the map

### Quiz cards

**Front 1:** Why does “need indices + unsorted” tip you toward a hash map rather than sort + two pointers?  
**Back 1:** Sorting shuffles indices. Hash map preserves index while giving O(1) complement checks.

**Front 2:** Where in the loop do you insert into the map relative to the lookup, and why?  
**Back 2:** Lookup first, then insert — so `x` never pairs with itself at the same index when `2*x == target`.

**Front 3 (variant):** “Two Sum in a *sorted* array, return values or indices.” Alternate pattern?  
**Back 3:** Opposite-end two pointers: grow sum with `right`, shrink with `left`. If indices must refer to the original array, keep (value, index) pairs or stick with the hash approach.

**Action for you:** Implementing `two-sum` next unlocks the whole hash-map-complement family (3Sum discussion, two-sum IV in BST variants, etc.). Highest leverage unfinished item in the repo.

---

# Part III — Pattern cheat map (expanded)

| Pattern | Core tip-off | Problems in your repo | Complexity (typical) | Nearby interview cousins |
|--------|--------------|------------------------|----------------------|---------------------------|
| Single-pass running max / extrema | Need extreme value(s); unsorted | `largest-element`, `second-largest-element` | O(n)/O(1) | k-th largest (heap), third-largest |
| Accumulator / conditional count | Sum or “how many satisfy P” | `sum-arr-elements`, `count-odd-arr` | O(n)/O(1) | prefix sums, frequency maps |
| Linear search + early exit | First index of target; unsorted | `linear-search` | O(n)/O(1) | find all indices; sentinel search |
| Adjacent invariant check | Is sorted / monotonic? | `check-arr-sorted-i` | O(n)/O(1) | rotated-sorted check; one-swap sortable |
| Streak counter + reset | Longest consecutive run of X | `max-consecutive-ones` | O(n)/O(1) | longest same-char run; then sliding window with budget |
| Opposite-end two pointers (reverse) | Reverse in place | `reverse-arr` | O(n)/O(1) | reverse words; palindrome check |
| In-place cyclic shift | Rotate by 1 | `left-rotate-array-by-one` | O(n)/O(1) | right rotate by 1; buffer rotate by k |
| Block reverse rotation | Rotate by k, O(1) space | `left-rotate-array-by-k` | O(n)/O(1) | right rotate by k; rotate matrix layers |
| Write/read pointer (partition) | Move X to end; keep order; in place | `move-zeros-end` | O(n)/O(1) | separate colors (Dutch flag is related but multi-way) |
| Write pointer (unique compress) | Sorted; remove dups in place | `remove-duplicates-sorted-arr` | O(n)/O(1) | allow at most 2; remove element in place |
| Two-pointer sorted merge + dedup | Two sorted arrays → sorted union | `union-two-sorted-arr` | O(n+m)/O(n+m) | intersection; merge sorted lists |
| Sum / XOR gap in a range | Exactly one missing in 0..n | `find-missing-number` | O(n)/O(1) | find duplicate; find two missing |
| Hash-map complement *(preview)* | Two indices sum to target | `two-sum` *(stub)* | O(n)/O(n) | 3Sum, two-sum variants, subarray sum equals k |

---

# Part IV — How to revise (expanded)

### A 30-minute session template

1. **5 min — cheat map skim.** Cover the problem column; from tip-off alone, name the pattern.
2. **20 min — two deep problems.** For each: quiz cards → rebuild skeleton on paper → re-walk the example table blind → only then peek at the section.
3. **5 min — transfer.** Invent one fake prompt per pattern you touched (“longest consecutive vowels,” “move all −1s to front,” “union of three sorted arrays”). Name the pattern out loud.

### Weekly rhythm (fits your 9am revision idea)

- **Day after solving:** deep section for *new* problems only (fresh tip-offs).
- **Weekly:** re-quiz cards from older clusters without re-reading skeletons first.
- **Before interviews:** cheat map + any card you missed twice.

### Red flags you’re memorizing code (stop and reset)

- You remember variable names from `solution.py` but can’t explain *why* `written` advances.
- You can reverse an array but freeze on “reverse subarray l..r.”
- You know Two Sum’s dict approach only for that exact LeetCode number, not for “pair with given difference.”

### Green flags you’re learning patterns

- You hear “in place + preserve order + special values to the end” and instantly say “write pointer.”
- You hear “both sorted, need sorted combined uniques” and say “merge with dedup.”
- You can switch left-rotate ↔ right-rotate by adjusting reverse order or using `n−k`.

---

## Repo gaps (honest backlog notes)

1. **`two-sum` unfinished** — highest leverage next solve for hash-map patterns.
2. **Only `PROBLEMS/Arrays` exists** — no strings / linked lists / trees / recursion / DP folders yet; this pack covers 100% of what’s in the repo.
3. **Empty `expected.txt`** on several solved folders (`find-missing-number`, `left-rotate-array-by-k`, `move-zeros-end`, `remove-duplicates-sorted-arr`, `union-two-sorted-arr`, plus stub `two-sum`, and `interesection-two-sorted-arr`) — solutions look complete, but automated `dsa check` may not verify until expecteds are filled.
4. **`remove-duplicates-sorted-arr` return shape** — returns a slice; interviews/LeetCode often want integer `k`. Know both.

---

*You’ve built a solid Arrays foundation: scans → streaks → two pointers → write pointers → merge → math gap. Fill `two-sum`, then the same recognition muscles transfer hard into the next topic folders you add.*
