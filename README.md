# gator-taxi
GatorTaxi is a ride-sharing service that receives numerous ride requests every day. In
order to efficiently manage these ride requests, GatorTaxi plans to develop a new
software that utilizes a min-heap and a Red-Black Tree (RBT) data structure to keep track
of pending ride requests. The system is designed to handle ride requests based on the
triplet (rideNumber, rideCost, tripDuration), where rideNumber is a unique integer
identifier for each ride, rideCost is the estimated cost in integer dollars for the ride, and
tripDuration is the total time in integer minutes needed to get from the pickup to the
destination.

Two data structures are used in this project to keep track of the GatorTaxi:
1) Red Black Tree
The Red-Black Tree (RBT) is used to store the ride requests as triplets (rideNumber,
rideCost, tripDuration) ordered by rideNumber. The RBT is implemented as a balanced
binary search tree with the following properties:
  ● Each node is colored either red or black.
  ● The root node is always black.
  ● All leaf nodes (i.e., NULL nodes) are black.
  ● If a node is red, its children must be black.
  ● For each node, all paths from the node to its descendant leaf nodes contain the
  same number of black nodes (i.e., the black height of the tree is the same for all
  paths).

![image](https://github.com/pranav-gautam/gator-taxi/assets/64377125/6d78a867-6e5f-4e5a-8d79-1c9d1a2ee5d3)

To implement these properties I have created another class which acts as a node of the red
black tree.

2) Min-Heap
The min-heap is implemented as an array of triplets (rideNumber, rideCost,
tripDuration). Each element of the array represents a node in the min-heap. The array is
0-indexed, with the root node at index 0, and for any element at index i, its left child is at
index 2i+1 and its right child is at index 2i+2. The heap is ordered by rideCost.

![image](https://github.com/pranav-gautam/gator-taxi/assets/64377125/0905c37e-782e-4e5c-9f5d-823bb82b68d1)
