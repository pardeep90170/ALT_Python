#question-> write a python programmer that takes two input from the user .
#their name and a password .
print("enter ur name")
name=input()
slicing1=name[:10]
print("enter ur password")
password=input()
slicing2=password[:6]
print(slicing1)
print(slicing2)

# GAME GENERATOR
print("Hello Welcome to game generator")
pet_name=input("Enter the your pet name:\n")
city_name=input("Enter the your city name:\n")
pet_name_slicing=pet_name[:3]
city_name_slicing=city_name[:2]
print(f"Combine the petname and city->{pet_name_slicing+city_name_slicing}")
