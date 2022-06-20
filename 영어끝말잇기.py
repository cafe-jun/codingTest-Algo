from collections import deque


def solution(n, words: list[str]):
    answer = []

    # 선행 뒷자리와 후행 앞자리가 같아야 한다 
    # 말한 단어를 큐에 넣음 
    
    word_q = deque()
    incorrect = 0
    word_set = []
    for idx,word in enumerate(words):
        if not word_q:
            word_q.append(word)
            word_set.append(word)
        else:
            pre_word = word_q.popleft()
            if pre_word[-1] != word[0] or word in word_set:
                incorrect = idx;
                break
            else:
                word_q.append(word)
                word_set.append(word)
            
        
    
     
    if incorrect == 0: 
        answer = [0,0] 
    else: 
        answer = divmod(incorrect,n) 
        answer = [answer[1]+1,answer[0]+1]
    return answer


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))

print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))