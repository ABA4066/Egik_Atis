import math

from textdistance import cosine

Xilk=float(input("\nX₀ Değerini Girin(m)\n"))
Yilk=float(input("\nY₀ Değerini Girin(m)\n"))
V=float(input("\nV₀ Değerini Girin(m/s²)\n"))
aci=float(input("\nθ₀ Değerini Girin(°)\n"))
t=float(input("\nt Değerini Girin(s)\n"))

aci=math.radians(aci)
Vx=V*math.cos(aci)
Vy=V*math.sin(aci)

y=Yilk+Vy*t+0.5*(-9.81)*(t**2)
x=Xilk+Vx*t
h=(Vy**2)/(9.81)
R=(2*Vx*Vy)/(9.81)

print("\nX Konumu: {}m dir\n".format(x))
print("\nY Konumu: {}m dir\n".format(y))
print("\nMax Yükseklik: {}m dir\n".format(h))
print("\nMenzil: {}m dir\n".format(R))