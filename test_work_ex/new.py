def handle_object(obj, key, action):
    if action == "get":
        return obj[key]
    elif action == "add":
        obj.append("")
        return obj
    elif action == "delete":
        del obj[key]
        return obj
    else:
        return obj

#print(handle_object([1, 2, 3], 2, "delete"))

def get_sum_of_numbers(number, type="odd"):
    if type == "odd":
        a = [i for i in range(1, number+1, 2)]
        return sum(a)
    elif type == "even":
        a = [i for i in range(0, number+1, 2)]
        return sum(a)
    else:
        a = [i for i in range(0, number+1)]
        return sum(a)


print(get_sum_of_numbers(10))
