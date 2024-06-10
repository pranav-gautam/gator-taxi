import sys

class Ride:
    def __init__(self, ride_number, ride_cost, trip_duration):
        """
        Constructor to create a Ride object with the given ride_number, ride_cost, and trip_duration.
        Initializes heap_pointer and rbt_node to None.

        Args:
        - ride_number (int): The ride number.
        - ride_cost (int): The cost of the ride.
        - trip_duration (int): The duration of the trip.
        """
        self.ride_number = ride_number
        self.ride_cost = ride_cost
        self.trip_duration = trip_duration
        self.heap_pointer = None
        self.rbt_node = None
        
    def __lt__(self, other):
        """
        Comparison method for Ride objects, to check if self is less than other.
        Compares based on ride_cost and trip_duration.
        
        Args:
        - other (Ride): The other Ride object to compare to.

        Returns:
        - bool: True if self is less than other, False otherwise.
        """
        if self.ride_cost == other.ride_cost:
            return self.trip_duration < other.trip_duration
        else:
            return self.ride_cost < other.ride_cost
        
    def __gt__(self, other):
        """
        Comparison method for Ride objects, to check if self is greater than other.
        Compares based on ride_cost and trip_duration.

        Args:
        - other (Ride): The other Ride object to compare to.

        Returns:
        - bool: True if self is greater than other, False otherwise.
        """
        if self.ride_cost == other.ride_cost:
            return self.trip_duration > other.trip_duration
        else:
            return self.ride_cost > other.ride_cost
        
    def __eq__(self, other):
        """
        Comparison method for Ride objects, to check if self is equal to other.
        Compares based on ride_number.

        Args:
        - other (Ride): The other Ride object to compare to.

        Returns:
        - bool: True if self is equal to other, False otherwise.
        """
        return self.ride_number == other.ride_number
        
    def __str__(self):
        """
        String representation of Ride object.

        Returns:
        - str: A string representation of Ride object in the format (ride_number, ride_cost, trip_duration).
        """
        return f"({self.ride_number},{self.ride_cost},{self.trip_duration})"


class Node:
    def __init__(self, rideNumber, rideCost, tripDuration, color='RED'):
        """
        Constructor to create a Node object with the given rideNumber, rideCost, tripDuration, and color.
        Initializes left, right, and color attributes with default value 'RED'.

        Args:
        - rideNumber (int): The ride number.
        - rideCost (int): The cost of the ride.
        - tripDuration (int): The duration of the trip.
        - color (str, optional): The color of the node. Defaults to 'RED'.
        """
        self.left = None
        self.right = None        
        self.color = color
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration

class RBTree:
    def __init__(self):
        """
        Constructor to create a Red-Black Tree object.
        Initializes root attribute as None.
        """
        self.root = None

    def _is_red(self, node):
        """Check if a node is red."""
        if node is None:
            return False
        return node.color == 'RED'

    def _rotate_left(self, node):
        """Rotate a node to the left."""
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = 'RED'
        return x

    def _rotate_right(self, node):
        """Rotate a node to the right."""
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = 'RED'
        return x

    def _flip_colors(self, node):
        """Flip the colors of a node and its children."""
        node.color = 'RED'
        node.left.color = 'BLACK'
        node.right.color = 'BLACK'

    def find_range_values(self, min_val, max_val):
        """Find all the values within a given range."""
        res = []
        self.inorder_range(self.root, res, min_val, max_val)
        return res

    def search(self, ride_number):
        """Search for a node with a given ride number."""
        node = self._search(self.root, ride_number)
        if node is None:
            return None
        else:
            return node

    def _search(self, node, ride_number):
        """Helper function to search for a node with a given ride number."""
        if node is None:
            return None
        if node.rideNumber == ride_number:
            return node
        elif ride_number < node.rideNumber:
            return self._search(node.left, ride_number)
        else:
            return self._search(node.right, ride_number)

    def get(self, rideNumber):
        """Get the values associated with a given ride number."""
        return self._get(self.root, rideNumber)

    def _get(self, node, rideNumber):
        """Helper function to get the values associated with a given ride number."""
        if node is None:
            return None
        if rideNumber < node.rideNumber:
            return self._get(node.left, rideNumber)
        elif rideNumber > node.rideNumber:
            return self._get(node.right, rideNumber)
        else:
            return (node.rideNumber, node.rideCost, node.tripDuration)

    def _insert(self, node, rideNumber, rideCost, tripDuration):
        """Helper function to insert a new node with given values."""
        if node is None:
            return Node(rideNumber, rideCost, tripDuration)

        if rideNumber < node.rideNumber:
            node.left = self._insert(node.left, rideNumber, rideCost, tripDuration)
        elif rideNumber > node.rideNumber:
            node.right = self._insert(node.right, rideNumber, rideCost, tripDuration)
        else:
            raise ValueError("Duplicate rideNumber in the Red-Black Tree.")

        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)
        return node

    def insert(self, rideNumber, rideCost, tripDuration):
        """
        Insert a new node with the given values into the Red-Black Tree.
        """
        self.root = self._insert(self.root, rideNumber, rideCost, tripDuration)
        self.root.color = 'BLACK'

    def _delete(self, node, rideNumber):
        """
        Delete a node with the given rideNumber from the Red-Black Tree.
        """
        if node is None:
            return None
        if rideNumber < node.rideNumber:
            node.left = self._delete(node.left, rideNumber)
        elif rideNumber > node.rideNumber:
            node.right = self._delete(node.right, rideNumber)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._min_node(node.right)
                node.rideNumber = min_node.rideNumber
                node.rideCost = min_node.rideCost
                node.tripDuration = min_node.tripDuration
                node.right = self._delete(node.right, min_node.rideNumber)

        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)

        return node

    def _contains_helper(self, node, rideNumber):
        """
        Helper function to check if a node with the given rideNumber exists in the Red-Black Tree.
        """
        if node is None:
            return None
        if rideNumber == node.rideNumber:
            return node
        elif rideNumber < node.rideNumber:
            return self._contains_helper(node.left, rideNumber)
        else:
            return self._contains_helper(node.right, rideNumber)

    def contains(self, rideNumber):
        """
        Check if a node with the given rideNumber exists in the Red-Black Tree.
        """
        return self._contains_helper(self.root, rideNumber) is not None

    def delete(self, rideNumber):
        """
        Delete a node with the given rideNumber from the Red-Black Tree.
        """
        self.root = self._delete(self.root, rideNumber)

    def _min_node(self, node):
        """
        Helper function to find the minimum node in a subtree rooted at the given node.
        """
        if node.left is None:
            return node
        return self._min_node(node.left)

    def inorder_range(self, root, res, min_val, max_val):
        """
        In-order traversal of the Red-Black Tree to find nodes within the given range of values.
        """
        if root is not None:
            if min_val < root.rideNumber:
                self.inorder_range(root.left, res, min_val, max_val)
            if min_val <= root.rideNumber and max_val >= root.rideNumber:
                res.append(root)
            if max_val > root.rideNumber:
                self.inorder_range(root.right, res, min_val, max_val)

from typing import List

class MinHeap:
    def __init__(self):
        """Initialize an empty MinHeap."""
        self.heap_list = [None]
        self.current_size = 0
        
    def size(self) -> int:
        """Get the current size of the heap."""
        return self.current_size

    def build_heap(self, ride_list: List[Ride]):
        """Build a heap from a list of rides."""
        self.current_size = len(ride_list)
        self.heap_list = [None] + ride_list[:]
        i = len(ride_list) // 2
        while (i > 0):
            self._perc_down(i)
            i -= 1
    
    def get_min(self) -> Ride:
        """Get the minimum ride from the heap."""
        if self.current_size == 0:
            return None
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self._perc_down(1)
        return min_val

    def _get_min_child(self, i):
        """Get the index of the minimum child of a node at index i."""
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, ride: Ride):
        """Insert a ride into the heap."""
        self.heap_list.append(ride)
        self.current_size += 1
        self._perc_up(self.current_size)
        
    def delete(self, elem):
        """Delete a ride from the heap."""
        n = len(self.heap_list)
        for i in range(n):
            if self.heap_list[i] is not None:
                if self.heap_list[i].ride_number == elem:
                    self.current_size -= 1
                    break

        self.heap_list[i] = self.heap_list[n-1]

        self.heap_list = self.heap_list[:n-1]

        while 2*i+1 < len(self.heap_list):
            min_child = 2*i+1
            if 2*i+2 < len(self.heap_list) and self.heap_list[2*i+2] < self.heap_list[2*i+1]:
                min_child = 2*i+2

            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
                i = min_child
            else:
                break
                
        return self.heap_list

    def is_empty(self) -> bool:
        """Check if the heap is empty."""
        return self.current_size == 0
    
    def _perc_up(self, i):
        """Perform percolation up on a node at index i."""
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
                self.heap_list[i].heap_pointer = i
                self.heap_list[i // 2].heap_pointer = i // 2
            i = i // 2
    
    def _perc_down(self, i):
        """Perform percolation down on a node at index i."""
        while (i * 2) <= self.current_size:
            min_child = self._get_min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
                self.heap_list[i].heap_pointer = i
                self.heap_list[min_child].heap_pointer = min_child
            i = min_child

class RideManager:
    def __init__(self):
        """Initialize a RideManager object with a MinHeap and an RBTree."""
        self.heap = MinHeap()
        self.rbtree = RBTree()

    def insert(self, ride_number, ride_cost, trip_duration):
        """Insert a new ride with the given details into the RideManager."""
        if self.rbtree.contains(ride_number):
            return "Duplicate RideNumber"

        ride = Ride(ride_number, ride_cost, trip_duration)
        self.heap.insert(ride)
        self.rbtree.insert(ride_number, ride_cost, trip_duration)

    def print_ride(self, ride_number):
        """Print the details of a ride with the given ride_number."""
        node = self.rbtree.search(ride_number)
        if node is None:
            return "(0,0,0)"
        else:
            return "(" + str(node.rideNumber) + "," + str(node.rideCost) + "," + str(node.tripDuration) + ")"

    def print_rides(self, ride_number1, ride_number2):
        """Print the details of all rides within the given ride_number range."""
        allRides = ""
        rides = []
        rides = self.rbtree.find_range_values(ride_number1, ride_number2)
        if len(rides) == 0:
            return "(0,0,0)"
        else:
            for ride in rides:
                allRides = allRides + "(" + str(ride.rideNumber) + "," + str(ride.rideCost) + "," + str(
                    ride.tripDuration) + "),"
            return allRides[:-1]

    def get_next_ride(self):
        """Get the next ride with the minimum cost from the RideManager."""
        if self.heap.is_empty():
            return "No active ride requests"
        ride = self.heap.get_min()
        self.rbtree.delete(ride.ride_number)
        return ride

    def cancel_ride(self, ride_number):
        """Cancel a ride with the given ride_number from the RideManager."""
        node = self.rbtree.search(ride_number)
        print('')
        if node is not None:
            self.heap.delete(node.rideNumber)
            self.rbtree.delete(node.rideNumber)

    def update_trip(self, ride_number, new_trip_duration):
        """Update the trip duration of a ride with the given ride_number."""
        node = self.rbtree.search(ride_number)
        if node is not None:
            if new_trip_duration <= node.tripDuration:
                return
            elif node.tripDuration < new_trip_duration and new_trip_duration <= 2 * node.tripDuration:
                self.cancel_ride(ride_number)
                self.insert(ride_number, node.rideCost + 10, new_trip_duration)
            else:
                self.cancel_ride(ride_number)

rideManager=RideManager()

# Create an output file for writing
output = open("output.txt", "w")   

# Open the input file for reading
file = open(sys.argv[1], "r")

# Initialize a list to store output lines
output_li = []

# Loop through each line in the input file
for s in file.readlines():
    n = []
    # Extract integers from parentheses in the line
    for num in s[s.index("(") + 1:s.index(")")].split(","):
        if num != '':
            n.append(int(num))
    
    # Perform operations based on keywords in the line
    if "Insert" in s:
        val = rideManager.insert(n[0], n[1], n[2])
        if val == "Duplicate RideNumber":
            output_li.append(val)
            output_li.append('\n')
    elif "Print" in s:
        if len(n) == 1:
            val = rideManager.print_ride(n[0])
        elif len(n) == 2:
            val = rideManager.print_rides(n[0], n[1])
        output_li.append(val)
        output_li.append('\n')
    elif "UpdateTrip" in s:
        rideManager.update_trip(n[0], n[1])
    elif "GetNextRide" in s:
        ride = rideManager.get_next_ride()
        if type(ride) == Ride:
            output_li.append(str((ride.ride_number,ride.ride_cost,ride.trip_duration)))
        else:
            output_li.append("No active ride requests")
        output_li.append('\n')
    elif "CancelRide" in s:
        rideManager.cancel_ride(n[0])

# Write the output lines to the output file
for i in output_li[:-1]:
    output.write(i)

# Close the output file
output.close()