"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visits  = []
    #방문했는지 확인 하는 리스트
    #모든 정점 false로 설정
    for i in graph:
        visits.append(False)
   
    visited = [] #BFS 방문 순서를 저장할 리스트
    queue = deque([start])#시작 정점 큐에 넣기
    visits[start] = True #시작 정점 탐색 예정으로 방문처리

    # TODO: 큐 생성 및 시작 정점 추가
    ## 방문한 정점 집합
    pass

    while queue:#큐가 빌때까지 반복
        visit = queue.popleft()# 가장 앞에있는 정점 꺼내기
        visited.append(visit)#꺼낸 정점 방문 순서 기록

        for i in graph[visit]:#현재 정점이랑 연결된 정점확인
            if not visits[i]:#정점이 방문을 안했으면 큐에넣고 나중에 탐색
                queue.append (i)
                visits[i]=True #큐에 넣은순간 방문 처리 (중복해서 들어가지않는다)


    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들 확인
    ## 방문하지 않은 정점이면 큐에 추가
    pass
    
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

