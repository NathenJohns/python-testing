
is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not (is_male) and is_tall:
    print("You are a not a male but are tall")   
else:
    print("You are either not male not tall or both")


# Can use 'and' both conditions need to be true
# Can use 'or' where one only needs to be true
