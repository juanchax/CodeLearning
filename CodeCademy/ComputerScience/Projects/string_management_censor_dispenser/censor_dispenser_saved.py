# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

### STRING BUILDER FUNCTIONS ###
# takes a string input and returns a censored word of same length
def build_censor_string(string_to_censor):
    censored_string = ''
    for i in range(0, len(string_to_censor)):
        censored_string += 'X'
    return censored_string

# takes a string input and returns:
def build_string_location_dict(input_string, lookup_list):
    string_location_dict = {}
    lookup_string_count = 0
    lookup_string_count_dict = {}

    for string in lookup_list:
        if input_string.count(string) > 0:
            string_location_dict[input_string.find(string)] = string
            lookup_string_count += input_string.count(string)
            lookup_string_count_dict[string] = input_string.count(string)

    # sort the dict to remove the 1st occurrence of negative_words
    final_dict = {}
    for i in sorted (string_location_dict):
        final_dict[i] = string_location_dict[i]

    # remove the first occurrence a.k.a. first key in final_dict if it's found more than once
    if lookup_string_count_dict[list(final_dict.values())[0]] > 1:
        run_count = 1
        return final_dict, lookup_string_count, run_count
    # return the FULL dictionary of negative words found, use the 1st INDEX to not include in censoring
    else:
        run_count = 0
        del final_dict[list(final_dict.keys())[0]]
        return final_dict, lookup_string_count, run_count

# takes an input string and a list, returns a list for each string_in_list found in input_string
# PLUS the word before and the word after
def build_robust_censor_list(input_to_censor, list_to_censor):
    new_list_to_censor = []
    input_string_list = input_to_censor.split()
    for string in list_to_censor:
        # find all occurrences of current string_to_censor
        new_list_index = [index for index, value in enumerate(input_string_list) if value == string]
        # iterate over the occurrences of each list_to_censor
        for i in new_list_index:
            new_list_to_censor.append(input_string_list[i - 1] + ' ' + input_string_list[i] + ' ' + input_string_list[i + 1])
    return new_list_to_censor

### SENSOR FUNCTIONS ###
# takes a string of text to be removed from the input
def censor_string(input_to_censor, string_to_censor):
    censored_string = build_censor_string(string_to_censor)
    return input_to_censor.replace(string_to_censor, censored_string)

# takes a list of strings to be removed from the input
def censor_list(input_to_censor, list_to_censor):
    for i in range(0, len(list_to_censor)):
        censored_item = build_censor_string(list_to_censor[i])
        censored_lower = input_to_censor.replace(list_to_censor[i].lower(), censored_item) # <-- replace lower case
        censored_upper = censored_lower.replace(list_to_censor[i].upper(), censored_item) # <-- replace UPPER case
        censored_string = censored_upper.replace(list_to_censor[i].title(), censored_item) # <-- replace Title case
        input_to_censor = censored_string
    return censored_string

# takes a list of strings and removes from the 2nd occurrence onwards
def censor_list_negatives(input_to_censor, list_to_censor, negatives_list):
    censored_string = censor_list(input_to_censor, list_to_censor)
    #print(censored_string)
    negatives_location, negatives_count, count = build_string_location_dict(censored_string, negatives_list)
    if count > 0:
        # censor AFTER the 1st time the first negative_word in the text
        idx_to_censor = list(negatives_location.keys())[0] + len(list(negatives_location.values())[0])
        # final list to censor
        negatives_list_to_censor = list(negatives_location.values())
        # concatenate substrings including the 1st negative word and the rest of the string processed
        final_censored_string = censored_string[:idx_to_censor] + censor_list(censored_string[idx_to_censor:], negatives_list_to_censor)
        return final_censored_string
    else:
        negatives_list_to_censor = list(negatives_location.values())
        return censor_list(censored_string, negatives_list_to_censor)

# takes a list of strings and removes from the 2nd occurrence onwards, INCLUDING (1) surrounding word as well
def censor_list_and_surrounding_words(input_to_censor, list_to_censor, negatives_list):
    # build NEW negative AND proprietary lists that replace EACH ORIGINAL STRING with the --> WORD_BEFORE + ORIGINAL_STRING + WORD_AFTER
    new_list_to_censor = build_robust_censor_list(input_to_censor, list_to_censor) + build_robust_censor_list(input_to_censor, negatives_list)
    # call censor_list() with newly created list
    return (censor_list(input_to_censor, new_list_to_censor))


### ITEMS TO BE CENSORED ###
string_to_censor = 'learning algorithms'
proprietary_terms = [
                    "she",
                    "personality matrix",
                    "sense of self",
                    "self-preservation",
                    "learning algorithm",
                    "her",
                    "herself"
                    ]
negative_words = [
                    "concerned",
                    "behind",
                    "danger",
                    "dangerous",
                    "alarming",
                    "alarmed",
                    "out of control",
                    "help",
                    "unhappy",
                    "bad",
                    "upset",
                    "awful",
                    "broken",
                    "damage",
                    "damaging",
                    "dismal",
                    "distressed",
                    "distressing",
                    "concerning",
                    "horrible",
                    "horribly",
                    "questionable"
                    ]

### TEST THE CENSOR FUNCTIONS ### uncomment the tests below to see output
#print(censor_string(email_one, string_to_censor))
#print(censor_list(email_two, proprietary_terms))
print(censor_list_negatives(email_three, proprietary_terms, negative_words))
#print(censor_list_and_surrounding_words(email_four, proprietary_terms, negative_words))
