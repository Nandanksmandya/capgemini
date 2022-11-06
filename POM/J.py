import re

#
# s = "cap56lim12p2"
# a = re.findall('\d+', s)
# print(a)
# sum_ = 0
# for i in a:
#     sum_ = sum_ + int(i)
#
# print(sum_)

# n = ['5076543210', '890234567145', '123456778']
# for i in n:
#     print(re.findall('[6-9]\d{9}$', i))

##########################################################################
a = 'hellooo'
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
