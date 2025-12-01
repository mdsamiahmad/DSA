<h2><a href="https://leetcode.com/problems/linked-list-cycle-ii/">142. Linked List Cycle II</a></h2>
<h3>Medium</h3>
<hr>
<p>Given the <strong>head</strong> of a linked list, return the node where the cycle begins.  
If there is no cycle, return <code>null</code>.</p>

<p>A cycle exists if a node in the list can be reached again by continuously following the <code>next</code> pointer.</p>

<p>Do not modify the linked list.</p>

<h3>Example 1:</h3>
<pre>
<b>Input:</b> head = [3,2,0,-4], pos = 1  
<b>Output:</b> node with value 2
<b>Explanation:</b> The tail connects to the second node.
</pre>

<h3>Example 2:</h3>
<pre>
<b>Input:</b> head = [1,2], pos = 0  
<b>Output:</b> node with value 1
</pre>

<h3>Example 3:</h3>
<pre>
<b>Input:</b> head = [1], pos = -1  
<b>Output:</b> null
</pre>

<hr>
<h3>Constraints:</h3>
<ul>
  <li>The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
  <li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
  <li><code>pos</code> is <code>-1</code> or a valid index where the tail connects.</li>
</ul>

<hr>
<h3>Follow-up:</h3>
<p>Can you solve it using <strong>O(1)</strong> memory?</p>
