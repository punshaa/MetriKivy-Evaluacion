# MetriKivy 📊

Aplicación móvil desarrollada con Kivy para el registro y análisis de métricas de usuario. MetriKivy permite rastrear eventos de interacción (clics) y tiempo de sesión, generando logs detallados para análisis posterior.

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Métricas Implementadas](#-métricas-implementadas)
- [Instalación](#-instalación)
- [Dependencias](#-dependencias)
- [Ejecución](#-ejecución)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Archivos Generados](#-archivos-generados)
- [Contribuciones](#-contribuciones)
- [Enlaces](#-enlaces)
- [Licencia](#-licencia)
- [Historial de Commits](#-historial-de-commits)

## 📱 Descripción

MetriKivy es una aplicación multiplataforma desarrollada con el framework Kivy de Python que permite registrar y analizar métricas de uso de la aplicación. La aplicación está diseñada para funcionar tanto en dispositivos Android como en sistemas de escritorio (Windows, Linux, macOS).

### Funcionalidades Principales

- **Registro de Eventos**: Cuenta y registra cada interacción del usuario (clics en botones)
- **Tiempo de Sesión**: Mide y muestra en tiempo real la duración de cada sesión de uso
- **Sistema de Logging**: Genera archivos de log detallados con todas las métricas registradas
- **Interfaz Intuitiva**: UI simple y clara que muestra las métricas en tiempo real
- **Multiplataforma**: Compatible con Android y sistemas de escritorio

## ✨ Características

- ✅ Registro automático de eventos de usuario
- ✅ Contador de clics en tiempo real
- ✅ Timer de sesión actualizado cada segundo
- ✅ Sistema de logging persistente
- ✅ Compatibilidad multiplataforma (Android/Desktop)
- ✅ Almacenamiento automático de logs según la plataforma

## 📊 Métricas Implementadas

MetriKivy implementa las siguientes métricas:

### 1. **Registro de Eventos (Clics)**
- **Descripción**: Registra cada vez que el usuario presiona el botón de acción
- **Implementación**: Se incrementa un contador y se registra en el log con el total acumulado
- **Formato del Log**: `EVENTO: Botón presionado. Total clics: {número}`

### 2. **Tiempo de Sesión**
- **Descripción**: Mide la duración total de cada sesión de uso de la aplicación
- **Implementación**: 
  - Registra el inicio de sesión al abrir la aplicación
  - Muestra un contador en tiempo real en la interfaz
  - Registra la duración total al cerrar la aplicación
- **Formato del Log**:
  - Inicio: `SESION: Aplicación iniciada`
  - Fin: `SESION: Aplicación cerrada. Duración total: {segundos} segundos`

### 3. **Logging Detallado**
- Todos los eventos se registran con timestamp
- Formato: `YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE`
- Los logs se almacenan en `metrikivy_metrics.log`

## 🚀 Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### Instalación en Sistema de Escritorio

1. **Clonar el repositorio** (o descargar los archivos):
   ```bash
   git clone <url-del-repositorio>
   cd MetriKivy
   ```

2. **Crear un entorno virtual** (recomendado):
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar las dependencias**:
   ```bash
   pip install kivy
   ```

### Instalación para Android

Para compilar la aplicación para Android, necesitarás:

1. **Instalar Buildozer**:
   ```bash
   pip install buildozer
   ```

2. **Configurar el entorno** (en Linux o WSL):
   ```bash
   buildozer android debug
   ```

3. **El APK se generará en** `bin/metrikivy-0.1-arm64-v8a_armeabi-v7a-debug.apk`

### Instalación Directa (APK)

Si ya tienes el APK compilado:

1. Descarga el archivo `metrikivy-0.1-arm64-v8a_armeabi-v7a-debug.apk` desde la carpeta `bin/`
2. Habilita la instalación de aplicaciones desde fuentes desconocidas en tu dispositivo Android
3. Instala el APK directamente en tu dispositivo

## 📦 Dependencias

### Dependencias Principales

- **Python 3.7+**: Lenguaje de programación base
- **Kivy 2.0+**: Framework para desarrollo de aplicaciones multiplataforma
  ```bash
  pip install kivy
  ```

### Dependencias de Desarrollo (para Android)

- **Buildozer**: Herramienta para empaquetar aplicaciones Python para Android
  ```bash
  pip install buildozer
  ```

### Dependencias del Sistema (para Android)

- Android SDK
- Android NDK
- Java JDK
- Cython

> **Nota**: Buildozer descargará automáticamente las dependencias necesarias durante la compilación.

## ▶️ Ejecución

### Ejecución en Sistema de Escritorio

1. **Asegúrate de tener el entorno virtual activado** (si lo estás usando)

2. **Ejecuta la aplicación**:
   ```bash
   python main.py
   ```

3. **La aplicación se abrirá** y podrás:
   - Ver el contador de clics
   - Ver el tiempo de sesión en tiempo real
   - Presionar el botón para registrar eventos

### Ejecución en Android

1. **Instala el APK** en tu dispositivo Android
2. **Abre la aplicación** desde el menú de aplicaciones
3. **Los logs se guardarán** en el almacenamiento interno de la aplicación

### Verificación de Logs

Los logs se generan automáticamente en:
- **Desktop**: `metrikivy_metrics.log` en el directorio del proyecto
- **Android**: `metrikivy_metrics.log` en el almacenamiento interno de la app

Para ver los logs:
```bash
# En desktop
cat metrikivy_metrics.log

# O abrir con un editor de texto
```

## 📁 Estructura del Proyecto

```
MetriKivy/
│
├── main.py                      # Código principal de la aplicación
├── buildozer.spec              # Configuración para compilar APK Android
├── metrikivy_metrics.log       # Archivo de logs generado (se crea al ejecutar)
├── README.md                   # Este archivo
│
├── bin/                        # Directorio con APK compilado
│   └── metrikivy-0.1-arm64-v8a_armeabi-v7a-debug.apk
│
├── screenshots/                # Capturas de pantalla de la aplicación
│   ├── main_screen.png
│   ├── metrics_display.png
│   ├── android_screen.png
│   └── logs_example.png
│
├── documentacion/              # Documentación del proyecto
│   └── MetriKivy_Documentacion.pdf
│
└── kivy_wsl_env/              # Entorno virtual (si se usa WSL)
    └── ...
```

## 📸 Capturas de Pantalla

Las capturas de pantalla de la aplicación se encuentran en la carpeta `screenshots/`. A continuación se muestran las imágenes de la aplicación en funcionamiento:

### Pantalla Principal

<img src="https://github.com/punshaa/MetriKivy-Evaluacion/raw/main/screenshots/main_screen.png" alt="Pantalla Principal" width="600"/>

*Vista inicial de la aplicación mostrando el título, contador de clics y timer de sesión*

### Aplicación en Uso

<img src="https://github.com/punshaa/MetriKivy-Evaluacion/raw/main/screenshots/metrics_display.png" alt="Métricas en Acción" width="600"/>

*Aplicación registrando eventos y mostrando métricas en tiempo real*

### Vista en Android

<img src="https://github.com/punshaa/MetriKivy-Evaluacion/raw/main/screenshots/android_screen.png" alt="Aplicación Android" width="600"/>

*MetriKivy ejecutándose en un dispositivo Android*

### Logs Generados

<img src="https://github.com/punshaa/MetriKivy-Evaluacion/raw/main/screenshots/logs_example.png" alt="Archivo de Logs" width="600"/>

*Ejemplo del archivo de logs generado por la aplicación*


### Descripción de la Interfaz

La interfaz de MetriKivy incluye:
- **Título**: "Métricas de Usuario" en la parte superior
- **Contador de Clics**: Muestra el número total de clics registrados
- **Timer de Sesión**: Muestra el tiempo transcurrido desde el inicio
- **Botón de Acción**: Botón azul para registrar nuevos eventos

## 📄 Archivos Generados

### Archivos de Log

La aplicación genera automáticamente el archivo `metrikivy_metrics.log` que contiene:

- **Formato**: `YYYY-MM-DD HH:MM:SS - LEVEL - MESSAGE`
- **Contenido**:
  - Registro de inicio de sesión
  - Registro de cada evento (clic)
  - Registro de cierre de sesión con duración total
  - Separadores entre sesiones

### Ejemplo de Log

```
2025-11-23 20:01:13,821 - INFO - SESION: Aplicación iniciada
2025-11-23 20:01:15,624 - INFO - EVENTO: Botón presionado. Total clics: 1
2025-11-23 20:01:16,003 - INFO - EVENTO: Botón presionado. Total clics: 2
2025-11-23 20:01:22,710 - INFO - SESION: Aplicación cerrada. Duración total: 8.89 segundos
2025-11-23 20:01:22,710 - INFO - ------------------------------
```

### APK

El archivo APK compilado se encuentra en:
- **Ubicación**: `bin/metrikivy-0.1-arm64-v8a_armeabi-v7a-debug.apk`
- **Arquitecturas soportadas**: arm64-v8a, armeabi-v7a
- **Versión**: 0.1 (debug)

### Documentación PDF

El proyecto incluye un archivo PDF con documentación completa que contiene:
- **Descripción detallada del proyecto**: Objetivos, alcance y propósito
- **Arquitectura y diseño**: Estructura de la aplicación y decisiones de diseño
- **Especificaciones técnicas**: Requisitos, dependencias y configuración
- **Guía de uso**: Instrucciones paso a paso para usuarios
- **Diagramas y esquemas**: Visualizaciones de la arquitectura y flujo de datos
- **Análisis de métricas**: Explicación detallada de las métricas implementadas

📄 **Acceso al PDF**: [`documentacion/MetriKivy_Documentacion.pdf`](documentacion/MetriKivy_Documentacion.pdf)

> ✅ **El archivo PDF está disponible** en la carpeta `documentacion/` del repositorio.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir al proyecto:

1. **Fork el repositorio**
2. **Crea una rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. **Commit tus cambios** (`git commit -m 'Add some AmazingFeature'`)
4. **Push a la rama** (`git push origin feature/AmazingFeature`)
5. **Abre un Pull Request**

### Guías de Contribución

- Mantén el código limpio y bien documentado
- Sigue las convenciones de estilo de Python (PEP 8)
- Agrega comentarios explicativos cuando sea necesario
- Prueba tus cambios antes de hacer commit

### Áreas de Mejora

- [ ] Agregar más tipos de métricas (tiempo entre clics, frecuencia, etc.)
- [ ] Implementar visualización gráfica de métricas
- [ ] Exportar métricas a formatos CSV/JSON
- [ ] Agregar configuración de usuario
- [ ] Mejorar la interfaz gráfica
- [ ] Agregar estadísticas históricas

## 🔗 Enlaces

### Documentación del Proyecto

- **PDF Explicativo**: Ver el archivo PDF incluido en el repositorio para documentación detallada del proyecto, arquitectura, diseño y especificaciones técnicas.
  - **Ubicación**: [`documentacion/MetriKivy_Documentacion.pdf`](documentacion/MetriKivy_Documentacion.pdf)
  - **Contenido**: Explicación completa del proyecto, requisitos, diseño de la aplicación y guía de uso

### Documentación Técnica

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Python for Android](https://python-for-android.readthedocs.io/)

### Recursos Útiles

- [Kivy GitHub](https://github.com/kivy/kivy)
- [Python Official Site](https://www.python.org/)
- [Android Developer Guide](https://developer.android.com/)

### Repositorio

- **Repositorio**: [GitHub - MetriKivy](https://github.com/usuario/metrikivy) *(actualizar con la URL real)*

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

```
MIT License

Copyright (c) 2025 Camila Yarella Aceitón

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📜 Historial de Commits

### Commit Principal

```
26d5ee4 - Camila Yarella Aceitón, 24 hours ago : Entrega Final: APK y Codigo
```

Este commit incluye:
- ✅ Código fuente completo de la aplicación
- ✅ Archivo de configuración Buildozer
- ✅ APK compilado para Android
- ✅ Sistema de logging implementado
- ✅ Métricas de usuario funcionales

### Detalles del Proyecto

- **Autor**: Camila Yarella Aceitón
- **Versión**: 0.1
- **Última actualización**: Noviembre 2025
- **Estado**: Funcional - Listo para uso

---

## 📧 Contacto

Para preguntas, sugerencias o reportes de bugs, por favor abre un issue en el repositorio o contacta al desarrollador.

---

**Desarrollado con ❤️ usando Kivy y Python**

