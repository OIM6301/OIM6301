with open("data/mess.txt") as file:
    mess = file.read()
    # print(mess)

counter = {}

for c in mess:
    if c in counter:  # when the key does exist
        counter[c] += 1
    else:  # when the key does not exist
        counter[c] = 1

# print(counter)

result = []
for c, freq in counter.items():
    if freq == 1:
        result.append(c)

# print(result)
print(''.join(result))