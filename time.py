import random
import time

questions_answers = []
questions_answers.append(['The epoch is the point where the time starts, \
and is platform independent.', 'F'])
questions_answers.append(['For Unix, the epoch is January 1, 1970, 00:00:00 (UTC).'
                          , 'T'])
questions_answers.append(['The term seconds since the epoch refers to the \
total number of elapsed seconds since the epoch', 'T'])
questions_answers.append(['Function strptime() can parse \
4-digit years when given %y format code.', 'F'])
questions_answers.append(['UTC is Coordinated Universal Time.', 'T'])
questions_answers.append(['DST is Daylight Saving Time, an adjustment \
of the timezone by (usually) two hours during part of the year.', 'F'])
questions_answers.append(['The time value as returned by gmtime(), \
localtime(), and strptime(), and accepted by asctime(), mktime() and \
strftime(), is a sequence of 9 integers.', 'T'])

random.shuffle(questions_answers)

user_score = 0

start_time = time.perf_counter()

for item in questions_answers:
    print('True or false: ' + item[0])
    answer = input('Please enter T if it is true and F if it is false: ')
    if answer == item[1]:
        print('Excellent!')
        user_score += 1
    else:
        print('Not correct:( Maybe you will be lucky next time!')

end_time = time.perf_counter()

print('Congratulations! Your total score is: ' + str(user_score) + ', total time is '
      + str(end_time - start_time) + ' seconds.')






