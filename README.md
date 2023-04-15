# Cloud PDV

# Point of sale web made with django y python and firebird database

Aplicacion web de punto de venta. 



Versiones de 64 bits en todos los componentes



**Para Windows x64** **Utiliza python 3.10.0**



https://www.python.org/downloads/release/python-3100/

https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

Base de datos Firebird SQL 4.0.2

https://firebirdsql.org/en/firebird-4-0/




```bash
pip install Django==4.1.7
pip install openpyxl==3.1.1
pip install django-bootstrap4==22.3
pip install aiohttp== 3.8.4
pip install mod_wsgi== 4.9.4
pip install fdb==2.0.2
pip install django-firebird==2.2.1
pip install django-utils-six==2.0

```

Puedes crear el archivo de requirementes asi

**requirements.txt**

```bash
Django==4.1.7
openpyxl==3.1.1
django-bootstrap4==22.3
aiohttp== 3.8.4
mod_wsgi== 4.9.4
fdb==2.0.2
django-firebird==2.2.1
django-utils-six==2.0
```

requiere de  

fdb 2.02

https://pypi.org/project/fdb/



django-firebird

https://pypi.org/project/django-firebird/



Modificar el archivo

C:\Python310\Lib\site-packages\django\db\backends\firebird\operations.py
en la linea 14 
de
```bash
from django.utils.encoding import force_bytes, force_text
```
a
```bash
from django.utils.encoding import force_bytes, force_str
```
y en donde se encuentre 

en linea 288 y 290
```bash
force_text
```
por 

```bash
force_str
```
Funciona en windows con apache bajado de https://www.apachelounge.com

https://www.apachelounge.com/download/

httpd-2.4.46-win64-VS16.zip



y en linux ubuntu con nginx



