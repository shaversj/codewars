def rot13(message):
    import string
    result = ""
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase

    for letter in message:
        if letter.isupper() and letter.isalpha():
            print(letter)
            current_letter_idx = alpha_upper.index(letter)
            new_letter_idx = 0
            if current_letter_idx + 13 > 24:
                new_letter_idx = current_letter_idx - 13
            else:
                new_letter_idx = current_letter_idx + 13

            new_letter = alpha_upper[new_letter_idx]
            result += new_letter
        elif letter.lower() and letter.isalpha():
            print(letter)
            current_letter_idx = alpha_lower.index(letter)
            new_letter_idx = 0
            if current_letter_idx + 13 > 24:
                new_letter_idx = current_letter_idx - 13
            else:
                new_letter_idx = current_letter_idx + 13

            new_letter = alpha_lower[new_letter_idx]
            result += new_letter
        else:
            result += letter

    return result


print(rot13("EBG13 rknzcyr."))
