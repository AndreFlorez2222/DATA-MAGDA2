# Leer los archivos Excel y concatenar solo las columnas deseadas
dfs_concatenados = []
for archivo in archivos:
    df = pd.read_excel(archivo, parse_dates=['FECHA_REGISTRO'])
    ...
