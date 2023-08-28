from collections import deque

def word_conversion(begin, target, words):
    # 초기화
    queue = deque()
    queue.append([begin, 0])
    visitied = [0] * len(words) 
    

    # 계산
    while queue:
        word, cnt = queue.popleft()
        if word == target: return cnt
        for i in range(len(words)):
            if not visitied[i]:
               if sum(x != y for x, y in zip(word, words[i])) == 1: #두문자를 비교해서 한글자만 변경되어있는것
                   queue.append([words[i], cnt +1]) 
                   visitied[i] = 1
    return 0     # 결과
