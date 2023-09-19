n=int(input())
#take n lines of input its a name and 3 numbers separated by space
#store it in a dictionary
d={}
for i in range(n):
    s=input()
    l=s.split()
    d[l[0]]=l[1:]
#take a name as input and print the average of the 3 numbers
name=input()
l=d[name]
sum=0
for i in l:
    sum+=float(i)
print("{0:.2f}".format(sum/3))
