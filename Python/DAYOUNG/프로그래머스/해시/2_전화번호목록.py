# def solution(phone_book):
#     answer = True
#     for i in range(len(phone_book)-1):
#         hash1 = {}
#         hash2 = {}
#         for j in range(len(phone_book[i])):
#             hash1[phone_book[i][j:]] = 0
#             hash2[phone_book[i+1][:j+1]] = 0
#             print(hash1)
#             print(hash2)
#             print("-------------------")
#         for key1 in list(hash1.keys()):
#             if key1 in hash2:
#                 answer = False
#     return answer

# print(solution(["119", "97674223", "1195524421"]))

# def solution2(phone_book):
#     answer = True
#     for i in range(len(phone_book)-1):
#         hash1 = {}
#         for j in range(len(phone_book[i])):
#             hash1[phone_book[i][j:]] = 0
#             compare = phone_book[i+1][0:len(phone_book[i])-j]
#             # print(hash1)
#             # print(compare)
#             # print("-------------------")
#             if compare in hash1:
#                 answer = False
#                 break
#         # if not answer:
#         #     break
#     return answer

# print(solution2(["119", "97674223", "1195524421"]))
# print(solution2(["123", "456", "789"]))
# print(solution2(["12", "123", "1235", "567", "88"]))
# print(solution2(["312321", "2134", "24124"]))

# def solution3(phone_book):
#     answer = True
#     phone_book = sorted(phone_book)
#     print("phone_book: ",phone_book)
#     for i in range(len(phone_book)-1):
#         hash1 = []
#         hash2 = []
#         for j in range(len(phone_book[i])):
#             hash1.append(phone_book[i][j:])
#             hash2.append(phone_book[i+1][0:j+1])
#         print(hash1)
#         print(hash2)
#         print("---------------------------")

#     return answer

# print(solution3(["312321", "2134", "24124"]))
# print(solution3(["123", "456", "789"]))

def solution4(phone_book):
    for i in range(len(phone_book)):
        k1 = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            k2 = len(phone_book[j])
            print(phone_book[i], phone_book[j][:k1])
            print(phone_book[j], phone_book[i][:k2])
            print("--")
            if phone_book[i] in phone_book[j][:k1] or phone_book[j] in phone_book[i][:k2] :
                return False
    return True

print(solution4(["119", "97674223", "1195524421"]))
print("----==-")
print(solution4(["123", "456", "789"]))
print("----==-")
print(solution4(["12", "123", "1235", "567", "88"]))
print("----==-")
print(solution4(["312321", "2134", "24124"]))