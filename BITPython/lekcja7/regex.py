# regex to game filter

example = '''
DEFENSE
AC 17
AC 16, touch 13, flat-footed 13 (+3 armor, +3 Dex)
hp 10 (1d8+2)
Fort -2, Ref +5, Will 0
'''
import re

def parse_defense(string):
    match = re.search('AC (\d+), touch (\d+), flat-footed (\d+), \([+-]?\d\)', string) # .search, pierwszy znaleziony \d matchuje cyfry
    stats = {'AC': int(match.group(1)),
            'touch': int(match.group(2)),
            'flat-footed': int(match.group(3)),
            'armor': int(match.group(4))
            }
    return stats

if __name__ == '__main__':
    print(parse_defense(example))


# regex to e-mail

    p = [a-zA-Z0-9]
    q = [\-\_\.]
    
    ^q*p+q*p*\@(pq){2,}\.p{2,}