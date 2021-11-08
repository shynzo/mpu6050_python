#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Código para leitura Serial do Arduíno baseado no código de eduardo-ssr.

@criador: shynzo
"""

import serial
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from datetime import datetime

def main(port):
    #Inicialização das listas
	acelX = np.array([])
	acelY = np.array([])
	acelZ = np.array([])
	gyroX = np.array([])
	gyroY = np.array([])
	gyroZ = np.array([])
	while True:
		try:
			ser = serial.Serial(serial_ports[int(port)], 115200,timeout=1) #Conectando ao Arduino no serial no baud 115200
			if ser.is_open: #Se estiver aberta, derá início ao programa
				print("Comunicação Serial Estabelecida.\n")
				break
			else: #Se não tiver aberta, tentará novamente
				print("Erro na Comunicação Serial. Tentando novamente...\n")
				sleep(1)
				continue
		except Exception as e: #Se houver alguma exceção, tentará novamente
			print("Erro na Comunicação Serial. \nCausa:{} \nTentando novamente...".format(e))
			sleep(1)
			continue
	sleep(2) #Sincronizar com a reinicialização do Arduino
	while True:    
		print("Escala de leitura:") #Escala de leitura do acelerômetro
		print("0 ----> +- 2g\n")
		print("1 ----> +- 4g\n")
		print("2 ----> +- 8g\n")
		print("3 ----> +- 16g\n")
		print("INFO: A escala padrão da aceleração é de +/- 2g, sendo que g é a força g (equivale a aproximadamente 9,8 m/s²).\n"
		"i.e.: Quanto menor o valor de g, mais sensível será a medição do acelerômetro")
		command = (input("Escolha o intervalo de leitura (Recomendado +-8g):\n> "))
		if command == '0':
			ser.write('0\r'.encode()) #ser.write é para enviar o comando via serial para o Arduino. Caso não esteja devidamente configurado no código .ino, haverá problemas.
			print('Escala definida em +-2g !')
			break
		elif command =='1':
			ser.write('1\r'.encode())
			print('Escala definida em +-4g !')
			break
		elif command == ('2'):
			ser.write('2\r'.encode())
			print('Escala definida em +-8g !')
			break
		elif command == ("3") :
			ser.write('3\r'.encode())
			print('Escala definida em +-16g !')
			break
		else:
			print("Comando inválido, tente outro.\n")
			continue
	sleep(3) #Sincronizar com o Arduino
	print("\nPor padrão, a escala de giroscópio está configurada para +-500°/s cujo é uma sensibilidade média.")
	input("\nVerifique se o LED TX do seu Arduino está pulsando e então pressione 'Enter' para iniciar a leitura e \"Ctrl+C\" para pausar: \n")
	while True:    
		try:
			line = ser.readline().decode("utf-8", errors="ignore") #Leitura do serial
			try:
				entrada = line.split(";") #Separação da string para adquirir os dados
				print("AcX: {}m/s² | AcY: {}m/s² | AcZ: {}m/s² | Gx: {}°/s | Gy: {}°/s | Gz: {}°/s".format(entrada[0], entrada[1], entrada[2], entrada[3], entrada[4], entrada[5]))
				acelX = np.append(acelX, np.float64(entrada[0])) #Adicionando a lista para ser acrescentado no arquivo posteriormente
				acelY = np.append(acelY, np.float64(entrada[1]))
				acelZ = np.append(acelZ, np.float64(entrada[2]))
				gyroX = np.append(gyroX, np.float64(entrada[3]))
				gyroY = np.append(gyroY, np.float64(entrada[4]))
				gyroZ = np.append(gyroZ, np.float64(entrada[5]))
			except Exception as e:
				print(e)
				pass
		except KeyboardInterrupt:
			agora = datetime.strftime(datetime.now(),"%d-%m-%Y_%H%M%S") #Adquirir data e hora correspondente
			arquivo = 'Dados_Brutos_{}.csv'.format(agora) #Formatação do nome do arquivo
			print ("Voce pressionou Ctrl+C para interromper este programa! Seus dados serão salvos na pasta \"Dados\" no arquivo \"{}\"".format(arquivo))
			plt.plot(acelX, "-r", label="Eixo X") #Configurando o eixo X para o gráfico de aceleração
			plt.plot(acelY, "-g", label="Eixo Y") #Configurando o eixo Y para o gráfico de aceleração
			plt.plot(acelZ, "-b", label="Eixo Z") #Configurando o eixo Z para o gráfico de aceleração
			plt.legend()
			plt.xlabel('Tempo (ms)')
			plt.ylabel('Aceleração (m/s²)')
			plt.show() #Plotando o gráfico de aceleração
			plt.plot(gyroX, "-r", label="Eixo X") #Configurando o eixo X para o gráfico de giroscópio
			plt.plot(gyroY, "-g", label="Eixo Y") #Configurando o eixo Y para o gráfico de giroscópio
			plt.plot(gyroZ, "-b", label="Eixo Z") #Configurando o eixo Z para o gráfico de giroscópio
			plt.legend()
			plt.xlabel('Tempo (ms)')
			plt.ylabel('Velocidade Angular (°/s)')
			plt.show() #Plotando o gráfico de giroscópio
			try:
				x = np.vstack((acelX,acelY,acelZ,gyroX,gyroY,gyroZ))
				with open(os.path.join('data', arquivo), "w") as f:
					np.savetxt(f, x.transpose(), delimiter=';', fmt='%1.4f', header='AcX; AcY; AcZ; GyX; GyY; GyZ') #Salvando o arquivo
			except Exception as e:
				print("Ocorreu a seguinte exceção durante o salvamento do arquivo de dados:\n{}".format(e))
			finally:
				break

if __name__ == "__main__":
	os.system('cls')
	print("======= Lista de dispositivos USB =======")
	serial_ports = glob.glob('COM3') #Adquirindo os dispositivos que estão na porta COM3
	while(len(serial_ports)==0): #Enquanto não houver dispositivos na porta COM3, não irá sair deste looping
		print ("Conecte o Arduino...\n")
		sleep(1)
		serial_ports = glob.glob('COM3')
	for i in range(len(serial_ports)): #Printa as opções de dispositivos e captura a seleção do usuário
		print (i, " - ", serial_ports[i])  
		port = input("Escolha a porta do Arduino:\n> ")
	while True:
		main(port) #Iniciará o programa
		reiniciar = input("Deseja reiniciar o programa? (S/N)\n> ")
		if reiniciar.upper() == "S": #Caso reinicie, reiniciará o looping e voltará para o programa principal
			continue
		else:
			print("Obrigado por usar o programa!")
			break
	