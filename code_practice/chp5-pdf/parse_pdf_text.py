import pprint

pdf_txt = '../../data/chp5/en-final-table9.txt'
openfile = open(pdf_txt, 'r')

double_lined_countries = [
    'Bolivia (Plurinational \n',
    'Democratic People\xe2\x80\x99s \n',
    'Democratic Republic \n',
    'Micronesia (Federated \n',
    'Saint Vincent and \n',
    'The former Yugoslav \n',
    'United Republic \n',
    'Venezuela (Bolivarian \n',
]
previous_line = ''

def clean(line):
    """
        Cleans line breaks, spaces, and special characters from our line.
    """
    line = line.strip('\n').strip()
    line = line.replace('\xe2\x80\x93', '-')
    line = line.replace('\xe2\x80\x99', '\'')

    return line


def turn_on_off(line, status, start, prev_line, end='\n'):
    """
        This function checks to see if a line starts/ends with a certain
        value. If the line starts/ends with that value, the status is
        set to on/off (True/False).
    """

    if line.startswith(start):
        print line + ' starts with ' + start
        status = True
        print 'Setting FLAG to TRUE'
    elif status:
        if line == end and prev_line != 'and areas':
            print 'Turning off FLAG'
            status = False

    return status


countries = []
totals = []
country_line = total_line = False

for line in openfile:

    # if country_line or total_line:
    #     print '%r' % line
    if country_line:
        print 'country_line is TRUE'
        print '%r' % line
        if previous_line in double_lined_countries:
            line = ' '.join([clean(previous_line), clean(line)])
            countries.append(line)
        elif line not in double_lined_countries:
            countries.append(clean(line))

    elif total_line:
        if len(line.replace('\n', '').strip()) > 0:
            totals.append(clean(line))

    country_line = turn_on_off(line, country_line, 'and areas', previous_line)
    total_line = turn_on_off(line, total_line, 'total', previous_line)

    # previous_line = clean(line)
    previous_line = line


test_data = dict(zip(countries, totals))
pprint.pprint(test_data)

# pprint.pprint('\nCountries:\n')
# pprint.pprint(countries)
