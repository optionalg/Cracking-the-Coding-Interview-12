# Write a method that returns all subsets of a set.

def itr_get_subset(lis):
    subset = [[]]
    for values in lis:
        temp_subset = subset[:]
        for sub in temp_subset:
            subset.append(sub + [values])
    return subset

# lis = [2,3,5]
# print (get_subset(lis))

def get_subset(lis):
	if len(lis) == 1:
		return [[], lis]
	subset = get_subset(lis[1:])
	temp_subset = subset[:]
	for sub_lis in temp_subset:
		subset.append([lis[0]] + sub_lis)
	return subset

lis = [2,3,5]
print (get_subset(lis))