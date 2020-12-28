from input_output import get_input_data, write_data


file_name = 'in/hamsters.in1'

data = get_input_data(file_name)
daily_food = data['s']
total_hamsters = data['c']
hamsters = data['hamsters']

bought_hamsters = 0
available_food = daily_food

previous_greedsiess = 0
checked = 0
while available_food > 0 and checked < total_hamsters:

    current_hamster = hamsters.get_min_value()
    checked += 1

    if bought_hamsters > 0:
        if available_food >= (current_hamster.daily_food + current_hamster.greediness):
            bought_hamsters += 1
            available_food -= (current_hamster.daily_food + current_hamster.greediness)
            hamsters.remove_min_element()
        if checked == 2:
            available_food -= previous_greedsiess
        else:
            break
    else:
        if current_hamster.daily_food <= available_food:
            bought_hamsters += 1
            available_food -= current_hamster.daily_food
            previous_greedsiess = current_hamster.greediness
            hamsters.remove_min_element()

print(bought_hamsters)
write_data(file_name, bought_hamsters)