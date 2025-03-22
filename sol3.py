import re

format_finding = r"mul\(\d+,\d+\)" #format of string to be found


mul_all = [] #initialize the list of mul functions found

k = "" #Initialize the whole text

# get the whole text to one string
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
# split by dont()
tests_donts = k.split("don't()")

# remove the first set since they are not affected
unaffected = k.split("don't()").pop(0)
# making sure theyre in a singletext
unnafected_text = "".join(unaffected)
tests_donts.pop(0)
tests_donts_dos = []
# spliting the whole dont statements by dos
for tests in tests_donts:
    tests_donts_dos.append(tests.split("do()"))

# delete the first since they are not affected yet
for kunta in tests_donts_dos:
    kunta.pop(0)


tests_donts_dos_texts = ""
for hui in tests_donts_dos:
    for jj in hui:
        tests_donts_dos_texts += "".join(jj)


all = unaffected + tests_donts_dos_texts

mul_lists = re.findall(format_finding,all)

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
    for i in range(len(m) - 1):
        sum += int(m[i]) * int(m[i +1])
print(sum)


