#Date: 09/30/2019
#Class: CS5310
#Assignment: Fractional Knapsack
#Author(s): Mohammad Jaminur Islam

import unittest
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

from src.dataItem import DataItem
from src.fractionalKanpSack import FractionalKanpSack, Result

fractionalKanpSack = FractionalKanpSack(4)

class MyTestCase(unittest.TestCase):
    def test_class(self):
        self.assertIsInstance(fractionalKanpSack,FractionalKanpSack)

    def test_data_container(self):
        data = fractionalKanpSack.data;
        # assert isinstance(data,Q.PriorityQueue() )
        assert isinstance(data,Q.PriorityQueue)

    def test_container_capacity(self):
        capacity = fractionalKanpSack.capacity;
        assert (capacity != None and capacity>0)

    def test_insert(self): #insertion test
        item1 =  DataItem(10,40) #define a Data item passing the weight and value
        fractionalKanpSack.insert_item(item1)
        assert fractionalKanpSack.data.qsize() == 1
        while fractionalKanpSack.data.empty() == False:#freeing the queue
            item = fractionalKanpSack.data.get()
        assert fractionalKanpSack.data.qsize() == 0

    def test_algorithm_execution(self): #test algorthm 2
        #insertion begin
        item1 = DataItem(10, 40) #define a Data item passing the weight and value
        fractionalKanpSack.insert_item(item1)
        item1 = DataItem(1, 50) #define a Data item passing the weight and value
        fractionalKanpSack.insert_item(item1)
        item1 = DataItem(4, 80) #define a Data item passing the weight and value
        fractionalKanpSack.insert_item(item1)
        # insertion end
        assert fractionalKanpSack.data.qsize() == 3
        result = fractionalKanpSack.execute_fractional_kanp_sack() #call to algorithm

        while fractionalKanpSack.data.empty() == False:#freeing the queue
            item = fractionalKanpSack.data.get()
            # print("item_weight: ", item.item_weight)
            # print("item_value: ", item.item_value)
        assert fractionalKanpSack.data.qsize() == 0
        print("max_benifit: ", result.total_benefit)  # total benefit
        if (isinstance(result, Result)):
            if len(result.result) > 0:
                for ele in result.result:
                    print("Amount taken from item: ", ele.amount_taken)  # see what weights has been taken


    def test_algorithm_execution2(self): #tested the algorithm with the test case
            #insertion begin
            fractionalKanpSack2 = FractionalKanpSack(10)
            item1 = DataItem(4, 12) #define a Data item passing the weight and value
            fractionalKanpSack2.insert_item(item1)
            item1 = DataItem(8, 32) #define a Data item passing the weight and value
            fractionalKanpSack2.insert_item(item1)
            item1 = DataItem(2, 40) #define a Data item passing the weight and value
            fractionalKanpSack2.insert_item(item1)
            item1 = DataItem(6, 30)#define a Data item passing the weight and value
            fractionalKanpSack2.insert_item(item1)
            item1 = DataItem(1, 50)#define a Data item passing the weight and value
            fractionalKanpSack2.insert_item(item1)
            #insertion end
            assert fractionalKanpSack2.data.qsize() == 5

            result = fractionalKanpSack2.execute_fractional_kanp_sack() #call to algorithm

            while fractionalKanpSack2.data.empty() == False:#freeing the queue
                item = fractionalKanpSack2.data.get()

            assert fractionalKanpSack2.data.qsize() == 0

            if(isinstance(result,Result)):
                print("max_benifit: ", result.total_benefit)  # total benefit

                if len(result.result)>0:
                    for ele in result.result:
                        print("Amount taken from item: ",ele.amount_taken) #see what weights has been taken

if __name__ == '__main__':
    unittest.main()
