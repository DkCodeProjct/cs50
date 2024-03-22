
from codez import removeVovle

def main():
    testVovelLower()
    testVovelUpper()

def testVovelLower():
    assert removeVovle('abblio') == 'bbl'
    assert removeVovle('twitter') == 'twttr'
    assert removeVovle('google') == 'ggl'

def testVovelUpper():
    assert removeVovle('GOOGLE') == 'GGL'
    assert removeVovle('TWITTER') == 'TWTTR'




