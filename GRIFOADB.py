import os
import subprocess
import platform
import zipfile
import shutil
import sys

os.system("title GRIFOADB.exe")

VERSION = "1.0"

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
GRAY = "\033[90m"

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DRIVER_DIR = os.path.join(BASE_DIR, "Driver")
ADB_ZIP = os.path.join(DRIVER_DIR, "ADB.zip")
ADB_DIR = r"C:\ADB"


def limpiar():
    os.system("cls")


def pausa():
    print()
    input(" Pulsa ENTER para volver...")


def titulo():
    print(CYAN + r"""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║ GRIFOADB                                             ║
║ ANDROID ADB TOOL                                     ║
║                                                      ║
║ v1.0                                                 ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""" + RESET)


def encabezado(texto):
    print()
    print(CYAN + "╔" + "═" * 56 + "╗" + RESET)
    print(CYAN + "║" + RESET + f" {texto:<55}" + CYAN + "║" + RESET)
    print(CYAN + "╚" + "═" * 56 + "╝" + RESET)
    print()


def architecture_name():
    arquitectura = platform.machine().lower()

    if arquitectura in ("amd64", "x86_64"):
        return "64 bits"

    if arquitectura == "arm64":
        return "ARM64"

    return "32 bits"


def adb_exe():
    ruta = os.path.join(ADB_DIR, "adb.exe")

    if os.path.isfile(ruta):
        return ruta

    return "adb"


def adb_existe():
    ruta = os.path.join(ADB_DIR, "adb.exe")
    return os.path.isfile(ruta)


def ejecutar_adb(comando):
    try:
        programa = adb_exe()

        resultado = subprocess.run(
            [programa] + comando,
            cwd=ADB_DIR if os.path.isdir(ADB_DIR) else None,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=30
        )

        salida = resultado.stdout.strip()
        error = resultado.stderr.strip()

        if salida:
            print(WHITE + salida + RESET)

        if error:
            print(YELLOW + error + RESET)

        return resultado.returncode == 0

    except FileNotFoundError:
        print()
        print(RED + "  X No se encontro adb.exe." + RESET)
        print()
        print("  Debe existir:")
        print(r"  C:\ADB\adb.exe")
        return False

    except Exception as error:
        print()
        print(RED + "  X Error ejecutando ADB:" + RESET)
        print("  " + str(error))
        return False


def instalar_adb():
    print()
    print(CYAN + " Instalando ADB..." + RESET)
    print()

    adb = os.path.join(ADB_DIR, "adb.exe")
    fastboot = os.path.join(ADB_DIR, "fastboot.exe")

    # Si ADB ya existe, no volver a copiar ni sobrescribir archivos.
    if os.path.isfile(adb):
        print(GREEN + r"  OK ADB ya esta instalado en C:\ADB." + RESET)

        if os.path.isfile(fastboot):
            print(GREEN + "  OK Fastboot disponible." + RESET)
        else:
            print(YELLOW + "  ! fastboot.exe no fue encontrado." + RESET)

        return True

    if not os.path.isfile(ADB_ZIP):
        print(RED + "  X No se encontro ADB.zip" + RESET)
        print()
        print("  Debe estar en:")
        print(r"  Driver\ADB.zip")
        return False

    TEMP_DIR = os.path.join(DRIVER_DIR, "_ADB_TEMP")

    try:
        os.makedirs(ADB_DIR, exist_ok=True)

        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR, ignore_errors=True)

        os.makedirs(TEMP_DIR, exist_ok=True)

        print(CYAN + "  Descomprimiendo ADB.zip..." + RESET)

        with zipfile.ZipFile(ADB_ZIP, "r") as zip_ref:
            zip_ref.extractall(TEMP_DIR)

        print(GREEN + "  OK Descomprimido." + RESET)
        print()

        elementos = os.listdir(TEMP_DIR)

        if (
            len(elementos) == 1
            and os.path.isdir(os.path.join(TEMP_DIR, elementos[0]))
        ):
            origen = os.path.join(TEMP_DIR, elementos[0])
        else:
            origen = TEMP_DIR

        print(CYAN + r"  Copiando contenido de ADB a C:\ADB..." + RESET)
        print()

        for elemento in os.listdir(origen):
            origen_item = os.path.join(origen, elemento)
            destino_item = os.path.join(ADB_DIR, elemento)

            try:
                if os.path.isdir(origen_item):
                    shutil.copytree(
                        origen_item,
                        destino_item,
                        dirs_exist_ok=True
                    )
                else:
                    if os.path.isfile(destino_item):
                        print(
                            YELLOW
                            + "  ! Ya existe: "
                            + elemento
                            + " - se conserva."
                            + RESET
                        )
                    else:
                        shutil.copy2(
                            origen_item,
                            destino_item
                        )

            except PermissionError:
                print(
                    YELLOW
                    + "  ! No se pudo reemplazar: "
                    + elemento
                    + " - se conserva el existente."
                    + RESET
                )

        shutil.rmtree(TEMP_DIR, ignore_errors=True)

        if not os.path.isfile(adb):
            print()
            print(RED + r"  X No aparece C:\ADB\adb.exe" + RESET)
            return False

        print()
        print(GREEN + r"  OK ADB disponible en C:\ADB." + RESET)

        if os.path.isfile(fastboot):
            print(GREEN + "  OK Fastboot disponible." + RESET)
        else:
            print(YELLOW + "  ! fastboot.exe no fue encontrado." + RESET)

        return True

    except PermissionError:
        print()
        print(RED + r"  X Windows no permitio escribir en C:\ADB." + RESET)
        print(YELLOW + "  Algunos archivos pueden estar protegidos o en uso." + RESET)
        return False

    except zipfile.BadZipFile:
        print()
        print(RED + "  X ADB.zip esta dañado o no es un ZIP valido." + RESET)
        return False

    except Exception as error:
        print()
        print(RED + "  X Error instalando ADB:" + RESET)
        print("  " + str(error))
        return False


def instalar_driver():
    limpiar()
    titulo()
    encabezado("INSTALAR ADB DRIVER")

    print(
        "  Arquitectura detectada: "
        + GREEN
        + architecture_name()
        + RESET
    )

    print()

    if not instalar_adb():
        pausa()
        return

    print()
    print(CYAN + "  Preparando instalacion del driver..." + RESET)
    print()

    arquitectura = platform.machine().lower()

    if arquitectura in ("amd64", "x86_64", "arm64"):
        dpinst = os.path.join(
            DRIVER_DIR,
            "DPInst_x64.exe"
        )
    else:
        dpinst = os.path.join(
            DRIVER_DIR,
            "DPInst_x86.exe"
        )

    if not os.path.isfile(dpinst):
        print(RED + "  X No se encontro:" + RESET)
        print()
        print("  " + dpinst)
        pausa()
        return

    print(CYAN + "  Ejecutando instalador del driver..." + RESET)
    print()

    try:
        resultado = subprocess.run(
            [dpinst, "/f"],
            cwd=DRIVER_DIR
        )

        print()
        print(
            WHITE
            + "  DPInst termino con codigo: "
            + str(resultado.returncode)
            + RESET
        )

        if resultado.returncode == 0:
            print(GREEN + "  OK DPInst finalizo correctamente." + RESET)

        elif resultado.returncode == 2147483648:
            print(YELLOW + "  DPInst no realizo cambios o el driver" + RESET)
            print(YELLOW + "  ya estaba instalado." + RESET)

        else:
            print(YELLOW + "  DPInst devolvio un codigo diferente de 0." + RESET)

    except Exception as error:
        print()
        print(RED + "  X Error ejecutando DPInst:" + RESET)
        print("  " + str(error))

    print()
    print(GREEN + "  Proceso terminado." + RESET)

    pausa()


def iniciar_adb():
    if not adb_existe():
        print(RED + r" X No existe C:\ADB\adb.exe" + RESET)
        return False

    try:
        resultado = subprocess.run(
            [
                adb_exe(),
                "start-server"
            ],
            cwd=ADB_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=30
        )

        if resultado.stdout.strip():
            print(WHITE + resultado.stdout + RESET)

        if resultado.stderr.strip():
            print(YELLOW + resultado.stderr + RESET)

        return resultado.returncode == 0

    except Exception as error:
        print(RED + "  X Error iniciando ADB:" + RESET)
        print("  " + str(error))
        return False


def fastboot_exe():
    ruta = os.path.join(
        ADB_DIR,
        "fastboot.exe"
    )

    if os.path.isfile(ruta):
        return ruta

    return "fastboot"


def ejecutar_fastboot(comando):
    try:
        programa = fastboot_exe()

        print()
        print(
            CYAN
            + "  > fastboot "
            + " ".join(comando)
            + RESET
        )

        resultado = subprocess.run(
            [programa] + comando,
            cwd=ADB_DIR if os.path.isdir(ADB_DIR) else None,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=120
        )

        salida = resultado.stdout.strip()
        error = resultado.stderr.strip()

        if salida:
            print(WHITE + salida + RESET)

        if error:
            print(YELLOW + error + RESET)

        return resultado.returncode == 0

    except FileNotFoundError:
        print()
        print(RED + "  X No se encontro fastboot.exe." + RESET)
        print()
        print("  Debe existir:")
        print(r"  C:\ADB\fastboot.exe")
        return False

    except Exception as error:
        print()
        print(RED + "  X Error ejecutando Fastboot:" + RESET)
        print("  " + str(error))
        return False


def menu_adb():
    while True:
        limpiar()
        titulo()
        encabezado("ADB")

        print("  1. Ver dispositivos")
        print("  2. Comprobar conexion")
        print("  3. Reiniciar servidor ADB")
        print("  4. Detener servidor ADB")
        print("  5. Iniciar servidor ADB")
        print("  6. Diagnostico FRP")
        print("  7. Version de ADB")
        print()
        print("  0. Volver")
        print()

        opcion = input(
            "  GrifoADB / ADB > "
        ).strip()

        if opcion == "1":
            limpiar()
            titulo()
            encabezado("DISPOSITIVOS ADB")

            iniciar_adb()
            print()

            ejecutar_adb([
                "devices",
                "-l"
            ])

            print()
            print(
                GRAY
                + "  Si aparece 'unauthorized', desbloquea el"
                + RESET
            )
            print(
                GRAY
                + "  telefono y acepta la depuracion USB."
                + RESET
            )

            pausa()

        elif opcion == "2":
            limpiar()
            titulo()
            encabezado("COMPROBAR CONEXION")

            iniciar_adb()
            print()

            correcto = ejecutar_adb([
                "get-state"
            ])

            print()

            if correcto:
                print(
                    GREEN
                    + "  OK ADB responde correctamente."
                    + RESET
                )
            else:
                print(
                    RED
                    + "  X El telefono no esta respondiendo por ADB."
                    + RESET
                )

            pausa()

        elif opcion == "3":
            limpiar()
            titulo()
            encabezado("REINICIAR ADB")

            ejecutar_adb([
                "kill-server"
            ])

            print()
            iniciar_adb()

            print()
            print(
                GREEN
                + "  OK Servidor ADB reiniciado."
                + RESET
            )

            pausa()

        elif opcion == "4":
            ejecutar_adb([
                "kill-server"
            ])

            print()
            print(
                GREEN
                + "  OK Servidor ADB detenido."
                + RESET
            )

            pausa()

        elif opcion == "5":
            limpiar()
            titulo()
            encabezado("INICIAR ADB")

            if iniciar_adb():
                print()
                print(
                    GREEN
                    + "  OK Servidor ADB iniciado."
                    + RESET
                )

            pausa()

        elif opcion == "6":
            limpiar()
            titulo()
            encabezado("DIAGNOSTICO FRP")

            iniciar_adb()

            print()
            print(CYAN + "  ro.frp.pst" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.frp.pst"
            ])

            print()
            print(CYAN + "  ro.boot.flash.locked" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.boot.flash.locked"
            ])

            print()
            print(CYAN + "  ro.boot.verifiedbootstate" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.boot.verifiedbootstate"
            ])

            print()
            print(
                GRAY
                + "  Este apartado solamente consulta informacion."
                + RESET
            )

            pausa()

        elif opcion == "7":
            limpiar()
            titulo()
            encabezado("VERSION ADB")

            ejecutar_adb([
                "version"
            ])

            pausa()

        elif opcion == "0":
            break

        else:
            print(
                RED
                + "\n  Opcion no valida."
                + RESET
            )

            pausa()


def menu_aplicaciones():
    while True:
        limpiar()
        titulo()
        encabezado("APLICACIONES")

        print("  1. Abrir YouTube")
        print("  2. Abrir Ajustes")
        print("  3. Abrir navegador")
        print("  4. Pantalla principal")
        print("  5. Aplicaciones instaladas")
        print()
        print("  0. Volver")
        print()

        opcion = input(
            "  GrifoADB / Aplicaciones > "
        ).strip()

        if opcion == "1":
            ejecutar_adb([
                "shell",
                "am",
                "start",
                "-a",
                "android.intent.action.VIEW",
                "-d",
                "https://www.youtube.com"
            ])

            pausa()

        elif opcion == "2":
            ejecutar_adb([
                "shell",
                "am",
                "start",
                "-a",
                "android.settings.SETTINGS"
            ])

            pausa()

        elif opcion == "3":
            ejecutar_adb([
                "shell",
                "am",
                "start",
                "-a",
                "android.intent.action.VIEW",
                "-d",
                "https://www.google.com"
            ])

            pausa()

        elif opcion == "4":
            ejecutar_adb([
                "shell",
                "input",
                "keyevent",
                "3"
            ])

            pausa()

        elif opcion == "5":
            ejecutar_adb([
                "shell",
                "pm",
                "list",
                "packages"
            ])

            pausa()

        elif opcion == "0":
            break

        else:
            print(
                RED
                + "\n  Opcion no valida."
                + RESET
            )

            pausa()


def menu_telefono():
    while True:
        limpiar()
        titulo()
        encabezado("TELEFONO")

        print("  1. Informacion del telefono")
        print("  2. Modelo")
        print("  3. Version de Android")
        print("  4. Bateria")
        print("  5. Almacenamiento")
        print("  6. Reiniciar en Recovery")
        print()
        print("  0. Volver")
        print()

        opcion = input(
            "  GrifoADB / Telefono > "
        ).strip()

        if opcion == "1":
            ejecutar_adb([
                "shell",
                "getprop"
            ])

            pausa()

        elif opcion == "2":
            ejecutar_adb([
                "shell",
                "getprop",
                "ro.product.model"
            ])

            pausa()

        elif opcion == "3":
            ejecutar_adb([
                "shell",
                "getprop",
                "ro.build.version.release"
            ])

            pausa()

        elif opcion == "4":
            ejecutar_adb([
                "shell",
                "dumpsys",
                "battery"
            ])

            pausa()

        elif opcion == "5":
            ejecutar_adb([
                "shell",
                "df",
                "-h"
            ])

            pausa()

        elif opcion == "6":
            limpiar()
            titulo()
            encabezado("REINICIAR EN RECOVERY")

            print(
                YELLOW
                + "  El telefono se reiniciara en Recovery."
                + RESET
            )

            print()

            confirmar = input(
                "  ¿Continuar? [S/N]: "
            ).strip().upper()

            if confirmar == "S":
                iniciar_adb()

                ejecutar_adb([
                    "reboot",
                    "recovery"
                ])

            else:
                print()
                print(
                    YELLOW
                    + "  Operacion cancelada."
                    + RESET
                )

            pausa()

        elif opcion == "0":
            break

        else:
            print(
                RED
                + "\n  Opcion no valida."
                + RESET
            )

            pausa()


def menu_herramientas():
    while True:
        limpiar()
        titulo()
        encabezado("HERRAMIENTAS")

        print("  1. Reiniciar telefono")
        print("  2. Reiniciar en Recovery")
        print("  3. Reiniciar en Bootloader")
        print("  4. Captura de pantalla")
        print("  5. Ver procesos")
        print("  6. Ver propiedades Android")
        print()
        print("  0. Volver")
        print()

        opcion = input(
            "  GrifoADB / Herramientas > "
        ).strip()

        if opcion == "1":
            ejecutar_adb([
                "reboot"
            ])

            pausa()

        elif opcion == "2":
            ejecutar_adb([
                "reboot",
                "recovery"
            ])

            pausa()

        elif opcion == "3":
            ejecutar_adb([
                "reboot",
                "bootloader"
            ])

            pausa()

        elif opcion == "4":
            archivo = os.path.join(
                BASE_DIR,
                "captura.png"
            )

            try:
                resultado = subprocess.run(
                    [
                        adb_exe(),
                        "exec-out",
                        "screencap",
                        "-p"
                    ],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=30
                )

                if resultado.returncode == 0:
                    with open(
                        archivo,
                        "wb"
                    ) as imagen:
                        imagen.write(
                            resultado.stdout
                        )

                    print(
                        GREEN
                        + "  OK Captura guardada:"
                        + RESET
                    )

                    print(
                        "  " + archivo
                    )

                else:
                    print(
                        RED
                        + "  X No se pudo hacer la captura."
                        + RESET
                    )

                    if resultado.stderr:
                        print(
                            resultado.stderr.decode(
                                "utf-8",
                                errors="ignore"
                            )
                        )

            except Exception as error:
                print(
                    RED
                    + f"  X Error: {error}"
                    + RESET
                )

            pausa()

        elif opcion == "5":
            ejecutar_adb([
                "shell",
                "ps"
            ])

            pausa()

        elif opcion == "6":
            ejecutar_adb([
                "shell",
                "getprop"
            ])

            pausa()

        elif opcion == "0":
            break

        else:
            print(
                RED
                + "\n  Opcion no valida."
                + RESET
            )

            pausa()


def menu_frp():
    while True:
        limpiar()
        titulo()
        encabezado("FRP - DIAGNOSTICO")

        print("  1. Comprobar conexion ADB")
        print("  2. Ver estado FRP")
        print("  3. Ver estado del bootloader")
        print("  4. Ver estado Verified Boot")
        print("  5. Ver modelo y numero de serie")
        print("  6. Ver version de Android")
        print("  7. Ver cuentas del dispositivo")
        print("  8. Abrir Ajustes")
        print("  9. Abrir configuracion de cuentas")
        print("  10. Reiniciar telefono")
        print()
        print("  0. Volver")
        print()

        opcion = input(
            "  GrifoADB / FRP > "
        ).strip()

        if opcion == "1":
            limpiar()
            titulo()
            encabezado("COMPROBAR ADB")

            iniciar_adb()

            print()

            ejecutar_adb([
                "get-state"
            ])

            pausa()

        elif opcion == "2":
            limpiar()
            titulo()
            encabezado("ESTADO FRP")

            iniciar_adb()

            print()
            print(CYAN + "  ro.frp.pst" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.frp.pst"
            ])

            print()
            print(
                GRAY
                + "  Este valor depende de la version y fabricante."
                + RESET
            )

            pausa()

        elif opcion == "3":
            limpiar()
            titulo()
            encabezado("ESTADO BOOTLOADER")

            iniciar_adb()

            print()
            print(CYAN + "  ro.boot.flash.locked" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.boot.flash.locked"
            ])

            print()
            print(CYAN + "  ro.boot.verifiedbootstate" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.boot.verifiedbootstate"
            ])

            pausa()

        elif opcion == "4":
            limpiar()
            titulo()
            encabezado("VERIFIED BOOT")

            iniciar_adb()

            print()
            print(CYAN + "  ro.boot.verifiedbootstate" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.boot.verifiedbootstate"
            ])

            print()
            print(CYAN + "  ro.boot.flash.locked" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.boot.flash.locked"
            ])

            pausa()

        elif opcion == "5":
            limpiar()
            titulo()
            encabezado("IDENTIFICACION DEL DISPOSITIVO")

            iniciar_adb()

            print()
            print(CYAN + "  Modelo:" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.product.model"
            ])

            print()
            print(CYAN + "  Fabricante:" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.product.manufacturer"
            ])

            print()
            print(CYAN + "  Numero de serie:" + RESET)

            ejecutar_adb([
                "get-serialno"
            ])

            pausa()

        elif opcion == "6":
            limpiar()
            titulo()
            encabezado("VERSION DE ANDROID")

            iniciar_adb()

            print()
            print(CYAN + "  Android:" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.build.version.release"
            ])

            print()
            print(CYAN + "  SDK:" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.build.version.sdk"
            ])

            print()
            print(CYAN + "  Build:" + RESET)

            ejecutar_adb([
                "shell",
                "getprop",
                "ro.build.display.id"
            ])

            pausa()

        elif opcion == "7":
            limpiar()
            titulo()
            encabezado("CUENTAS DEL DISPOSITIVO")

            iniciar_adb()

            print()
            print(
                GRAY
                + "  Consulta de cuentas configuradas."
                + RESET
            )

            print()

            ejecutar_adb([
                "shell",
                "cmd",
                "account",
                "list"
            ])

            pausa()

        elif opcion == "8":
            limpiar()
            titulo()
            encabezado("ABRIR AJUSTES")

            iniciar_adb()

            ejecutar_adb([
                "shell",
                "am",
                "start",
                "-a",
                "android.settings.SETTINGS"
            ])

            pausa()

        elif opcion == "9":
            limpiar()
            titulo()
            encabezado("CONFIGURACION DE CUENTAS")

            iniciar_adb()

            ejecutar_adb([
                "shell",
                "am",
                "start",
                "-a",
                "android.settings.SYNC_SETTINGS"
            ])

            pausa()

        elif opcion == "10":
            limpiar()
            titulo()
            encabezado("REINICIAR TELEFONO")

            confirmar = input(
                "\n  ¿Reiniciar el telefono? [S/N]: "
            ).strip().upper()

            if confirmar == "S":
                iniciar_adb()

                ejecutar_adb([
                    "reboot"
                ])

            pausa()

        elif opcion == "0":
            break

        else:
            print(
                RED
                + "\n  Opcion no valida."
                + RESET
            )

            pausa()


def menu_reparacion_moto():
    while True:
        limpiar()
        titulo()
        encabezado("MANTENIMIENTO FASTBOOT - MOTO E5 PLAY")

        print(
            YELLOW
            + "  ATENCION: fastboot -w BORRA LOS DATOS."
            + RESET
        )

        print()
        print("  1. Ejecutar mantenimiento Fastboot")
        print("  2. Comprobar dispositivo Fastboot")
        print()
        print("  0. Volver")
        print()

        opcion = input(
            "  GrifoADB / Fastboot > "
        ).strip()

        if opcion == "1":
            limpiar()
            titulo()
            encabezado("MANTENIMIENTO FASTBOOT")

            print(
                YELLOW
                + "  ESTE PROCESO BORRARA LOS DATOS DEL TELEFONO."
                + RESET
            )

            print()
            print("  Comandos:")
            print("  1. fastboot oem fb_mode_set")
            print("  2. fastboot -w")
            print("  3. fastboot oem fb_mode_clear")
            print("  4. fastboot reboot")

            print()

            confirmar = input(
                "  Escribe BORRAR para continuar: "
            ).strip().upper()

            if confirmar != "BORRAR":
                print()
                print(
                    YELLOW
                    + "  Proceso cancelado."
                    + RESET
                )

                pausa()
                continue

            print()
            print(
                CYAN
                + "  [1/4] Activando FB mode..."
                + RESET
            )

            if not ejecutar_fastboot([
                "oem",
                "fb_mode_set"
            ]):
                print()
                print(
                    RED
                    + "  X No se pudo ejecutar FB mode set."
                    + RESET
                )

                pausa()
                continue

            print()
            print(
                YELLOW
                + "  [2/4] Borrando datos..."
                + RESET
            )

            if not ejecutar_fastboot([
                "-w"
            ]):
                print()
                print(
                    RED
                    + "  X El borrado devolvio un error."
                    + RESET
                )

                pausa()
                continue

            print()
            print(
                CYAN
                + "  [3/4] Limpiando FB mode..."
                + RESET
            )

            if not ejecutar_fastboot([
                "oem",
                "fb_mode_clear"
            ]):
                print()
                print(
                    YELLOW
                    + "  ! fb_mode_clear devolvio un error."
                    + RESET
                )

            print()
            print(
                CYAN
                + "  [4/4] Reiniciando telefono..."
                + RESET
            )

            ejecutar_fastboot([
                "reboot"
            ])

            print()
            print(
                GREEN
                + "  OK Proceso terminado."
                + RESET
            )

            pausa()

        elif opcion == "2":
            limpiar()
            titulo()
            encabezado("COMPROBAR FASTBOOT")

            print(
                CYAN
                + "  Buscando dispositivos..."
                + RESET
            )

            print()

            ejecutar_fastboot([
                "devices"
            ])

            print()
            print(
                GRAY
                + "  Si aparece un numero de serie, Fastboot detecta"
                + RESET
            )

            print(
                GRAY
                + "  el dispositivo."
                + RESET
            )

            pausa()

        elif opcion == "0":
            break

        else:
            print(
                RED
                + "\n  Opcion no valida."
                + RESET
            )

            pausa()


def menu():
    while True:
        limpiar()
        titulo()

        print(
            GRAY
            + "  Herramienta ADB para Android"
            + RESET
        )

        print()

        print(
            CYAN
            + "  ┌─ MENU PRINCIPAL"
            + RESET
        )

        print("  │")
        print("  │  1. Instalar ADB Driver")
        print("  │  2. Aplicaciones")
        print("  │  3. Telefono")
        print("  │  4. ADB")
        print("  │  5. Herramientas")
        print("  │  6. FRP")
        print("  │  7. Mantenimiento Fastboot")
        print("  │")

        print(
            CYAN
            + "  └─ 0. Salir"
            + RESET
        )

        print()

        opcion = input(
            "  GrifoADB > "
        ).strip()

        if opcion == "1":
            instalar_driver()

        elif opcion == "2":
            menu_aplicaciones()

        elif opcion == "3":
            menu_telefono()

        elif opcion == "4":
            menu_adb()

        elif opcion == "5":
            menu_herramientas()

        elif opcion == "6":
            menu_frp()

        elif opcion == "7":
            menu_reparacion_moto()

        elif opcion == "0":
            limpiar()

            print()
            print(
                CYAN
                + "  GrifoADB finalizado."
                + RESET
            )

            print()
            break

        else:
            print(
                RED
                + "\n  Opcion no valida."
                + RESET
            )

            pausa()


if __name__ == "__main__":
    try:
        menu()

    except KeyboardInterrupt:
        print()
        print(
            YELLOW
            + "  Programa cancelado."
            + RESET
        )
        print()

    except Exception as error:
        print()
        print(
            RED
            + f"  Error: {error}"
            + RESET
        )

        input(
            "\n  Pulsa ENTER para cerrar..."
        )