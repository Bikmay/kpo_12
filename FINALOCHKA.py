from matplotlib import pyplot as plt
import graf as g

# x = [1, 2, 3, 5]
# y = [1, 2, 3, 8]
#
# plt.plot(x, y, 'r')
# plt.grid(True, linestyle='-', color='0.75')
# plt.show()

print("count child")
a=input()

print("count nodes")
b=input()

g.A.create_graf(int(a), int(b), True, True)

x = g.A.nodes_count_on_each
print("x")
print(x)

y = g.A.alphas_on_each
print("y")
print(y)

plt.plot(x, y, 'r')
plt.grid(True, linestyle='-', color='0.75')
plt.show()