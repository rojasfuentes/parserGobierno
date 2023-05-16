from beforeWords import cantidad_05, fechaEmision_12, fechaEntrega_13, marca_17
from onlyFirst import lote_03, caducidad_04, fechaFabr_14, paisOrigen_16, noElementos
from last import noRemision_01, codigoProd_02, noOrdRep_06, noContrato_07, destino_18, licitacion_19, entidadFed_20
from itertools import repeat
import pandas as pd
import datetime


noRemision_01 = [element for element, num in zip(noRemision_01, noElementos) for _ in repeat(None, num)]
codigoProd_02 = [element for element, num in zip(codigoProd_02, noElementos) for _ in repeat(None, num)]
noOrdRep_06 = [element for element, num in zip(noOrdRep_06, noElementos) for _ in repeat(None, num)]
noContrato_07 = [element for element, num in zip(noContrato_07, noElementos) for _ in repeat(None, num)]
fechaEmision_12 = [element for element, num in zip(fechaEmision_12, noElementos) for _ in repeat(None, num)]
fechaEntrega_13 = [element for element, num in zip(fechaEntrega_13, noElementos) for _ in repeat(None, num)]
destino_18 = [element for element, num in zip(destino_18, noElementos) for _ in repeat(None, num)]
licitacion_19 = [element for element, num in zip(licitacion_19, noElementos) for _ in repeat(None, num)]
entidadFed_20 = [element for element, num in zip(entidadFed_20, noElementos) for _ in repeat(None, num)]

vacio = [''] * len(noRemision_01)

df = pd.DataFrame({'Remision': noRemision_01, 
                   'Código de Producto': codigoProd_02, 
                   'Lote': lote_03, 
                   'Caducidad': caducidad_04, 
                   'Cantidad': cantidad_05, 
                   'No. Orden de Reposicion': noOrdRep_06, 
                   'No. Contrato': noContrato_07, 
                   'Proveedor': vacio,
                   'Precio de Compra': vacio,
                   'IVA': vacio,
                   'Tipo de Moneda': vacio,
                   'Fecha de emision': fechaEmision_12, 
                   'Fecha máxima de entrega': fechaEntrega_13, 
                   'Fecha de Fabricación': fechaFabr_14, 
                   'Registro Sanitario': vacio,
                   'País de Origen' : paisOrigen_16, 
                   'Marca': marca_17, 
                   'Destino': destino_18, 
                   'Licitación': licitacion_19, 
                   'Entidad Federativa': entidadFed_20})

fecha = datetime.datetime.now().strftime("%Y-%m-%d")
df.to_excel(f'output {fecha}.xlsx', index=False)





