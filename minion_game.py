def minion_game(string):
    vowels = 'AEIOU'
    kev = 0
    stu = 0
    for x in range(len(s)):
        if s[x] in vowels:
            kev += (len(s) - x)
        else:
            stu += (len(s) - x)
    if stu > kev:
        print('Stuart ' + str(stu))
    elif stu < kev:
        print('Kevin ' + str(kev))
    elif stu == kev:
        print('Draw')
