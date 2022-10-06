def solution(survey, choices):
    answer = ''
    matrix = [{"R": 0, "T": 0}, {"C": 0, "F": 0},
              {"J": 0, "M": 0}, {"A": 0, "N": 0}]

    def select_survey(matrix, survey, choice):
        if choice < 4:
            matrix[survey[0]] += abs(4-choice)
        elif choice > 4:
            matrix[survey[1]] += abs(4-choice)

    for idx, choice in enumerate(choices):
        if survey[idx] in ["RT", "TR"]:
            select_survey(matrix[0], survey[idx], choice)
        elif survey[idx] in ["FC", "CF"]:
            select_survey(matrix[1], survey[idx], choice)
        elif survey[idx] in ["MJ", "JM"]:
            select_survey(matrix[2], survey[idx], choice)
        else:
            select_survey(matrix[3], survey[idx], choice)
    print(matrix)
    for m in matrix:
        items = list(m.items())
        if items[0][1] < items[1][1]:
            answer += items[1][0]
        else:
            answer += items[0][0]
    return answer


# print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]) == "TCMA")
print(solution(["TR", "RT", "TR"], [7, 1, 3]) == "RCJA")
