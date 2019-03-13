def find_secret_message(paragraph):
    li1 = paragraph.lower().replace(".", "").split(" ")
    li2 = list(set(li1))
    print(li1)
    print(li2)
    for i in li2:
        li1.remove(i)
    return " ".join(li1)


paragraph = 'This is a test. this test is fun.'
print(find_secret_message(paragraph))
