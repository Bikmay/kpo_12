import graf as g
import numpy as np


print("count child")
a=input()

print("count nodes")
b=input()

c=int(input())

for i in range(c):
    print(i)
    g.A.create_graf(int(a),int(b))


print("dispers alpha")
print(np.var(g.A.alphas))

print("dispers height")
print(np.var(g.A.height_graf))

print("dispers handing")
print(np.var(g.A.handing_nodes))

print("dispers count nodes")
print(np.var(g.A.count_nodes_grafs))








