#Topics: #CLIInputs #StringLowerMethod #StringCountMethod #TypeCasting #if-elif-else #ConditionalOperators #fstring

name1 = input("What is your name?\n")
name2 = input("What is your (present/expected) partner's name?\n")
print("The Love Calculator is calculating your score...")
combined_name = (name1 + name2).lower()
t_count=combined_name.count("t")
r_count=combined_name.count("r")
u_count=combined_name.count("u")
e_count=combined_name.count("e")
l_count=combined_name.count("l")
o_count=combined_name.count("o")
v_count=combined_name.count("v")
e_count=combined_name.count("e")

love_score = int(str(t_count+r_count+u_count+e_count) + str(l_count+o_count+v_count+e_count))

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
