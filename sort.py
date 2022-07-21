#  sortuje alfabetycznie  podatności -s
file=open('calc.txt','r')
x = file.read().split("\n")
y = []
for i in x:
    #print(i)
    new = os.path.basename(i)
    y.append(new)

z = sorted(y)
print(z)
for i in z:
    print(i)
file.close()
