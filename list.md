# 

## 1. Graph Theory

### Topological Sorting

1. First determine indegree (number of incombing edges)
2. Remove all nodes that have 0 indegress, update indegree, get the next batch of nodes that have 0 indegree, repeat until there are no nodes with 0 indegree.
3. If there are still any nodes left, it means there is a cycle in the graph.

While performing (2), we can attach these nodes to an array, which will be the topological sort.

[207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)

[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

[1857. Largest Color Value in a Directed Graph](https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/)

### Clone graph

Clone neighbors of each node

[133. Clone Graph](https://leetcode.com/problems/clone-graph/)


### Dijkstra's Algorithm

Basically always find the node with the smallest distance to the initial node, iterate through neighbours of this node, update the stack/heap using the distance (defined as required in the problem)

<details>
    
<summary>Sample Template</summary>
    
```python

stack = [[0, 0, 0]]

while stack:
    # pop from the stack to get the node with the smallest distance
    node = heappop(stack)
    cur_dis, nx, ny = node

    # iterate through neighbours
    for dx, dy in dirrs:
        x, y = nx + dx, ny + dy
        if m>x>=0<=y<n:
            # logic to update distance, it depends on the problem
            dis = max(abs(heights[x][y] - heights[nx][ny]), cur_dis)
            # if 'distance' is found to be smaller, push it back into the heap, using new 'distance' as key
            if dis < diss[x][y]:
                diss[x][y] = dis
                heappush(stack, [diss[x][y], x, y])
return diss[-1][-1]
```
</details>

Example problems:

[1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/description/)

[778. Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/description/)

**the following problems are to find the largest distance, we just need to change min heap to a max heap**

[1102. Path With Maximum Minimum Value](https://leetcode.com/problems/path-with-maximum-minimum-value/description/)

[2812. Find the Safest Path in a Grid](https://leetcode.com/problems/find-the-safest-path-in-a-grid/description/)


## 2. Stack

### Mono Stack

1. Define a condition A between two elements, monostack contains only elements that satisfy condition A in ascending order, say ```[...a, b, c...]```, in ascending order, element **b** satisfys condition A to element **a**. 
2. Condition A can be
   1. A comparison: such as greater than: elements are all numbers, element **b** > element **a**, then in the monostack, b comes after a,

      [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/description/)
      <details>

      <summary>Example explanation</summary>
      
      For array `[1,5,10,13,18,11,4,2]`.
      
      1. Now we want to find all elements that are bigger than an element at index i for all i, store all these values to an array called `left`.
      
         Maintain an index stack whose corresponding elements are monotonically increasing.
         
         Looking at the first element, mono stack is empty, so we push the index directly in `[0]`, representing elements `[1]`, and first_smaller_element_to_left_index is -1, so that when we use the formula (current_index - first_smaller_element_to_left_index - 1), we get `(0 - (-1) -1) = 0`, meaning no elements are smaller to the left.

         Then we process the second element (index `1`, value `5`), value `5` is bigger than the element represented by stack top (index `0`, value `1`), so we store the current stack top to the `left` array, so for current element (index 1, value 5), first_smaller_element_to_left_index is 0, and the amount of elements that are bigger than 5 to left is (1 - 0 - 1), (current_index - first_smaller_element_to_left_index - 1). Now left is `[-1, 0]`

         for the first 5 elements `[1,5,10,13,18]`, we have current mono stack as `[0,1,2,3,4]`, left as `[-1,0,1,2,3]`.
   
      
         When we process the next new element at index 5 (value 11), if the new element is smaller than stack top, pop stack until stack top is smaller than the new element, in the example, we will pop out index 4 (value 18), then index 3 (value 13), and then the stack top index 2 (value 10) is smaller than 11, so the mono stack is now `[0,1,2]` (representing `[1,5,10]`), and the top of the stack (index 2 representing element 10) is the index of the first element that's (1) smaller than current element and (2) to the left the current element (which is 11, with index 5), so now we know, the amount of elements that are bigger than 7 to left is (5 - 2 - 1), (current_index - first_smaller_element_to_left_index - 1). We now have left as `[-1,0,1,2,3,2]`

      3. We can do the same for elements to the right
      
      4. But we use >= on one side, > on the other side, to avoid duplication.
      
      </details>
      
      
       
      at this moment, we have found all elements that are bigger than the new element

      Advanced: [2104. Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/description/)
      
   3. Or a boolean: such as element **b** doesn't contain element **a**, then in mono stack, b comes after a,
   
      [2345. Finding the Number of Visible Mountains](https://leetcode.com/problems/finding-the-number-of-visible-mountains/description/)
4. Condition A should be able to be stacked monotonically, such as if b > a, c > b, then c > a, the ">" condition can be stacked. If b doesn't contain a, c doesn't contain b, then c doesn't contain a, the "doesn't contain" condition can be stacked.
5. More generally, when we pop from monostack,
   ```python
   while stack and arr[stack[-1]] < arr[i]:
      popped = stack.pop()
      if stack:
         left = stack[-1]
         right = i
      do something
   stack.append[i]
   ```
   This means that `arr[i]` is the first element to the right that's bigger than element represented popped index, and the element represented by the next stack top (now it's also `stack[-1]`) is the first element to the left that's bigger than element represented popped index. As the code shown above, popped is the index of the element being popped, `left` is the first element to the left that's bigger, `right`  is the first element to the right that's bigger. If we want to find bigger/equal instead of bigger, we change the condition from `arr[stack[-1]] < arr[i]` to `arr[stack[-1]] <= arr[i]`.
 
**Special problem for mono stack**

[975. Odd Even Jump](https://leetcode.com/problems/odd-even-jump/description/)

This problem used monostack to find the index of the next larger/smaller element, only this time we sort all `(value, index)` pair first

<details>

<summary>Example explanation</summary>

For array `[10,13,12,14,15,12,13,14]`.

For example, if we sort it increasingly by value, the sorted `(value, index)` pair is `[(10, 0), (12, 2), (12, 5), (13, 1), (13, 6), (14, 3), (14, 7), (15, 4)]`

Then apply mono stack algo on the index, which is `[0, 2, 5, 1, 6, 3, 7, 4]`, once we found a index that's bigger than the stack top, it means this is the first element that's >= the element represented by stack top (because the array is already sorted). For example, for the second element in the `(value, index)` pair, `(12, 2)`, it's the third element in the original array, the next element that's >= than 12 is the 12 located at index 5. And if we apply monostack to the array `[0, 2, 5, 1, 6, 3, 7, 4]`, when we found 5 > 2, 5 is the first element that's bigger than 2, which meanings the element represented by index 5 is the ***first element*** that's ***>=*** the element represented by index 2, the ***>=*** is guaranteed because we sorted the `(value, index)` pair by `value`, the ***first element*** is guaranteed by monostack property.

</details>

## 3. Queue

### Deque (double ended queue)

[239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

## 4. Divide and conquer

### 

[4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

## 5. Union Find/Disjoint sets

It can find and update sets in `log(n)` time.

[305. Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/description/)
[1101. The Earliest Moment When Everyone Become Friends](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/description/)

## 6. Segment Tree

## Range sum, min, max

## 7. Linked List

## Reverse

[92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/description)

[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

## 999. Misc

### Count number of ones: count by each digit
[233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/description/)
