def greet_user():
    print("Hello!")

greet_user()

def greet_user1(username):
    print(username+"hello")

greet_user1("zhushengquan")


def print_person(name, age):
    print("my name is " + name + ", I'm " + str(age) + " years old")

#位置实参
print_person("zsq", 14)
#关键字实参
print_person(age=25, name='zengxiaohan')

def describe_pet(name, type = 'dog'):
    print(name + " " + type)
describe_pet('fuck')
describe_pet("fuck", 'cat')

def print_models(unprint_designs, completed_models):
    while unprint_designs:
        current_design = unprint_designs.pop().upper()
        completed_models.append(current_design)
unprint_designs = ['a', 'b', 'c', 'd']
completed_models = []
print_models(unprint_designs[:], completed_models)

print(unprint_designs, completed_models)

def make_pizza(*toppings):
    print(toppings)

make_pizza("person1")
make_pizza("person1", "person2", "person3")

def make_pizza1(*toppings):
    for toppings in toppings:
        print('-' +toppings)
make_pizza1('a', 'b', 'c')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('z', 'sq', hobby='game', age=22, dream='money')
print(user_profile)

