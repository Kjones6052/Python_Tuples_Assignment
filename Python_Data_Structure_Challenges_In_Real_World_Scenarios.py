# Task 1: Customer Order Processing 
# Refine your skills in tuple unpacking by managing customer orders.
# Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, 
# the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.
# Sample Order Data:
# orders = [
#     ("Alice", "Laptop", 1),
#     ("Bob", "Camera", 2),
#     # More orders...
# ]
# - Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.

orders = ("Alice", "Laptop", 1), ("Bob", "Camera", 2), ("Chuck", "TV", 1), ("Deirdre", "Cable Pack", 3)

def print_orders():
    for order in orders:
        name, product, quantity = order
        print(f"{name}'s order: {product} x {quantity}")

print_orders()