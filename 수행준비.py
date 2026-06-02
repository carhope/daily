# BFS 함수
def bfs(graph, start):

    # 방문한 학생 저장
    visited = []

    # 큐 생성
    queue = []

    # 시작 학생 큐에 삽입
    queue.append(start)

    # 큐가 빌 때까지 반복
    while len(queue) > 0:

        # 큐의 맨 앞 데이터 꺼내기
        current = queue.pop(0)

        # 아직 방문하지 않았다면
        if current not in visited:

            # 방문 처리
            visited.append(current)

            # 연결된 학생 확인
            for next_student in graph[current]:

                # 아직 방문하지 않았고
                # 큐에도 없는 경우
                if next_student not in visited and next_student not in queue:

                    # 큐 뒤에 삽입
                    queue.append(next_student)

    return visited


# 학생 수 입력
n = int(input("학생 수 입력: "))

# 연락 관계 수 입력
m = int(input("연락 관계 수 입력: "))

# 그래프 생성
graph = {}

# 학생 이름 입력
for i in range(n):

    name = input("학생 이름 입력: ")

    graph[name] = []


# 연락 관계 입력
for i in range(m):

    a, b = input("연락 가능한 두 학생 입력: ").split()

    # 무방향 그래프
    graph[a].append(b)
    graph[b].append(a)


# 시작 학생 입력
start = input("처음 공지를 받은 학생 입력: ")

# BFS 실행
result = bfs(graph, start)

# 결과 출력
print("\n공지 전달 순서")

for student in result:
    print(student, end=" ")

print("\n총 전달 인원:", len(result), "명")