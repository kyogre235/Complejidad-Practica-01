# Complejidad-Practica-01
Integrantes del equipo:
- Alvarado Camaho Andrea(318064343)
- Jacome Delgado Alejandro (320011704)
- Jimenez Sanchez Emma Alicia (320046155)
---
## Guía de instalación

#### Dependencias necesarias:
- Python:

    🟢 Ubuntu/Debian
    ```
    sudo apt install python3 -y
    ```

    🔵 Arch Linux/Manjaro
    ```
    sudo pacman -S python
    ```

    🟠 Fedora
    ```
    sudo dnf install python3 -y

1. Copiar el URL del repositorio en la carpeta a instalar el programa, con el siguiente comando:
```
https://github.com/kyogre235/Complejidad-Practica-01.git
```
2. Debe de estar ubicado en la siguiente carpeta:
```
~/.../Complejidad-Practica-01
```
3. Comando para ejecutar el programa copiar el siguiente comando:
```
python lectura_entrada.py archivo_a_leer archivo_a_guardar
```

- `archivo_a_leer`: es un archivo `.txt` que deberá tener el siguiente formato:
    - Primera linea del archivo: número entero positvo K.
    - Segunda línea : lista de vértices del ejemplar. `Ejemplo : [1,2,3]`.
    - Tercera línea : lista de tuplas que sería las aristas. `Ejemplo : [(1,2),(2,3)]`

En este programa asumimos que el ejemplar de entrada es conexo.

- `archivo_a_guardar`: nombrar el archivo `.txt` a guardar. 