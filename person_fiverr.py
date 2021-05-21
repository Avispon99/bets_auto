class Person:
    def __init__(self, genero, nombre, apellido1, apellido2, lugar_nacimiento, cedula, fecha_dia,
                        fecha_mes, fecha_ano, calle, num_calle, cod_postal, municipio,
                        departamento, telefono, user, email, password,
                        nacionalidad, fecha_exp_dia, fecha_exp_mes, fecha_exp_ano,
                        lugar_exp_dept, lugar_exp_mun, limite_diario, limite_semanal, limite_mensual, segundo_nombre,
                        pep, tipo_documento, ciudad_nacimiento):
        #27 campos
        self.genero = genero #0
        self.nombre = nombre #1
        self.apellido1 = apellido1 #2
        self.apellido2 = apellido2 #3
        self.lugar_nacimiento = lugar_nacimiento #4
        self.cedula = cedula #5
        self.fecha_dia = fecha_dia #6
        self.fecha_mes = fecha_mes #7
        self.fecha_ano = fecha_ano #8
        self.calle = calle #9
        self.num_calle = num_calle #10
        self.cod_postal = cod_postal #11
        self.municipio = municipio #12
        self.departamento = departamento #13
        self.telefono = telefono #14
        self.user = user #15
        self.email = email #16
        self.password = password #17
        self.nacionalidad = nacionalidad #18
        self.fecha_exp_dia = fecha_exp_dia #19
        self.fecha_exp_mes = fecha_exp_mes
        self.fecha_exp_ano = fecha_exp_ano
        self.lugar_exp_dept = lugar_exp_dept #22
        self.lugar_exp_mun = lugar_exp_mun
        self.limite_diario = limite_diario #24
        self.limite_semanal = limite_semanal
        self.limite_mensual = limite_mensual #26
        self.segundo_nombre = segundo_nombre #27
        self.pep = pep #28
        self.tipo_documento=tipo_documento #29
        self.ciudad_nacimiento = ciudad_nacimiento