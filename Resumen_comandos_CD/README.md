# Resumen_Comandos.tex
En este archivo, se usaron dos paquetes de Latex (listings y minted) para implementar código fuente de los diferentes lenguajes de programación que se utilizaron. Para usarlas, primero se debe instalar el shell en Latex instalando Pygments en Python, lo cual se realiza por medio del siguiente código en la cmd: `pip install Pygments`. Luego, instale el siguiente paquete:
`\usepackage{listings}`

Después de la instalación, se debe seguir los siguientes pasos:
1. Seleccionar en Latex Opciones > Configurar TexStudio > Órdenes y cambiar PdfLaTex `pdflatex -synctex=1 -interaction=nonstopmode %.tex`, por `pdflatex -synctex=1 -interaction=nonstopmode --shell-escape %.tex`.
2. Una vez guardados los cambios, se debe seleccionar Compilar y agregar en Órdenes del usuario `user:graphviz-pdflatex`:`txs:///pdflatex/[--shell-escape]`.
3. Finalmente, hacer clic en Herramientas > Usuarios > `1:user:graphviz-pdflatex`.

Con esto, la consola de Latex estará configurada y se podrá insertar código usando listings. Es posible personalizar los colores de los comandos y los bloques de código usando `\lstdefinestyle{<nombre_estilo>}{<personalización>}`. Más información sobre personalización en la página oficial de Latex de [listings](https://www.overleaf.com/learn/latex/Code_listing) y de [colores para las letras en Latex](https://es.overleaf.com/learn/latex/Using_colours_in_LaTeX).

**Importante:** Al escribir código en listing, se debe seleccionar el lenguaje de programación que escribirá en dicho código. En listing se define al inicio del código como ``[language=<lenguaje>]``, o escribir el nombre del estilo con las configuraciones personalizadas.


Un ejemplo de cómo usar este paquete:
```
\begin{lstlisting}[language=SQL]
SELECT columna, COUNT (*)
FROM conj-de-datos.tabla
GROUP BY columnas;
\end{lstlisting}
```

Es importante evitar escribir código con tildes dentro de los bloques listing, puesto que generará errores y no compilará el documento. En el caso del lenguaje R, evitar el uso de doble comillas (") y usar las comillas simples ('').


Más información sobre instalación de shell en Latex: [How to invoke latex with the -shell-escape flag in TeXStudio (former TeXMakerX)?](https://tex.stackexchange.com/questions/99475/how-to-invoke-latex-with-the-shell-escape-flag-in-texstudio-former-texmakerx)
