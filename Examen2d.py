import numpy as np
import matplotlib.pyplot as plt

plt.axis([-200,200,-200,200])
plt.axis('on')
plt.grid(True)
#Dibujar el circulo tomando como centro 0 y 0, junto a un radio de 40
r = 8*5
xc  = 0
yc = 0
#puntos de inicio y final
p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color=(8/10,3/10,3/10))
    xlast=xp 
    ylast=yp

#Diametro para dibujar el rectangulo  
d= r*2

#Rectangulo que cubre el circulo
x=np.array([xc+d,xc+d,xc-d,xc-d,xc+d])
y=np.array([yc+d,yc-d,yc-d,yc+d,yc+d])
plt.plot(x,y, color=(3/10,8/10,3/10))
#El otro rectangulo
x=np.array([xc,xc,xc-(d*2),xc-(d*2),xc])
y=np.array([yc,yc-(d*2),yc-(d*2),yc,yc])
plt.plot(x,y, color=(3/10,3/10,8/10))

plt.show()
