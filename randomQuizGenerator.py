#! Python3
# randomQuizGenerator.py - generate quiz tickets with random questions and answers.

import random

# Ticket data. Keys - state name, values - capitals.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau',
            'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
            'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Luisiana': 'Baton Rouge', 'Maine': 'Augusta',
            'Mariland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln',
            'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismark', 'Ohio': 'Columbus',
            'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austine', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olimpia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generation 35 exam tickets.
for quizNum in range(35):

    # Create exam tickets and respond keys
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write exam ticket header
    quizFile.write('Name:\n\nDate:\n\n')
    quizFile.write((' ' * 15) +
                   'Checking knowledge of USA states capitals (Ticket %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Randomizing states capitals
    states = list(capitals.keys())
    random.shuffle(states)

    # Create loop for all 50 states and create question for each of them
    for questionNum in range(50):

        # Taking Correct and incorrect questions
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write questions in a file
        quizFile.write('%s. Choose state capital %s.\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write answer key in a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
