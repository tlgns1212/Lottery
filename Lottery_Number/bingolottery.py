
# 역대 당첨번호 각 자리별로 확률 구하기
import random
import sys
input = sys.stdin.readline

five_choices = [[] for _ in range(5)]
lottery_str = []
lottery_file = open("Lottery_Number/bingo_lottery.txt", "r", encoding="utf8")
while True:
    line = lottery_file.readline()
    if not line:
        break
    lottery_str.append(line)
lottery_file.close()

lottery_list = []
for i in lottery_str:
    lottery_list.append(i.replace('\t', ',').split(','))

# print(lottery_list)

percentage_by_spot = [0 for _ in range(76)]
for i in lottery_list:
    percentage_by_spot[int(i[2])] += 1
    percentage_by_spot[int(i[3])] += 1
    percentage_by_spot[int(i[4])] += 1
    percentage_by_spot[int(i[5])] += 1
    percentage_by_spot[int(i[6])] += 1
    percentage_by_spot[int(i[7])] += 1
    percentage_by_spot[int(i[8])] += 1
    percentage_by_spot[int(i[9])] += 1
    percentage_by_spot[int(i[10])] += 1
    percentage_by_spot[int(i[11])] += 1
    percentage_by_spot[int(i[12])] += 1
    percentage_by_spot[int(i[13])] += 1
    percentage_by_spot[int(i[14])] += 1
    percentage_by_spot[int(i[15])] += 1
    percentage_by_spot[int(i[16])] += 1
    percentage_by_spot[int(i[17])] += 1
    percentage_by_spot[int(i[18])] += 1
    percentage_by_spot[int(i[19])] += 1
    percentage_by_spot[int(i[20])] += 1
    percentage_by_spot[int(i[21])] += 1
    percentage_by_spot[int(i[22])] += 1
    percentage_by_spot[int(i[23])] += 1
    percentage_by_spot[int(i[24])] += 1
    percentage_by_spot[int(i[25])] += 1
    percentage_by_spot[int(i[26])] += 1
    percentage_by_spot[int(i[27])] += 1
    percentage_by_spot[int(i[28])] += 1
    percentage_by_spot[int(i[29])] += 1
    percentage_by_spot[int(i[30])] += 1
    percentage_by_spot[int(i[31])] += 1
    percentage_by_spot[int(i[32])] += 1
    percentage_by_spot[int(i[33])] += 1
    percentage_by_spot[int(i[34])] += 1
    percentage_by_spot[int(i[35])] += 1
    percentage_by_spot[int(i[36])] += 1
    percentage_by_spot[int(i[37])] += 1
    percentage_by_spot[int(i[38])] += 1
    percentage_by_spot[int(i[39])] += 1
    percentage_by_spot[int(i[40])] += 1
    percentage_by_spot[int(i[41])] += 1
    percentage_by_spot[int(i[42])] += 1
    percentage_by_spot[int(i[43])] += 1
    percentage_by_spot[int(i[44])] += 1
    percentage_by_spot[int(i[45])] += 1
    percentage_by_spot[int(i[46])] += 1
    percentage_by_spot[int(i[47])] += 1
    percentage_by_spot[int(i[48])] += 1
    percentage_by_spot[int(i[49])] += 1
    percentage_by_spot[int(i[50])] += 1
    # percentage_by_spot[int(i[51])] += 1
    # percentage_by_spot[int(i[52])] += 1
    # percentage_by_spot[int(i[53])] += 1
    # percentage_by_spot[int(i[54])] += 1
    # percentage_by_spot[int(i[55])] += 1
    # percentage_by_spot[int(i[56])] += 1
    # percentage_by_spot[int(i[57])] += 1
    # percentage_by_spot[int(i[58])] += 1
    # percentage_by_spot[int(i[59])] += 1
    # percentage_by_spot[int(i[60])] += 1
    # percentage_by_spot[int(i[61])] += 1
    # percentage_by_spot[int(i[62])] += 1
    # percentage_by_spot[int(i[63])] += 1
    # percentage_by_spot[int(i[64])] += 1
    # percentage_by_spot[int(i[65])] += 1
    # percentage_by_spot[int(i[66])] += 1
    # percentage_by_spot[int(i[67])] += 1
    # percentage_by_spot[int(i[68])] += 1
    # percentage_by_spot[int(i[69])] += 1
    # percentage_by_spot[int(i[70])] += 1
    # percentage_by_spot[int(i[71])] += 1
    # percentage_by_spot[int(i[72])] += 1
    # percentage_by_spot[int(i[73])] += 1
    # percentage_by_spot[int(i[74])] += 1
    # percentage_by_spot[int(i[75])] += 1
    # percentage_by_spot[int(i[76])] += 1

a = 0
sums = []
for i in percentage_by_spot:
    # print(f'{a} = {i}')
    sums.append([a, i])
    a += 1
sums.sort(key=lambda x: -x[1])
a = 1

for i in sums:
    if i[0] < 16:
        five_choices[0].append(i)
    elif i[0] < 31:
        five_choices[1].append(i)
    elif i[0] < 46:
        five_choices[2].append(i)
    elif i[0] < 61:
        five_choices[3].append(i)
    else:
        five_choices[4].append(i)
for i in five_choices:
    print(f'-{a}번재 줄 {i}')
    a += 1

# 1위부터 75위까지 한줄에 하나씩 출력하는 방법
# for i in sums:
#     print(f'{a} = {i}')
#     a += 1


# print(percentage_by_spot)
# for i in range(len(percentage_by_spot)):
#     percentage_by_spot[i] /= len(lottery_list)


# # 각 자리별로 하나씩 뽑기(마지막은 보너스 번호)
# for i in percentage_by_spot:
#     print(random.choices([j for j in range(0,46)],i), end = " ")
# print()


# # 미완성
# recommend_lottery_num = [[0 for _ in range(46)] for _ in range(7)]
# print("몇 번 로또를 뽑을지 정하시오 : ",end = "")
# how_much = int(input())
# for _ in range(how_much):
#     n = 0
#     for i in percentage_by_spot:
#         recommend_lottery_num[n][random.choices([j for j in range(0,46)],i)]
#         n += 1
# print(recommend_lottery_num)
