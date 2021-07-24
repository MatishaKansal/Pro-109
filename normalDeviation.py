import statistics
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()


mean = statistics.mean(data)
print("mean is " + str(mean))

median = statistics.median(data)
print("median is " + str(median))

mode = statistics.mode(data)
print("mode is " + str(mode))

stdev = statistics.stdev(data)
print("standard deviation is " + str(stdev))

firststdev_start, firststdev_end = mean - stdev, mean + stdev
secstdev_start, secstdev_end = mean - (2*stdev), mean + (2*stdev)
thirdstdev_start, thirdstdev_end = mean - (3 *stdev), mean + (3 *stdev)

list_of_onestdev = [result for result in data if result > firststdev_start and result < firststdev_end]
list_of_twostdev = [result for result in data if result > secstdev_start and result < secstdev_end]
list_of_threestdev = [result for result in data if result > thirdstdev_start and result < thirdstdev_end]

print("{}%  of data lies within one standard deviation".format((len(list_of_onestdev)*100/len(data))))
print("{}%  of data lies within second standard deviation".format((len(list_of_twostdev)*100/len(data))))
print("{}%  of data lies within third standard deviation".format((len(list_of_threestdev)*100/len(data))))