# IV/UFG Identificação: sistema de identificação visual de candidatos/colaborador

[![git repository](https://github.com/ikatyang/emoji-cheat-sheet/workflows/Up%20to%20Date/badge.svg)](https://github.com/adrielmori/Grupo10-Dominios_de_Software)

## Integrantes:

Adriel Lenner Vinhal Mori</br>
Igor Moreira Pádua
<br>Marcos Vinícius de Moraes</br>
Paulo Roberto Vieira

## Rotina/Guia básico para reprodução do projeto

Para este guia, foi considerando a utilização do ambiente de trabalha no VScode, interpretador a linguagem python através do anaconda e é nesserário uma webCam para input frames na fase de face identify. 

## Ferramentas que você deverá instalar no seu computador:

- Python
- Anaconda

## Python

Recomendado: Python 3.9.13
- Instalar o python
```
conda install python=3.9.13
conda create -n an_env python=3.9.13
```
- Conferir a instalação: 
```
conda list python
```

## Cv2

- Instalar: 
```
conda -c anaconda install opencv-python
```

- Conferir a instalação: 
```
conda list opencv-python
```

## Pillow

Obs.: Pode ocorrer conflito de versão por conta da incopatibilidade das versões de python no interpretador do VScode; listado em ![Fórum StrackOverflow](https://stackoverflow.com/questions/63660023/unable-to-install-pillow-6-2-1-in-conda)

- Instalar Pillow: 
```
sudo apt install openjdk-17-jdk
```

- Verificar a instalação: 
```
conda list pilow
```

## Numpy

- Instalar Numpy: 
```
conda install -c anaconda numpy
```
- Verificar a instalação: 
```
conda list numpy
```
## Cmake

- Instalar com cmake: 
```
conda install -c anaconda cmake
```
- Verificar a instalação: 
```
conda list cmake
```

## dlib

```
conda install -c conda-forge dlib
```

## Face Recognition

```
conda install -c conda-forge face_recognition
```

## VS Code

```
https://code.visualstudio.com/download

sudo snap install code --classic
```

## OBRIGADO!

![Parabéns!](https://raw.githubusercontent.com/devsuperior/bds-assets/main/img/trophy.png)
