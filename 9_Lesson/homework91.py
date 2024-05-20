def popular_words(text: str, words: list) -> dict:
    my_dict = {}
    text_list = text.lower().split()
    for key in words:
        if key in text_list:
            my_dict[key] = text_list.count(key)
        else:
            my_dict[key] = 0
    return my_dict


assert popular_words('When I was One I had just begun When I was Two I was nearly new ',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
