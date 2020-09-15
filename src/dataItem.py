#Date: 09/30/2019
#Class: CS5310
#Assignment: Fractional Knapsack
#Author(s): Mohammad Jaminur Islam

from filecmp import cmp


class DataItem(object):
    def __init__(self,item_weight,item_value):
        self.item_weight = item_weight #items available during kanpsack
        self.item_value = item_value #the items total value or worth
        self.per_weight_value = (-1)* item_value/item_weight #it is multiplied by -1 to work as max priority queue
        self.amount_taken = 0 #for tracking the amount taken during calculation

    def __cmp__(self, other): #comparator for priority queue
        return cmp(self.per_weight_value, other.per_weight_value)

    def __lt__(self, other): #less than operator define for comparator that helping Priority queue
        return self.per_weight_value < other.per_weight_value

