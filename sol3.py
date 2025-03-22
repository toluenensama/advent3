import re

format_finding = r"mul\(\d+,\d+\)"
format_do = r"do(?:\(\))"
format_dont = r"don't(?:\(\))"

mul_all = []
mul_dont = []
mul_do = []
mul_doo = []
mul_dontdo = []
do = []
line_count = 0
k = ""

with open("day3.txt","r") as file:
    for line in file:
        line.rstrip('\n')
        k += line
print(len(k))

with open("day3.txt","r") as file:
    for line in file:
        line.rstrip('\n')
        mul_all.append(re.findall(format_finding,line))


print(type(k))
tetz = "ihasgdhaijdon't()ghgahsdo()diasddon't()hdo()gasvdo()isjgadon't()dfhasi"

tests_donts = k.split("don't()")
unaffected = k.split("don't()").pop(0)
unnafected_text = "".join(unaffected)
tests_donts.pop(0)
tests_donts_dos = []
for tests in tests_donts:
    tests_donts_dos.append(tests.split("do()"))

for kunta in tests_donts_dos:
    kunta.pop(0)


tests_donts_dos_texts = ""
for hui in tests_donts_dos:
    for jj in hui:
        tests_donts_dos_texts += "".join(jj)


all = unaffected + tests_donts_dos_texts
print(len(all))

mul_lists = re.findall(format_finding,all)
print(len(unnafected_text))

sum = 0
sum_all = 0
sum_dont = 0




for i in mul_all:
    for j in i:
        k = j[3:][1:]
        if len(k) != 0:
            m = k[:len(k)-1].split(",")
            for i in range(len(m) - 1):
                sum_all += int(m[i]) * int(m[i +1])

for i in mul_lists:
    k = i[3:][1:]
    m = k[:len(k)-1].split(",")
    print(m)
    for i in range(len(m) - 1):
        sum += int(m[i]) * int(m[i +1])
print(sum)


