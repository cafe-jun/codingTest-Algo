
def solution(babbling: list[str]):
    answer = 0

    words = ["aya", "ye", "woo", "ma"]
    for ba in babbling: 
        for word in words: 
            if len(word) > len(ba):
                break;
            jump = 0
            for i in range(0,len(ba)): 
                
                if ba[i+jump:i+len(word)+jump] == word: 
                    if i+len(word) > len(ba):
                        jump = 0 
                        break;
                    ba = ba[0:i+jump]+'X'*len(word)+ba[i+len(word)+jump:]
                    jump =len(word)+1
        
        if ba.count('X') == len(ba):
            answer += 1
            break
    return answer
print(solution(["wooyemawooye"]))
print(solution(["yeye", "yeye"]))
print(solution(["yayae"]))
print(solution(["aya", "yee", "u", "maa"]))
print(solution([ "yeye","ayaye", "uuu", "yemawoo", "ayaayaa"]))