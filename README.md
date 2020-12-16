# Simulador e Montador IJVM

Este artigo tem como objetivo mostrar o desenvolvimento do montador e simulador IJVM, assim como o recebimento dos seus mnemônicos e o equivalente em binário baseado no comportamento da máquina virtual IJVM. Ademais, para cada instrução apresentada indica-se a sua operação em execução, bem como as alterações nos registradores, apresentando seus
valores em cada ciclo e a modificação nos dados da pilha de memória.

Microarquitetura é a forma como um determinado conjunto de instruções (ISA) é implementado em um processador, podendo ser implementado com microarquiteturas diferentes. As implementações podem variar devido a diferentes objetivos de um dado projeto ou a mudanças na tecnologia. A microarquitetura inclui os elementos constitutivos do processador e como estes interligam e interoperam para implementar o ISA. A ISA é aproximadamente o mesmo que o modelo de programação de um processador como visto por um programador de linguagem Assembly ou escritor de compilador. O ISA inclui o modelo de execução, registradores do processador, endereço e formatos de dados, entre outras coisas.

Máquina virtual Java – JVM, é um programa que carrega e executa os aplicativos Java, convertendo os bytecodes em código executável de máquina. A JVM é responsável pelo gerenciamento dos aplicativos, à medida que são executados. Graças à máquina virtual Java, os programas escritos em Java podem funcionar em qualquer plataforma de hardware e software que possua uma versão da JVM, tornando assim essas aplicações independentes da plataforma onde funcionam.

A IJVM desenvolvido por Andrew S. Tanenbaum é um exemplo de microarquitetura, que tem por função implementar o nível ISA. O nível ISA está posicionado logo acima da microarquitetura, e é ele que define como a microarquitetura deve ser construída. A IJVM faz parte da JVM e possui apenas instruções que lidam com inteiros. 

Sabe-se que IJVM é uma arquitetura de conjunto de instruções criada por Andrew Tanenbaum para sua arquitetura MIC-1. Por conseguinte, praticamente todas as linguagens de programação suportam o conceito de procedimentos, que tem variáveis locais, tais variáveis podem ser acessadas dentro dos procedimentos, mas deixam de ser acessíveis assim que o procedimento é devolvido. Dessa forma, é necessário um lugar da memória para manter essas variáveis. Assim, uma área na memória, denominada pilha, é reservada para o armazenamento de variáveis locais de um procedimento. Ademais, temse o conjunto de instrução da IJVM. Dessa forma, a tabela abaixo ilustra tais instruções, nas quais a primeira coluna dá a codificação hexadecimal da instrução, a segunda fornece o mnemônico em linguagem de montagem, enquanto a terceira fornece uma breve descrição do seu efeito.

### 
