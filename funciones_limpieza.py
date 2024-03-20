def remover_outliers(df):
    """
    Esta función elimina los valores atípicos de un DataFrame.

    Args:
    - df: DataFrame que contiene datos.

    Returns:
    - DataFrame: DataFrame sin valores atípicos.
    """
    # Seleccionar solo columnas numéricas
    df_numeric = df.select_dtypes(include=['number'])

    # Calcular el rango intercuartílico (IQR) para columnas numéricas
    Q1 = df_numeric.quantile(0.25)
    Q3 = df_numeric.quantile(0.75)
    IQR = Q3 - Q1

    # Definir los límites para identificar valores atípicos
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    # Filtrar los datos para quitar valores atípicos en columnas numéricas
    df_sin_outliers = df[~((df_numeric < lower_limit) | (df_numeric > upper_limit)).any(axis=1)]

    return df_sin_outliers


def convertir_variables_categoricas(df):
    """
    Esta función toma un DataFrame y convierte las columnas con variables categóricas binarias,
    ternarias o de cualquier otra cantidad de valores únicos en valores numéricos.

    Args:
    - df: DataFrame que contiene datos.

    Returns:
    - DataFrame: DataFrame con las variables categóricas convertidas.
    """
    # Realizar una copia del DataFrame para evitar modificar el original
    df_convertido = df.copy()
    
    # Iterar sobre todas las columnas del DataFrame
    for col in df.columns:
        # Verificar si la columna es de tipo objeto (categórica)
        if df[col].dtype == 'object':
            unique_values = df[col].unique()
            # Asignar un número único a cada valor único en la columna
            value_map = {val: idx for idx, val in enumerate(unique_values)}
            # Convertir los valores categóricos a valores numéricos según el mapeo
            df_convertido[col] = df_convertido[col].map(value_map)
    
    return df_convertido