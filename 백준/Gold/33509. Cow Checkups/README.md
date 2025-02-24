# [Gold III] Cow Checkups - 33509 

[문제 링크](https://www.acmicpc.net/problem/33509) 

### 성능 요약

메모리: 222076 KB, 시간: 1292 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 2월 24일 16:00:50

### 문제 설명

<p><strong>Note: We suggest using a language other than Python to earn full credit on this problem.</strong></p>

<p>Farmer John's $N$ ($1 \leq N \leq 7500$) cows are standing in a line, with cow $1$ at the front of the line and cow $N$ at the back of the line. FJ's cows also come in many different species. He denotes each species with an integer from $1$ to $N$. The $i$'th cow from the front of the line is of species $a_i$ ($1 \leq a_i \leq N$).</p>

<p>FJ is taking his cows to a checkup at a local bovine hospital. However, the bovine veterinarian is very picky and wants to perform a checkup on the $i$'th cow in the line, only if it is of species $b_i$ ($1 \leq b_i \leq N$).</p>

<p>FJ is lazy and does not want to completely reorder his cows. He will perform the following operation <strong>exactly once</strong>.</p>

<ul>
	<li>Select two integers $l$ and $r$ such that $1 \leq l \le r \leq N$. Reverse the order of the cows that are between the $l$-th cow and the $r$-th cow in the line, inclusive.</li>
</ul>

<p>FJ wants to measure how effective this approach is. For each $c=0 \ldots N$, help FJ find the number of distinct operations ($l,r$) that result in exactly $c$ cows being checked. Two operations ($l_1,r_1$) and ($l_2,r_2$) are different if $l_1 \neq l_2$ or $r_1 \neq r_2$.</p>

### 입력 

 <p>The first line contains an integer $N$.</p>

<p>The second line contains $a_1, a_2, \ldots, a_N$.</p>

<p>The third line contains $b_1, b_2, \ldots, b_N$.</p>

### 출력 

 <p>Output $N+1$ lines with the $i$-th line containing the number of distinct operations ($l,r$) that result in $i-1$ cows being checked.</p>

