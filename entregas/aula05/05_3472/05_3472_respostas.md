### Questão 1

Das classes disponibilizadas, basta nos perguntarmos se <classe1> sempre é <classe2> para sabermos se uma classe é herdeira de outra. Por exemplo, uma pizzaria sempre é um restaurante, um gerente sempre é um funcionário e um funcionário sempre é uma pessoa (por enquanto). Mas um funcionário nem sempre é um chefe de cozinha.

Dito isso, podemos organizar nossas classes em três "famílias", onde a classe mais à esquerda é a classe base:

* **Restaurante** -> Pizzaria
* **Pessoa** -> Funcionário -> Garçom, Gerente, Chefe de cozinha
* **Iguaria (comida)** -> Pizza, Bolo

Nesse exemplo todos os atributos das classes mães podem ser herdados, já que todos os atributos são aplicáveis às suas classes herdeiras (um gerente tem idade e uma pizzaria tem endereço, por exemplo). Poderíamos argumentar ainda que uma classe como pizza teria seu atributo nome fixado como "pizza" e um novo atributo sabor poderia ser adicionado. 

---

### Questão 2

Precisamos ter em mente que um restaurante pode possuir várias iguarias e a mesma iguaria pode estar contida em vários restaurantes. Nesse exercício, no entanto a ideia de "item do cardápio" e "comida" se confunde de maneira inapropriada. Basta pensar que dois restaurantes podem vender exatamente a mesma comida por preços diferentes. A mesma pizza (a comida em si) pode ser indistinguível apesar do preço. Portanto é inapropriado que o atributo preço faça parte da classe iguaria, ele é uma consequência da relação iguaria/restaurante. 

Para reforçar, basta fazermos o seguinte exercício. Um restaurante deverá ter um atributo cardápio para sabermos o que ele vende. Dada a estrutura fornecida, o natural é popularmos esse atributo com referências a instâncias da classe iguaria (ex.: instâncias de pizza, onde pizza.borda=True, pizza.nome = pizza de frango, pizza.preco=10.0). Agora se observarmos a classe chefe de cozinha, naturalmente seu método preparar deve receber um "pedido" e retornar uma referência a uma instância de iguaria. Mas isso gera uma contradição no nível de abstração e no nível prático. Primeiro que a informação contida no cardápio e o produto do chefe de cozinha não são a mesma coisa, mas esse modelo os trata como tal. Segundo que o chefe de cozinha retornará uma instância de comida que exige a definição de um atributo preço, mas isso é uma informação que está além das competências do chefe e deveria existir antes do método preparar ser chamado.

A solução natural é que o restaurante possua um atributo cardápio que contém "itens do cardápio" (esse atributo e seu conteúdo podem ser classes em si). Cada item do cardápio deve ter um nome, um atributo de preço e um atributo de "receita" que contém uma referência a uma classe (a classe em si, não a uma instância da mesma, ex.: iguaria, bolo, bebida) e os argumentos a serem usados na criação de uma instância da classe referenciada (o que o chefe de cozinha receberá no seu método preparar, ex.: sabor: frango, borda: False).

Dessa forma a relação entre iguaria e restaurante se dá como sendo um dos possíveis valores de um atributo de uma instância de classe que pertence a um atributo do restaurante.

---

### Questão 3

* **Gerente:** obviamente o argumento dessa função deve ser o funcionário a ser demitido, isto é, uma instância da classe funcionário (ou de alguma subclasse de funcionário). 
    * **TIPO:** funcionário (ou subclasse de funcionário) -- Certamente para isso funcionar, o gerente precisaria da informação do "quadro de funcionários" do restaurante que o emprega, mas essa informação seria mais apropriadamente fornecida na criação da instância gerente (que o associará a um restaurante e, consequentemente ao seu quadro de funcionários), então não precisa pertencer aos argumentos do método.
* **Garçom:** Anotar pedido deve receber um item do cardápio. 
    * **Tipo:** item do cardápio (conforme questão 2). -- informações como modificações no pedido (ex.: cebola=0) poderia ser delegadas a argumentos adicionais e opcionais, então não entram no escopo da pergunta.
* **Chefe de cozinha:** o argumento a ser recebido seria do tipo "receita" (conforme questão 2). Essencialmente é só a parte do item do cardápio relevante ao chefe, que não precisa da informação do preço, por exemplo.