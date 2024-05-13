import sys
input=sys.stdin.readline
## 달팽이는 올라가고 싶다
a,b,v=map(int,input().split())
day=0
nail_meter=0

while nail_meter<=v:
    nail_meter+=a
    day+=1
    if nail_meter>=v:
        print(day)
        break
    nail_meter-=b