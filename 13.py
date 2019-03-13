def find_secret_message(paragraph):
    li = paragraph.lower().split(" ")
    li = [i.strip('.,:!?') for i in li]
    result = []
    for index, value in enumerate(li):
        li_before = li[:index]
        if value in li_before and value not in result:
            result.append(value)
    return " ".join(result)


paragraph = 'This is a test. this test is fun.,:!?.'
print(find_secret_message(paragraph))
