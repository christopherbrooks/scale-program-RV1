import random

len_scale_pattern = int(input("length of scale pattern"))
number_of_octaves = int(input("number of octaves")) 
total_number_of_notes = len_scale_pattern * number_of_octaves

def get_all_factors(n):
    factors = []
    for i in range(2,n+1):
        if n%i == 0:
            factors.append(i)
    return factors

list_of_factors = get_all_factors(total_number_of_notes)
number_of_notes_in_rhythm = random.choice(list_of_factors)

beats_in_measure = random.choice([3, 4, 5]) # this may be expanded
subdivision = random.choice([3, 4, 5]) # this may be expanded
subdivisions_available = subdivision * beats_in_measure 

n = number_of_notes_in_rhythm
rhythm_pattern = []

while n > 0:
    rhythm = random.randint(1, subdivisions_available-n)
    rhythm_pattern.append(rhythm)
    subdivisions_available = subdivisions_available - rhythm
    n = n - 1
rhythm = subdivisions_available
rhythm_pattern.append(rhythm)
 
print (rhythm_pattern)

