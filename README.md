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
    sudo pacman -S python3
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
3. Comando para ejecutar el programa que genera la codificacion:
```
python3 lectura_entrada.py grafica1.txt salida.txt
```

- `garfica1.txt`: es un archivo `.txt` que deberá tener el siguiente formato:
    - Primera linea del archivo: número entero positvo K.
    - Segunda línea : lista de vértices del ejemplar. `Ejemplo : [1,2,3]`.
    - Tercera línea : lista de tuplas que sería las aristas. `Ejemplo : [(1,2),(2,3)]`
- por defecto, se tienen en esta carpeta archivos con graficas pre-codificadas guardadas en archivos llamados `grafican.txt`, como `grafica1.txt`, `grafica2.txt`, etc...
- `salida`: nombrar el archivo `.txt` a guardar.

4. Comando para resolver el problema del camino euleriano:

```
python3 lectura_entrada.py grafica1.txt euler1.txt ; python3 euleriano.py euler1.txt
```

Donde todo lo que esta antes del `;` es la llamada a la codificacion anteriormente hecha y lo demas es:

- `euleriano.py` es el archivo donde se resuleve el problema
- `euler1.txt` es donde se guardo la codificacion de la grafica en binario (nesesario para la resolver la ruta euleriana)
