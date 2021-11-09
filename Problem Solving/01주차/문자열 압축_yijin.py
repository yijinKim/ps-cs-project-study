def solution(s):
    answer_len = []  # 모든 답안의 길이 저장하는 변수

    if len(s) == 1:  # 이거 안하면 testcase5 통과 못함
        return 1

    for digit in range(1, len(s) // 2 + 1):  # 슬라이싱 개수를 1~절반까지
        answer = ""
        cnt = 1
        tmp = s[:digit]

        for j in range(digit, len(s), digit):
            new_tmp = s[j:j+digit]  # 그 다음 슬라이싱한 문자열
            if new_tmp == tmp: # 앞과 같으면 개수 추가
                cnt += 1
            else:  # 앞과 다른 새로운 문자열이면
                if cnt > 1: # 이전의 반복됐던 문자열 저장하고
                    tmp = str(cnt) + tmp
                    cnt = 1
                answer += tmp
                tmp = new_tmp  # 새로운 문자열을 tmp로 할당함.
        # for문이 끝난 후 마지막 문자열이 남게됨.
        if cnt > 1:
            tmp = str(cnt) + tmp
        answer += tmp
        answer_len.append(len(answer))

    return min(answer_len)

s = 'abcabcabcabcdededededede'
print(solution(s))