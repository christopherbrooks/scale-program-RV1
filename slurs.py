import random

# sets up slurs for scale. Every set of slurs must be closed: start with ( and end with )
def get_slurs(number_notes_bowing_pattern):

    bow_pattern = []
    left_slur_or_empty = ["(", " "]
    right_slur_or_empty = [")", " "]

    right_slur = False
    left_slur = False

    n = 0
    bow_pattern.append(random.choice(left_slur_or_empty)) # first note

    if bow_pattern[n] == "(": # if the first note has a slur
        left_slur = True
    n += 1

    while n < number_notes_bowing_pattern - 2: # n starts on 2nd note (1) loop to next to last note
        if left_slur:
            bow_pattern.append(random.choice(right_slur_or_empty))
            if bow_pattern[n] == ")":
                left_slur = False
                right_slur = True
        elif right_slur:
            bow_pattern.append(random.choice(left_slur_or_empty))
            if bow_pattern[n] == "(":
                left_slur = True
                right_slur = False
        n +=1

    if right_slur:
        bow_pattern.append(" ")
    elif left_slur:
        bow_pattern.append(")")
    return bow_pattern


if __name__ == '__main__':
    number_notes_bowing_pattern = int(input("how many notes in bowing pattern?"))
    print(get_slurs(number_notes_bowing_pattern))

