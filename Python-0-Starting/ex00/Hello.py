#list is an ordered and mutable collection of elements, supports duplicates and direct changing
ft_list = ["Hello", "tata!"]
#tuple is an ordered and immutable collection, elements can't be changed after creation
ft_tuple = ("Hello", "toto!")
#set is an unordered and unique collection, doesn't support direct changing, we need to remove first
ft_set = {"Hello", "tutu!"}
#dict (dictionary) is an ordered and mutable collection of key-value pairs, supports direct changing
ft_dict = {"Hello" : "titi!"}

#your code here
#we can access the elements by their index in the list and update them directly
ft_list[1] = "World!"

#to change an element we need to overwrite the whole content of a tuple
ft_tuple = ("Hello", "United Arab Emirates!")

#if we need to update an element, we have to remove it and add the new element
ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!")

#we can update the key value, add a new key-value and delete a key and access key value safely.
ft_dict["Hello"] = "42AbuDhabi!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)