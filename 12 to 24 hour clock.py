t_12 = int(input("Enter current time in 0000 format"))
Day= int(input("Enter '1' for day '0'for night"))

if Day == 0:
    t_24 = t_12 + 1200
else:
    t_24 = t_12

print ("The current time in 24 hours is %.2i" %t_24)