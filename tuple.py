# 1. Create a tuple of mixed datatype
student = (1, "Anu", 52, True)
print("Original student tuple:")
print(student)
print("-" * 30)

# 2. Perform slicing (Fixing your original syntax)
slice_Student = student[1:3]
print("Sliced tuple [1:3]:")
print(slice_Student)
print("-" * 30)

# 3. Iterate through tuple and display elements
print("Iterating through elements:")
for element in student:
    print(element)
print("-" * 30)

# 4. Perform packing
# Packing new data into a single variable
packed_student = 2, "Rahul", 88, False
print("Packed student data:")
print(packed_student)
print("-" * 30)

# 5. Perform unpacking
# Unpacking the packed tuple into individual variables
roll_no, name, marks, passed = packed_student
print("Unpacked elements:")
print("Roll No:", roll_no)
print("Name:", name)
print("Marks:", marks)
print("Passed:", passed)