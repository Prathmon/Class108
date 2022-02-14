import random
import plotly.express as px

count = []
dice = []

for i in range(0, 100) :
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice.append(dice1 + dice2)
    count.append(i)

print(count, dice)

graph = px.bar(x = dice, y = count)
graph.show()