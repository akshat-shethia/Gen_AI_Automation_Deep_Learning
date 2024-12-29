import re

f = open(r"Section 6\Bookshelf\bookshelf.txt", "r")
string = f.read()
print(string)

# To find the names of all the books
result = re.findall(r".*;(.{1,25});.*", string)
print(result)
# ['Filling the Gap', 'Harpo Speaks', 'My Autobiography', 'Where Have I Been?', 'Fatherhood', "That's NOT All, Folks", "It's Always Something", 'Pryor Convictions', 'Bootleg', 'Moab Is My Washpot', 'Jen-X: My Open Book', 'Rock This', 'Random Acts of Badness', 'Cancer Schmancer', 'Hollywood Causes Cancer', 'Born Standing Up', 'Why We Suck', 'Ernie: The Autobiography', 'My Shit Life So Far', 'American on Purpose', 'Killing Willis', 'Dyn-o-mite!', 'The Filthy Truth', 'So, Anyway...']

# To find all the authors who published books in the year 2000 and above
result = re.findall(r"(.{1,25});.+;2[0-9]{3}", string)
print(result)
# ['Danny Bonaduce', 'Fran Drescher', 'Alan Thicke', 'Rodney Dangerfield', 'Tom Green', 'Rik Mayall', 'Tommy Chong', 'Alan Thicke', 'Steve Martin', 'Denis Leary', 'Stephen Fry', 'Frankie Boyle', 'Craig Ferguson', 'Todd Bridges', 'Kevin Smith', 'Jimmie Walker', 'Andrew Dice Clay', 'John Cleese', 'Cheech Marin', 'Eric Idle']
