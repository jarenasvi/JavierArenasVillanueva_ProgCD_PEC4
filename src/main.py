"""MAIN del proyecto PEC4"""

import argparse
from modules.data_loader import load_dataset
from modules.eda import show_head, show_columns, show_info
from modules.cleaning import (rename_columns, drop_columns, group, merge_datasets)
from modules.visualization import plot_temporal
from modules.analysis import analyze_dataset

def exercise_1():
    """
    Ejecuta ejercicio 1.

    Parámetros:
        None.

    Devuelve:
        Muestra por pantalla las primeras filas, columnas e información del dataset cargado.
    """
    print("-----------EJERCICIO 1-----------")
    df = load_dataset()
    show_head(df)
    show_columns(df)
    show_info(df)


def exercise_2():
    """
    Ejecuta ejercicio 2.

    Parámetros:
        None.

    Devuelve:
        DataFrame fusionado de rendimiento y abandono y muestra el EDA información por pantalla.
    """
    print("-----------EJERCICIO 2-----------")
    df_rendiment = load_dataset("data/rendiment_estudiants.xlsx")
    df_abandono = load_dataset("data/taxa_abandonament.xlsx")

    df_rendiment = rename_columns(df_rendiment, "rendiment")
    df_abandono = rename_columns(df_abandono, "abandono")

    df_rendiment = drop_columns(df_rendiment, "rendiment")
    df_abandono = drop_columns(df_abandono, "abandono")

    df_rendiment = group(df_rendiment, "rendiment")
    df_abandono = group(df_abandono, "abandono")

    df_merged = merge_datasets(df_rendiment, df_abandono)

    show_head(df_merged)
    show_columns(df_merged)
    show_info(df_merged)

    return df_merged


# ---------- EJERCICIO 3 ----------
def exercise_3(df_merged):
    """
    Ejecuta ejercicio 3.

    Parámetros:
        df_merged (pd.DataFrame): Dataset fusionado de rendimiento y abandono.

    Devuelve:
        Genera y guarda la figura en la carpeta img/.
    """
    print("-----------EJERCICIO 3-----------")
    plot_temporal(df_merged)


# ---------- EJERCICIO 4 ----------
def exercise_4(df_merged):
    """
    Ejecuta ejercicio 4.

    Parámetros:
        df_merged (pd.DataFrame): Dataset fusionado de rendimiento y abandono.

    Devuelve:
        Genera un JSON con metadata, estadísticas globales, análisis por rama y rankings en la carpeta report/
    """
    print("-----------EJERCICIO 4-----------")
    analyze_dataset(df_merged)


# ---------- MAIN ----------
def main():
    """
    Ejecuta el main, todos los ejercicios.

    Parámetros:
        None.

    Devuelve:
        Ejecuta los ejercicios seleccionados o todos si no se indica argumento.
    """
    parser = argparse.ArgumentParser(
        description="PEC4 - Programación para la Ciencia de Datos"
    )
    parser.add_argument(
        "-ex",
        "--exercise",
        type=int,
        choices=[1, 2, 3, 4],
        help="Ejecuta los ejercicios del 1 hasta el indicado"
    )

    args = parser.parse_args()

    # Sin argumentos ejecutamos todos
    if args.exercise is None:
        exercise_1()
        df_merged = exercise_2()
        exercise_3(df_merged)
        exercise_4(df_merged)
        return

    # Si indicamos el ejercicio
    if args.exercise >= 1:
        exercise_1()

    if args.exercise >= 2:
        df_merged = exercise_2()

    if args.exercise >= 3:
        exercise_3(df_merged)

    if args.exercise >= 4:
        exercise_4(df_merged)


if __name__ == "__main__":
    main()
