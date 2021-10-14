def persents (x, y):
    """What percentage of x is y"""
    one_percent = x / 100
    result = y / one_percent
    print(str (y) + " is " + str(result) + "percents of" + str(x))

persents(200,50)