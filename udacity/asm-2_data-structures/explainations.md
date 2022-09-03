# Problem 1. LRU Cache
The function has 3 main operations: search, order and add/remove

To satisfy the O(1) time complexity requirement, I created a double linked list `LruCache` (for ordering and adding/removing) with addition parameters `cache` dictionary (to get cache by key)

# Problem 2. Find files
In the solution function, I used:
- A loop to go through each directory at the same level
- Recursion to go through each directory level

So the time complexity will be O(n)

# Problem 3. Huffman encoding
## Encoding data

- Loop through data to store unique character and it's frequency into a dictionary. It takes O(n) time.
- Use `min-heap` data structure to store unique character and its frequency. It's insert/pop operation take O(log(n)) time 
- Remove every 2 lowest priority node. Then add new node with the sum frequency to the Huffman tree and  `min-heap`. This operation takes O(n*log(n)) time.
- Traverse the Huffman treen to generate binary code. It take O(n * log(n)) time. 

So the overall time complexity is O(n * log(n))

## Decoding data
- Go through the Huffman tree based on the binary code. It takes O(n * log(n)) time.

# Problem 4. User in group
The solution function will go through each user of each group level to find if the user exists.
So the time complexity will be O(n)

# Problem 5. Blockchain
Creating a new block will have O(1) time complexity

# Problem 6. Linked List Union and Intersection
- Adding elements to linked list takes O(n^2) time
- Finding union takes O(n) time
- Finding intersection takes O(n) time

So the overall time complexity is O(n^2)
