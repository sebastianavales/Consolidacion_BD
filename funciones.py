import pandas as pd
import glob
import warnings
import datetime
import os

def transformacion(ruta_importacion, ruta_exportacion):

    ## Cambiar a la ruta seleccionada
    os.chdir(ruta_importacion)

    ## Importación de recursos necesarios

    # Archivos CSV a formatear
    archivos_csv = [archivo for archivo in os.listdir(ruta_importacion) if archivo.endswith('.csv')]

    for archivo in archivos_csv:

        warnings.filterwarnings('ignore')

        # Nombre de archivo
        nombre = os.path.basename(archivo)

        # Lectura de archivo
        archivo = pd.read_csv(archivo, sep=';', header=None)

        # Titulos de archivo
        columns = ['Sociedad','Numero de Documento','Ejercicio','Posicion','Cuenta de Mayor',\
            'Cuenta alternativa','Texto Posicion','Poliza (Clave Ref. 1)','Ramo (Clave Ref. 2)',\
            'Clave Referencia 3','Indicador D/H','Importe Moneda Local','Documento Compensacion',\
            'Fecha de Compensacion','Fecha de Contabilizacion','Periodo','Fecha de Documento',\
            'Fecha Fin Vigencia','Fecha Valor','Clase de Documento','Recibo (Referencia)',\
            'Texto Cabecera','Deudor','Acreedor','Nit','Nombre']
        archivo.columns = columns

        # Formateo de columnas tipo número
        def format_value(value):
            if pd.notnull(value):
                return str(value).replace('.0', '')
            return value
        
        columns_to_format = ['Poliza (Clave Ref. 1)', 'Ramo (Clave Ref. 2)', 'Clave Referencia 3', 'Importe Moneda Local', 'Documento Compensacion', 'Fecha Fin Vigencia', 'Recibo (Referencia)', 'Deudor', 'Acreedor', 'Nit']
        archivo[columns_to_format] = archivo[columns_to_format].applymap(format_value)

        # Filtro para eliminar clase de documento
        sin_II = archivo.loc[archivo['Clase de Documento'] != 'II']

        # Exportar el DataFrame
        export = ruta_exportacion
        archivo_salida = os.path.join(export, nombre)
        sin_II.to_csv(archivo_salida, sep=";", index=False)
        print(f"Archivo '{nombre}' transformado con éxito.")

def transformacion2(ruta_importacion, ruta_exportacion):

    ## Cambiar a la ruta seleccionada
    os.chdir(ruta_importacion)

    ## Importación de recursos necesarios

    # Archivos CSV a formatear
    archivos_csv = [archivo for archivo in os.listdir(ruta_importacion) if archivo.endswith('.csv')]

    for archivo in archivos_csv:

        warnings.filterwarnings('ignore')

        # Nombre de archivo
        nombre = os.path.basename(archivo)

        # Lectura de archivo
        archivo = pd.read_csv(archivo, sep=';', header=None)

        # Titulos de archivo
        columns = ['Sociedad','Numero de Documento','Ejercicio','Posicion','Cuenta de Mayor',\
            'Cuenta alternativa','Texto Posicion','Poliza (Clave Ref. 1)','Ramo (Clave Ref. 2)',\
            'Clave Referencia 3','Indicador D/H','Importe Moneda Local','Documento Compensacion',\
            'Fecha de Compensacion','Fecha de Contabilizacion','Periodo','Fecha de Documento',\
            'Fecha Fin Vigencia','Fecha Valor','Clase de Documento','Recibo (Referencia)',\
            'Texto Cabecera','Deudor','Acreedor','Nit','Nombre']
        archivo.columns = columns

        # Formateo de columnas tipo número
        def format_value(value):
            if pd.notnull(value):
                return str(value).replace('.0', '')
            return value
        
        columns_to_format = ['Poliza (Clave Ref. 1)', 'Ramo (Clave Ref. 2)', 'Clave Referencia 3', 'Importe Moneda Local', 'Documento Compensacion', 'Fecha Fin Vigencia', 'Recibo (Referencia)', 'Deudor', 'Acreedor', 'Nit']
        archivo[columns_to_format] = archivo[columns_to_format].applymap(format_value)

        # Exportar el DataFrame
        export = ruta_exportacion
        archivo_salida = os.path.join(export, nombre)
        archivo.to_csv(archivo_salida, sep=";", index=False)
        print(f"Archivo '{nombre}' transformado con éxito.")
    
def maduracion(fecha_corte, archivo_salida, ruta_importacion, ruta_exportacion):

    ## Cambiar a la ruta seleccionada

    os.chdir(ruta_importacion)

    ## Importación de recursos necesarios

    # Archivos CSV a concatenar
    all_files = [os.path.basename(archivo) for archivo in glob.glob(f"{ruta_importacion}/*.csv")]

    # Titulos de columnas
    columns = ['Sociedad','Numero de Documento','Ejercicio','Posicion','Cuenta de Mayor',\
            'Cuenta alternativa','Texto Posicion','Poliza (Clave Ref. 1)','Ramo (Clave Ref. 2)',\
            'Clave Referencia 3','Indicador D/H','Importe Moneda Local','Documento Compensacion',\
            'Fecha de Compensacion','Fecha de Contabilizacion','Periodo','Fecha de Documento',\
            'Fecha Fin Vigencia','Fecha Valor','Clase de Documento','Recibo (Referencia)',\
            'Texto Cabecera','Deudor','Acreedor','Nit','Nombre']
    
    ## Concatenación de archivos

    # Lista para almacenar los DataFrames de los archivos CSV
    dataframes = []

    # Cargar cada archivo CSV en un DataFrame y agregarlo a la lista
    for file in all_files:
        warnings.filterwarnings('ignore')
        df = pd.read_csv(file, sep=';', header=None)
        dataframes.append(df)

    print('[1/4] Todos los archivos fueron cargados.')

    # Concatenar los DataFrames en uno solo
    maduracion = pd.concat(dataframes, ignore_index=True)
    maduracion.columns = columns

    ##Formateo de columnas

    # Formateo de columnas tipo número
    def format_value(value):
        if pd.notnull(value):
            return str(value).replace('.0', '')
        return value
    columns_to_format = ['Recibo (Referencia)', 'Nit']
    maduracion[columns_to_format] = maduracion[columns_to_format].applymap(format_value)

    # Formateo de columnas tipo texto
    maduracion['Nit'] = maduracion['Nit'].fillna('Vacío')
    maduracion['Nombre'] = maduracion['Nombre'].fillna('Vacío')
    maduracion['Recibo (Referencia)'] = maduracion['Recibo (Referencia)'].fillna('Vacío')

    print('[2/4] Transformación de columnas completada.')

    ## Formulas de maduración

    # Fecha corte
    fecha_corte = pd.to_datetime(fecha_corte)

    # Fecha cont
    maduracion['Fecha cont'] = pd.to_datetime(maduracion['Fecha de Contabilizacion'], format='%Y%m%d').dt.strftime('%Y/%m/%d')

    # Días entre la fecha de corte y la fecha contable ingresada
    maduracion['Días Transcurridos'] = (fecha_corte - pd.to_datetime(maduracion['Fecha cont'])).dt.days.astype(int)

    # 30 días
    maduracion['30 días'] = maduracion['Importe Moneda Local'].where(maduracion['Días Transcurridos'] <= 30, '')

    # 60 días
    maduracion['60 días'] = maduracion['Importe Moneda Local'].where((maduracion['Días Transcurridos'] > 30) & \
                                                                    (maduracion['Días Transcurridos'] <= 60), '')

    # 90 días
    maduracion['90 días'] = maduracion['Importe Moneda Local'].where((maduracion['Días Transcurridos'] > 60) & \
                                                                    (maduracion['Días Transcurridos'] <= 90), '')

    # 180 días
    maduracion['180 días'] = maduracion['Importe Moneda Local'].where((maduracion['Días Transcurridos'] > 90) & \
                                                                    (maduracion['Días Transcurridos'] <= 180), '')

    # 360 días
    maduracion['360 días'] = maduracion['Importe Moneda Local'].where((maduracion['Días Transcurridos'] > 180) & \
                                                                    (maduracion['Días Transcurridos'] <= 360), '')

    # >360 días
    maduracion['>360 días'] = maduracion['Importe Moneda Local'].where(maduracion['Días Transcurridos'] > 360, '')

    print(f'[3/4] Formulas de maduración aplicadas con fecha de corte {fecha_corte}.')

    ## Consolidado de información

    # Agrupación de registros para consolidar información
    groupby = maduracion.groupby(['Cuenta de Mayor', 'Nit', 'Nombre', 'Recibo (Referencia)', 'Fecha de Contabilizacion']) .agg({'30 días':'sum', '60 días':'sum', '90 días':'sum', '180 días':'sum', '360 días':'sum', '>360 días':'sum', 'Importe Moneda Local':'sum'}).reset_index()

    ## Exportación

    # Calcula el número total de filas en el DataFrame
    total_filas = len(groupby)

    # Define el tamaño de la fracción
    tamano_fraccion = 500000

    # Calcula el número total de fracciones
    total_fracciones = total_filas // tamano_fraccion + (1 if total_filas % tamano_fraccion != 0 else 0)

    # Ruta y nombre de exportación
    export = ruta_exportacion
    nombre = archivo_salida

    # Bucle para dividir y exportar en fracciones
    for i in range(total_fracciones):
        inicio = i * tamano_fraccion
        fin = min((i + 1) * tamano_fraccion, total_filas)
    
        # Obtén la fracción actual del DataFrame
        fraccion_df = groupby.iloc[inicio:fin]

        # Exporta la fracción a un archivo CSV
        ruta_resultado = os.path.join(export, f'{nombre}_{i + 1}.csv')
        fraccion_df.to_csv(ruta_resultado, sep=';' ,encoding='utf-8-sig', index=False)

        print(f'[4/4] Archivo {nombre}_{i + 1}.csv exportado en la ruta {export}.')