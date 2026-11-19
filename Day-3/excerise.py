def count_vowels(str1):
    count=0
    vowels=['a','e','i','o','u']
    for i in str1:
        if i in vowels:
            count+=1

    return count


def is_odd(num1):
    return True if num1%2 else False


def largest_num(list1):
    if len(list1)<=0:
        raise ValueError("Dont provide an empty List")
    max_num=-999
    for i in list1:
        if max_num<i:
            max_num=i

    return max_num


def remove_duplicates(list1):
    unique_list=[]
    for i in list1:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

def word_frequency(text):
    str1=text.lower()
    str_list=[i for i in str1]
    unique_list=list(set(str_list))
    result_dict={}
    for i in unique_list:
        result_dict[i]=str_list.count(i)

    return result_dict



print(count_vowels("Python Developer"))
print(is_odd(2))
print(largest_num([1,3,6,18]))
print(remove_duplicates(['Git','Java','Java','C#','Git','Ruby']))
print(word_frequency("Python is rich librabry lanunage and useful for machine learning"))
