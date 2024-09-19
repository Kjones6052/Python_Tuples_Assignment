# Task 1: Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: 
# (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is 
# `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:
# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

def flight_info(itinerary):
    for tuple in itinerary:
        name, departure, arrival = tuple
        number = (itinerary.index(tuple) + 1)
        itinerary_num = f"Itinerary {number}"
        print(f"{itinerary_num}: {name} - From {departure} to {arrival}")


flight_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
flight_info(flight_itineraries)