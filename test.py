import matplotlib.pyplot as plt
from database import Database
from imessage import Chat
from imessage import Recipient

db = Database("/Users/john/Library/Messages/chat.db")

word = input("> ")
chat = Chat("+14084311571", "chat976120161778148208")
data = db.getCountForWord(chat, word)
displayName = chat.getDisplayname()

labels = [Recipient(d[1]).getName() + ": " + str(d[0]) for d in data]
total = sum([d[0] for d in data])
sizes = [d[0]/total for d in data]

print(labels)
# print(sizes)
print(total)

# for d in data:
#   print(d)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
explode = [0] * len(labels)  # only "explode" the 2nd slice (i.e. 'Hogs')
explode[sizes.index(max(sizes))] = 0.05
explode = tuple(explode)

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)
ax1.set_title("\"{0}\" in {1}".format(word, displayName))
#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
plt.savefig("image.png",bbox_inches='tight',dpi=300)
# plt.show()

class Example:
  def __repr__(self): # __repr__ implementation
    return "Hello!"

exampleInstance = Example() # Create an instance of Example
testVariable = str(exampleInstance) # Variable would now contain string "Hello!"
print(exampleInstance) # Would print Hello! to the console
print(exampleInstance.__repr__()) # Would also print Hello! to the console