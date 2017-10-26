# bpsk-borugo

## O que é BPSK?
A modulação por deslocamento de fase é um esquema de modulação digital onde a fase da portadora é variada de modo a representar os níveis 0 e 1, sendo que, durante a cada intervalo de bit, esta permanece constante. A amplitude e a frequência permanecem sempre inalteradas. Esta modulação também é conhecida como BPSK (Binary Phase Shift Keying). Nela, o símbolo é identificado pela mudança da fase de um sinal senoidal: uma com fase 0, e outra com fase 180 graus. A primeira coisa a ser feita é o estabelecimento de um padrão entre transmissor e receptor, para que a comunicação possa ser efetuada e haja entendimento entre eles.

## Funcionamento Geral do Projeto
O projeto consiste em duas duplas de arquivos, um python e um do GNURadio. Uma dupla tem o papel de transmissor e a outra de receptor. O receptor é responsável por preparar uma conexão via socket para estabelecer a comunicação com o transmissor e receber dados. Já o transmissor é responsável por se conectar com o receptor via socket e enviar dados para ele. Os dados a serem transmitidos e recebidos são palavras que escrevemos numa interface para fazer uma espécie de chat através de som modulado.

## Frequência de Transmissão e Banda ocupada
Utilizamos uma frequncia de corte de 2200 Hz, com uma banda de 4500 Hz

## TX
#### Gráfico no tempo e em frequência do sinal não codificado
![tx_naocodificado](https://i.imgur.com/mom96tB.png)
Esse gráfico mostra o sinal não codificado, ou seja, ele não passou por nenhum tratamento ou modulação para ser transmitido. É a plotagem do áudio puro no tempo e na frequência.

#### Gráfico no tempo e em frequência do sinal codificado (após o constellation modulator)
![tx_codificado](https://i.imgur.com/uCtQtnc.png)
Esse gráfico mostra o sinal codificado. Nota-se a repetição das portadoras no gráfico de frequência e a onda no tempo apenas no domínio real.

#### Gráfico no tempo e em frequência do sinal modulado
![tx_modulado](https://i.imgur.com/Iv3SG8m.png)
Esse gráfico mostra o sinal modulado. Nele, temos a repetição das portadoras tanto no eixo positivo quanto no negativo. Esse sinal é aquele que ser enviado ao outro computador.

#### Diagrama de constelação.
![tx_constellation](https://i.imgur.com/8w49IdK.png)
O diagrama de constelação é a representação visual da modulação ou demodulação do sinal. Nesse caso, como temos um diagrama disperso mas com uma região meio circular no centro, trata-se de um sinal modulado.

## RX
#### Sinal de áudio recebido no tempo e em frequência
![rx_naocodificado](https://i.imgur.com/hb5gOb9.png)
Esse gráfico mostra o sinal modulado recebido pelo outro computador; nota-se que temos várias repetições, dadas pela modulação do áudio original.

#### Sinal de áudio demodulado no tempo e em frequência
![rx_demodulado](https://i.imgur.com/GF3tIkf.png)
Esse gráfico mostra o sinal demodulado filtrado e com um ganho menor do que o original, porém, ainda é possível recuperar informações dele.

#### Diagrama de constelação.
![rx_constellation](https://i.imgur.com/OoonX36.png)
O diagrama de constelação é a representação visual da modulação ou demodulação do sinal. Nesse caso, como temos um diagrama com dois pontos bem definidos, trata-se do sinal demodulado, pois o programa está identificando o símbolo recebido.
