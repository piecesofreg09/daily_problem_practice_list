# All problems divided to sub type

## 1. Graph Theory

### Topological Sorting

1. First determine indegree (number of incombing edges)
2. Remove all nodes that have 0 indegress, update indegree, get the next batch of nodes that have 0 indegree, repeat until there are no nodes with 0 indegree.
3. If there are still any nodes left, it means there is a cycle in the graph.

While performing (2), we can attach these nodes to an array, which will be the topological sort.

[207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)

[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)


## 2. Stack

### Mono Stack

1. Define a condition A between two elements, monostack contains only elements that satisfy condition A in ascending order, say ```[...a, b, c...]```, in ascending order, element **b** satisfys condition A to element **a**. 
2. Condition A can be
   1. A comparison: such as greater than: elements are all numbers, element **b** > element **a**, then in the monostack, b comes after a,
   2. Or a boolean: such as element **b** doesn't contain element **a**, then in mono stack, b comes after a,
   
      Example problem:
      [2345. Finding the Number of Visible Mountains](https://leetcode.com/problems/finding-the-number-of-visible-mountains/description/)
3. Condition A should be able to be stacked monotonically, such as if b > a, c > b, then c > a, the ">" condition can be stacked. If b doesn't contain a, c doesn't contain b, then c doesn't contain a, the "doesn't contain" condition can be stacked.
