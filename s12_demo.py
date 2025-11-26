# import csv

# header = ["Stock", "Share"]
# data = [
#     ["MSFT", 25],
#     ["GOOG", 30],
#     ["AAPL", 15],
#     ["AMZN", 10],
# ]

# with open("data/data.csv", "w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     # csv_writer.writerows(data) # or
#     csv_writer.writerow(header)
#     for row in data:
#         csv_writer.writerow(row)


counter = {}
gene_sequence = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCT"
for base in gene_sequence:
    if base in counter:  # when the key does exist
        counter[base] += 1
    else:  # when the key does not exist
        counter[base] = 1

print(counter)