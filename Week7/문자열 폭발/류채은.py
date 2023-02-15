import re
import copy
entire_string = input()
bomb = input()


while True:
    prev_entire_string = copy.deepcopy(entire_string)
    entire_string = re.sub(bomb,'',prev_entire_string)

    if entire_string == '':
        print('FRULA')
        break
    elif len(entire_string) == len(prev_entire_string):
        print(entire_string)
        break
