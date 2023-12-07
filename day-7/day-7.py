# Constants used to identify hand type
FIVE_OF_A_KIND = 0
FOUR_OF_A_KIND = 1
FULL_HOUSE = 2
THREE_OF_A_KIND = 3
TWO_PAIR = 4
ONE_PAIR = 5
HIGH_CARD = 6

LETTER_RANKINGS = ['A', 'K', 'Q', 'J', 'T']

ranked_hands = [[],[],[],[],[],[],[]]
number_of_hands = 0

def determine_hand_type(hand):
    frequencies = {}
    for i in range(len(hand)):
        if hand[i] in frequencies:
            frequencies[hand[i]] += 1
            
            if frequencies[hand[i]] == 5:
                return FIVE_OF_A_KIND
        else:
            frequencies[hand[i]] = 1
    
    keys = list(frequencies.keys())
    if len(keys) == 5: return HIGH_CARD
    elif len(keys) == 4: return ONE_PAIR
    elif len(keys) == 2:
        if frequencies[keys[0]] == 4 or frequencies[keys[1]] == 4:
            return FOUR_OF_A_KIND
        else: return FULL_HOUSE    
    else:
        for i in range(len(keys)):
            if frequencies[keys[i]] == 3: return THREE_OF_A_KIND
            elif frequencies[keys[i]] == 2: return TWO_PAIR

def add_to_ranked(input, h_type):
    if len(ranked_hands[h_type]) == 0:
        ranked_hands[h_type].append(input)
    else:
        for i in range(len(ranked_hands[h_type])):
            current_hand = ranked_hands[h_type][i]
            if compare(current_hand[0], input[0]) == input[0]:
                ranked_hands[h_type][i] = input
                ranked_hands[h_type].insert(i+1, current_hand)
                return
        # if it exits the loop, no weaker hand has been found, so append it to the list
        ranked_hands[h_type].append(input)

#compares two hands of the same type, and returns stronger hand
def compare(hand1, hand2):
    for i in range(5):
        if '0' <= hand1[i] <= '9':
            #if hand1 has digit and hand2 has letter, hand2 is stronger
            if '0' > hand2[i] or hand2[i] > '9': return hand2
            elif hand1[i] > hand2[i]: return hand1
            elif hand2[i] > hand1[i]: return hand2
        else:
            #if hand1 has letter and hand2 has digit, hand1 is stronger
            if '0' <= hand2[i] <= '9': return hand1
            else:
                #if both have letter, compare to the index of the letter_rankings list
                index1 = LETTER_RANKINGS.index(hand1[i])
                index2 = LETTER_RANKINGS.index(hand2[i])
                if index1 < index2: return hand1
                elif index2 < index1: return hand2

def calculate_score():
    rank = 0
    total = 0
    
    for hand_type in range(len(ranked_hands)):
        current_set = ranked_hands[hand_type]
        for hand in range(len(current_set)):
            total += (number_of_hands - rank) * (int)(current_set[hand][1])
            rank += 1
    return total

with open("day-7\\input.txt", 'r') as input_file:
    for line in input_file:
        input = line.split()
        hand_type = determine_hand_type(input[0])
        add_to_ranked(input, hand_type)
        number_of_hands += 1
    
    print(calculate_score())