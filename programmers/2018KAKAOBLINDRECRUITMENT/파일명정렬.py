import heapq

# https://school.programmers.co.kr/questions/14398 6,7,8,9 특수문자 관련 오류
# https://school.programmers.co.kr/questions/27123  파일이 숫자로 끝날경우 에러


def solution(files: list[str]):
    answer = []
    tmp = []
    # head,number,tail 로 분리
    for idx, file in enumerate(files):
        number = ''
        head = ''
        is_num_mode = False
        for c in file:
            if ord('0') <= ord(c) <= ord('9'):
                is_num_mode = True
                number += c
            else:
                # head 랑 number 그리고 tail 을 분리
                # (head,number,순서) 우선순위큐 담기
                if is_num_mode == True:
                    heapq.heappush(tmp, (head.lower(), int(number), idx))
                    break
                else:
                    head += c
        else:
            # 파일이 숫자로 끝날경우
            heapq.heappush(tmp, (head.lower(), int(number), idx))
    print(tmp)
    for _ in range(len(tmp)):
        head, number, idx = heapq.heappop(tmp)
        answer.append(files[idx])
    return answer


print(solution(["O 00321", "O 49qcGPHuRLR5FEfoO00321"])
      == ["O 49qcGPHuRLR5FEfoO00321", "O 00321"])
print(solution(["O00321", "O49qcGPHuRLR5FEfoO00321"])
      == ["O49qcGPHuRLR5FEfoO00321", "O00321"])
print(solution(["aoo020bar020.zip", "FOO0001bar010.zip", "foo001bar020.zip"]))
print(solution(["img12.png", "img10.png", "img02.png",
      "img1.png", "IMG01.GIF", "img2.JPG"]) == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
      == ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])
