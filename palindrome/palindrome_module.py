def palindrome(str_in):
    str_list = list(str_in.lower())
    new_str_list = []
    for i in range(len(str_list)):
        if str_list[i].isalpha() == True:
            new_str_list.append(str_list[i])
    rev_str_list = list(reversed(new_str_list))
    for i in range(len(new_str_list)):
        if new_str_list[i] == rev_str_list[i]:
            continue
        else:
            return False
    return True


def main():
    str_input = input("Please enter a Palindrome:\n")
    palindrome(str_input)
    return
    


if __name__ == '__main__':
    main()
