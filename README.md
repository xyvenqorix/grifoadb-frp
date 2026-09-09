# 🦅 GrifoADB

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=28&pause=1000&color=00D9FF&center=true&vCenter=true&width=650&lines=Android+ADB+Tool;Android+Device+Diagnostic;ADB+%26+Fastboot+Utility;Built+with+Python" alt="GrifoADB" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows" />
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Android-ADB-3DDC84?style=for-the-badge&logo=android" />
  <img src="https://img.shields.io/badge/Fastboot-Tools-4285F4?style=for-the-badge&logo=android" />
</p>

## ⚠️ IMPORTANTE — EJECUCIÓN

> 🔴 **Se recomienda ejecutar GrifoADB como ADMINISTRADOR.**

Para obtener el mejor funcionamiento, especialmente al instalar controladores, trabajar con `C:\ADB` y utilizar herramientas de Fastboot, **ejecuta el programa como administrador**.

### ⭐ Opción recomendada

**Se recomienda utilizar `GrifoADB.exe` en lugar del archivo `.py`.**

El `.exe` es la opción más cómoda para utilizar la herramienta sin tener que abrir Python manualmente.

**Clic derecho → `GrifoADB.exe` → `Ejecutar como administrador`**

<p align="center">
  <b>Herramienta de diagnóstico y mantenimiento para dispositivos Android mediante ADB y Fastboot.</b>
</p>


## 📦 ¿Qué es GrifoADB?

**GrifoADB** es una herramienta para Windows creada en Python que reúne diferentes funciones de **ADB y Fastboot** en una interfaz de consola sencilla.

Está pensada para diagnóstico, mantenimiento y comunicación con dispositivos Android compatibles.


## 🛠️ Funciones

### 📱 ADB

* Ver dispositivos conectados
* Comprobar conexión ADB
* Iniciar servidor ADB
* Detener servidor ADB
* Reiniciar servidor ADB
* Consultar versión de ADB
* Diagnóstico básico del dispositivo

### 🔧 Aplicaciones

* Abrir YouTube
* Abrir Ajustes
* Abrir navegador
* Volver a la pantalla principal
* Listar aplicaciones instaladas

### 📊 Información del teléfono

* Información completa del dispositivo
* Modelo
* Fabricante
* Versión de Android
* Nivel SDK
* Estado de batería
* Almacenamiento
* Propiedades del sistema

### 🔄 Reinicio y herramientas

* Reiniciar dispositivo
* Reiniciar en Recovery
* Reiniciar en Bootloader
* Capturar pantalla
* Ver procesos
* Consultar propiedades Android

### 🔐 Diagnóstico FRP

* Comprobar conexión ADB
* Consultar estado relacionado con FRP
* Consultar estado del bootloader
* Consultar Verified Boot
* Consultar modelo
* Consultar fabricante
* Consultar número de serie
* Consultar versión de Android
* Consultar cuentas del dispositivo
* Abrir Ajustes
* Abrir configuración de cuentas
* Reiniciar dispositivo

> ℹ️ Las funciones de diagnóstico solamente muestran información disponible para el dispositivo y los permisos proporcionados por Android.

### ⚡ Fastboot

* Detectar dispositivos Fastboot
* Reiniciar mediante Fastboot
* Mantenimiento Fastboot
* Funciones compatibles con dispositivos Motorola

> ⚠️ Algunas operaciones de Fastboot pueden borrar datos. Lee siempre las advertencias mostradas por el programa antes de continuar.

---

## 📁 Estructura recomendada

```text
GrifoADB/
│
├── GrifoADB.exe
│
└── Driver/
    ├── ADB.zip
    ├── DPInst_x64.exe
    └── DPInst_x86.exe
```

El programa utiliza los archivos de la carpeta `Driver` para preparar ADB y los controladores.

---

## 💻 Requisitos

* Windows 10 / Windows 11
* Cable USB compatible
* Dispositivo Android compatible
* Depuración USB activada para las funciones ADB
* Controladores USB correspondientes al dispositivo
* Permisos de administrador recomendados

Para Fastboot, el dispositivo debe encontrarse en un modo compatible con Fastboot.

---

## 🚀 Uso rápido

### 1️⃣ Descargar GrifoADB

Descarga la versión disponible del proyecto.

### 2️⃣ Ejecutar como administrador

Haz clic derecho sobre:

```text
GrifoADB.exe
```

y selecciona:

```text
Ejecutar como administrador
```

### 3️⃣ Instalar ADB

Desde el menú principal:

```text
1. Instalar ADB Driver
```

El programa preparará ADB en:

```text
C:\ADB
```

### 4️⃣ Conectar el teléfono

Conecta el dispositivo mediante USB.

Si Android muestra:

```text
¿Permitir depuración USB?
```

acepta la autorización correspondiente.

### 5️⃣ Comprobar conexión

En GrifoADB:

```text
ADB
→ Ver dispositivos
```

Si el dispositivo aparece correctamente, ADB está funcionando.

---

## 🧰 Ejecutar desde Python

También puedes ejecutar la versión `.py` directamente si tienes Python instalado.

```text
python GrifoADB.py
```

Sin embargo:

> ⭐ **Para un uso normal se recomienda `GrifoADB.exe`.**

El `.exe` evita tener que ejecutar manualmente el script mediante Python.

---

## 🔐 Permisos de administrador

GrifoADB puede necesitar permisos elevados para determinadas tareas de Windows, especialmente:

* Instalación de controladores
* Escritura en `C:\ADB`
* Ejecución de determinadas herramientas del sistema
* Operaciones relacionadas con Fastboot

Por eso:

> 🛡️ **Se recomienda ejecutar siempre `GrifoADB.exe` como administrador para obtener el mejor funcionamiento.**

---

## ⚠️ Advertencia

GrifoADB es una herramienta de diagnóstico y mantenimiento.

Algunas operaciones pueden modificar el estado del dispositivo o eliminar información.

**Antes de utilizar funciones de borrado o mantenimiento, asegúrate de que el dispositivo y la operación sean correctos.**

No ejecutes comandos de borrado si no estás seguro de lo que hacen.

---

## 📌 Compatibilidad

La disponibilidad de determinadas funciones depende de:

* Modelo del dispositivo
* Fabricante
* Versión de Android
* Estado del bootloader
* Permisos ADB
* Controladores instalados
* Soporte del fabricante para ADB/Fastboot

No todas las funciones funcionan en todos los dispositivos.

---

## 🦅 GrifoADB

<p align="center">
  <b>Android ADB & Fastboot Utility</b>
  <br>
  <sub>Built with Python 🐍</sub>
</p>
