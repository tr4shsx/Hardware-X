�
    Z
�d  �                   �   � d dl Z d dlZd dlZd dlmZ d dlmZ d� Zd� Zd� Z	d� Z
d� Zd	� Zd
� Zd� Zedk    r e�   �          dS dS )�    N)�bibliotecas)�pacotesc                  �   � t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         d S )N�[1;33mud  
──▒▒▒▒▒────▄████▄─────
─▒─▄▒─▄▒──███▄█▀──────
─▒▒▒▒▒▒▒─▐████──█──█──
─▒▒▒▒▒▒▒──█████▄──────
─▒─▒─▒─▒───▀████▀─────

H A R D W A R E - Xu1   
[1;32m Versão 3.2.0
 Atualizado em 15 jun 2023z[1;32m Powered by @TR4SHPXDM�[0m)�print� �    �hardware-x.py�exibir_bannerr      s[   � �	�,����	� � � � � 
�
B�C�C�C�	�
,�-�-�-�	�)�����r
   c                  �\  � t          d�  �         t          j        �   �         } t          j        �   �         | z
  dk     r`t          d�  �        D ]6}t          j        d�  �         t          d|dz  dz   � dd	|z  � �d
��  �         �7t          j        �   �         | z
  dk     �`t          d�  �         d S )Nr   �   �
   g�������?z[1;�   �   zm[+] Carregando �.� )�endz)[1;32mCarregamento completo!           )r   �time�range�sleep)�
start_time�is     r   �exibir_animacao_carregamentor      s�   � �	�,��������J�
�)�+�+�
�
"�Q�
&�
&��r��� 	I� 	I�A��J�s�O�O�O��?�a��c�"�f�?�?�c�A�g�?�?�R�H�H�H�H�H� �)�+�+�
�
"�Q�
&�
&� 
�
9�:�:�:�:�:r
   c                  �F  � t          d�  �         t          d�  �         t          D ]N} t          d�  �         t          d| � d��  �         t          j        dd| g�  �         t          d| � d	��  �         �Ot          d�  �         t          d
�  �         t	          �   �          d S )Nr   z![+] Instalando bibliotecas pip...�[1;32mz[+] Instalando z...�pip�installz[1;32m[+] z instalada com sucesso!�![+] Pressione (Enter) para Voltar)r   r   �
subprocess�call�input)�
bibliotecas    r   �instalar_bibliotecas_pipr$   "   s�   � �	�,����	�
-�.�.�.�!� D� D�
��l�����/�
�/�/�/�0�0�0����	�:�6�7�7�7��B�z�B�B�B�C�C�C�C�	�,����	�
-�.�.�.�	�G�G�G�G�Gr
   c                  �  � t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          D ]O} t          d�  �         t          d| � d��  �         t          j        dd	| d
g�  �         t          d| � d��  �         �Pt          d�  �         t          d�  �         t	          �   �          d S )Nz[1;34mz![+] Instalando Pacotes do Sistemaz4
[1;32m____________________________________________�,============================================�[1;31mz[+] Instalando [ zk ]
[1;32m____________________________________________
============================================
[1;33m�pkgr   z-yz[1;34m[+] z instalado com Sucesso !r   )r   r   r    r!   r"   )�pacotes    r   �instalar_pacotes_sistemar*   1   s�   � �	�,����	�
-�.�.�.�	�
D�E�E�E�	�
8�9�9�9�� A� A���l�����  _�&�  _�  _�  _�  	`�  	`�  	`����	�6�4�8�9�9�9��?�v�?�?�?�@�@�@�@�	�,����	�
-�.�.�.�	�G�G�G�G�Gr
   c                  �P  � t          d�  �         t          d�  �         d} t          d�  �         t          d�  �         t          j        d| g�  �         t          d�  �         t          d�  �         t          d�  �         t          j        d	d
g�  �         t          �   �          d S )Nz[1;36mzAtualizando o script...z%https://github.com/tr4shsx/Hardware-Xr'   zBaixando o script atualizado...�wgetz-[1;32mScript atualizado baixado com sucesso!z!Executando o script atualizado...�pythonzhardware-x.py)r   r    r!   �exit)�
url_githubs    r   �atualizar_scriptr0   B   s�   � �	�,����	�
#�$�$�$�8�J�	�,����	�
+�,�,�,��O�V�Z�(�)�)�)�	�
<�=�=�=�	�,����	�
-�.�.�.��O�X��/�0�0�0��F�F�F�F�Fr
   c                  �0  � t          j        t           j        dk    rdnd�  �         t          �   �          t	          d�  �         t	          d�  �         t	          d�  �         t	          d�  �         t	          d�  �         t	          d	�  �         t	          d
�  �         t	          d�  �         t	          d�  �         t	          d�  �         t	          d�  �         t	          d�  �         t	          d�  �         t	          d�  �         t          d�  �         d S )N�posix�clear�clsr   �,____________________________________________r&   r   u   
[+] Informações sobre:
z[1;32m[+] Nome : HARDWARE - Xz[+] Desenvolvido por: TR4SHPXDMu$   [+] Última atualização: 15/6/2023u   [+] Versão: 4.1.1z[+] Linguagem: Python 3.11.4z"[+] Telegram: https://t.me/tr4shswz-============================================
z([1;33m[+] Pressione (Enter) para Voltar)�os�system�namer   r   r"   r	   r
   r   �sobre_o_scriptr9   R   s  � ��I���G�+�+�g�g��7�7�7��O�O�O�	�,����	�
8�9�9�9�	�
8�9�9�9�	�,����	�
(�)�)�)�	�
-�.�.�.�	�
+�,�,�,�	�
0�1�1�1�	�
����	�
(�)�)�)�	�
.�/�/�/�	�,����	�
8�9�9�9�	�
:�;�;�;�	�
7�8�8�8�8�8r
   c                  �   � t          �   �          t          �   �          t          �   �          t          �   �          t	          �   �          d S )N)r   r   r$   r*   r0   r	   r
   r   �mainr;   f   sA   � ��O�O�O� �"�"�"��������������r
   c                  ��  � t          j        t           j        dk    rdnd�  �         t          �   �          t	          �   �          d} | dk    �r�t          j        t           j        dk    rdnd�  �         t          �   �          t          d�  �         t          d�  �         t          d�  �         t          d	�  �         t          d
�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          t          d�  �        �  �        } | dk    rDt          j        t           j        dk    rdnd�  �         t          �   �          t          �   �          �n�| dk    rDt          j        t           j        dk    rdnd�  �         t          �   �          t          �   �          �n>| dk    rCt          j        t           j        dk    rdnd�  �         t          �   �          t          �   �          n�| dk    rCt          j        t           j        dk    rdnd�  �         t          �   �          t          �   �          n�| dk    rqt          j        t           j        dk    rdnd�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          �   �          n5t          j        t           j        dk    rdnd�  �         t          d�  �         | dk    ���t          j        t           j        dk    rdnd�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         t          d�  �         d S )Nr2   r3   r4   �����r   z@[1;33m[+] Termos e acordos
[+] Utilize apenas para fins legais
z3[1;32m____________________________________________z4[1;32m============================================
u)   [1;32m( 1 ) ➜ Instalar bibliotecas pipu%   ( 2 ) ➜ Instalar pacotes do sistemau   ( 3 ) ➜ Atualizaru   ( 4 ) ➜ Sobreu   ( 0 ) ➜ Sairz3[1;32m============================================z[1;33mHardware-X@:~ �   �   �   r   r   zO[+] Obrigado por usar :)
acesse o nosso canal no telegram
https://t.me/Tr4shSw
zScript finalizadou   Créditos: @tr4shpxdmu   [1;31mOpção inválida!r'   r   u   [1;32mCréditos: @tr4shpxdm)r6   r7   r8   r   r   r   �intr"   r$   r*   r0   r9   r.   )�opcaos    r   r;   r;   n   s9  � ��I���G�+�+�g�g��7�7�7��O�O�O� �"�"�"��E�
�1�*�*�
�	�R�W��/�/�'�'�U�;�;�;������U�V�V�V��F�G�G�G��H�I�I�I��<�=�=�=��5�6�6�6��#�$�$�$��� � � �������F�G�G�G��F�G�G�G��E�4�5�5�6�6���A�:�:��I���G�!3�!3�g�g��?�?�?��O�O�O�$�&�&�&�&��a�Z�Z��I���G�!3�!3�g�g��?�?�?��O�O�O�$�&�&�&�&��a�Z�Z��I���G�!3�!3�g�g��?�?�?��O�O�O�������a�Z�Z��I���G�!3�!3�g�g��?�?�?��O�O�O�������a�Z�Z��I���G�!3�!3�g�g��?�?�?��,�����f�g�g�g��%�&�&�&��)�*�*�*��F�F�F�F��I���G�!3�!3�g�g��?�?�?��0�1�1�1�S �1�*�*�V �I���G�+�+�g�g��7�7�7�	�,����	�
����	�)����	�
+�,�,�,�	�)�����r
   �__main__)r6   r    r   r#   r   r)   r   r   r   r$   r*   r0   r9   r;   �__name__r	   r
   r   �<module>rE      s�   �� 	�	�	�	� � � � � ���� "� "� "� "� "� "� � � � � � �� � � ;� ;� ;�� � �� � �"� � � 9� 9� 9�(� � �7� 7� 7�t �z����D�F�F�F�F�F� �r
   