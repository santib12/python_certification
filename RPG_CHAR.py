# FreeCodeCamp Lab, creating a small app that creates a character for an RPG adventure
# Objective: FUfill the user stories below and get all the test to pass to complete lab

full_dot = '●'
empty_dot = '○'

def create_character(char_name, strength, intelligence, charisma):

    if isinstance(char_name, str) != True:
        return 'The character name should be a string'
    if char_name == '':
        return 'The character should have a name'
    if len(char_name) > 10:
        return 'The character name is too long'
    if " " in char_name:
        return 'The character name should not contain spaces'
    if isinstance(strength, int) != True or isinstance(intelligence, int) != True or isinstance(charisma,int) != True:
        return 'All stats should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    str_bar = full_dot * strength + empty_dot * (10 - strength)
    int_bar = full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_bar = full_dot * charisma + empty_dot * (10 - charisma)

    character = f'{char_name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}'

    return character


if __name__ == "__main__":

    char = create_character("Santiago", 1, 4, 2)
    print(char)