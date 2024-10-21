# Estrutura que define um ponto de conversão
class PontoConversao:
    def __init__(self, tensao, temperatura):
        self.tensao = tensao  # Tensão em milivolts
        self.temperatura = temperatura  # Temperatura em graus Celsius

# Função para fazer a interpolação linear
def interpolar(tensao, tabela):
    for i in range(len(tabela) - 1):
        if tabela[i].tensao <= tensao <= tabela[i + 1].tensao:
            v2 = tabela[i + 1].tensao
            v1 = tabela[i].tensao
            t1 = tabela[i].temperatura
            t2 = tabela[i + 1].temperatura

            # Interpolação linear
            return t1 + ((tensao - v1) / (v2 - v1)) * (t2 - t1)

    # Se o valor estiver fora do intervalo da tabela, retorna None
    return None

def main():
    # Tabela de conversão simplificada para um termopar tipo K
    conversao_tabela = [
        PontoConversao(0.000, 0.0),
        PontoConversao(1.000, 25.0),
        PontoConversao(2.000, 50.0),
        PontoConversao(3.000, 75.0),
        PontoConversao(4.000, 100.0),
        PontoConversao(5.000, 125.0),
        PontoConversao(6.000, 150.0),
        PontoConversao(7.000, 175.0),
        PontoConversao(8.000, 200.0),
        PontoConversao(9.000, 225.0),
        PontoConversao(10.000, 250.0)
    ]

    # Entrada de tensão medida
    tensao_medida = float(input("Insira a tensão medida (em mV): "))

    # Conversão da tensão para temperatura
    temperatura = interpolar(tensao_medida, conversao_tabela)

    if temperatura is not None:
        print(f"A temperatura correspondente é: {temperatura:.2f}°C")
    else:
        print("Tensão fora do intervalo da tabela.")

if __name__ == "__main__":
    main()
