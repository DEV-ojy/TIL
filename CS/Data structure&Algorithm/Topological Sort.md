# Topological Sort

이번 포스트에서는 `그래프`를 활용한 정령 알고리즘 가운데 하나인 **Topological Sort** 기법을 살펴보도록 하겠습니다 

## concept - 개념

`Topological Sort`란 Directed Acyclic Graph를 활용해 노드들 사이에 선후관계를 중심으로 정령하는 알고리즘입니다 이때 사용되는 기법이 깊이우선탐색(DFS)입니다 

옷입기로 예시를 들어보겠습니다 우선 아래 그래프를 깊이우선탐색으롤 모든 노드를 탐색하고 노드들에 방문시점/방문종료시점을 기록해 둡니다 

![image](https://user-images.githubusercontent.com/80239748/156882721-7f31dcf4-d8cf-462c-a454-dda0e3d5865d.png)

이후 방문종료시점의 내림차순으로 정령합니다 

![image](https://user-images.githubusercontent.com/80239748/156882738-257ac76b-e871-42af-a0d6-c796f087ae5d.png)

`Topological Sort`의 계산복잡도는 깊이우선탐색에 비례합니다 따라서 O(|V|+|E|)가 됩니다 