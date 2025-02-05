
old_list = input("Enter list of values: ").split()

new_list = list(set(old_list))

print("Original List:", old_list)
print("List without Duplicates:", new_list)