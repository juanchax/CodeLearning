import random

money = 100
#player_2_money = 100

#Write your game of chance functions here
def flip_coin(bet, selection, money):
    bet_amount = bet
    money = money
    selection = selection.lower()

    if selection == 'heads' or selection == 'tails': # Check the user made a valid selection
        if bet_amount > money: # Check the user has enough money to bet
            return 'You do not have enough money for that bet. Please bet %s or less' % (money), money
        else:
            if selection == 'heads': # Assign a value to selection
                selection_value = 1
            elif selection == 'tails':
                selection_value = 0

            flip_result = random.randint(0,1) # Toss that freakin' coin already!

            if flip_result == selection_value: # Winners take all
                money += bet_amount
                return 'You won! You are $%s richer, and have a total of $%s' % (bet_amount, money), money
            else: # Losing sucks!
                bet_amount = -bet_amount
                money += bet_amount
                return 'You lost! You are $%s poorer, and have a total of $%s' % (abs(bet_amount), money), money
    else:
        return 'Hmm.. It seems you\'ve selected an invalid option. Please choose \'heads\' or \'tails\'.', money # C'mon! It's a coin, it's not *that* hard, is it?

# Play Coin Toss
message, money = flip_coin(30, 'tails', money)
print(' -- Flip Coin -- ')
print(message)
print(' --------------- ')

def cho_han(bet, prediction, money):
    bet_amount = bet
    money = money
    prediction = prediction.lower()

    if prediction == 'even' or prediction == 'odd': # Check the user entered a valid prediction
        if bet_amount > money: # Check the user has enough money for the bet
            return 'You do not have enough money for that bet. Please bet %s or less' % (money), money
        else:
            roll_result = random.randint(1,6) + random.randint(1,6) # Yeah! Proud Mary keep on rollin'
            if roll_result % 2:
                result = 'even'
            else:
                result = 'odd'

            if prediction == result: # Ooooh yeah! Winning feels good!
                money += bet_amount
                return 'You won! You are $%s richer, and have a total of $%s' % (bet_amount, money), money
            else: # Whatevs, it's not like I even *wanted* to play -- no, I am *not* a sore loser
                bet_amount = -bet_amount
                money += bet_amount
                return 'You lost! You are $%s poorer, and have a total of $%s' % (abs(bet_amount), money), money
    else:
        return 'Woah, hang on.. That\'s not a valid guess. Wanna try again? Please make sure you choose either \'even\' or \'odd\' this time.', money # Fat fingers tend to type anything *but* what's actually expected

# Play Cho-Han
message, money = cho_han(45, 'odd', money)
print(' -- Cho Han -- ')
print(message)
print(' ------------- ')

def pick_card(bet_1, player_1, player_1_money, bet_2, player_2, player_2_money):
    bet_amount_1 = bet_1
    bet_amount_2 = bet_2
    money_1 = player_1_money
    money_2 = player_2_money

    if bet_amount_1 > money_1 and bet_amount_2 > money_2:
        return 'Neither of you have enough money for this bet. Please lower your bets and try again.', money_1, money_2
    elif bet_amount_1 > money_1:
        return '%s doesn\'t have enough money for this bet. Please bet %s or lower.' % (player_1.title(), money_1), money_1, money_2
    elif bet_amount_2 > money_2:
        return '%s doesn\'t have enough money for this bet. Please bet %s or lower.' % (player_2.title(), money_2), money_1, money_2
    else:
        player_1_card = random.randint(1, 13)
        player_2_card = random.randint(1, 13)

        if player_1_card == player_2_card:
            return 'It\'s a tie! %s has a total of $%s, %s has a total of $%s' % (player_1.title(), money_1, player_2.title(), money_2), money_1, money_2
        elif player_1_card > player_2_card:
            bet_amount_2 = -bet_amount_2
            money_1 += abs(bet_amount_2)
            money_2 += bet_amount_2
            return '%s wins $%s and has a total of $%s. %s loses $%s and is left with a total of $%s' % (player_1.title(), abs(bet_amount_2), money_1, player_2.title(), abs(bet_amount_2), money_2), money_1, money_2
        else:
            bet_amount_1 = -bet_amount_1
            money_1 += bet_amount_1
            money_2 += abs(bet_amount_1)
            return '%s wins $%s and has a total of $%s. %s loses $%s and is left with a total of $%s' % (player_2.title(), abs(bet_amount_1), money_2, player_1.title(), abs(bet_amount_1), money_1), money_1, money_2

player_1_money = 100
player_2_money = 100
message, player_1_money, player_2_money = pick_card(10, 'jack', player_1_money, 13, 'jill', player_2_money)
print(' -- Pick Cards -- ')
print(message)
print(' ---------------- ')

def roulette(bet_amount, bet, money):
    bet_amount = bet_amount
    red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    low_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    high_numbers = [19, 20, 21, 22, 23, 24, 25 , 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    payout = {
                'straight': 35,
                'split': 17,
                'street': 11,
                'corner': 8,
                'basket': 6,
                'six': 5,
                'column': 2,
                'dozen': 2,
                'even': 1,
                'odd': 1,
                'red': 1,
                'black': 1,
                'high': 1,
                'low': 1
                }



    if bet_amount > money: # Check the user has enough money for the bet
        return 'You do not have enough money for that bet. Please bet %s or less' % (money), money
    else:
        result = random.randint(-1, 36)
        if result == -1:
            result = 00
        return 'moving on..'


    # red numbers list

    # black numbers list

    # is odd or even || black or red
    # LOWERCASE - check it is a valid string


    odd_or_even_guess = 'odd or even'

    odd_or_even_value = 1


    if type(guess) == type(odd_or_even_guess):
        if guess == 'even':
            return 1
