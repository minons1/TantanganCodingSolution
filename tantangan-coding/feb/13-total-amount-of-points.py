def points(games):
    poin = 0
    for game in games:
        res = [int(x) for x in game.split(':')]
        if res[0] > res[1]:
            poin += 3
        elif res[0] == res[1]:
            poin += 1
    return poin


print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])) #30
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4'])) #10
print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4'])) # 0
print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4'])) #15
print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4'])) #12