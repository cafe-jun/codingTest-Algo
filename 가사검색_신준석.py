class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.count = 0
        self.children = {}
        
class Trie:
    result: dict
    def __init__(self):
        self.head = Node(None)
        self.result = {}
        self.count = 0
        
    def insert(self, string):
        current_node = self.head
        self.count += 1
        
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
            current_node.count += 1
        current_node.data = string
        
    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []
        print(current_node.children)
        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
                print(current_node.children)
            else:
                return None

        current_node = [current_node]
        
        next_node = []
        while True:
            for node in current_node:
                print(list(node.children.values()))
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words
    
    def search_query_cnt(self, query):
        # 실행한 결과가 있는지 확인 
        for result_q in list(self.result.keys()):
            if result_q == query:
                return self.result[result_q]
        current_node = [self.head]
        # 문자열 길이 
        search_node = []
        for q in query:
            search_node = current_node
            current_node = []
            for node in search_node:
                if q in node.children:    
                    current_node.append(node.children[q])
                elif q == '?': 
                    for next_node in list(node.children.values()):
                        current_node.append(next_node)    
                else:
                    continue
        count = 0
        for node in current_node:
            if node.data:
                count +=1
        self.result[query] = count
        return count
    def start_search_with(self,prefix) :
        current_node = self.head

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0

        return current_node.count

def solution(words: list[str], queries: list[str]):
    answer = []
    front_trie = {}
    back_trie = {}
    
    for word in words:
        if len(word) not in front_trie:
            front_trie[len(word)] = Trie()
            back_trie[len(word)] = Trie()
        print(word[::-1])
        front_trie[len(word)].insert(word)
        back_trie[len(word)].insert(word[::-1])

           
    for query in queries:
        if len(query) not in front_trie:
            answer.append(0)
            continue
       # 전부 물음표인 경우
        if len(query) == query.count('?'):
            answer.append(front_trie[len(query)].count)
            continue

        if query[-1] == '?':
            w = query.count('?')
            p = query[:len(query) - w]
            answer.append(front_trie[len(query)].start_search_with(p))
        else:
            w = query.count('?')
            p = query[w:][::-1]
            answer.append(back_trie[len(query)].start_search_with(p))
    return answer


    
    


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))
# 	[3, 2, 4, 1, 0]
# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao",'krozen'],["????o","fro??", "????o","????o", "fr???", "fro???", "????o","pro?",'?????']))



# def solution(words: list[str], queries: list[str]):
#     answer = []
#     query_result = []
    
#     # len start end 
#     for i,query in enumerate(queries):
#         start = 0
#         end = 0
#         query_len = len(query)
#         # 전제 조회 예외 
#         if query.count('?') == query_len:
#             answer.append(get_len_match_word(query_len,words))
#             query_result.append(query)  
#             continue
#         if query in query_result:
#             answer.append(answer[query_result.index(query)])
#             query_result.append(query)  
#             continue
        
#         if query[0] == '?':
#             start = query.count('?')
#             end = query_len
#         else:
#             start = 0
#             end = query.index('?')
#         # 중복된 키워드가 있는지 조회 

#         count = 0
#         for word in words:
#             if len(word) != query_len:
#                 continue
#             if word[start:end] == query[start:end]:
#                 count +=1
#         query_result.append(query)     
#         answer.append(count)
#     return answer


# def get_len_match_word(lenght,words):
#     count = 0
#     for word in words:
#         if len(word) == lenght:
#             count +=1
#     return count
    
    
    