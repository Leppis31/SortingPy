import random
import time

class GenerateDataClass:
    def __init__(self, size) -> None:
        self.size = size

    def Generate_data(self) -> int:
        data = [random.randint(0, 1000000) for _ in range(self.size)]
        return data

class QuickSortClass:
    def __init__(self, data) -> None:
        self.data = data

    def quickSort(self, data) -> int:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.quickSort(left) + middle + self.quickSort(right)

    def quickSortMain(self) -> float:
        startTime = time.time()
        sortedData = self.quickSort(self.data)
        endTime = time.time()
        executionTime = endTime - startTime
        text = "-----------QuickSort-----------"
        tiedosto = Write("tiedosto.txt", executionTime, sortedData, text, 0, 0, 0)
        tiedosto.writeNumbers()
        return executionTime

class MedianOfThreeClass:
    def __init__(self, data) -> None:
        self.data = data

    def quickSortMedian(self, data) -> int:
        if len(data) <= 1:
            return data
        pivot = self.medianOfThree(data)
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.quickSortMedian(left) + middle + self.quickSortMedian(right)

    def medianOfThree(self, array) -> int:
        first = array[0]
        mid = array[len(array) // 2]
        last = array[-1]
        return sorted([first, mid, last])[1]

    def medianOfThreeMain(self) -> float:
        startTime = time.time()
        sortedData = self.quickSortMedian(self.data)
        endTime = time.time()
        executionTime = endTime - startTime
        text = "\n\n-----------MedianOfThree-----------"
        tiedosto = Write("tiedosto.txt", executionTime, sortedData, text, 0, 0, 0)
        tiedosto.writeNumbers()
        return executionTime

class InsertionSort:
    def __init__(self, data, threshold, thresholds=[]) -> None:
        self.data = data
        self.threshold = threshold
        self.thresholds = thresholds

    def quicksortInsertion(self, data) -> int:
        if len(data) <= self.threshold:
            return self.insertionSort(data)
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.quicksortInsertion(left) + middle + self.quicksortInsertion(right)

    def insertionSort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    def thresHoldTester(self) -> int:
        nopeinAika = float('inf')
        thresholdValue = 0
        for threshold in self.thresholds:
            self.threshold = threshold
            startTime = time.time()
            self.quicksortInsertion(self.data)
            endTime = time.time()
            executionTime = endTime - startTime
            if nopeinAika > executionTime:
                thresholdValue = threshold
                nopeinAika = executionTime
        print(f"Nopein threshold arvo on: {thresholdValue}, nopeudella {nopeinAika}s")
        return thresholdValue

    def InsertionSortMain(self) -> float:
        startTime = time.time()
        sortedData = self.quicksortInsertion(self.data)
        endTime = time.time()
        executionTime = endTime - startTime
        text = "\n\n-----------InsertionSort-----------"
        tiedosto = Write("tiedosto.txt", executionTime, sortedData, text, 0, 0, 0)
        tiedosto.writeNumbers()
        return executionTime

class Write:
    def __init__(self, filename, time, data, sortType, timeDif, timedif2, timedif3) -> None:
        self.filename = filename
        self.time = time
        self.data = data
        self.sortType = sortType
        self.timeDif = timeDif
        self.timedif2 = timedif2
        self.timedif3 = timedif3

    def writeNumbers(self) -> None:
        with open(self.filename, 'a') as file:
            file.write(self.sortType + '\n')
            for i in self.data:
                file.write(str(i) + ' ')

    def writeTimeStat(self) -> None:
        with open(self.filename, 'a') as file:
            if self.timeDif > 0:
                file.write(f"\n\nQuickSort VS MedianOfThree: {self.timeDif}s\n")
                file.write(f"QuickSort VS Inserted: {self.timedif2}s\n")
                file.write(f"MedianOfThree VS Inserted: {self.timedif3}s\n")
            else:
                file.write(f"\n\n{self.sortType} Aika: {self.time}s\n")

class Main:
    def __init__(self) -> None:
        generateData = GenerateDataClass(75000)
        data = generateData.Generate_data()

        quicksort = QuickSortClass(data)
        mediaofthree = MedianOfThreeClass(data)

        thresholds = [5, 10, 15, 20, 100]
        insertionsort = InsertionSort(data, 0, thresholds)
        threshold = insertionsort.thresHoldTester()
        insertionsort = InsertionSort(data, threshold)

        timeQuickSort = quicksort.quickSortMain()
        timeMediaOfThree = mediaofthree.medianOfThreeMain()
        timeInsertionSort = insertionsort.InsertionSortMain()

        timeDif = timeQuickSort - timeMediaOfThree
        timeDifQuickSortVsInsert = timeQuickSort - timeInsertionSort
        timeDifMediaVsInsert = timeMediaOfThree - timeInsertionSort

        tiedosto1 = Write("tiedosto.txt", timeQuickSort, [], "QuickSortClass", 0, 0, 0)
        tiedosto2 = Write("tiedosto.txt", timeMediaOfThree, [], "MedianOfThreeClass", 0, 0, 0)
        tiedosto3 = Write("tiedosto.txt", timeInsertionSort, [], "InsertionSortClass", 0, 0, 0)
        tiedosto4 = Write("tiedosto.txt", 0, [], "AikaErot", timeDif, timeDifQuickSortVsInsert, timeDifMediaVsInsert)

        tiedosto1.writeTimeStat()
        tiedosto2.writeTimeStat()
        tiedosto3.writeTimeStat()
        tiedosto4.writeTimeStat()

if __name__ == "__main__":
    app = Main()