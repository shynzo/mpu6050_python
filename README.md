# Integração Arduino MPU6050 com Python

Este repositório tem como função facilitar a vida de quem precisa capturar os dados do MPU6050 com um programa Python para plotar gráficos e salvar os dados de forma fácil e rápida.

Itens necessários:
- 🖥️ Arduino 🖥️ 
- 🏃‍♂️ Sensor MPU6050 🏃‍♂️
- 🐍 [Python 3] 🐍 

## Funções

- Salvar dados do MPU6050
- Plotar gráfico de Acelerômetro e gráfico de Giroscópio

O programa Arduino foi adaptado de [LastMinuteEngineers] e remodelado para se adequar com o propósito de simplificação de tal integração. Já o programa Python também foi adaptado do código feito pelo [Eduardo Sousa Sales Rodrigues] em sua pesquisa pela UnB, logo, entrego os creditos de criação de ideia ao blog e ao Eduardo.

# Como funciona o sensor?

Seguindo o tutorial de [LastMinuteEngineers], é dado que a medição de acelerômetro é dada em 4 escalas programáveis de **±2g**, **±4g**, **±8g** e **±16g**, sendo **g** a força da gravidade e quanto menor a escala, mais sensíveis serão as leituras do acelerômetro. No site é disponibilizado a indicação de como funciona cada eixo de acelerômetro sendo a seguinte:

![alt text](https://lastminuteengineers.com/wp-content/uploads/arduino/MPU6050-Module-Accelerometer-Axis.jpg)

> Nota: Quando iniciar o programa _"main.py"_ será possível selecionar qual a escala de acelerômetro você deseja usar!

Assim como o acelerômetro, também a rotação é feita por um giroscópio que pode ser programado em 4 escalas de **±250°/s**, **±500°/s**, **±1000°/s** e **±2000°/s**, sendo quanto menor a escala, mais sensíveis serão as leituras do giroscópio. No site é disponibilizado a indicação de como funciona cada eixo de giroscópio sendo a seguinte:

![alt text](https://lastminuteengineers.com/wp-content/uploads/arduino/MPU6050-Module-Gyroscope-Axis.jpg)

> Nota: Já a escala de giroscópio só é possível modificar na linha 52 do arquivo _"Leitura_mpu6050.ino"_ onde basta alterar o valor "500" pelos valores ditos acima.

> Para mais informações, acesse o site [LastMinuteEngineers].

# Instalação
Começamos com o esquema de ligação do MPU6050 com o Arduino:

![alt text](https://lastminuteengineers.com/wp-content/uploads/arduino/Wiring-MPU6050-Accel-Gyro-Module-with-Arduino.png)

Em seguida, conecte o seu Arduino em seu computador e realize a seguinte sequencia de passos:

- Primeiramente abra o arquivo _"Leitura_mpu6050.ino"_ na pasta Arduino.
- Em seu Arduino IDE,  vá em Ferramentas>Gerenciar Bibliotecas.
- Quando carregar a janela do Gerenciador de Bibliotecas, pesquise por "mpu6050" e clique para instalar "Adafruit MPU6050"
![alt text](https://lastminuteengineers.com/wp-content/uploads/arduino/Adafruit-MPU6050-Library-Installation.png)
<<<<<<< Updated upstream
- Ao finalizar a instalação da biblioteca e suas dependências e carregue o código para o seu Arduino!
=======
- Ao finalizar a instalação da biblioteca e suas dependências e carregue o código para o seu Arduino.
>>>>>>> Stashed changes

> Verifique a porta do seu Arduino! Isto é bem importante para o prosseguimento do uso.

Indo agora para o Python, abra o seu prompt de comando dentro da pasta do repositório e rode o seguinte comando:

```sh
pip install -r requirements.txt
```

Ao término da instalação das bibliotecas necessárias para execução do código Python, você já estará com tudo pronto para iniciar!

# Iniciando a Leitura

Abra o arquivo _"main.py"_ na pasta scr/Python. Caso o seu Arduino esteja na porta COM3, poderá prosseguir tranquilamente, caso não, no arquivo _"main.py"_ modifique a linha 123 e 127 correspondente para a porta do seu Arduino.
```python
serial_ports = glob.glob('PORTA DO SEU ARDUINO AQUI!')
```
Conferindo isto, inicie o seu programa e ele te encaminhará daqui para frente. Simples e fácil!


## Licença

GNU v3 2007

**Free Software, Hell Yeah!**

[//]: #
   [LastMinuteEngineers]: <https://lastminuteengineers.com/mpu6050-accel-gyro-arduino-tutorial/>
   [Eduardo Sousa Sales Rodrigues]: <https://bdm.unb.br/bitstream/10483/23639/1/2018_EduardoSousaSalesRodrigues_tcc.pdf>
   [Python 3]: <https://www.python.org/downloads/>
