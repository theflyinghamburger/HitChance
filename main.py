def populateD20():  # Creates 20x20 array of [j,i] for state space of 2d20
    rows, cols = (20, 20)
    _arr = [[[j, i] for i in range(1, cols + 1)] for j in range(1, rows + 1)]
    return _arr

def inputData():
    print("Enter Target AC:")
    targetAC = int(input())
    print("Enter Hit Bonus:")
    hitBonus = int(input())
    return targetAC, hitBonus

def chooseRollType(_arr, _mode, i , j):
    if _mode == "reg":  # Case for regular roll
        _roll = _arr[i][j][0]
    elif _mode == "dis":  # Case for disadvantage
        if _arr[i][j][0] < _arr[i][j][1]:
            _roll = _arr[i][j][0]
        else:
            _roll = _arr[i][j][1]
    elif _mode == "adv":  # Case for advantage
        if _arr[i][j][0] > _arr[i][j][1]:
            _roll = _arr[i][j][0]
        else:
            _roll = _arr[i][j][1]
    return _roll

def toHitChance(_AC, _bonus, _arr, _mode="reg"):
    successCount = 0
    for i in range(len(_arr)):
        for j in range(len(_arr[0])):
            roll = chooseRollType(_arr, _mode, i, j)  # Logic for choosing 2d20 roll combination

            if roll >= _AC - _bonus:  # Success condition
                successCount += 1
    hitChance = round((successCount / 400) * 100, 2)  # state space = 400
    if hitChance < 5:
        hitChance = 5  # Nat 20 always hits, chance for nat 20 is 5%
    return hitChance


if __name__ == '__main__':
    arr = populateD20()
    AC, bonus = inputData()

    attack = toHitChance(AC, bonus, arr)
    print("Hit percentage: " + str(attack))

    attackDis = toHitChance(AC, bonus, arr, "dis")
    print("Hit percentage with disadvantage: " + str(attackDis))
    
    attackAdv = toHitChance(AC, bonus, arr, "adv")
    print("Hit percentage with advantage: " + str(attackAdv))
