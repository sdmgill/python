#5-1
print('"Section 5-1"')
car = 'subaru'
print("Is car == 'subaru'?. I predict True.")
print (car=='subaru')

print("Is car == 'audi'?. I predict False.")
print (car=='audi')

#5-2
print('\n"Section 5-2"')
car = 'BmW'
if car.lower() == 'bmw':
	print("We have a winner")
else:
	print("We have a loser")


car = 'BmW'
if car.lower() != 'bmw':
	print("\nWe have a winner")
else:
	print("\nWe have a loser")
	
length = 21
width = 28
if length == 21 and width == 21:
	print("\nWe have a Square.")
if length ==21 or width == 21:
	print("\nWe have a rectangle due to an 'or'.")
if length == 21 and width != 21:
	print("\nWe have a rectangle due to a '!='.")
else:
	print("\nWe have something else.")
	
bug_list = ['spider','ant','scorpion','killer bees']
bug = 'ant'
if bug in bug_list:
	print("\nCall Orkin")
else:
	print("\nCall in the bomb squad")
	
#5-3
print('\n"Section 5-3"')
alien_color = 'green'
if alien_color == 'green':
	print("You have been awarded 5 points!")
	
alien_color = 'red'
if alien_color == 'green':
	print("You have been awarded 5 points!")
	
#5-4
print('\n"Section 5-4"')
alien_color = 'green'
if alien_color == 'green':
	print("You have been awarded 5 points!")
elif alien_color != 'green':
	print("You have been awarded 10 points!")
	
alien_color = 'red'
if alien_color == 'green':
	print("\nYou have been awarded 5 points!")
elif alien_color != 'green':
	print("\nYou have been awarded 10 points!")
	
#5-5
print('\n"Section 5-5"')
alien_color = 'green'
if alien_color == 'green':
	print("You have been awarded 5 points!")
elif alien_color == 'yellow':
	print("You have been awarded 10 points!")
elif alien_color == 'red':
	print("You have been awarded 15 points!")
	
alien_color = 'yellow'
if alien_color == 'green':
	print("You have been awarded 5 points!")
elif alien_color == 'yellow':
	print("You have been awarded 10 points!")
elif alien_color == 'red':
	print("You have been awarded 15 points!")
	
alien_color = 'red'
if alien_color == 'green':
	print("You have been awarded 5 points!")
elif alien_color == 'yellow':
	print("You have been awarded 10 points!")
elif alien_color == 'red':
	print("You have been awarded 15 points!")
	
#5-6
print('\n"Section 5-6"')
age = 54
if age < 2:
	sol = 'baby'
elif age < 4:
	sol  = 'todler'
elif age < 13:
	sol = 'kid'
elif age < 20:
	sol = 'teenager'
elif age < 65:
	sol = 'adult'
elif age >=65:
	sol='old fuck'
	
print("You and a " + sol + " because you are " + str(age) + " years old.")

#5-7
print('\n"Section 5-7"')
favorite_fruits = ['apples','bananas','oranges']
if 'apples' in favorite_fruits:
	print("You really like apples.")
if 'pineapples' in favorite_fruits:
	print("You really like pineapples.")
if 'oranges' in favorite_fruits:
	print("You really like oranges.")
if 'kiwis' in favorite_fruits:
	print("You really like kiwis.")
if 'bananas' in favorite_fruits:
	print("You really like bananas.")
	
#5-8
print('\n"Section 5-8"')
user_names = ['sean','dinna','connor','bulldog','admin']
for user_name in user_names:
	if user_name.lower() == 'admin':
		print("Hello " + user_name.title() + ", would you like to see a Status Report?")
	else:
		print("Hello " + user_name.title() + ", thank you for logging in again.")
		
#5-9
print('\n"Section 5-9"')
#user_names = ['sean','dinna','connor','bulldog','admin']
user_names = []
if user_names:
	for user_name in user_names:
		if user_name.lower() == 'admin':
			print("Hello " + user_name.title() + ", would you like to see a Status Report?")
		else:
			print("Hello " + user_name.title() + ", thank you for logging in again.")
else:
	print("We need to get some users!!")
	
#5-10
print('\n"Section 5-10"')
current_users =['sean','dinna','connor','bulldog']
new_users = ['Dinna','Bulldog','John','Mary']
for new_user in new_users:
	if new_user.lower() in current_users:
		print("Sorry " + new_user.title() + ", that username is already taken. Please choose another.")
	else:
		print("Your username has been accepted. For your records, your username is " + new_user.title() + ".")
		
#5-11
print('\n"Section 5-11"')
ord_list = list(range(1,10))
for num in ord_list:
	if num == 1:
		print(str(num) + "st")
	elif num == 2:
		print(str(num) + "nd")
	elif num == 3:
		print(str(num) + "rd")
	else:
		print(str(num) + "th")

print('\n"Section 5-11 a more gooder way"')	
ord_list = list(range(1,10))
for num in ord_list:
	if num == 1:
		suf='st'
	elif num == 2:
		suf='nd'
	elif num == 3:
		suf='rd'
	else:
		suf='th'
	print(str(num) + suf)
	

	
	
	

