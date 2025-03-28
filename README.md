# Complejidad-Practica-02
Integrantes del equipo:
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

1. Clonar el repositorio en la carpeta a instalar el programa, con el siguiente comando:
```
git clone https://github.com/kyogre235/Complejidad-Practica-01.git
```
2. Debe de estar ubicado en la siguiente carpeta:
```
~/.../Complejidad-Practica-01
```
3. Comando para crear los certificados a partir de un archivo con la gráfica:
```
python3 genCertificados.py Ejemplar1.txt certificado.txt
```
- `genCertificados.py` : es el archivo donde se genera los certificados.
- `Ejemplar1.txt`: es un archivo `.txt` que deberá tener el siguiente formato:
    - Primera linea del archivo: número entero positvo K.
    - Segunda línea : lista de vértices del ejemplar. `Ejemplo : [1,2,3]`.
    - Tercera línea : lista de tuplas que sería las aristas. `Ejemplo : [(1,2),(2,3)]`
- por defecto, se tienen en esta carpeta archivos con graficas pre-codificadas guardadas en archivos llamados `EjemplarN.txt`, como `Ejemplar1.txt`, `Ejemplar2.txt`, etc...
- `certificado`: nombrar el archivo `.txt` a guardar el certificado.

4. Comando para verficar el certificado cumple con ser una ruta inducida:

```
python3 verificador.py EjemplarN/certificadoN.txt EjemplarN.txt 
```

- `verficador.py` es el archivo donde se resuelve el algoritmo de verificación.
- `EjemplarN/certificadoN.txt` es el archivo donde se encuentra el certificado para el ejemplar1.
- `EjemplarN.txt` es el archivo donde se encuentran los datos de la gráfica.
- en la carpeta `EjemplarN/` se encuentran los certificados pre-codificados para poder probar el ejemplar con el mismo nombre.

por ejemplo, usando el siguiente comando:
```
python3 verificador.py Ejemplar1/certificado1.txt Ejemplar1.txt
```
probamos el primer certificado del ejemplar 1.
