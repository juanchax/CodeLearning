import csv
import json

compromised_users = []

# Open the passwords csv file
with open('passwords.csv') as password_file:
    # Read CSV file
    password_csv = csv.DictReader(password_file)
    # append usernames to compromised_users list
    for password_row in password_csv:
        compromised_users.append(password_row['Username'])

# Create a new file to save the usernames
with open('compromised_users.txt', 'w') as compromised_user_file:
    #iterate over the compromised_users list
    for compromised_user in compromised_users:
        # write the compromised_user to the compromised_user_file
        compromised_user_file.write(compromised_user)

# Create JSON to send info
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {}
    boss_message_dict['recipient'] = 'The Boss'
    boss_message_dict['message'] = 'Mission Success'
    json.dump(boss_message_dict, boss_message)

# Remove password.csv file
with open('new_passwords.csv','w') as new_passwords_obj:
    slash_null_sig = '''
 _  _     ___   __  ____
/ )( \   / __) /  \(_  _)
) \/ (  ( (_ \(  O ) )(
\____/   \___/ \__/ (__)
 _  _   __    ___  __ _  ____  ____
/ )( \ / _\  / __)(  / )(  __)(    \
) __ (/    \( (__  )  (  ) _)  ) D (
\_)(_/\_/\_/ \___)(__\_)(____)(____/
        ____  __     __   ____  _  _
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __
(  ( \/ )( \(  )  (  )
/    /) \/ (/ (_/\/ (_/\
\_)__)\____/\____/\____/
'''
    new_passwords_obj.write(slash_null_sig)
