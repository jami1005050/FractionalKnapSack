#Date: 09/30/2019
#Class: CS5310
#Assignment: Fractional Knapsack
#Author(s): Mohammad Jaminur Islam



try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
from src.dataItem import DataItem


def getNumericOnly():
    # print("enter a number")
    value = input()
    while not value.isnumeric():
        value = input("This is not a numeric input please enter a numeric number again")
    return value

class FractionalKanpSack(object):
    def __init__(self,capacity):
        # self.data = [] #item array
        self.data =Q.PriorityQueue()
        self.capacity = capacity #maximum weight we can carry

    def insert_item(self,value): #item insert
        if(isinstance(value,DataItem)):
            # heapq.heappush(self.data, value)
            self.data.put( value)



    def pop_item(self): #item pop with index
        if(self.data.qsize()>0):
            # return heapq.heappop(self.data)
            return self.data.get()

    def execute_fractional_kanp_sack(self): #algorithm implementation
        if (self.data.qsize()) == 0: #check if there is no available item then no execution
            return
        profit_max_weight = 0 #total weight we can take
        result = [] #the items that will be taken
        total_benefit =0 #total benefit from the taken item
        while profit_max_weight < self.capacity: #check if the total item taken is over the size of the kanpsack
            item = self.pop_item()
            if(isinstance(item,DataItem)): #check if the item is the considered type of object
                item.amount_taken = min(item.item_weight,self.capacity-profit_max_weight) #amount to be taken for items
                result.append(item) # add the item to the resulted list
                total_benefit = total_benefit + item.amount_taken * item.per_weight_value*(-1) #cumulative benefits
                profit_max_weight = profit_max_weight + min(item.item_weight,self.capacity-profit_max_weight) #cumulative weight
                # print("Incremental weight for each step is: ",profit_max_weight)
                # print("Incremental benefit for each step is:",total_benefit)
        # print("The final benefit for fractional knapsack : ",total_benefit)
        # print("The final weight for fractional knapsack : ",profit_max_weight)
        return Result(result,total_benefit,profit_max_weight) #return the Result class

class Result: # a temporary class to hold the result of the kanpsack algorithm
    def __init__(self,result,total_benefit,profit_max_weight):
        self.result = result #array of object that has been taken during knapsack process
        self.total_benefit = total_benefit #total benefit
        self.profit_max_weight = profit_max_weight #total max weight


if __name__ =="__main__":
    print("input the number of times you want to run the test")
    try:
        numberOftest = int(getNumericOnly())  # user input for no of test
        loopCounter = 0
        while (loopCounter < numberOftest):
            print("For Test case: ", loopCounter + 1)
            print("provide the capacity of the knapsack")
            try:
                capacity = float(getNumericOnly())  # capacity user input for kanpsack
            except ValueError:
                print("That's not an number!")
            fractionalKanpSack = FractionalKanpSack(capacity)  # white creating the knapsack object you need to provide the capacity of the knapsack
            print("Provide the number of items are available in the ")

            try:
                numberOfItems = int(getNumericOnly())  # number of available item input
                itemCounter = 0
                while itemCounter < numberOfItems:
                    print("Provide the item weight")
                    try:
                        itemWeight = float(getNumericOnly())
                    except ValueError:
                        print("That's not an number!")
                    print("Provide the item value")
                    try:
                        itemValue = float(getNumericOnly())
                    except ValueError:
                        print("That's not an number!")
                    item1 = DataItem(itemWeight, itemValue)  # define a Data item passing the weight and value
                    fractionalKanpSack.insert_item(item1)  # insert in the priority queue
                    itemCounter = itemCounter + 1  # increment to take next inputs
                result = fractionalKanpSack.execute_fractional_kanp_sack()  # call to algorithm

                if (isinstance(result, Result)):
                    print("max_benifit: ", result.total_benefit)  # total benefit

                    if len(result.result) > 0:
                        for ele in result.result:
                            print("Amount taken from item: ", ele.amount_taken)  # print the results of taken values

                while fractionalKanpSack.data.empty() == False:  # freeing the queue
                    item = fractionalKanpSack.data.get()
                loopCounter = loopCounter + 1  # incrementing loop counter to take the next input

            except ValueError:
                print("That's not an int!")
            # insert items in to knaosack

    except ValueError:
        print("That's not an int!")
