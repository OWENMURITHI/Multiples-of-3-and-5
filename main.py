total = 0

maxrange = input("Enter the maximum range") #Get the maximum range from the keyboard
print("")

max = int(maxrange)

for i in range (0,max):
    if i%3 == 0 or i%5 ==0:
        total = total +i

print (total)