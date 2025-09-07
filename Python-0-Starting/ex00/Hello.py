ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
#list is an ordered and mutable collection of elements, supports duplicates and changing.
#we can access the elements by their index in the list and update them directly
ft_list[1] = "World"

#tuple is an ordered and immutable collection, elements can't be changed after creation
#to change an element we need to overwrite the whole content of a tuple
ft_tuple = ("Hello", "United Arab Emirates!")

#set is an unordered and unique collection
#if we need to update an element, we have to remove it and add the new element
ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!")

#dict is dictionary which is a mutable collection of key-value pairs
#we can update the key value, add a new key-value and delete a key and access key value safely.
ft_dict["Hello"] = "42AbuDhabi!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)