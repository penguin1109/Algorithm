#### 1781 - 컵라면
- 문제 설명 :
N개의 문제가 주어져 있고 각각의 문제를 풀었을때 주어지는 컵라면의 개수와 데드라인이 정해져 있을 때에 최대로 받을 수 있는 컵라면의 수를 구하여라

- 풀이 방법 :

```python
import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key = lambda x : (x[0], -x[1]))

q = []
for i in range(len(arr)):
    a,b = arr[i][0], arr[i][1]
    if (a > len(q)):
        heapq.heappush(q,b)
    else:
        comp = heapq.heappop(q)
        if (comp < b):
            heapq.heappush(q, b)
        else:heapq.heappush(q,comp)
print(sum(q))
```

#### 1715 - 카드 정렬하기
- 문제 설명 :
N개의 숫자 카드에 대해서 각각을 비교하는 횟수의 최솟값을 구하시오

- 풀이 방법 :
1. 오름차순으로 정렬하거나 애초에 입력을 받을 때에 우선순위 큐를 사용해서 입력을 받는다.
2. 2개의 수를 pop해서 더한 값을 answer에 갱신해 줄 뿐만 아니라 큐에 넣는다.
3. 1개만 남으면 break

```python
import sys, heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    heapq.heappush(q, int(input()))

answer = 0
while (q):
    if (len(q)>=2):
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        answer += (a+b)
        heapq.heappush(q, a+b)
    else:
        break

print(answer)
```

```java
package greedy;
import java.util.*;
import java.io.*;

public class _1715 {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		
		PriorityQueue<Integer> q = new PriorityQueue<Integer>(); // 우선순위가 낮은 숫자 순 = 오름차순
		
		int N = Integer.parseInt(bf.readLine());
		for (int i = 0;i<N;i++) {
			q.add(Integer.parseInt(bf.readLine()));
		}
		int answer = 0;
		
		while (!q.isEmpty()) {
			if (q.size() >=2) {
				int a = q.poll();
				int b = q.poll();
				answer+= (a+b);
				q.add(a+b);
			}
			else {
				break;
			}
		}
		
		System.out.println(answer);
	}
}

```