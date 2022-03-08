# import requests
# import mysql.connector
# import pandas as pd
#
# We are a currency exchange that maintains the current exchange rates between currencies. A user can come to us with some amount in one currency and request the equivalent amount in a different currency. Given a list of exchange rates between currencies, write a function that calculates currency rate between any 2 currencies.
# Example -
# list_of_exchanges
#(GBP, EUR, 10)     - read as "1 GBP equals 10 EUR"
#(EUR, USD, 1.1)    - "1 EUR equals 1.1 USD"

#(10 GBP, USD) => ? - "10 GBP equals how many USD?"
# srcAmt = 10
# src = GBP
# dst = USD
#Answer: 110
#Explanation: 10 GBP = 10 x (10 EUR) = 10 x (10 x (1.1 USD)) = 110 USD
#
#Example 2 -
#(GBP, EUR, 10)     - read as "1 GBP equals 10 EUR"
#(EUR, USD, 1.1)    - "1 EUR equals 1.1 USD"
#(USD, JPY, 108.3)
#(10 GBP, JPY) => ? - "10 GBP equals how many JPY?"
#
#Answer: 11913
#Explanation: 10 GBP = 10 x (10 EUR) = 10 x (10 x (1.1 USD)) = 10 x (10 x(1.1 x (108.336 JPY))) = 11913 JPY

# input = [("GBP", "EUR", 10), ()]

#with depth-first-search:

class Node:
    def __init__(self, graph, src):
        self.name = src #"a"
        self.children = []
        for data in graph:
            if (src == data[0]):
                self.children.append(
                    (data[2], Node(graph, data[1]))
                )


def find_on(graph, src):
    return Node(graph, src)


def exchange(graph, srcAmt, src, dst): #(grah,
    node = find_on(graph, src) #find_on(graph, src)
    acc = srcAmt
    return exchange_recursive(node, acc, dst)


# depth first search
def exchange_recursive(node, acc, dst):

    if node.name == dst:
        return acc

    visited.add(node.name)

    for val, child in node.children:
        if child.name in visited:
            continue
        res = exchange_recursive(child, acc * val, dst)

        if res != -1:
            return res


if __name__ == "__main__":
    list_of_exchange = [("GBP", "EUR", 10), ("EUR", "USD", 1.1), ("USD", "JPY", 108.3)]

    # srcAmt = 10
    # src = "GBP"
    # dst = "JPY"

    srcAmt = int(input("Input Amount: "))
    src = input("Input current currency: ")
    dst = input("Input exchange currency: ")

    visited = set()
    value = exchange(list_of_exchange, srcAmt, src, dst)
    print(round(value, 0), dst)

#w/o depth-first-search:

# def exchange(list_of_exchange, srcAmt, src, d st):
#     for tuples in list_of_exchange:
#         if (src == tuples[0]) and (dst == tuples[1]):
#             return srcAmt * tuples[2]
#
#     temp_srcAmt = 0
#     temp_dst = 0
#     for tuples in list_of_exchange:
#         if(src == tuples[0]):
#             temp_srcAmt = srcAmt * tuples[2]
#             temp_dst = tuples[1]
#             break
#
#     for tuples in list_of_exchange:
#         if (temp_dst == tuples[0]) and (dst == tuples[1]):
#             return temp_srcAmt * tuples[2]
#             break
#
#
# # x -> y
# # |-> a -10-> b
#
# list_of_exchange = [("a", "b", 10), ("b", "c", 5)]
# srcAmt = 10
# src = "a"
# dst = "c"
# exchange(list_of_exchange, srcAmt, src, dst)
