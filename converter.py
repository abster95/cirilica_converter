import typing
import argparse
import os

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
lookup['џ'.capitalize()] = 'Dž'
lookup['Nj'] = 'њ'.capitalize()
lookup['Lj'] = 'љ'.capitalize()
lookup['Dž'] = 'џ'.capitalize()


def cirilica_to_latinica(text: str):
    translated = ''
    relevant = cirilica + [c.capitalize() for c in cirilica]
    for char in text:
        if char in lookup and char in relevant:
            translated += lookup[char]
        else:
            translated += char
    return translated


def latinica_to_cirilica(text: str):
    problematic = ['л', 'н', 'Л', 'Н', 'д', 'Д']
    translated = ''
    relevant = latinica + [l.capitalize() for l in latinica]
    for char in text:
        if char == 'j' or char == 'ž':
            if translated[-1:] in problematic:
                translated = translated[:-1] + \
                    lookup[cirilica_to_latinica(translated[-1:])+char]
                continue
        if char in lookup and char in relevant:
            translated += lookup[char]
        else:
            translated += char
    return translated


def resolve_text(text):
    if os.path.exists(text):
        with open(text, 'r', encoding='utf8') as fp:
            text = fp.read()
    return text

def get_out_path(text, translation):
    output = translation + ".txt"
    if os.path.exists(text):
        output =  os.path.splitext(text)[0] + "_" + output
    return output

def translate(text, output, func):
    translated = func(text)
    print(translated)
    with open(output, 'w', encoding='utf8') as fp:
        fp.write(translated)
    return translated

def translate_cirilica(args):
    text = args.text
    output = args.output
    if not output:
        output = get_out_path(text, "latinica")
    text = resolve_text(text)
    return translate(text,output, cirilica_to_latinica)

def translate_latinica(args):
    text = args.text
    output = args.output
    if not output:
        output = get_out_path(text, "cirilica")
    text = resolve_text(text)
    return translate(text,output, latinica_to_cirilica)



def add_cirilica_to_latinica_subparser(subparsers):
    parser = subparsers.add_parser("cirilica2latinica")
    parser.add_argument("text", type=str, help="Text or file containing text in cyrillic")
    parser.add_argument("--output", type=str, required=False, default='', help="Output file for text in latin")
    parser.set_defaults(function=translate_cirilica)

def add_latinica_to_cirilica_subparser(subparsers):
    parser = subparsers.add_parser("latinica2cirilica")
    parser.add_argument("text", type=str, help="Text or file containing text in latin")
    parser.add_argument("--output", type=str, required=False, default='', help="Output file for text in cyrillic")
    parser.set_defaults(function=translate_latinica)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converts strings or documents from Cyrillic to Latin and vice versa")
    subparsers = parser.add_subparsers()
    add_cirilica_to_latinica_subparser(subparsers)
    add_latinica_to_cirilica_subparser(subparsers)
    args = parser.parse_args()
    args.function(args)