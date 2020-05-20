# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

### SENSOR FUNCTIONS ###

# takes a string input and returns a censored word of same length
def word_censored(my_string):
    censored_word = ''
    for i in range(0, len(my_string)):
        censored_word += 'X'
    return censored_word

# takes a string of text to be removed from the input
def censor_string(text_to_censor, string_to_censor):
    censored_word = word_censored(string_to_censor)
    return text_to_censor.replace(string_to_censor, censored_word)

# takes a list of strings to be removed from the input
def censor_list(text_to_censor, list_to_censor):
    for i in range(0, len(list_to_censor)):
        censored_word = word_censored(list_to_censor[i])
        censored_lower = text_to_censor.replace(list_to_censor[i].lower(), censored_word) # <-- replace lower case
        censored_upper = censored_lower.replace(list_to_censor[i].upper(), censored_word) # <-- replace UPPER case
        censored_text = censored_upper.replace(list_to_censor[i].title(), censored_word) # <-- replace Title case
        text_to_censor = censored_text
    return censored_text

# takes a list of strings and removes from the 2nd occurrence onwards
def censor_list_negatives(text_to_censor, list_to_censor, negatives_list):
    censored_text = censor_list(list_to_censor)

    return censored_text

        # use string.find() to get the index for each negative word
        # build a list of indexes and then censor the words in list[1:] <-- IGNORES THE 1st OCCURRENCE!!

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
                    "distressed",
                    "concerning",
                    "horrible",
                    "horribly",
                    "questionable"
                    ]

### RUN THE CENSOR FUNCTIONS ###
print(censor_string(email_one, string_to_censor))
print(censor_list(email_two, proprietary_terms))
