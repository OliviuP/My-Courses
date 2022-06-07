# 3.	Given dictionary
numbers = {1: 'one', 2: 'two', 3: 'three'}


# a.	Use len() to print out its length.
print(len(numbers))
# b.	Using set-item operator [], add a new key-pair: 4:"four".
numbers['4'] = 'four'
print(numbers)
# c.	Using get-item operator [], print out the value assigned to key 2.
print(numbers.get(2))

# d.	Using get-item operator [], print out value for unassigned key, like 10. What happens?
print(numbers.get(10, "not found"))  # none
# e.	Using dictionary function get(key), replace the previous get-item operator 􀏞􀏟 and print out the value for key 10. What happens?
print(numbers.get(10))
# f.	Using dictionary function get(key, default), print out the value for key 10, this time setting default value to "unknown".
print(numbers.get(10, 'unknown'))
# g.	Using dictionary function get(key, default), print out the value for key 3. Set default value to "unknown".
print(numbers.get(3, 'unknown'))
# h.	Use pop() to print out value assigned to 2. Print out the dictionary after using pop()
print(numbers.pop(2))
print(numbers)
# i.	Create a new dictionary {0: “zero”}. Using update(), update main dictionary with values from the new dictionary. Print out the main dictionary.
nb = {0: 'zero'}
numbers.update(nb)
print(numbers)
# j.	Using clear(), clear the dictionary.3.	Given dictionary {1: “one”, 2”two”, 3: “three”}:

numbers.clear()
print(numbers)

print(24*12)
