def count_numbers_and_strings(data_structure):
    total_sum = 0

    if isinstance(data_structure, str):                                         # если структура данных - строка
        return len(data_structure)
    elif isinstance(data_structure, int) or isinstance(data_structure, float):  # если структура данных - число
        return data_structure
    elif isinstance(data_structure, list) or isinstance(data_structure, tuple): # если структура данных - список или кортеж
        for item in data_structure:
            total_sum += count_numbers_and_strings(item)
    elif isinstance(data_structure, dict):                                      # если структура данных - словарь
        for key, value in data_structure.items():
            if isinstance(key, str):
                total_sum += len(key)
            else:
                total_sum += count_numbers_and_strings(list(key))
            if isinstance(value, str):
                total_sum += len(value)
            elif isinstance(value, int) or isinstance(value, float):
                total_sum += value
            else:
                total_sum += count_numbers_and_strings(list(value))
    elif isinstance(data_structure, set):                                       # если структура данных - множество
        total_sum += count_numbers_and_strings(list(data_structure))

    return total_sum

data_structure = [
     [1, 2, 3],
     {'a': 4, 'b': 5},
     (6, {'cube': 7, 'drum': 8}),
     "Hello",
     (((), [{(2, 'Urban', ('Urban2', 35))}]))
]

result = count_numbers_and_strings(data_structure)
print(result)