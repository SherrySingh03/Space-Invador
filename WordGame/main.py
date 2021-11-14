guess_count = 0
no_lives = 3
def rightanswer():
    global guess_count
    guess_count += 1
    print('Congrats! Your answer is correct')
    if guess_count == 6:
        print('You nailed it, congratulations! Thank you for playing the game!')
        l = input('Press any key to exit...')
        quit()
def wronganswer():
    global no_lives
    global guess_count
    guess_count += 1
    no_lives -= 1
    print('Nope, wrong answer. *sad flute plays*')
    print('Lives remaining:' + 'X'*no_lives + '\n')
    if no_lives == 0:
        print("Looks like you don't have what it takes. Now go away, practice and come back when you're ready.")
        k = input('Press any key to exit...')
        quit()
    elif guess_count == 6:
        print('You nailed it, congratulations! Thank you for playing the game!')
        l = input('Press any key to exit...')
        quit()
def answer(answer_right):
    print(f"The correct answer is : \n\n**drumroll**\n{answer_right}\n\n**drumroll**\n\n")
def sentence1():
    print('Three eyes have I, all in a row; when the red one opens, all freeze. Who am I?')
    answer1 = input('Answer: ')
    if answer1.lower() == 'traffic light':
        rightanswer()
    else:
        wronganswer()
        answer("  Traffic Light  ")
def sentence2():
    print('What gets wetter and wetter the more it dries?')
    answer2 = input('Answer: ')
    if answer2.lower() == 'towel':
        rightanswer()
    else:
        wronganswer()
        answer("  Towel  ")
def sentence3():
    print('I have a tail, and I have a head, but i have no body. I am NOT a snake. What am I?')
    answer3 = input('Answer: ')
    if answer3.lower() == 'coin':
        rightanswer()
    else:
        wronganswer()
        answer("  Coin  ")


def sentence4():
    print('What is so fragile that when you say its name you break it?')
    answer4 = input('Answer: ')
    if answer4.lower() == 'silence':
        rightanswer()
    else:
        wronganswer()
        answer("  Silence  ")


def sentence5():
    print('The more of this there is, the less you see. What is it?')
    answer5 = input('Answer: ')
    if answer5.lower() == 'darkness':
        rightanswer()
    else:
        wronganswer()
        answer("  Darkness  ")


def sentence6():
    print('I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?')
    answer6 = input('Answer: ')
    if answer6.lower() == 'shadow':
        rightanswer()
    else:
        wronganswer()
        answer("  Shadow  ")


print("\n Welcome to the Word Game. In this game, you'll be asked to guess words using the hints provided. You'll get "
      "5 questions")
print("and in order to win, you have to get all of them right. Moreover, you'll get 3 lives(XXX) and for each wrong "
      "answer")
print(" one X will be lost and you'll lose the game on losing all three of these ❤")

lines = [sentence5(), sentence4(), sentence3(), sentence2(), sentence1(), sentence6()]
