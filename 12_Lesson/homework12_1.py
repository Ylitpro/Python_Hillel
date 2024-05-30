import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
    """
    Reads text from the html_file, cleans it from HTML tags, and writes the cleansed text to the result_file.
    :param html_file: The name of the input file to be cleared
    :param result_file: The name of the output file to write the cleansed text.
    :return: The file with cleansed text from HTML tags.
    """
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        cleaned_text = []
        tag_found = False
        for char in html:
            if char == '<':
                tag_found = True
            elif char == '>':
                tag_found = False
            elif not tag_found:
                cleaned_text.append(char)

        cleaned_text = ''.join(cleaned_text)
        with open(result_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)


delete_html_tags('draft.html')
