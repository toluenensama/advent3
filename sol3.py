import re

format_finding = r"mul\(\d+,\d+\)"
format_do = r"do(?:\(\)).mul\(\d+,\d+\)"
format_doo = r"do(?:\(\))mul\(\d+,\d+\)"
format_dont = r"don't(?:\(\)).mul\(\d+,\d+\)"
format_dontdo = r"don't(?:\(\))mul\(\d+,\d+\)"

mul_all = []
mul_dont = []
mul_do = []
mul_doo = []
mul_dontdo = []
do = []
line_count = 0

with open("day3.txt","r") as file:
    for line in file:
        line.rstrip('\n')
        mul_dont.append(re.findall(format_dont,line))
        mul_all.append(re.findall(format_finding,line))
        dont= line.split("don't()")
        print("dont: ",re.findall(format_dont,line))
        print("do: ",re.findall(format_do,line))
        print("dontdo: ",re.findall(format_dontdo,line))
        print("doo: ",re.findall(format_doo,line))
        line_count += 1

print(line_count)
print(len(dont[0]))
# print(dont[0])


for text in dont:
    if len(text.split("do()")) >= 2:
        print((text.split("do()")[0]),"\n")
        mum = "".join(text)
    else:
        print(text.split("do()"),"\n")
    
print(mum)
mul1 = re.findall(format_finding,mum)
print(len(mul1))
# for items in dont:
#     for item in items:
#         do.append(item.split("do()"))


# print(len(dont[0]))
# print(len(dont[0][0].split("do()")[0]))
# a = dont[0][0].split("do()")[0]
# g = re.findall(format_finding,a)
# print(g)
# print(dont[0])
# print(len(do[0]))
# print(mul_do)
# print(mul_doo)
# print(mul_dont)
# # print(mul_all)
# print(mul_dontdo)
sum = 0
sum_do = 0
sum_dont = 0

# for i in mul_dont:
#     for j in i:
#         k = j[10:][1:]
#         if len(k) != 0:
#             print(k)
#             m = k[1:][:len(k)-2].split(",")
#             print("mull dont",m)
#             for i in range(len(m) - 1):
#                 sum_dont += int(m[i]) * int(m[i +1])


for i in mul_all:
    for j in i:
        k = j[3:][1:]
        if len(k) != 0:
            m = k[:len(k)-1].split(",")
            # print("mull all",m)
            for i in range(len(m) - 1):
                sum += int(m[i]) * int(m[i +1])

# print(sum)
# print(sum_do)
# print(sum_dont)

# final_sum = (sum - sum_dont) + sum_do
# print(final_sum)
