import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
  N = int(input())

  distance = 0
  velocity = 0

  for i in range(N):
    command = list(map(int, input().split()))
    # print(command)

    if command[0] == 1:
      velocity += command[1]
      distance += velocity
    elif command[0] == 2 and velocity > command[1]:
      velocity -= command[1]
      distance += velocity
    elif command[0] == 2 and velocity <= command[1]:
      velocity = 0
      distance -= velocity
    elif command[0] == 0:
      distance += velocity
  
  print(f'#{tc} {distance}')