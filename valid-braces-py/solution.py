def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    queue = []

    for char in string:
        if char in braces:
            queue.insert(0, char)
        else:
            if queue:
                if char != braces.get(queue.pop(0)):
                    return False
            else:
                return False

    if len(queue) > 0:
        return False

    return True


print(validBraces("(((({{"))