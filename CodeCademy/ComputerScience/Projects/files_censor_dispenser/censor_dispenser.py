# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

### SENSOR FUNCTIONS ###

# takes a string of text to be removed from the input
def censor_string(text, my_string):
    return text.replace(my_string,'XXXXXX')

# takes a list of strings to be removed from the input
def censor_list(text, my_list):
    for i in range(0, len(my_list)):
        censored_display = '' # write code to replace word with 'XXX' of same length
        censored_lower = text.replace(my_list[i].lower(), 'XXXXXX') # <-- replace lower case
        censored_upper = censored_lower.replace(my_list[i].upper(), 'XXXXXX') # <-- replace UPPER case
        censored_text = censored_upper.replace(my_list[i].title(), 'XXXXXX') # <-- replace Title case
        text = censored_text
    return censored_text

# takes a list of strings and censors after the 2nd occurrence
def censor_list_negatives(text, my_list, negatives_list):
        for i in range(0, len(my_list)):
            censored_display =
            censored_lower = text.replace(my_list[i].lower(), 'XXXXXX') # <-- replace lower case
            censored_upper = censored_lower.replace(my_list[i].upper(), 'XXXXXX') # <-- replace UPPER case
            censored_text = censored_upper.replace(my_list[i].title(), 'XXXXXX') # <-- replace Title case
            text = censored_text

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
