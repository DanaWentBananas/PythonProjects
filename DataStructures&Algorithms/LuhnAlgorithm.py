x = list(input("Enter number"))

p = int(x.pop())

x.reverse()

for i,ding in enumerate(x):
    x[i] = int(x[i])
    if i%2==0:
        x[i]=x[i]*2
        if x[i]>9:
            x[i] = x[i] - 9

print(x)

summ = p + sum(x)

    
if summ%10==0:
    print("valid")
else:
    print("not valid")
