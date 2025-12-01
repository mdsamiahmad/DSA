<h2><a href="https://leetcode.com/problems/linked-list-cycle/">141. Linked List Cycle</a></h2>
<h3>Easy</h3>
<hr>
<p>Given the <strong>head</strong> of a linked list, determine if the linked list contains a cycle.</p>

<p>A cycle exists if a node in the list can be reached again by continuously following the <code>next</code> pointer.</p>

<p>Return <code>true</code> if there is a cycle, otherwise return <code>false</code>.</p>

<h3>Example 1:</h3>
<pre>
<b>Input:</b> head = [3,2,0,-4], pos = 1
<b>Output:</b> true
<b>Explanation:</b> The tail connects to the second node.
</pre>

<h3>Example 2:</h3>
<pre>
<b>Input:</b> head = [1,2], pos = 0
<b>Output:</b> true
</pre>

<h3>Example 3:</h3>
<pre>
<b>Input:</b> head = [1], pos = -1
<b>Output:</b> false
</pre>

<hr>
<h3>Constraints:</h3>
<ul>
  <li>The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
  <li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
  <li><code>pos</code> is <code>-1</code> or a valid index for the cycle connection.</li>
</ul>

<hr>
<h3>Follow-up:</h3>
<p>Can you solve it using <strong>O(1)</strong> memory?</p>
