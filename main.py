import csv, os
import matplotlib.pyplot as plt

class video:
    def __init__(self, views, likes, titles):
        self.views = views
        self.likes = likes
        self.titles = titles

    def openAIParse(self):

def classConst():

def readFile():
    dir = r"FILL IN DIR FOR PROJECT"
    files = os.listdir(dir)
    country_nodes = ["United States",
                     "Great Britain",
                     "India", "Denmark",
                     "Canada", "France",
                     "Korea", "Russia",
                     "Japan", "Mexico"]
    for ind, f in enumerate(files):
        file_path = os.path.join(dir, f)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                csv_data = list(csv_reader)
            viewsArr = []
            likesArr = []
            titles = []
            for index, elem in enumerate(csv_data):
                for i, _ in enumerate(elem):
                    if index != 0:
                        if i == 1:
                            titles.append(_)
                        if i == 2:
                            viewsArr.append(int(_))
                        if i == 3:
                            likesArr.append(int(_))
            dataArr = []
            for i, e in enumerate(viewsArr):
                dataArr.append([likesArr[i], e, titles[i]])
            data = dataAnalysis(dataArr)
            l1 = []
            l2 = []
            for i, e in enumerate(data):
                l1.append(e[0])
                l2.append(e[1])
            deltaL1 = rateOfChange(l1)
            deltaL2 = rateOfChange(l2)

            averageDeltaX = average(deltaL1)
            averageDeltaY = average(deltaL2)

            slope1 = (averageDeltaY / averageDeltaX)
            constant1 = l2[0]

            bestFitLine1 = bestFitElements(slope1, l1, constant1)

            graph(data, country_nodes[ind], bestFitLine1)
            saveData(data, country_nodes[ind], f)
        except:
            continue

def selectionSort(Array):
    newArray = Array.copy()
    for j in range(len(newArray)):
        iMin = j
        for i in range(j+1, len(newArray)):
            if newArray[i][0]<newArray[iMin][0]:
                iMin = i
        if iMin != j:
            temp = newArray[iMin]
            newArray[iMin] = newArray[j]
            newArray[j] = temp
    return newArray

#used for finding best fit line
def rateOfChange(array):
    arrayout = []
    for i, e in enumerate(array[1:]):
        arrayout.append(e-array[i-1])
    return arrayout

def average(array):
    sum = 0
    for i in array:
        sum+=i
    return sum/len(array)

def bestFitElements(averageDelta, Y, constant):
    l = []
    for i, e in enumerate(Y):
        l.append(e*averageDelta+constant)
    return l

#sorts the data
def dataAnalysis(data):
    dataArray = selectionSort(data)
    minRat = 2*31-1
    minVid = ""
    greatRat = 0
    greatVid = ""
    for i in range(len(dataArray) - 1, -1, -1):
        e = dataArray[i]
        try:
            ratio = e[1] / e[0]
            if minRat > ratio:
                minRat = ratio
                minVid = e[2]
            if greatRat < ratio:
                greatRat = ratio
                greatVid = e[2]
            dataArray[i].append(ratio)
        except:
            dataArray.pop(i)
    if len(dataArray)>0:
        print("greatest ratio")
        print(greatRat)
        print(greatVid)
        print("smallest ratio")
        print(minRat)
        print(minVid)
        print("--------------------------------------------------------------------")
    return dataArray

def graph(data, i, bestFitLine1):
    dataX = []
    dataY = []
    ratio = []
    for e in data:
        dataX.append(e[0])
        dataY.append(e[1])
        ratio.append(e[3])
    plt.plot(dataX, dataY, label = "views vs likes")
    plt.plot(dataX, bestFitLine1, label = "best fit line")
    plt.xlabel("likes")
    plt.ylabel("views")
    plt.legend(loc = "upper right")
    plt.title(f"{i} views vs likes")
    plt.show()
    plt.plot(dataX, ratio, label = "views/likes vs likes")
    plt.xlabel("likes")
    plt.ylabel("views/likes")
    plt.legend(loc = "upper right")
    plt.title(f"{i} ratio vs likes")
    plt.show()

def saveData(data, country, file):
    with open("data.txt", "a", encoding="utf-16") as f:
        if country == "United States\n":
            f.write(file[0:8])
        f.write(f"{country}\n")
        for i in data:
            f.write(f"{str(i)}\n")

if __name__ == "__main__":
    readFile()
