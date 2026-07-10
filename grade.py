def total(marks):
    return sum(marks)

def percentage(total_marks, n):
    return total_marks / n

def grade(p):
    if p >= 90:
        return "A+"
    elif p >= 75:
        return "A"
    elif p >= 60:
        return "B"
    elif p >= 50:
        return "C"
    else:
        return "F"

marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    marks.append(int(input("Enter mark: ")))

t = total(marks)
p = percentage(t, n)
g = grade(p)

print("Total marks =", t)
print("Percentage =", p)
print("Grade =", g)