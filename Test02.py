correos = ['ejemplo1@gmail.com', 
           'ejemplo2@dominio.com', 
           'ejemplo3@hotmail.com', 
           'ejemplo4@dominio.com']

# Imprimir la lista de correos donde sean solo correos de dominio.com
print([correo for correo in correos if '@dominio.com' in correo])
