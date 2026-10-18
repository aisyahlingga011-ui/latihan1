grade = 70

# if else biasa
if grade >= 65:
    print("passed the exam")
else:
    print("below the passing grade")

# one-line / sebaris
if grade >= 65: print("passed the exam")
if grade < 65: print("below the passing grade")

# ternary
print("passed the exam") if grade >= 65 else print("below the passing grade")

# ternary dengan nilai balik
message = "passed the exam" if grade >= 65 else "below the passing grade"
print(message)