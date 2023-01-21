
title = 'Senior Software Engineer, Trilogy (Remote) - $200,000/year USD'
words_ignore = ['middle', 'mid', 'senior', 'data', 'vision',
                'machine', 'full', 'mentor', 'commod', 'fullstack',
                'cybersecurity', 'applied', 'solutions', 'lead']

w2 = 'middle mid senior'
flag = True
for item in words_ignore:
    if item in title.lower():
        flag = False

if flag:
    print('write')
else:
    print('do not write')

