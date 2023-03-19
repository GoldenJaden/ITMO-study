n = 53
coins = [[10, 10], [5, 5, 5], [3, 3, 3, 3, 3], [2, 2, 2], [1]]
ans = []
change = 0
while change != n:
    flag = False
    for i in range(len(coins)):
        if len(coins[i]) != 0 and change + coins[i][0] <= n:
            change += coins[i][0]
            ans.append(coins[i][0])
            coins[i].pop()
            flag = True
            break
    if not flag:
        break
print(change, ans)
print(coins)