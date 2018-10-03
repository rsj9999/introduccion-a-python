def split_into_words(lyrics):
    """
    Split a string into lowercase words, removing all punctuation characters,
    returning the result.
    """
    result = []
    for word in lyrics.lower().split():  # lower() convierte las palabras en minusculas
        word = word.strip(',.;()"¡!')  # strip() elimina del incio y del final los caracteres que le pasemos
        result.append(word)
    return result