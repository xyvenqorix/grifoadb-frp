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

<p align="center">
  <b>Herramienta ADB y Fastboot para diagnóstico, mantenimiento y administración de dispositivos Android.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square" />
  <img src="https://img.shields.io/badge/License-Open%20Source-lightgrey?style=flat-square" />
</p>

---

## 📱 ¿Qué es GrifoADB?

**GrifoADB** es una herramienta de consola desarrollada en **Python para Windows** que reúne funciones de **ADB** y **Fastboot** en un solo programa.

Está diseñada para facilitar tareas de diagnóstico, información del dispositivo, conexión ADB, herramientas Android y operaciones de mantenimiento.

---

## ✨ Características

### 🔌 ADB

* 📱 Ver dispositivos conectados.
* 🔗 Comprobar conexión ADB.
* ▶️ Iniciar servidor ADB.
* ⛔ Detener servidor ADB.
* 🔄 Reiniciar servidor ADB.
* ℹ️ Consultar versión de ADB.
* 🔍 Diagnóstico básico del dispositivo.

### 📲 Información del teléfono

* 📋 Información del dispositivo.
* 📱 Modelo.
* 🏭 Fabricante.
* 🤖 Versión de Android.
* 🔢 Nivel SDK.
* 🔋 Estado de batería.
* 💾 Almacenamiento.
* 🔐 Número de serie.
* ⚙️ Propiedades del sistema.

### 🛠️ Herramientas

* 🔄 Reiniciar teléfono.
* 🧰 Reiniciar en Recovery.
* ⚡ Reiniciar en Bootloader.
* 📸 Captura de pantalla.
* 📊 Ver procesos.
* ⚙️ Ver propiedades de Android.

### 📦 Aplicaciones

* ▶️ Abrir YouTube.
* ⚙️ Abrir Ajustes.
* 🌐 Abrir navegador.
* 🏠 Volver a la pantalla principal.
* 📋 Listar aplicaciones instaladas.

### 🔐 Diagnóstico

GrifoADB permite consultar información relacionada con el estado del dispositivo:

* Estado de ADB.
* Estado FRP disponible mediante propiedades del sistema.
* Estado del bootloader.
* Verified Boot.
* Modelo y fabricante.
* Número de serie.
* Versión de Android.
* SDK.
* Build.
* Información de cuentas disponible mediante ADB.

> Los resultados dependen del fabricante, modelo y versión de Android.

### ⚡ Fastboot

* 🔎 Detectar dispositivos Fastboot.
* 🔄 Reiniciar mediante Fastboot.
* 🛠️ Ejecutar operaciones de mantenimiento compatibles.
* 📱 Comprobar conexión Fastboot.

---

## 🛡️ Ejecución recomendada

<p align="center">
  <img src="https://img.shields.io/badge/RECOMENDADO-GrifoADB.exe-00D9FF?style=for-the-badge" />
</p>

Para usuarios normales se recomienda utilizar:

**`GrifoADB.exe`**

en lugar de ejecutar directamente el archivo `.py`.

### 🔑 Ejecutar como administrador

Se recomienda ejecutar `GrifoADB.exe` como **Administrador**, especialmente para las funciones relacionadas con:

* Instalación de drivers.
* Escritura en `C:\ADB`.
* Instalación de componentes.
* Determinadas operaciones de Windows.

Para hacerlo:

**Clic derecho → Ejecutar como administrador**

> ⚠️ ADB no necesita necesariamente permisos de administrador para todas sus funciones. Los permisos elevados son especialmente importantes para la instalación de drivers y determinadas operaciones del sistema.

---

## 📦 Requisitos

<p align="center">
  <img src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6?style=for-the-badge&logo=windows" />
  <img src="https://img.shields.io/badge/USB-Connection-555555?style=for-the-badge&logo=usb" />
  <img src="https://img.shields.io/badge/Android-Device-3DDC84?style=for-the-badge&logo=android" />
</p>

* Windows 10 / Windows 11.
* Cable USB.
* Dispositivo Android compatible.
* ADB/Fastboot.
* Python 3.x solamente si se utiliza el código fuente.

Para utilizar ADB normalmente debes tener habilitada la **Depuración USB** y aceptar la autorización RSA en el teléfono cuando Android la solicite.

---

## 📁 Estructura

```text
GrifoADB/
│
├── GrifoADB.py
│
├── Driver/
│   ├── ADB.zip
│   ├── DPInst_x64.exe
│   └── DPInst_x86.exe
│
└── README.md
```

El programa utiliza:

```text
C:\ADB\
```

para almacenar las herramientas ADB y Fastboot.

---

## 🚀 Ejecutar desde Python

Si quieres ejecutar el código fuente:

```text
python GrifoADB.py
```

También puedes utilizar:

```text
py GrifoADB.py
```

---

## 📦 Crear GrifoADB.exe

Para crear un ejecutable de Windows:

```text
pyinstaller --onefile --console --name GrifoADB GrifoADB.py
```

El resultado estará en:

```text
dist\GrifoADB.exe
```

Para incluir la carpeta `Driver`:

```text
pyinstaller --onefile --console --name GrifoADB --add-data "Driver;Driver" GrifoADB.py
```

---

## 🔧 Instalación de ADB

Desde el menú principal:

```text
1. Instalar ADB Driver
```

GrifoADB busca:

```text
Driver\ADB.zip
```

y prepara:

```text
C:\ADB
```

También puede ejecutar el instalador de drivers correspondiente a la arquitectura de Windows.

---

## 🖥️ Menú principal

```text
╔══════════════════════════════════════════════════════╗
║                                                      ║
║ GRIFOADB                                             ║
║ ANDROID ADB TOOL                                     ║
║                                                      ║
║ v1.0                                                 ║
║                                                      ║
╚══════════════════════════════════════════════════════╝

1. Instalar ADB Driver
2. Aplicaciones
3. Telefono
4. ADB
5. Herramientas
6. FRP
7. Mantenimiento Fastboot

0. Salir
```

---

## ⚠️ Advertencia

Algunas funciones pueden modificar el estado del dispositivo o eliminar información.

Antes de utilizar funciones de mantenimiento, asegúrate de comprender qué operación vas a ejecutar.

Especialmente:

```text
fastboot -w
```

puede borrar los datos del dispositivo.

**Utiliza estas funciones únicamente en dispositivos que tengas autorización para administrar.**

---

## 🧰 Tecnologías

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,windows,android" alt="Technologies" />
</p>

* Python 3
* ADB
* Fastboot
* Windows
* Android Debug Bridge

---

## 📊 Estado del proyecto

<p align="center">
  <img src="https://img.shields.io/badge/GrifoADB-v1.0-00D9FF?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows" />
</p>

🚧 **Proyecto en desarrollo**

Se pueden añadir nuevas funciones y mejoras en futuras versiones.

---

## 👨‍💻 Autor

<p align="center">
  <b>Rodol / Rodol_UGC</b>
</p>

<p align="center">
  🦅 <b>GrifoADB</b>
</p>

<p align="center">
  Android ADB Tool
</p>

---

## ⭐ Contribuciones

Las ideas, mejoras y reportes de errores son bienvenidos.

Si encuentras un problema:

1. Comprueba que el dispositivo está conectado.
2. Comprueba que ADB funciona correctamente.
3. Revisa el mensaje mostrado por GrifoADB.
4. Si continúa el problema, abre un Issue indicando los pasos para reproducirlo.

---

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?font=Fira+Code&size=20&pause=1000&color=00D9FF&center=true&vCenter=true&width=500&lines=GrifoADB;Android+ADB+Tool;Built+with+Python;Made+for+Android+Diagnostics" alt="GrifoADB" />
</p>

<p align="center">
  🦅 <b>GrifoADB</b> — ADB & Fastboot Utility
</p>
