#!/usr/bin/python3
# main program
if __name__ == "__main__":
    '''
    from module.unitest_function import add, sub, mul, div, mod


    print(add(1, 1))
    print(sub(2, 3))
    print(mul(2, 3))
    print(div(3, 4))
    print(mod(4, 6))
    '''
    from module.de_se_json import Peers
    import json


    person1 = Peers("Kwabena", "Sapong", "Ghana")
    person1.intro()
    print()
    print(person1.__dict__)
    print(type(person1.__dict__))
    print()
    print(person1.to_json_string())
    print(type(person1.to_json_string()))
    print()
    print(person1)
    print()
    #print(person1.load_json_from_file("my_file.json"))
    #json_format = person1.to_json_string()
    person1.save_json_to_file("Mutio.json")
