def binary_search(word_list, target):
    left = 0
    right = len(word_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if word_list[mid] == target:
            return True
        elif word_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# 테스트를 위한 단어 리스트
word_list = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fish', 'giraffe', 'horse', 'iguana']

# 검색할 단어
target_word = input("검색할 단어를 입력하세요 : ")

if binary_search(word_list, target_word):
    print(f"'{target_word}'는 리스트에 포함되어 있습니다.")
else:
    print(f"'{target_word}'는 리스트에 포함되어 있지 않습니다.")
