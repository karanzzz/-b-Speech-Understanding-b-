
def list_to_dict(input_list):
    def list_to_dict(input_list):
    result_dict = {}  
    if input_list: 
        for index, value in enumerate(input_list):
            result_dict[index] = value
    return result_dict
print(list_to_dict([1, 3.14, "hello", True]))
print(list_to_dict(["a", "a", "a"]))
print(list_to_dict([]))



