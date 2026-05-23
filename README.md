# EPAM Python Tasks Assignment

Three independent Python exercises covering classes, dictionaries, and string manipulation.

---

## Task 1 — Custom Dictionary Class

### Problem
Build a `Dictionary` class that stores word definitions and can look them up by key.

### Logic
- The class holds an internal `dict` (`_entries`) to store word-definition pairs.
- `newentry(word, definition)` assigns the definition to the word key.
- `look(word)` checks whether the word exists. If it does, the definition is returned; otherwise a formatted "Can't find entry for …" message is returned.

### Expected output
```
A fruit that grows on trees
Can't find entry for Banana
```

---

## Task 2 — How Much Will You Spend?

### Problem
Given a price dictionary, a list of purchased items, and a tax rate, calculate the total cost rounded to two decimal places. Items not found in the price dictionary are silently ignored.

### Logic
- Iterate over the purchased items list and sum only those that exist in the `costs` dictionary (unknown items are skipped via an `if item in costs` guard).
- Multiply the subtotal by `(1 + tax)` to apply the tax.
- Use `round(..., 2)` to return the result with exactly two decimal places.

### Expected output
```
70.85
```

---

## Task 3 — Nth Letter Concatenation

### Problem
Given a list of words, take the nth letter from each word (where n is the word's index in the list) and concatenate them into a single string.

### Logic
- Use `enumerate` to pair each word with its position index `n`.
- Index into each word with `word[n]` to extract the target character.
- Join all extracted characters with an empty string and return the result.
- An empty input list produces an empty string naturally.

### Expected output
```
yes

```

---

## Running the scripts

```bash
python3 dictionary.py
python3 cost.py
python3 n_letter.py
```

> Requires Python 3.6+ (f-strings used in Task 1).
