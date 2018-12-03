import graf as g
import numpy as np


f=open("out2.txt")

print("count child")
a=input()

print("count nodes")
b=input()

c=int(input())

for i in range(c):
    print(i)
    g.A.create_graf(int(a),int(b))

print("alphas")
print(g.A.alphas)

f.write("alphas")
f.write(g.A.alphas+'\n')

print("aver alphas")
print(g.A.sum(g.A.alphas)/len(g.A.alphas))

f.write("aver alphas")
f.write(g.A.sum(g.A.alphas)/len(g.A.alphas)+'\n')


print("dispers height")
print(np.var(g.A.height_graf))

f.write("dispers height")
f.write(np.var(g.A.height_graf)+'\n')

print("aver height")
print(g.A.sum(g.A.height_graf)/len(g.A.height_graf))

f.write("aver height")
f.write(g.A.sum(g.A.height_graf)/len(g.A.height_graf)+'\n')


print("dispers handing")
print(np.var(g.A.handing_nodes))



print("aver handing")
print(g.A.sum(g.A.handing_nodes)/len(g.A.handing_nodes))


print("dispers count nodes")
print(np.var(g.A.count_nodes_grafs))

print("aver count nodes")
print(g.A.sum(g.A.count_nodes_grafs)/len(g.A.count_nodes_grafs))








