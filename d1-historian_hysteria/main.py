# PART ONE
# get input from file
f = open("input.txt", "r")

# divide column into left and right
left = []
right = []
for line in f:
    left.append(int(line[:5]))
    right.append(int(line[5:].rstrip()))

left.sort()
right.sort()

# calculate differences
diff = []
for l in range(0, len(left)):
    diff.append(abs(left[l] -right[l]))

# print the sums
print("sums")
print(sum(diff))


# PART TWO
# count orruences
def countOccurences(l1, l2):
    occurrences = []
    for l1item in l1:
        counter = 0
        for l2item in l2:
            if(l1item == l2item):
                counter += 1
        occurrences.append(counter)
    return occurrences

# get occurences from left to right column
left_occ = countOccurences(left, right)
#right_occ = countOccurences(right, left)
occurrence_sum = []

# calculate total values of each occurered item
for ind in range(0, len(left)):
    occurrence_sum.append((left_occ[ind] * left[ind]))# + (right_occ[ind] * right[ind]))

print("occurences")
#print(occurrence_sum)
print(sum(occurrence_sum))

