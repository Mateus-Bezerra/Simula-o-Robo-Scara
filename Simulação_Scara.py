import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from IPython import display

data = pd.read_csv("Pasta2.csv",sep=";")
print(data)

x = data.X
y = 600-data.Y

plt.plot(x, y)
plt.show()

fig = plt.figure()
traco, = plt.plot([],[],'-')
plt.xlim(0,600)
plt.ylim(0,600)
def animate(frame_num):
    
    traco.set_data(x[:frame_num + 1], y[:frame_num + 1]) 
    return traco
anim = FuncAnimation(fig, animate, frames=297, interval=20)

video = anim.to_html5_video()
html = display.HTML(video)
display.display(html)
plt.close() 