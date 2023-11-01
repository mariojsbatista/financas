# Script para recibos arrendamento do site das finanças português
Permite automatizar criação e download de faturas de arrendamento usando um browser Firefox, Python e o plugin Selenium.

Este script foi executado em Windows com Python 3.10.6 com os seguintes módulos:

Package          Version
- async-generator  1.10
- attrs            22.1.0
- certifi          2022.6.15
- cffi             1.15.1
- cryptography     37.0.4
- h11              0.13.0
- idna             3.3
- outcome          1.2.0
- pip              22.3
- pycparser        2.21
- pyOpenSSL        22.0.0
- PySocks          1.7.1
- python-dateutil  2.8.2
- selenium         4.4.0
- setuptools       63.2.0
- six              1.16.0
- sniffio          1.2.0
- sortedcontainers 2.4.0
- trio             0.21.0
- trio-websocket   0.9.2
- urllib3          1.26.11
- wsproto          1.1.0

Dando como entrada a data do recibo, as senhas de entrada e o nome do imovel no site das Finanças o script gera o recibo e faz download* do recibo.
É necessário que no Firefox esteja permitido o download automático de PDFs.
