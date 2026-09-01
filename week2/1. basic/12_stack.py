"""
[스택 - 괄호 짝 맞추기]

문제 설명:
- 스택(Stack)을 사용하여 괄호가 올바르게 짝지어져 있는지 확인합니다.
- LIFO (Last In First Out) 구조를 활용합니다.

입력:
- s: 괄호 문자열 (예: "(())", "(()")

출력:
- True: 올바른 괄호
- False: 잘못된 괄호

예제:
입력: "(())"
출력: True

입력: "(()"
출력: False

힌트:
- 여는 괄호 '('는 스택에 push
- 닫는 괄호 ')'를 만나면 스택에서 pop
- 마지막에 스택이 비어있으면 True
"""

#개념: 스택은 임시저장하는 자료구조로 스택에 데이터를 넣는것을 푸시,꺼내는것을 팝이라고한다
#LIFO: 후입선출 나중에 넣은값을 먼저 꺼낸다

def is_valid_parentheses(s):
    """
    괄호 짝이 맞는지 확인
    
    Args:
        s: 괄호 문자열
    
    Returns:
        올바른 괄호면 True, 아니면 False
    """
    stack = [] #1. 빈 리스트 만들기

    for char in s:#글자를 꺼내서 순회
        if char == "(":#문자열 비교
            stack.append(char)#스택에 문자열 추가
        elif char == ")":#닫는 괄호가 있을때
            if len(stack) == 0:#stack이 없을때
                return False
            else:
                stack.pop()#있을때 스택에서 꺼냄

    # TODO: 문자열의 각 문자를 순회
    ## : 여는 괄호 '('면 스택에 추가
    ## : 닫는 괄호 ')'면
    ## 스택이 비어있으면 False 반환
    ## 아니면 스택에서 pop
    pass
    if (len(stack))==0:
        return True #스택이 비어있어야 True
    else:
        return False
    # TODO: 반복이 끝나면 스택이 비어있는지 확인
    pass

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "(())"
    result1 = is_valid_parentheses(test1)
    print(f"입력: {test1}")
    print(f"결과: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "(()"
    result2 = is_valid_parentheses(test2)
    print(f"입력: {test2}")
    print(f"결과: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "()(())"
    result3 = is_valid_parentheses(test3)
    print(f"입력: {test3}")
    print(f"결과: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "())("
    result4 = is_valid_parentheses(test4)
    print(f"입력: {test4}")
    print(f"결과: {result4}")


