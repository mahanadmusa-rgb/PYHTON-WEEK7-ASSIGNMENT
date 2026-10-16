# Week 7 Assignment: Hands-On Lab — Shopping List Manager

This repository contains my Python Week 7 assignment for Power Learn Project (PLP).

## Files

- `list_warmup.py` — Demonstrates list indexing, append, remove, and len.
- `shopping_list.py` — An interactive shopping list manager with add, remove, show, and done options.
- `list_report.py` — Prints a numbered list, counts item names with more than four letters, and finds the longest name using a loop.
- `screenshots/` — Contains screenshots showing the output of each program.

## Why check `in` before using `.remove()`?

Checking whether an item is in the list before calling `.remove()` makes the program safer. If the item is missing, `.remove()` raises a `ValueError`. Using `in` allows the program to display a helpful message instead of crashing.

## How to run

Run each program using Python:

```bash
python list_warmup.py
python shopping_list.py
python list_report.py
```