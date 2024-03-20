import pandas as pd

# Rutas de los archivos CSV
ruta_ipran = r'C:/Users/ADMIN/Documents/IPRAN/INFRAESTRUCTURA/2024/5-chona/power/ipran.csv'
ruta_huawei = r'C:/Users/ADMIN/Documents/IPRAN/INFRAESTRUCTURA/2024/5-chona/power/huawei.csv'

# Leer los archivos CSV
datos_ipran = pd.read_csv(ruta_ipran)
datos_huawei = pd.read_csv(ruta_huawei)

# Guardar los datos de HUAWEI.csv en un archivo Excel
ruta_excel_huawei = r'C:/Users/ADMIN/Documents/IPRAN/INFRAESTRUCTURA/2024/5-chona/power/huawei_excel.xlsx'
datos_huawei.to_excel(ruta_excel_huawei, sheet_name='pag', engine='openpyxl')
ruta_excel_ipran = r'C:/Users/ADMIN/Documents/IPRAN/INFRAESTRUCTURA/2024/5-chona/power/ipran_excel.xlsx'
datos_ipran.to_excel(ruta_excel_ipran, sheet_name='pag', engine='openpyxl')

