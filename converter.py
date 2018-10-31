import re
currentState = ''

with open('input', 'r') as input, open('output', 'w') as output:
    for line in input:
        lineArr = re.split(':\s*|\s*->\s*', line)
        if currentState == lineArr[0]:
            output.write(',\n    "' + lineArr[1] + '": "' + lineArr[2][:-1] + '"')
        else:
            if currentState == '':
                output.write(lineArr[0].lower() + 'Events = {\n    "' + lineArr[1] + '": "' + lineArr[2][:-1] + '"')
            else:
                output.write('}\n' + lineArr[0].lower() + 'Events = {\n    "' + lineArr[1] + '": "' + lineArr[2][:-1] + '"')
            currentState = lineArr[0]
    output.write('}')
