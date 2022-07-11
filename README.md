# ETL Tangel -Fintech
## Prueba tecnica Tangelo Fintech

ETL encargada de comunicarse con una API, obtiene información especifica del JSON que entrega el endpoint, se crea un DataFrame con base en la información obtenida, sobre la columna "Time" del DataFrame se realizan operaciones o calculos como cual es el dato máximo, mínimo, promedio y total, esta información se almacena en una BD sqlite que la misma ETL crea desde 0, por último el DataFrame se convierte a un archivo .json y se almacena en el escritorio.
Para ejecutar el archivo solo es necesario situarse en la dirección donde está el archivo .py y en la consola escribir "python ETL.py".
