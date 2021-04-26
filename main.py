total = 0

minRange = input("Enter the minimum range")
maxRange = input("Enter the maximum range") #Get the maximum range from the keyboard
print("")

min = int(minRange)
max = int(maxRange)

for i in range (min,max):
    if i%3 == 0 or i%5 ==0:
        total = total +i

print (total)