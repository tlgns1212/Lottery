# 역대 당첨번호 각 자리별로 확률 구하기
import random
import sys
input = sys.stdin.readline


lottery_str = []
lottery_file = open("lottery_won.txt", "r", encoding="utf8")
while True:
    line = lottery_file.readline()
    if not line:
        break
    lottery_str.append(line)
lottery_file.close()

lottery_list = []
for i in lottery_str:
    lottery_list.append(i.split())

# for i in lottery_list:
#     print(i)

percentage_by_spot = [[0 for _ in range(46)] for _ in range(7)]
for i in lottery_list:
    percentage_by_spot[0][int(i[1])] += 1
    percentage_by_spot[1][int(i[2])] += 1
    percentage_by_spot[2][int(i[3])] += 1
    percentage_by_spot[3][int(i[4])] += 1
    percentage_by_spot[4][int(i[5])] += 1
    percentage_by_spot[5][int(i[6])] += 1
    percentage_by_spot[6][int(i[7])] += 1

print(percentage_by_spot)
for i in range(len(percentage_by_spot)):
    for j in range(len(percentage_by_spot[i])):
        percentage_by_spot[i][j] /= len(lottery_list)


# 각 자리별로 하나씩 뽑기(마지막은 보너스 번호)
for i in percentage_by_spot:
    print(random.choices([j for j in range(0,46)],i), end = " ")
print()


# 미완성
recommend_lottery_num = [[0 for _ in range(46)] for _ in range(7)]
print("몇 번 로또를 뽑을지 정하시오 : ",end = "")
how_much = int(input())
for _ in range(how_much):
    n = 0
    for i in percentage_by_spot:
        recommend_lottery_num[n][random.choices([j for j in range(0,46)],i)]
        n += 1
print(recommend_lottery_num)