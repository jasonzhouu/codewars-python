def find_secret_message(paragraph):
    li = paragraph.lower().replace(".", "").split(" ")
    result = []
    for index, value in enumerate(li):
        li_before = li[:index]
        if value in li_before:
            if value not in result:
                result.append(value)
    return " ".join(result)


paragraph = 'This is a test. this test is fun.'
print(find_secret_message(paragraph))
