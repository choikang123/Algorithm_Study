import sys
import math
input=sys.stdin.readline
## 달팽이는 올라가고 싶다
# V - A: 달팽이가 가야 할 총 거리에서 첫 날에 달팽이가 오를 수 있는 거리를 빼는 부분이다.
# A - B: 달팽이가 하루에 실제로 이동할 수 있는 거리를 나타낸다. 달팽이는 낮에 A만큼 올라가지만 밤에 B만큼 내려오므로, 
# 하루 동안 달팽이가 실제로 이동하는 거리는 A - B 이다.
# (V - A) / (A - B): 달팽이가 V - A 거리를 A - B의 속도로 이동하는 데 필요한 시간을 나타낸다. 
# 달팽이가 이동해야 하는 거리를 하루 이동 거리로 나누어 필요한 일수를 계산한다.
# math.ceil(): 괄호 안의 수를 올림한다. (V - A) / (A - B)의 결과가 정수가 아닌 경우,
# 즉 달팽이가 마지막 날에 목표치에 도달하지 못하고 조금만 더 올라가면 도달할 수 있는 상황을 고려하여 올림 처리를 한다.
# math.ceil((V - A) / (A - B)) + 1: 첫 날을 제외한 나머지 일수에 첫 날을 더한 것이다.
# 첫 날에 달팽이는 A만큼 오르고 밤에 내려오지 않으므로, 이를 고려하여 1일을 더한다.
a,b,v=map(int,input().split())

result=math.ceil((v-a)/(a-b)+1)
print(result)