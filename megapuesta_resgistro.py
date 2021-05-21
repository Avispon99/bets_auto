from selenium import webdriver
import time
from helpers import wait_el, find_el, place_sel, campo_sel, getDriver, wait_landing_xpath
from person_fiverr import Person
import random

# Indicar nombre de la casa de apuestas
HOUSE_NAME = 'Megapuesta'



def register(executable_path, url, person, xpath_url, xpath_end, settings, tipo_user, login_email, browser):

    print(HOUSE_NAME)

    driver = getDriver(browser, executable_path)
    driver.delete_all_cookies()
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    #------------------------------------------------------
    #Direct find elements #--
    #------------------------------------------------------

    wait_landing_xpath(xpath_url, 'click', driver, '')

    
    #wait_el('id', 'onetrust-accept-btn-handler', '	', driver) #>> cookies answer

    time.sleep(3)

    tab_list = driver.window_handles
    driver.switch_to.window(tab_list[-1])

    #wait_el('xpath', '/html/body/op-root/div/op-main-template/div/div[2]/op-register/div/tabset/ul/li[2]/a', 'click_js',
    #        driver) #>> manual answer


    
    #Nombre
    wait_el('name', 'FirstName', 'send_keys', driver, person.nombre)
    find_el('name', 'MiddleName', 'send_keys', driver, person.segundo_nombre)
    find_el('name', 'LastName', 'send_keys', driver, person.apellido1)
    find_el('name', 'SecondLastName', 'send_keys', driver, person.apellido2)

    #Datos CC
    find_el('name', 'CivilIdentificationCode', 'send_keys', driver, person.cedula)
    place_sel('name', 'DocumentTypeID', driver, person.tipo_documento)

    # Fechas (expedicion de la cedula y nacimiento)
    find_el('name', 'btoIssueOn', 'send_keys', driver, person.fecha_exp_dia+'/'+person.fecha_exp_mes+'/'+person.fecha_exp_ano)
    find_el('name', 'DateOfBirth', 'send_keys', driver, person.fecha_dia +'/'+person.fecha_mes+'/'+person.fecha_ano)
   

    #Ubicacion expedicion cedula
    place_sel('name', 'DepartmentOfBirthID', driver, person.lugar_exp_dept)
    place_sel('name', 'MunicipalityOfBirthID', driver, person.lugar_exp_mun)
    

    #siguiente
    find_el('xpath', 
    '//button[@id="step1" and @class="btn btn-user-success next"]',
    'click_js',driver, '')


    #e-mail
    wait_el('name', 'Email', 'send_keys', driver, person.email)#
    find_el('name', 'ConfirmEmail', 'send_keys', driver, person.email)


    #password
    find_el('name', 'Password', 'send_keys', driver, person.password)
    find_el('name', 'ConfirmPassword', 'send_keys', driver, person.password)
    

    #Sexo
    if person.genero == 'Femenino':
        place_sel('name', 'Gender', driver, person.genero)#--
        
    elif person.genero == 'Masculino':
        place_sel('name', 'Gender', driver, person.genero)#-- 

    
    #Datos personal
    place_sel('name', 'CountryISO', driver, person.nacionalidad)
    place_sel('name', 'IssueDepartmentId', driver, person.lugar_nacimiento)
    place_sel('name', 'IssueMunicipalityId', driver, person.ciudad_nacimiento)


    #Siguiente
    find_el('xpath', 
    '//button[@id="step2" and @class="btn btn-user-success next"]',
    'click_js',driver, '')    

    #Datos adicionales
    wait_el('name', 'Address', 'send_keys', driver, person.calle)
    find_el('name', 'MobileNumber', 'send_keys', driver, person.telefono)

    place_sel('name', 'DepartmentID', driver, person.departamento)
    place_sel('name', 'MunicipalityID', driver, person.municipio)
    

    #Check
    driver.execute_script('document.getElementsByTagName("span")[44].click()')

    find_el('xpath', 
    '//*[@id="step3"]/button[2]',
    'justwait',driver, '')
    
    print('end')
    time.sleep(15)
    
    
    
    
    #--------------------------------------------------
    
    
    


if __name__ == '__main__':

    # Ubicacion del chromedriver
    executable_path = 'driver/chromedriver.exe'

    # Url de acceso a la casa de apuestas -> Cambiarla para cada script
    url = 'https://www.megapuesta.co/registrarse/' #--


    # Datos de prueba de la persona (fake)
    person = Person('Femenino', 'Araceli', 'Taheri', 'Rochel', 'Cordoba', 
                    '134604149', '2', '3', '1974', 'Cl 8 No 1-34', 
                    '', '73947', 'Puerto Caicedo', 'Putumayo', 
                    '313404725', 'arataro74','grsaidy17@gmail.com', 
                    'fO824HEFf', 'colombia', '5', '7', '2013', 'Putumayo', 
                    'Puerto Caicedo', '5000', '80000', '200000', 'lola',
                    'cedula de ciudadania','no','tuchín')#--

    # Dejar esto como está
    xpath_url = None
    xpath_end = None
    settings = None
    tipo_user = None
    login_email = None
    browser = 'Chrome'

    # Llamada funcion
    register(executable_path, url, person, xpath_url, xpath_end, settings, tipo_user, login_email, browser)