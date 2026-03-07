#  Product Stock Shortage Report
# Problem Description
# An inventory system stores product quantities in a dictionary.
# A product is considered low in stock if its quantity is less than 10.
# Your task is to return a list of all product names that are low in stock.

class Solution:
    def low_stock_products(self, inventory):
        result = []
        for k,v in inventory.items():
            if v<10:
                result.append(k)
            
        #Write your code here
       
        return result