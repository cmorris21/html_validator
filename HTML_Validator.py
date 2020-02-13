#!/bin/python3
import pandas as pd

def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    
    l = []
    balanced = True
    for i in range(len(html)):
        symbol = html[i]
        if symbol i "<":
            l.append(symbol)
        else:
            if l == []:
                balanced = False
            else:
                top =l.pop()
                if not _extract_tags(html):
                    balanced = False
        i += 1
    if balanced and l == []:
        return True
    else:
        retun False
        
        
        
    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    l = []
    for i in range(len(html)):
        if html[i] == "<":
            x = i
            tag = ""
            tag += "<"
            while html[x] != ">":
                tag += html[i]
                i += 1
            tag += ">"
         l.append(tag)
     return l
