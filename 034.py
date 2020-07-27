l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

max_val = l[0]
min_val = l[0]

for elem in l:
    if elem > max_val:
        max_val = elem
    if elem < min_val:
        min_val = elem

print(f"max: {max_val}") # 3
print(f"min: {min_val}") # 0

# max_val = max(l)
# min_val = min(l)
