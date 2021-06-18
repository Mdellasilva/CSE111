import math

print('This program is an implementation of the Rosenberg Self-Esteem Scale.')
print('This program will show you ten statements that you could possibly')
print('apply to yourself. Please rate how much you agree with each of the')
print('statements by responding with one of these four letters:')

print()

print('D means you strongly disagree with the statement.')
print('d means you disagree with the statement.')
print('a means you agree with the statement.')
print('A means you strongly agree with the statement.')

print()



def main():
    score = 0
    print(f'1. I feel that I am a person of worth, at least on an equal plane with others.')
    score += positive(answer())
    print(f'2. I feel that I have a number of good qualities.')
    score += positive(answer())
    print(f'3. All in all, I am inclined to feel that I am a failure.')
    score += negative(answer())
    print(f'4. I am able to do things as well as most other people.')
    score += positive(answer())
    print(f'5. I feel I do not have much to be proud of.')
    score += negative(answer())
    print(f'6. I take a positive attitude toward myself.')
    score += positive(answer())
    print(f'7. On the whole, I am satisfied with myself.')
    score += positive(answer())
    print(f'8. I wish I could have more respect for myself.')
    score += negative(answer())
    print(f'9. I certainly feel useless at times.')
    score += negative(answer())
    print(f'10. At times I think I am no good at all.')
    score += negative(answer())

    print()

    print(f'Your score is {score}.')

    print(f'A score below 15 may indicate problematic low self-esteem.')

def answer():
    letter = input('Enter D, d, a, or A: ')
    return letter

def positive(letter):
    if letter == 'D':
        score = 0
    elif letter == 'd':
        score = 1
    elif letter == 'a':
        score = 2
    elif letter == 'A':
        score = 3
    return score

def negative(letter):
    if letter == 'D':
        score = 3
    elif letter == 'd':
        score = 2
    elif letter == 'a':
        score = 1
    elif letter == 'A':
        score = 0
    return score

main()