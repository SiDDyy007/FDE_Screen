# 📦 Package Sorter - Thoughtful Robotics

This project contains a function for Thoughtful’s robotic automation factory to sort packages based on their dimensions and mass into appropriate stacks.

## 🧠 Sorting Rules

Each package is classified into one of three stacks:

- **STANDARD**: Not bulky and not heavy.
- **SPECIAL**: Either bulky or heavy.
- **REJECTED**: Both bulky and heavy.

### Definitions

- A package is **bulky** if:
  - Volume ≥ 1,000,000 cm³ **OR**
  - Any dimension (width, height, or length) ≥ 150 cm
- A package is **heavy** if:
  - Mass ≥ 20 kg

---

## 📁 File Structure

```
.
├── main.py      # Contains the core sort function
└── test.py      # Contains test cases using print statements
```

---

## 🚀 How to Run

1. **Run the sorter:**

```bash
python3 main.py
```

2. **Run test cases:**

```bash
python3 test.py
```

You’ll see the output classifications and error handling in action.

---

## 🧪 Example Output

```text
SPECIAL
SPECIAL
SPECIAL
REJECTED
STANDARD
SPECIAL
SPECIAL
STANDARD
SPECIAL
REJECTED
Error: Dimensions and mass must be non-negative numbers
Error: Dimensions and mass must be non-negative numbers
```

---

## ✅ Requirements

- Python 3.6+

No external dependencies required.
