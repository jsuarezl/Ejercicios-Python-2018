def levadura(file):
    s = ''
    for line in open(file):
        s += line
    print('Bases nitrogenadas:',
          {'c': str(s).count('c'), 't': str(s).count('t'), 'a': str(s).count('a'), 'g': str(s).count('g')})
