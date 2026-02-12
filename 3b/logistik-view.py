import matplotlib.pyplot as plt

x3 = 0.01
s = []
c = []
l = 0.01
for j in range(200):
    x0=x3
    for i in range(200):
        x0 = 1 - l*x0*x0
        s.append(x0)
        c.append(l)
    x3=x0
    l += 0.01

plt.plot(c,s,'r.',ms=1)
plt.show()