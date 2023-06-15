import matplotlib.pyplot as plt
import serial
ser=serial.Serial('COM6',9600)
fig=plt.figure(figsize=(10,7))
ax=fig.add_subplot()

fig.show()
x=[]
y=[]
i=0
l=200
ser.close()
ser.open()

while True:
    ser1=ser.readline().decode('ascii')
    ser2=float(ser1)
    x.append(i)
    y.append(ser2)
    ax.plot(x,y,color = 'b')
    fig.canvas.draw()
    ax.set_xlim(left=max(0,i-30),right=i+60)
    i+=1
    plt.pause(0.0001)


plt.show()
    
