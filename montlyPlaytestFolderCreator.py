import os
import datetime
import calendar
import platform
import subprocess

def crear_estructura_mes_completo():
    # Ruta fija
    directorio_base = r"C:\Users\MarianelaFlora\Desktop\Matches Historial"

    # Info actual
    fecha_hoy = datetime.datetime.now()
    anio = fecha_hoy.year
    mes_num = fecha_hoy.month
    
    # Nombre del mes en inglés (March, April, etc.)
    mes_nombre_en = fecha_hoy.strftime('%B')
    
    # Formato solicitado: "03_March"
    nombre_mes_formateado = f"{str(mes_num).zfill(2)}_{mes_nombre_en}"

    # Días del mes
    _, ultimo_dia = calendar.monthrange(anio, mes_num)
    directorio_mes = os.path.join(directorio_base, nombre_mes_formateado)

    try:
        if not os.path.exists(directorio_base):
            os.makedirs(directorio_base)
        if not os.path.exists(directorio_mes):
            os.makedirs(directorio_mes)

        for dia in range(1, ultimo_dia + 1):
            fecha_iterada = datetime.date(anio, mes_num, dia)
            
            # Lunes a Viernes (0-4)
            if fecha_iterada.weekday() < 5:
                dia_str = str(dia).zfill(2)
                mes_str = str(mes_num).zfill(2)
                nombre_carpeta_dia = f"{dia_str} - {mes_str} - {anio}"
                
                ruta_dia = os.path.join(directorio_mes, nombre_carpeta_dia)

                if not os.path.exists(ruta_dia):
                    os.makedirs(ruta_dia)

                # Sesiones y Matches
                for sesion in range(1, 4):
                    ruta_sesion = os.path.join(ruta_dia, f"Session {sesion} -")
                    if not os.path.exists(ruta_sesion):
                        os.makedirs(ruta_sesion)

                    for match in range(1, 4):
                        ruta_match = os.path.join(ruta_sesion, f"Match {match} -")
                        if not os.path.exists(ruta_match):
                            os.makedirs(ruta_match)

        print(f"Todo listo en: {nombre_mes_formateado}")
        abrir_carpeta(directorio_mes)

    except Exception as e:
        print(f"Error: {e}")

def abrir_carpeta(ruta):
    try:
        sistema = platform.system()
        if sistema == "Windows":
            os.startfile(ruta)
        else:
            subprocess.Popen(["open" if sistema == "Darwin" else "xdg-open", ruta])
    except:
        pass

if __name__ == "__main__":
    crear_estructura_mes_completo()