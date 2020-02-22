import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '5’UTR', 'Others', '3’UTR', 'CDS'
sizes = [15, 30, 45, 30]

explode = (0.06,0.06,0.05, 0.05)  # only "explode" the 2nd slice (i.e. 'Hogs')
colors = ["#CC7033","#C4573C","#6BA25E","#4474BB"]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        colors=colors, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
