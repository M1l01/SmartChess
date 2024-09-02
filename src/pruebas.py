class InvalidName(Exception):
    pass

name = "Emilio"

try:
    if name == "Emilio":
        raise InvalidName
    else:
        print(f"Tu nombre es {name}")
except InvalidName:
    print("Exception ocurred: Invalid Name")