import pandas as pd

# Rutas de los archivos Excel
archivos = ['C:/Users/ADMIN/Documents/IPRAN/INFRAESTRUCTURA/2024/5-chona/power/ipran_excel.xlsx',
            'C:/Users/ADMIN/Documents/IPRAN/INFRAESTRUCTURA/2024/5-chona/power/huawei_excel.xlsx']

# Leer los archivos Excel y concatenar solo las columnas deseadas
dfs_concatenados = []
for archivo in archivos:
    df = pd.read_excel(archivo, parse_dates=['FECHA_REGISTRO'])
    # Filtrar las columnas deseadas
    columnas_deseadas = ['ID', 'PROYECTO', 'PLATAFORMA', 'SOLICITUD', 'REFERENCIA', 'ESTADO',
                         'FECHA_REGISTRO', 'FECHA_CAMBIO_ESTADO', 'DU_ID']
    df_filtrado = df[columnas_deseadas]
    dfs_concatenados.append(df_filtrado)

# Concatenar los DataFrames
resultado = pd.concat(dfs_concatenados, ignore_index=True)

# Agregar la columna PROVEEDOR con la condición dada
resultado['PROVEEDOR'] = 'HUAWEI'
resultado.loc[resultado['PROYECTO'].str.contains('UAN NOKIA'), 'PROVEEDOR'] = 'NOKIA'

# Agregar las columnas de año, mes y número de semana
resultado['AÑO'] = resultado['FECHA_REGISTRO'].dt.year
resultado['MES'] = resultado['FECHA_REGISTRO'].dt.month
resultado['NUMERO_SEMANA'] = resultado['FECHA_REGISTRO'].dt.isocalendar().week

# Convertir las columnas FECHA_REGISTRO y FECHA_CAMBIO_ESTADO a tipo datetime
resultado['FECHA_REGISTRO'] = pd.to_datetime(resultado['FECHA_REGISTRO'])
resultado['FECHA_CAMBIO_ESTADO'] = pd.to_datetime(resultado['FECHA_CAMBIO_ESTADO'])

# Calcular la diferencia entre las fechas
resultado['SLA'] = resultado['FECHA_CAMBIO_ESTADO'] - resultado['FECHA_REGISTRO']
resultado.loc[resultado['FECHA_CAMBIO_ESTADO'].isnull(), 'SLA'] = "Pendiente"




# Guardar el resultado en un nuevo archivo Excel
resultado.to_excel('resultado_con_du_ids_proveedor_y_fecha8.xlsx', index=False)

print("Se han concatenado las columnas deseadas y se ha agregado la columna PROVEEDOR, AÑO, MES y NUMERO_SEMANA en un nuevo archivo Excel.")
