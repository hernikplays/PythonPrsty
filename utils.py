def load_text(path): # načte soubor s textem
    file = ""
    try:
        file = open(path)
    except:
        return ""
    current_text = file.readlines()
    text = []
    for l in current_text:
        text.append(l.replace('\n', '⤶'))
    
    file.close()
    return text