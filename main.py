import graf as g
import numpy as np


f=open("out2.txt", 'w')

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

f.write("alphas ")
f.write(str(g.A.alphas) + '\n')

print("aver alphas")
print(g.A.sum(g.A.alphas)/len(g.A.alphas))

print("dispers alphas")
print(str(np.var(g.A.alphas)))

f.write("aver alphas ")
f.write(str(g.A.sum(g.A.alphas)/len(g.A.alphas))+'\n')


print("dispers height")
print(str(np.var(g.A.height_graf)))

f.write("dispers height ")
f.write(str(np.var(g.A.height_graf)) + '\n')

print("aver height")
print(g.A.sum(g.A.height_graf)/len(g.A.height_graf))

f.write("aver height ")
f.write(str(g.A.sum(g.A.height_graf)/len(g.A.height_graf))+'\n')


print("dispers handing")
print(np.var(g.A.handing_nodes))

f.write("dispers handing ")
f.write(str(np.var(g.A.handing_nodes))+'\n')



print("aver handing")
print(g.A.sum(g.A.handing_nodes)/len(g.A.handing_nodes))

f.write("aver handing ")
f.write(str(g.A.sum(g.A.handing_nodes)/len(g.A.handing_nodes))+'\n')


print("dispers count nodes")
print(np.var(g.A.count_nodes_grafs))

f.write("dispers count nodes ")
f.write(str(np.var(g.A.count_nodes_grafs))+'\n')

print("aver count nodes")
print(g.A.sum(g.A.count_nodes_grafs)/len(g.A.count_nodes_grafs))

f.write("aver count nodes ")
f.write(str(g.A.sum(g.A.count_nodes_grafs)/len(g.A.count_nodes_grafs))+'\n')


f.write("count nodes ")
f.write(str(g.A.count_nodes_grafs) + "\n")

f.write("count handing nodes ")
f.write(str(g.A.handing_nodes)+"\n")

f.write("levels grafs ")
f.write(str(g.A.height_graf) + "\n")






