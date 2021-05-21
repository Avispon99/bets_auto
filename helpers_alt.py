from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from difflib import SequenceMatcher
import random


def wait_el(tipo, nombre, accion, driver, campo=''):
    '''Función que agrupa los wait for element visible
    tipo es la referencia del elemento: id, name, xpath, css_selector
    nombre es el identificador concreto id="casa"
    accion puede ser click, click_js o send_keys
    campo es lo que se escribe en caso de send_keys'''

    if nombre is None:
        return (False)

    try:
        # TIPO ELEMENTO
        if tipo == 'name':

            elemento = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, nombre)))

        elif tipo == 'id':

            elemento = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, nombre)))

        elif tipo == 'xpath':

            elemento = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, nombre)))

        elif tipo == 'css':

            elemento = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, nombre)))

        # ACCION
        if accion == 'send_keys':

            for letra in campo:
                elemento.send_keys(letra)
                time.sleep(random.uniform(0.01, 0.05))

        elif accion == 'click':

            elemento.click()

        elif accion == 'click_js':

            driver.execute_script('arguments[0].click()', elemento)

        elif accion == 'justwait':

            pass

        # SLEEP
        time.sleep(random.uniform(1.5, 3.0))

        return (elemento)

    except Exception as exc:
        print(exc)
        return (False)


def find_el(tipo, nombre, accion, driver, campo=''):
    '''Función que agrupa los find element
    tipo es la referencia del elemento: id, name, xpath, css_selector
    nombre es el identificador concreto id="casa"
    accion puede ser click, click_js o send_keys
    campo es lo que se escribe en caso de send_keys'''

    try:
        # TIPO ELEMENTO
        if tipo == 'name':

            elemento = driver.find_element_by_name(nombre)

        elif tipo == 'id':

            elemento = driver.find_element_by_id(nombre)

        elif tipo == 'xpath':
            
            elemento = driver.find_element_by_xpath(nombre)
            
        elif tipo == 'css':

            elemento = driver.find_element_by_css_selector(nombre)

        # ACCION
        if accion == 'send_keys':

            for letra in campo:
                elemento.send_keys(letra)
                time.sleep(random.uniform(0.01, 0.05))

        elif accion == 'click':

            elemento.click()

        elif accion == 'click_js':

            driver.execute_script('arguments[0].click()', elemento)

        elif accion == 'clear_send':

            elemento.clear()
            time.sleep(1)
            for letra in campo:
                elemento.send_keys(letra)
                time.sleep(random.uniform(0.01, 0.05))

        # SLEEP
        time.sleep(random.uniform(1.5, 3.0))

        return (elemento)

    except Exception as exc:
        print(exc)
        return (False)


def place_sel(tipo, nombre, driver, place):
    '''Función que busca el string mas parecido en un desplegable
    tipo es la referencia del elemento: id, name, xpath, css_selector
    nombre es el identificador concreto id="casa"
    place es el elemento buscado'''

    try:
        select_box = find_el(tipo, nombre, '', driver, '')
        options = [x for x in select_box.find_elements_by_tag_name("option")]
        
        ratios = []
        for option in options:
            
            com = option.text.upper()

            ignore_words = ['COMUNIDAD', 'COMUNITAT', 'REGIÓN', 'REGION', 'PRINCIPADO', 'FORAL', 'DIPUTACIÓN', 'ILLES',
                            'ISLAS', 'DIPUTACION', 'DISTRITO', 'TURISTICO, CULTURAL', 'DE INDIAS', 'D.C','D. T. y C']
            for word in ignore_words:
                if word in com:
                    com = com.replace(word, '')
            com = com.split('/')[0]
            ratios.append(SequenceMatcher(None, com, place.upper()).ratio())

        indice = ratios.index(max(ratios))
        select_box_2 = Select(find_el(tipo, nombre, '', driver, ''))
        select_box_2.select_by_index(indice)

        time.sleep(random.uniform(1.5, 3.0))

        return (True)

    except Exception as exc:
        print(exc)
        return (False)


def campo_sel(tipo, nombre, driver, campo, sel_type):
    '''Función que agrupa las llamadas a select
    tipo es la referencia del elemento: id, name, xpath, css_selector
    nombre es el identificador concreto id="casa"
    campo es lo que se escribe en caso de send_keys
    sel_type puede ser value o index'''

    try:

        elemento = Select(find_el(tipo, nombre, '', driver, ''))

        if sel_type == 'value':
            elemento.select_by_value(str(campo))
        elif sel_type == 'index':
            elemento.select_by_index(int(campo))

        time.sleep(random.uniform(1.5, 3.0))

        return (True)

    except Exception as exc:
        print(exc)
        return (False)


def getDriver(browser, executable_path):

    options = webdriver.ChromeOptions()
    if browser == 'Chrome':
        driver = webdriver.Chrome(options=options, executable_path=executable_path)
    return driver


def wait_landing_xpath(list_xpaths, action, driver, campo=''):

    return (False)


def place_sel2(tipo, nombre, driver, place):
    '''Función que busca el string mas parecido en un desplegable
    tipo es la referencia del elemento: id, name, xpath, css_selector
    nombre es el identificador concreto id="casa"
    place es el elemento buscado'''

    try:
        select_box = find_el(tipo, nombre, '', driver, '')
        options = [x for x in select_box.find_elements_by_tag_name("li")]
        #print('options:\n', options)#<<
        ratios = []
        for option in options:
            print('option:\n', type(option), option.text)#<<

                
            com = option.text.upper()

            ignore_words = ['COMUNIDAD', 'COMUNITAT', 'REGIÓN', 'REGION', 'PRINCIPADO', 'FORAL', 'DIPUTACIÓN', 'ILLES',
                            'ISLAS', 'DIPUTACION', 'DISTRITO', 'TURISTICO, CULTURAL', 'DE INDIAS', 'D.C','D. T. y C']
            for word in ignore_words:
                if word in com:
                    com = com.replace(word, '')
            com = com.split('/')[0]
            ratios.append(SequenceMatcher(None, com, place.upper()).ratio())
        print("ratios:\n",ratios)    
        indice = ratios.index(max(ratios))
        print('flag 3')
        select_box_2 = Select(find_el(tipo, nombre, '', driver, ''))
        select_box_2.select_by_index(indice)
        #select_box_2 = Select(find_el(tipo, nombre, '', driver, ''))#<<
        #select_box_2.select_by_index(indice)#<<

        time.sleep(random.uniform(1.5, 3.0))

        return (True)

    except Exception as exc:
        print(exc)
        return (False)