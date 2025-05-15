import pandas as pd

datos = pd.DataFrame({
    'Sustancia': ['Albumina', 'Fosfotasa alcalina', 'Bilirrubina directa', 'Nitrogeno ureico', 'Creatinina', 'Glucosa', 'Proteina Total', 'Acido urico' ],
    'Valores normales': ['3.5-5.0', '30-120', '0-0.2', '10-26', '0.6-1.3', '70-115', '6.0-8.0', '2.5-7.0'],
    'Unidad': ['g/dL', 'U/L', 'mg/dL', 'mg/dL', 'mg/dL', 'mg/dL', 'g/dL', 'mg/dL'],
    'Fecha de analisis': ['input', 'input', 'input', 'input', 'input', 'input', 'input', 'input']
})

datos['Fecha de analisis'] = pd.to_datetime(datos['Fecha de analisis'], format='%d/%m/%Y', errors='coerce')
datos['Fecha de analisis'] = datos['Fecha de analisis'].dt.strftime('%d/%m/%Y')

datos.to_excel('Datos médicos.xlsx', sheet_name='Quimica sanguinea')

datos2 = pd.DataFrame({
    'Tipo de célula': ['Leucocitos', 'Hemoglobina', 'Hematocrito', 'Plaquetas', 'Eritrocitos'],
    'Valores normales': ['4.5-11.0', 'Hombres: 14.0-18.0, Mujeres: 12.0-16.0', 'Hombres: 42.0-52.0, Mujeres: 37.0-47.0', '150-450', 'Hombres: 4.5-6.3, Mujeres: 4.2-5.4'],
    'Unidad': ['x10^3/uL', 'g/dL', '%', 'x10^3/uL', 'x10^3/uL'],
    'Fecha de analisis': ['input', 'input', 'input', 'input', 'input']
})

datos2['Fecha de analisis'] = pd.to_datetime(datos2['Fecha de analisis'], format='%d/%m/%Y', errors='coerce')
datos2['Fecha de analisis'] = datos2['Fecha de analisis'].dt.strftime('%d/%m/%Y')

with pd.ExcelWriter('Datos médicos.xlsx', engine='openpyxl', mode='a') as writer:
    datos2.to_excel(writer, sheet_name='Biometría Hematica')

datos3 = pd.DataFrame({
    'Examen': ['Colesterol total', 'HDL colesterol', 'LDL colesterol', 'Trigliceridos'],
    'Valores normales': ['Menos de 200', 'Entre 40 y 60', 'Menos de 100', 'Menos de 150'],
    'Unidad': ['mg/dL', 'mg/dL', 'mg/dL', 'mg/dL'],
    'Fecha de analisis': ['input', 'input', 'input', 'input']
})

datos3['Fecha de analisis'] = pd.to_datetime(datos3['Fecha de analisis'], format='%d/%m/%Y', errors='coerce')
datos3['Fecha de analisis'] = datos3['Fecha de analisis'].dt.strftime('%d/%m/%Y')

with pd.ExcelWriter('Datos médicos.xlsx', engine='openpyxl', mode='a') as writer:
    datos3.to_excel(writer, sheet_name='Lipidograma')

datos4 = pd.DataFrame({
    'Electrolito': ['Sodio', 'Potasio', 'Cloro', 'Calcio', 'Magnerio', 'Fosforo'],
    'Valores normales': ['135-145', '3.5-5.5', '96-106', '8.5-10.5', '1.4-2.2', '2.8-4.5'],
    'Unidad': ['mEq/L', 'mEq/L', 'mEq/L', 'mEq/L', 'mEq/L', 'mg/dL'],
    'Fecha de analisis': ['input', 'input', 'input', 'input', 'input', 'input']
})

datos4['Fecha de analisis'] = pd.to_datetime(datos4['Fecha de analisis'], format='%d/%m/%Y', errors='coerce')
datos4['Fecha de analisis'] = datos4['Fecha de analisis'].dt.strftime('%d/%m/%Y')

with pd.ExcelWriter('Datos médicos.xlsx', engine='openpyxl', mode='a') as writer:
    datos4.to_excel(writer, sheet_name='Electrolitos')
