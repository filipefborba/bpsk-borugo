# bpsk-borugo

## O que é BPSK?
A modulação por deslocamento de fase é um esquema de modulação digital onde a fase da portadora é variada de modo a representar os níveis 0 e 1, sendo que, durante a cada intervalo de bit, esta permanece constante. A amplitude e a frequência permanecem sempre inalteradas. Esta modulação também é conhecida como BPSK (Binary Phase Shift Keying). Nela, o símbolo é identificado pela mudança da fase de um sinal senoidal: uma com fase 0, e outra com fase 180 graus. A primeira coisa a ser feita é o estabelecimento de um padrão entre transmissor e receptor, para que a comunicação possa ser efetuada e haja entendimento entre eles.

## Funcionamento Geral do Projeto
O projeto consiste em duas duplas de arquivos, um python e um do GNURadio. Uma dupla tem o papel de transmissor e a outra de receptor. O receptor é responsável por preparar uma conexão via socket para estabelecer a comunicação com o transmissor e receber dados. Já o transmissor é responsável por se conectar com o receptor via socket e enviar dados para ele. Os dados a serem transmitidos e recebidos são palavras que escrevemos numa interface para fazer uma espécie de chat através de som modulado.

## Frequência de Transmissão e Banda ocupada

## TX
#### Gráfico no tempo e em frequência do sinal não codificado
#### Gráfico no tempo e em frequência do sinal codificado (após o constellation modulator)
![tx_codificado](https://i.imgur.com/uCtQtnc.png)
#### Gráfico no tempo e em frequência do sinal modulado
![tx_modulado](https://i.imgur.com/Iv3SG8m.png)
#### Diagrama de constelação.
![tx_constellation](https://i.imgur.com/8w49IdK.png)

## RX
#### Sinal de áudio recebido no tempo e em frequência
![rx_naocodificado](https://i.imgur.com/hb5gOb9.png)
#### Sinal de áudio demodulado no tempo e em frequência
![rx_demodulado](https://i.imgur.com/GF3tIkf.png)
#### Diagrama de constelação.
![rx_constellation](https://i.imgur.com/OoonX36.png)
