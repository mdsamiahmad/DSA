<h2><a href="https://leetcode.com/problems/container-with-most-water/">11. Container With Most Water</a></h2>
<h3>Medium</h3>
<hr>
<p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>ith</code> line are at <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that, together with the x-axis, form a container that contains the most water.</p>

<p>Return the maximum amount of water a container can store.</p>

<p><strong>Notice:</strong> You may not slant the container.</p>

<h3>Example 1:</h3>
<pre>
<b>Input:</b> height = [1,8,6,2,5,4,8,3,7]
<b>Output:</b> 49
<b>Explanation:</b> The above vertical lines are represented by the array [1,8,6,2,5,4,8,3,7].
The maximum area of water the container can contain is 49.
</pre>

<h3>Example 2:</h3>
<pre>
<b>Input:</b> height = [1,1]
<b>Output:</b> 1
</pre>

<hr>
<h3>Constraints:</h3>
<ul>
  <li><code>n == height.length</code></li>
  <li><code>2 &lt;= n &lt;= 10<sup>5</sup></li>
  <li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>