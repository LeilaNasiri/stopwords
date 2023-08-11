def prep_remove_stopwords(text, stopword_filename='stop.txt'):
    import io
    stoplist = []
    try:
        with io.open(stopword_filename, encoding='utf-8') as stop_file:
            for line in stop_file:
                stoplist.append(line.replace('\n', ''))
    except:
        raise Exception("Stop List reading error.")

    new_text = ""
    words = text.split('')
    for word in words:
        # print('word: %s' % word)

        if word not in stoplist:
             new_text = new_text + " " + word
    print('Preprocess: Remove Stop Words (done)')
    return new_text
