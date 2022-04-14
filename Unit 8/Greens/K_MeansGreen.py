import random
from copy import copy
from math import log

with open('star_data.csv') as f:
    to_look = [line for line in f]
    to_look.pop(0)
    training_set = [[float(x) for x in line.split(",")[:5]] for line in to_look]

K = 6
CATEGORIES = 5
K = 6
CATEGORIES = 5
K = 6
CATEGORIES = 5
means = random.sample(training_set, K)
means = [[mean] for mean in means]
old_means = copy(means)
new_means = [[] for i in range(K)]
while new_means != old_means:
    old_means = copy(new_means)
    for star in training_set:
        vectorized_star = (log(star[0]), log(star[1]), log(star[2]), star[3])
        s1, s2, s3, s4 = vectorized_star
        errors = []
        for mean in means:
            toCompare = mean[0]
            vectorized_mean = (log(toCompare[0]), log(toCompare[1]), log(toCompare[2]), toCompare[3])
            m1, m2, m3, m4 = vectorized_mean
            errors.append( ((m1 - s1)**2) + ((m2 - s2)**2) + ((m3 - s3)**2) + ((m4 - s4)**2) )
        means[errors.index(min(errors))].append(star)

    for index, star_group in enumerate(means):
        avgs = []
        for i in range(CATEGORIES):
            combined_sum = 0
            for star in star_group:
                combined_sum += star[i]
            avgs.append((combined_sum/len(star_group)))
        new_means[index].append(avgs)
    
means = copy(new_means)
for star in training_set:
        vectorized_star = (log(star[0]), log(star[1]), log(star[2]), star[3])
        s1, s2, s3, s4 = vectorized_star
        errors = []
        for mean in means:
            toCompare = mean[0]
            vectorized_mean = (log(toCompare[0]), log(toCompare[1]), log(toCompare[2]), toCompare[3])
            m1, m2, m3, m4 = vectorized_mean
            errors.append( ((m1 - s1)**2) + ((m2 - s2)**2) + ((m3 - s3)**2) + ((m4 - s4)**2) )
        means[errors.index(min(errors))].append(star)


for index, mean in enumerate(means):
    print(f"Mean {index}:", mean[0], '\n', '.'*80, '\n')
    for star in mean[1:]:
        print(star, " with star type: ", star[4])
    print()

