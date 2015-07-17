from flask import Flask, request

app = Flask(__name__)

def compare(a, b):
  if a == b:
    return '='
  elif a < b:
    return '<'
  else:
    return '>'

def solve_puzzle():
  # You can't beat constant time!
  # return ' ABCD\nA=>>>\nB<=<<\nC<>=>\nD<><='
  # But for the sake of problem solving...
  
  # Start with an ordered list for the source of relative values
  letters_by_value = ['B', 'D', 'C', 'A']
  letters_by_order = sorted(letters_by_value)
  solution = ' ' + ''.join(letters_by_order) + '\n'
  #iterate over them in the order they appear in the matrix
  for a in letters_by_order:
    solution += a
    # Compare this letter's value position to the position of each other letter
    solution += ''.join(compare(letters_by_value.index(a), letters_by_value.index(b)) for b in letters_by_order)
    solution += '\n'
  return solution

responses = {
  'Ping': 'OK',
  'Phone': '',
  'Email Address': '',
  'Position': '',
  'Referrer': '',
  'Years': '',
  'Name': '',
  'Puzzle': solve_puzzle(),
  'Resume': '',
  'Source': '',
  'Status': '',
  'Degree': ''
}

@app.route('/')
def respond():
  if 'q' in request.args and request.args.get('q') in responses:
    return responses[q]
  else:
    print request
    return "Nothing to see here."
  
app.run(host='0.0.0.0')
