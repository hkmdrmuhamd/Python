dictionary = {"a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","m":"M","n":"N","o":"O","p":"P","r":"R","s":"S","t":"T","u":"U","v":"V","y":"Y","z":"Z"}


List = list()
entry = input("Please enter your name and last name with a space between your first and last name ->")

for i in entry:
    List += [i]

check = ""

a = List.index(" ")
b = List[a+1]

for i in List:
    if List[0] == i:
        check += dictionary[i]
    elif i == " ":
        check += " "
        check += dictionary[b]
    elif i != b:
        check += i

print(check)