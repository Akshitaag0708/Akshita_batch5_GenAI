# Unique Product Purchase Analyzer
# Problem Description
# An e-commerce company records the products purchased by customers during a sale. However, some products appear multiple times in the purchase list because multiple customers bought them.
# The company wants to generate a list of unique products that were purchased only once during the sale.
# You are given a list of product names representing purchases. Your task is to return a list containing products that appear exactly once in the list.


class Solution:
    def unique_products(self, products):
        result = []
        
        for p in products:
            if products.count(p) == 1:
                result.append(p)
        return result