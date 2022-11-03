from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np

def main():
    driver = webdriver.Firefox()
    driver.get('https://nukadeti.ru/skazki/carevna_lyagushka')
    text = driver.find_element(By.CLASS_NAME, 'tale-text')
    blocks = text.find_elements(By.TAG_NAME, 'p')
    txt = []
    for i in blocks:
        txt = txt + [i.text]

    sentences = []
    for elem in txt:
        pieces, a = cut_to_sentence(elem)
        if a == 0:
            sentences = pieces + sentences
        if a == 1:
            sentences = [pieces] + sentences

    for i in range(0,10):
        print(sentences[i])
    driver.close()
    return 0

def cut_to_sentence(str):

    str = str.replace('...','§')
    dots = [a for a, num in enumerate(str) if (num == '.') or (num == '!') or (num == '?')] #finds all symbols position and puts in array
    if len(dots) == 0:
        return str, 1

    strs = [str[0:dots[0]+1]]
    for i in range(len(dots)-1):
            strs = strs + [str[dots[i]+1:dots[i+1]+1]]

    for i in range(len(strs)-1):
        strs[i] = strs[i].replace('§','...')
    return strs, 0

main()
#print(cut_to_sentence("awid...aw.d?daw."))
