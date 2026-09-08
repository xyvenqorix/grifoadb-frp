🐊 GrifoADB

Android ADB Tool para Windows

GrifoADB es una herramienta de consola desarrollada en Python para facilitar el uso de Android Debug Bridge (ADB) desde Windows mediante un menú sencillo.

Permite comprobar dispositivos, consultar información del teléfono, gestionar aplicaciones, realizar capturas de pantalla, reiniciar el dispositivo y otras operaciones ADB.

---

🖥️ Plataforma

Windows| Python| ADB| Fastboot
🪟 Compatible| 🐍 3.x| 🤖 Incluido| ⚡ Incluido

«Diseñado principalmente para Windows.»

---

✨ Características

- 📱 Información del teléfono
- 🔋 Estado de batería
- 💾 Información de almacenamiento
- 🤖 Versión de Android
- 📋 Modelo del dispositivo
- 🔄 Reinicio mediante ADB
- 📦 Lista de aplicaciones instaladas
- 📸 Capturas de pantalla
- 🕘 Acceso a aplicaciones recientes
- ▶️ Abrir YouTube
- ⚙️ Abrir Ajustes
- 🏠 Volver a la pantalla principal
- 🔌 Comprobar dispositivos conectados
- 🔧 Reiniciar el servidor ADB
- 🚀 ADB y Fastboot incluidos
- 🔌 Instalación del Google USB Driver

---

📦 Instalación

1. Clonar el repositorio

git clone https://github.com/TU-USUARIO/GrifoADB.git

2. Entrar en la carpeta

cd GrifoADB

3. Ejecutar

python grifoadb.py

«Cambia "grifoadb.py" por el nombre real de tu archivo Python si es diferente.»

---

🔌 Configurar el teléfono

Para utilizar ADB:

1. Activa las Opciones de desarrollador en tu teléfono.
2. Activa Depuración USB.
3. Conecta el teléfono al PC mediante USB.
4. Acepta la autorización de depuración USB en el teléfono.
5. Ejecuta GrifoADB.
6. Entra en:

ADB → Comprobar conexion

También puedes utilizar:

ADB → Ver dispositivos

---

🛠️ Estructura del proyecto

GrifoADB/
│
├── grifoadb.py
├── ADB/
│   ├── adb.exe
│   ├── fastboot.exe
│   └── ...
│
├── .gitignore
├── LICENSE
└── README.md

«La carpeta "ADB/" puede ser creada automáticamente por GrifoADB mediante la función de instalación.»

---

⚠️ Restablecimiento de fábrica

GrifoADB incluye una opción de Restablecimiento de fábrica.

Herramientas
└── Restablecimiento de fabrica

Esta operación puede borrar los datos del dispositivo.

Antes de utilizarla, asegúrate de tener una copia de seguridad de la información importante.

«El comportamiento del restablecimiento puede variar según el fabricante, versión de Android y permisos disponibles. GrifoADB no garantiza que el comando funcione en todos los dispositivos.»

---

🔐 Uso responsable

GrifoADB está pensado para utilizarse con dispositivos propios o dispositivos para los que tengas autorización.

No utilices ADB para acceder, modificar o eliminar información de dispositivos sin permiso.

---

🌐 Tecnologías

- 🐍 Python
- 🤖 Android ADB
- ⚡ Fastboot
- 🪟 Windows
- 🔌 Google USB Driver

---

📋 Versión

GrifoADB v1.2

---

📄 Licencia

Este proyecto utiliza la licencia indicada en el archivo ""LICENSE"" (LICENSE).

---

⭐ Proyecto

Si este proyecto te resulta útil, puedes darle una ⭐ al repositorio.

GrifoADB — Android ADB Tool

🐊 Simple · Portable · ADB · Windows
