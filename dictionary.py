user_dict = {}
num_enteries = int(input("the number of enteries: "))
for i in range(num_enteries):
    print(f"\n entry #{i+1}")
    key = input("enter key: ")
    value = input("enter value: ")
    user_dict[key] = value

print(f"Raw Dictionary Object: {user_dict}")

print("Formatted Key-Value Pairs:")
for key, value in user_dict.items():
    print(f"• {key}: {value}")

access_key = input("\nEnter a key from above to access its value: ")
print(f"Accessed Value: {user_dict.get(access_key)}")

new_key = input("\nEnter a new key to add: ")
new_value = input("Enter its value: ")
user_dict[new_key] = new_value

update_key = input("\nEnter an existing key to update: ")
update_value = input("Enter its new value: ")
user_dict[update_key] = update_value

remove_key = input("\nEnter a key to remove: ")
user_dict.pop(remove_key, None)

print("\nFinal Formatted Key-Value Pairs:")
for key, value in user_dict.items():
    print(f"• {key}: {value}")