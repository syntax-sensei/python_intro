fruits_list = ["apple", "banana", "orange", "apple", "grape"]
fruits_tuple = ("apple", "banana", "orange")
fruits_set = {"apple", "banana", "orange", "grape"}
fruits_dict = {"apple": 5, "banana": 3, "orange": 8, "grape": 2}

print("Membership Test for 'apple':")
print("List:", "apple" in fruits_list)
print("Tuple:", "apple" in fruits_tuple)
print("Set:", "apple" in fruits_set)
print("Dict (keys):", "apple" in fruits_dict)

print("\nLength of Each Structure:")
print("List:", len(fruits_list))     
print("Tuple:", len(fruits_tuple))   
print("Set:", len(fruits_set))       
print("Dict:", len(fruits_dict))     

print("\nIterating over List:")
for item in fruits_list:
    print(item)

print("\nIterating over Tuple:")
for item in fruits_tuple:
    print(item)

print("\nIterating over Set:")
for item in fruits_set:
    print(item)

print("\nIterating over Dict:")
for key, value in fruits_dict.items():
    print(f"{key}: {value}")

"""

Structure	Membership Check	          Performance	   Notes
List	    "apple" in fruits_list	      O(n)	           Slow for large lists (linear search)
Tuple	    "apple" in fruits_tuple	      O(n)	           Same as list
Set	        "apple" in fruits_set	      O(1)	           Very fast (uses hash table) ✅
Dict	    "apple" in fruits_dict	       O(1)	           Also fast (key lookup via hash) ✅

📝 Conclusion:

Use sets or dicts if the main goal is to test membership quickly.

Avoid using lists or tuples for large datasets where fast lookup is needed.

"""
