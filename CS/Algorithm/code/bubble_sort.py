 a = [6,5,3,1,8,7,2,4]
    
    # Solution 1
    for i in range(len(a)-1, 0, -1):
        flag = False
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        if not flag:
            break
    #    print(a)
    
    # Result #
    #[5, 3, 1, 6, 7, 2, 4, 8]
    #[3, 1, 5, 6, 2, 4, 7, 8]
    #[1, 3, 5, 2, 4, 6, 7, 8]
    #[1, 3, 2, 4, 5, 6, 7, 8]
    #[1, 2, 3, 4, 5, 6, 7, 8]
    
    # Solution 2
    end = len(a) -1
    while end > 0:
        last = 0
        for i in range(end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                last = i
        end = last
    #    print(a)
    
    # Result #
    #[5, 3, 1, 6, 7, 2, 4, 8]
    #[3, 1, 5, 6, 2, 4, 7, 8]
    #[1, 3, 5, 2, 4, 6, 7, 8]
    #[1, 3, 2, 4, 5, 6, 7, 8]
    #[1, 2, 3, 4, 5, 6, 7, 8]
    #[1, 2, 3, 4, 5, 6, 7, 8]