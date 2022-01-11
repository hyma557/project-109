import random
import plotly.express as px
import plotly.figure_factory as ff 
import statistics 

dice_result = []

for i in range(0, 1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

mean = sum(dice_result)/len(dice_result)
std = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

print(mean)
print(std)
print(mode)
print(median)

fsds, fsde = mean - std, mean + std
ssds, ssde = mean - (2*std), mean + (2*std)
tsds, tsde = mean - (3*std), mean + (3*std)
ld1s = [result for result in dice_result if result > fsds and result < fsde]
ld2s = [result for result in dice_result if result > ssds and result < ssde]
ld3s = [result for result in dice_result if result > tsds and result < tsde]

print("{}% of data lie with in first std".format(len(ld1s)*100/len(dice_result)))
print("{}% of data lie with in second std".format(len(ld2s)*100/len(dice_result)))
print("{}% of data lie with in third std".format(len(ld3s)*100/len(dice_result)))

#fig = ff.create_distplot([dice_result], ["result"], show_hist = False)
#fig.show()



