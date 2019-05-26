import typing
cirilica = ['а', 'б', 'в', 'г', 'д', 'ђ', 'е', 'ж', 'з', 'и', 'ј', 'к', 'л', 'љ',
            'м', 'н', 'њ', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ћ', 'џ', 'ш']

latinica = ['a', 'b', 'v', 'g', 'd', 'đ', 'e', 'ž', 'z', 'i', 'j', 'k', 'l', 'lj',
            'm', 'n', 'nj', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c', 'č', 'ć', 'dž', 'š']

assert len(cirilica) == len(latinica)
assert len(cirilica) == 30

lookup = {}

for c, l in zip(cirilica, latinica):
    lookup[c] = l
    lookup[l] = c
    lookup[c.capitalize()] = l.capitalize()
    lookup[l.capitalize()] = c.capitalize()

lookup['њ'.capitalize()] = 'Nj'
lookup['љ'.capitalize()] = 'Lj'
lookup['Nj'] = 'њ'.capitalize()
lookup['Lj'] = 'љ'.capitalize()

def cirilica_to_latinica(text: str):
    translated = ''
    for char in text:
        if char in lookup:
            translated += lookup[char]
        else:
            translated += char
    return translated

def latinica_to_cirilica(text: str):
    problematic = ['л', 'н', 'Л', 'Н']
    translated = ''
    for char in text:
        if char == 'j':
            if translated[-1:] in problematic:
                translated = translated[:-1] + lookup[cirilica_to_latinica(translated[-1:])+char]
                continue
        if char in lookup:
            translated += lookup[char]
        else:
            translated += char
    return translated

text = "Čovek piše tekst na latinici. Ljubi majka sina svoga, njeno ljalje Njegoš!!"
print(text)
print(latinica_to_cirilica(text))

