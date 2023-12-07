# Constants used to identify hand type
FIVE_OF_A_KIND = 0
FOUR_OF_A_KIND = 1
FULL_HOUSE = 2
THREE_OF_A_KIND = 3
TWO_PAIR = 4
ONE_PAIR = 5
HIGH_CARD = 6

CARD_RANKINGS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

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
    if 'J' in keys:
        number_of_jokers = frequencies['J']
        frequencies.pop('J')
        keys.remove('J')
        
        if len(keys) == 1 or number_of_jokers == 5: return FIVE_OF_A_KIND
        elif len(keys) == 4: return ONE_PAIR # if there is at least one J, there can be no high card type
        elif len(keys) == 2: #if four of a kind or full house
            #the only scenario where it would be full house is if there is one J, and 2 of each other type
            if frequencies[keys[0]] == 2 and frequencies[keys[1]] == 2:
                return FULL_HOUSE
            else: return FOUR_OF_A_KIND
        else: #cannot be a two pair, as J will always join up to make a three of a kind
            return THREE_OF_A_KIND
            
    else:
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
        index1 = CARD_RANKINGS.index(hand1[i])
        index2 = CARD_RANKINGS.index(hand2[i])
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