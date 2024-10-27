"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array  A[] of n integers each separated by a space.
Constraints
2<=n<=100
-100<=A[i]<=100
Output Format
Print the runner-up score.
"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

results = list(arr)
sorted_results = (sorted(results, reverse=True))

second = max(sorted_results, key=lambda x: x)
first = min(sorted_results, key=lambda x: x)

for i in range(len(sorted_results)):
            if sorted_results[i] <= second and sorted_results[i] != second:
                second = sorted_results[i]
                print(second)
                break

