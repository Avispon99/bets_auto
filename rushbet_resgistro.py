from selenium import webdriver
import time
from helpers import wait_el, find_el, place_sel, campo_sel, getDriver, wait_landing_xpath, place_sel2
from person_fiverr import Person
import random

# Indicar nombre de la casa de apuestas
HOUSE_NAME = 'Rushbet'



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

    """Paso 1"""
    #Datos de Usuario
    wait_el('id', 'signup-form-1-NICKNAME', 'send_keys', driver, person.user)
    find_el('id', 'signup-form-1-email', 'send_keys', driver, person.email)
    find_el('id', 'signup-form-1-password', 'send_keys', driver, person.password)
    find_el('id', 'signup-form-1-validatepassword', 'send_keys', driver, person.password) # confirm pass
    #find_el('id', 'signup-form-1-promotionalcode', 'send_keys', driver, person.opcionalCode) #opcional


    #Continuar
    find_el('css', 
    '#signup-form-1-submit',
    'click_js',driver, '')


    """Paso 2"""
    #Nombres
    wait_el('id', 'signup-form-2-FIRSTNAME', 'send_keys', driver, person.nombre)
    wait_el('name', 'FIRSTNAME2', 'send_keys', driver, person.segundo_nombre)
    find_el('id', 'signup-form-2-LASTNAME', 'send_keys', driver, person.apellido1)
    find_el('id', 'signup-form-2-LASTNAME2', 'send_keys', driver, person.apellido2)

    #Ubicacion
    elemento = driver.find_element_by_css_selector('#signup-form-2 > div:nth-child(1) > div.form-zipcode-container.signup-block-ZIPRESOLVE > div.col-sm-3.col-xs-6.voffset2.validator-result-select.signup-block-STATE > div.dropdown-wrapper > div.dropdown.webkit-scrollbar > ul')
    o=elemento.find_elements_by_tag_name("a")
    print('la o++ --\n',o, type(o))
    for lo in o:
        print(lo.text)

    
    elt = driver.find_elements_by_xpath('//*[@id="signup-form-2"]/div[1]/div[7]/div[1]/div[1]/div[2]/ul/li[1]/a')
    print('elt',elt[0].text,type(elt))

     
    print('---°°°')
    #place_sel2('css', '#signup-form-2 > div:nth-child(1) > div.form-zipcode-container.signup-block-ZIPRESOLVE > div.col-sm-3.col-xs-6.voffset2.validator-result-select.signup-block-STATE > div.dropdown-wrapper > div.dropdown.webkit-scrollbar > ul',
    # driver, person.departamento)
    print('---ooo')
    
    print('end')
    time.sleep(5000)#<<
    #------------------------------------------------------------------------------------------------------   

    # Nombres
    wait_el('id', 'formEl_173', 'send_keys', driver, person.nombre)#--
    wait_el('id', 'formField_14', 'send_keys', driver, person.segundo_nombre)#++
    find_el('id', 'formEl_540', 'send_keys', driver, person.apellido1)#--
    find_el('id', 'formField_25', 'send_keys', driver, person.apellido2)#--
    

    # Genero
    if person.genero == 'Femenino':
        find_el('id', 'Gender_F', 'click_js', driver, '')#--
        
    elif person.genero == 'Masculino':
        find_el('id', 'Gender_M', 'click_js', driver, '')#--


    # Fecha de naciomiento    
    find_el('xpath', '//select[@id="day_dateOfBirth"]/option[@value="'+person.fecha_dia.zfill(2)+'"]', 'click', driver)#--         
    find_el('xpath', '//select[@id="month_dateOfBirth"]/option[@value="'+person.fecha_mes.zfill(2)+'"]', 'click', driver)#-- 
    find_el('xpath', '//select[@id="year_dateOfBirth"]/option[@value="'+person.fecha_ano+'"]', 'click', driver)#--
 

    #Residencia
    place_sel('name', 'sogeiRegionCode', driver, person.departamento)
    place_sel('name', 'city', driver, person.municipio)
    find_el('name', 'address', 'send_keys', driver, person.calle)
    

    #Siguiente
    find_el('css', 
    '#p_p_id_registration_WAR_accountportlet_ > div.fn-portlet.portlet__content.portlet__content_border_show.portlet__content_type_registration.registerFormPortlet > div.registration-wrappper > div.registration-wizard.register-content-wrapper-wplay > div.portlet__actions.fn-register-controls > button',
    'click_js',driver, '')


    #Nacionalidad
    print('wait..')
    wait_el('name', 'citizenship', 'justwait',driver, person.nacionalidad)        
    place_sel('name', 'citizenship', driver, person.nacionalidad)


    #Datos de la Cedula
    place_sel('xpath', '//*[@id="p_p_id_registration_WAR_accountportlet_"]/div[2]/div[1]/div[2]/div[1]/div[2]/form/div/div[1]/fieldset[1]/div[2]/span/select', driver, person.lugar_exp_dept)
    place_sel('xpath', '//*[@id="p_p_id_registration_WAR_accountportlet_"]/div[2]/div[1]/div[2]/div[1]/div[2]/form/div/div[1]/fieldset[2]/div[2]/span/select', driver, person.lugar_exp_mun)
    find_el('id', 'formField_8', 'send_keys', driver, person.cedula)
    find_el('xpath', '//select[@id="day_idIssueDate"]/option[@value="'+person.fecha_exp_dia.zfill(2)+'"]', 'click', driver)
    find_el('xpath', '//select[@id="month_idIssueDate"]/option[@value="'+person.fecha_exp_mes.zfill(2)+'"]', 'click', driver)
    find_el('xpath', '//select[@id="year_idIssueDate"]/option[@value="'+person.fecha_exp_ano.zfill(2)+'"]', 'click', driver)
    

    #siguiente
    find_el('css', 
    '#p_p_id_registration_WAR_accountportlet_ > div.fn-portlet.portlet__content.portlet__content_border_show.portlet__content_type_registration.registerFormPortlet.registration__step-2 > div.registration-wrappper > div.registration-wizard.register-content-wrapper-wplay > div.portlet__actions.fn-register-controls > button',
    'click_js',driver, '')
 
 
    #Datos de contacto
    wait_el('name', 'email', 'send_keys', driver, person.email)
    wait_el('id', 'phone-field', 'send_keys', driver, person.telefono)



    #Password
    find_el('id', 'formEl_3508', 'send_keys', driver, person.password)


    #Desbloquear limites
    pth='//*[@id="p_p_id_registration_WAR_accountportlet_"]/div[2]/div[1]/div[2]/div[1]/div[3]/form/div/div[6]/div[2]'
    expand= driver.find_element_by_xpath(pth)
    expand.click()

    #Limpiar limites
    time.sleep(random.uniform(0.5, 2))    
    clear1='//*[@id="p_p_id_registration_WAR_accountportlet_"]/div[2]/div[1]/div[2]/div[1]/div[3]/form/div/div[6]/div[3]/div[1]/div[2]/input'
    clear2='weekdepositlimit'
    clear3='monthdepositlimit'
    driver.find_element_by_xpath(clear1).clear()
    driver.find_element_by_name(clear2).clear()
    driver.find_element_by_name(clear3).clear()

    #Escribir limites
    find_el('xpath', '//*[@id="p_p_id_registration_WAR_accountportlet_"]/div[2]/div[1]/div[2]/div[1]/div[3]/form/div/div[6]/div[3]/div[1]/div[2]/input',
     'send_keys', driver, person.limite_diario)
    find_el('name', 'weekdepositlimit', 'send_keys', driver, person.limite_semanal)
    find_el('name', 'monthdepositlimit', 'send_keys', driver, person.limite_mensual)



    #Checks

    """ Nota: Habilitar la linea si "aceptar terminos" deja de 
        aparecer marcado por defecto"""
    #driver.find_elements_by_css_selector("#terms-checkbox").click()       
    if person.pep == 'no' or 'No' or 'NO':     
        driver.find_element_by_xpath('//*[@id="pep"]').click() # Dejar simpre "no" por defecto si no es "pep"
        

    
    #Accept    
    wait_el('css', 
    '#p_p_id_registration_WAR_accountportlet_ > div.fn-portlet.portlet__content.portlet__content_border_show.portlet__content_type_registration.registerFormPortlet.registration__step-3 > div.registration-wrappper > div.registration-wizard.register-content-wrapper-wplay > div.portlet__actions.fn-register-controls > button',
    'justwait',driver, '') # No click

    print('END') 
    



if __name__ == '__main__':

    # Ubicacion del chromedriver
    executable_path = 'driver/chromedriver.exe'

    # Url de acceso a la casa de apuestas -> Cambiarla para cada script
    url = 'https://www.rushbet.co/?page=signup&step=1' #--


    # Datos de prueba de la persona (fake)
    person = Person('Femenino', 'Araceli', 'Taheri', 'Rochel', 'Cordoba', 
                    '134604149', '2', '3', '1974', 'Cl 8 No 1-34', 
                    '177 1A', '73947', 'Puerto Caicedo', 'Putumayo', 
                    '313404725', 'arataro74','grsaidy17@gmail.com', 
                    'fO824HEFf', 'colombia', '5', '7', '2013', 'BOLIVAR', 
                    'cartagena', '5000', '80000', '200000', 'lola', '') #--

    # Dejar esto como está
    xpath_url = None
    xpath_end = None
    settings = None
    tipo_user = None
    login_email = None
    browser = 'Chrome'

    # Llamada funcion
    register(executable_path, url, person, xpath_url, xpath_end, settings, tipo_user, login_email, browser)