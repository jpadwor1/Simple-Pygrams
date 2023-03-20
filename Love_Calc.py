print("Welcome to the Love Calculator!")
name_1 = input("What is your name?")
name_2 = input("What is their name?")
combined_name = name_1 + name_2
name = combined_name.lower()
t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
true = t + r + u + e

l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')
love = l + o + v + e

score = int(str(true) + str(love))

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score <= 50 and score >= 40:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

