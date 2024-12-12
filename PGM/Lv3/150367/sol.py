def solution(numbers):
    ans = []
    for num in numbers:
        num = bin(num)[2:]  # 이진수로 변환

        # 포화이진트리 형태로 변환
        n = -1
        while True:
            n += 1
            if len(num) == 2 ** n - 1:
                break
            elif len(num) > 2 ** n - 1:
                continue
            else:
                num = '0' * (2 ** n - 1 - len(num)) + num
                break

        # 트리 노드 초기화 [왼쪽자식, 값, 오른쪽자식]
        tree = [[0, 0, 0] for _ in range(len(num)+1)]

        # 포화이진트리 생성
        def make_tree(start, end, node_idx):
            if start > end:
                return
            mid = (start + end) // 2

            # 현재 노드 값 설정
            tree[node_idx][1] = int(num[mid])

            # 왼쪽 서브트리
            left_idx = node_idx * 2
            if start <= mid - 1:
                tree[node_idx][0] = left_idx
                make_tree(start, mid - 1, left_idx)

            # 오른쪽 서브트리
            right_idx = node_idx * 2 + 1
            if mid + 1 <= end:
                tree[node_idx][2] = right_idx
                make_tree(mid + 1, end, right_idx)

        # 트리 생성 시작 (루트 노드는 1번부터)
        make_tree(0, len(num) - 1, 1)


        # 문제 없으면 True 반환, 문제 있으면 False 반환
        def check(node_idx):
            if node_idx == 0:
                return True

            # 현재 노드가 0인데 자식 노드들에 1이 있으면 False
            if tree[node_idx][1] == 0:
                left_res = check(tree[node_idx][0])
                right_res = check(tree[node_idx][2])
                return left_res and right_res

            # 현재 노드가 1이면 그 아래 서브트리는 확인할 필요 없음
            return False


        # 가능한 트리인지 판단
        # 노드가 0인데 자식 노드에 1이 있으면 안 된다(잘못된 트리)
        is_valid = True
        for i in range(1, len(tree)):
            if tree[i][1] == 0:
                if check(tree[i][0]) and check(tree[i][2]):
                    pass
                else:
                    is_valid = False
                    break

        ans.append(1 if is_valid else 0)


    return ans


numbers = [5]

print(solution(numbers))