a = [2,0,1,2,3,0,2]

def counting_sort(list, s_list):
    cnt = [0] * (max(list) + 1)
    
    for i in list:
        cnt[i] += 1
        
    for idx in range(1, len(cnt)):
        cnt[idx] += cnt[idx-1]

    for j in range(len(a)-1, -1, -1):
        s_list[cnt[a[j]] - 1] = a[j]
        cnt[list[j]] -= 1
        
sorted_list = [0] * len(a)        
counting_sort(a, sorted_list)
print(sorted_list)