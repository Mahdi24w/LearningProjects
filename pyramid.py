

x = int(input("enter the height from 1 to 10: \n"))

while x < 1 or x > 10:
    x = int(input("enter the height only between 1 and 10: \n"))

if (x >= 1 and x <= 10):
    for i in range(1,x+1):
        print(" "*x + "#"*i + " "*2 + "#"*i)
        x-=1
