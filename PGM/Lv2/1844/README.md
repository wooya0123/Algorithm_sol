BFS 문제 <br>
접근 방법 1.<br>
목표 지점에 최댓값을 저장해두고 DFS 탐색을 하면서 방문 표시
만약 지금까지 거리가 목표 지점에 기록된 값보다 크면 더 이상 그 길을 조사 X
만약에 방문했던 곳이라면 이전 값과 현재 기록할 값을 비교하여 작은 것을 기록
-> 시간 초과

접근 방법2.<br>
방법 1에서 DFS -> BFS로 변경 (최단 거리이므로 BFS가 더 적합하다고 생각)
-> 시간 초과

접근 방법 3.<br>
BFS라면 너비 탐색이므로 목표 지점에 도달할 때까지 모든 길을 조사하면서 가기 때문에 가지 치기 삭제
방문했던 지점은 다시 가지 않음
-> 성공

벽이 없는 맵에서 최단거리와 벽이 있는 맵에서 최단거리 구할 때 차이점이 뭐지..?
