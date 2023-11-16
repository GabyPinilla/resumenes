import pandas as pd
# Creando funcion de filtro de fechas
def filtro_fechas(df, columna, fecha_inicio, fecha_fin):
    df[columna] = pd.to_datetime(df[columna])
    df_filtrado = df[df[columna].between(fecha_inicio, fecha_fin)]
    return df_filtrado

# Funcion funcion_agrupadora
def funcion_agrupadora(df, fila, valor, medida,orden):
    df_pivot = pd.pivot_table(
        data = df
        , index = fila
        #, columns = columna
        , values = valor
        , aggfunc= medida
        , margins = True # filas y columnas de totales
        , margins_name= 'total'
        , fill_value = 0 # se cambian los valores NaN por 0
    ).sort_values(by=orden, ascending=False).head(11) # ordena, toma total y los 10 primeros valores
    return df_pivot.sort_values(by=orden, ascending=True)

# Funcion para guardar df
def guardar_df(df, nombre_tabla, engine, existencia):
    df.to_sql(name = nombre_tabla, con = engine, if_exists = existencia)
    # if_exists{‘fail’, ‘replace’, ‘append’}, default 'fail'