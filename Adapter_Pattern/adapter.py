from abc import abstractmethod

class ScoreOperation():
    @abstractmethod
    def sort(self, array):
        pass

    @abstractmethod
    def search(self, array, key):
        pass

#adaptee
class QickSort():    
    def quickSort(self, array):
        self.sort(array, 0, len(array)-1)
        return array

    def sort(self, array, p, r):
        q = 0
        if(p<q):
            q = self.partition(array, p, r)
            self.sort(array, p, q-1)
            self.sort(array, q+1, r)

    def partition(self, a, p, r):
        x = a[r]
        j = p-1
        for i in range(p, r):
            if a[i] <= x:
                j += 1
                self.swap(a, j, i)
        self.swap(a, j+1, r)
        return j+1

    def swap(self, a, i, j):
        t = a[i]
        a[i] = a[j]
        a[j] = t

# adaptee
class BinarySearch():
    def binarySearch(self, array, key):
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) / 2
            midVal = array[mid]
            if midVal < key:
                low = mid + 1
            elif midVal > key:
                high = mid - 1
            else:
                return 1
        return -1

class OperationAdapter(ScoreOperation):
    def __init__(self):
        self.sortObj = QickSort()
        self.searchObj = BinarySearch()

    def sort(self, array):
        return self.sortObj.quickSort(array)

    def search(self, array, key):
        return self.searchObj.binarySearch(array, key) 