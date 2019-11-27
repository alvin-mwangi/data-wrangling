import pprint

pdf_txt = '../../data/chp5/en-final-table9.txt'
openfile = open(pdf_txt, 'r')


def clean(line):
    """
        Cleans line breaks, spaces, and special characters from our line.
    """
    line = line.strip('\n').strip()
    line = line.replace('\xe2\x80\x93', '-')
    line = line.replace('\xe2\x80\x99', '\'')

    return line


def turn_on_off(line, status, start, end='\n'):
    """
        This function checks to see if a line starts/ends with a certain
        value. If the line starts/ends with that value, the status is
        set to on/off (True/False).
    """

    if line.startswith(start):
        status = True
    elif status:
        if line == end:
            status = False

    return status


countries = []
totals = []
country_line = total_line = False

for line in openfile:

    # if country_line or total_line:
    #     print '%r' % line
    if country_line:
        countries.append(clean(line))
    elif total_line:
        totals.append(clean(line))

    country_line = turn_on_off(line, country_line, 'and areas')
    total_line = turn_on_off(line, total_line, 'total')

test_data = dict(zip(countries, totals))
pprint.pprint(test_data)
