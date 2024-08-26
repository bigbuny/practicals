#To find the maximum and minimum string in a tuple.

t=("AB", "CDE", "GHIJK", "LM","PQ", "RSTUVXWYZ")
weights=[[len(t[X]), t[X]] for X in range(len(t))]
weights_sep_sorted = sorted([weights[X][0] for X in range(len(weights))])
print(weights, '\n', weights_sep_sorted)
for i in range(len(t)):
    if weights[i][0] == weights_sep_sorted[0]:
        print(f"{weights[i][1]} is the minimum")
    if weights[i][0] == weights_sep_sorted[-1]:
        print(f"{weights[i][1]} is the maximum")

