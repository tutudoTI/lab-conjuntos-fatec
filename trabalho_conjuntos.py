# ==========================================
# ATIVIDADE PRÁTICA: TEORIA DOS CONJUNTOS
# Curso: Desenvolvimento de Software Multiplataforma - Fatec Osasco
# Aluno / Equipe: Arthur Prates de Oliveira & Arthur Souza
# ==========================================

# --- PARTE 1: TEORIA DOS CONJUNTOS (MANUAL VS NATIVO) ---

def remover_duplicados(lista):
    """Remove elementos repetidos de uma lista manualmente."""
    lista_limpa = []
    for item in lista:
        if item not in lista_limpa:
            lista_limpa.append(item)
    return lista_limpa

def uniao_manual(A, B):
    """Calcula a união de dois conjuntos usando apenas listas e laços."""
    resultado = list(A)  # Começa com todos os elementos de A
    for item in B:
        if item not in resultado:
            resultado.append(item)
    return resultado

def intersecao_manual(A, B):
    """Calcula a interseção (elementos presentes em A e B)."""
    resultado = []
    for item in A:
        if item in B and item not in resultado:
            resultado.append(item)
    return resultado

def diferenca_manual(A, B):
    """Calcula A - B (elementos que estão em A mas não em B)."""
    resultado = []
    for item in A:
        if item not in B and item not in resultado:
            resultado.append(item)
    return resultado

def diferenca_simetrica_manual(A, B):
    """Calcula a diferença simétrica (ou está em A ou em B, mas não em ambos)."""
    # (A - B) união (B - A)
    dif1 = diferenca_manual(A, B)
    dif2 = diferenca_manual(B, A)
    return uniao_manual(dif1, dif2)

def complemento_manual(A, U):
    """Calcula o complemento de A em relação ao conjunto Universo U."""
    return diferenca_manual(U, A)

def pertinencia(elemento, A):
    """Verifica se o elemento pertence ao conjunto A."""
    return elemento in A

def subconjunto(A, B):
    """Verifica se A é subconjunto de B (A contido em B)."""
    for item in A:
        if item not in B:
            return False
    return True

# --- PARTE 2: CLASSIFICADOR DE NÚMEROS ---

def classificar_numero(entrada):
    """Classifica um número nos conjuntos N, Z, Q, I, R."""
    print(f"\n--- Classificando o número: {entrada} ---")
    
    # Exemplo simples de tratamento para frações (ex: 3/4)
    if "/" in entrada:
        partes = entrada.split("/")
        num = float(partes[0])
        den = float(partes[1])
        val = num / den
        print(f"Tipo detectado: Fração (valor decimal: {val})")
        print("Pertence a: Q, R")
        print("Não pertence a: N, Z, I")
        
    elif "," in entrada or "." in entrada:
        # Simplificação para decimais / dízimas
        print("Tipo detectado: Número Decimal ou Dízima Periódica")
        print("Pertence a: Q, R")
        print("Não pertence a: N, Z, I")
        
    else:
        # Número inteiro
        val = int(entrada)
        if val >= 0:
            print("Pertence a: N, Z, Q, R (Assumindo N inclui o zero)")
        else:
            print("Pertence a: Z, Q, R (Inteiro negativo, não é natural)")

def crivo_eratostenes(n):
    """Gera todos os números primos até n usando o Crivo de Eratóstenes."""
    primos = []
    for num in range(2, n + 1):
        eh_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(num)
    return primos

def listar_divisores(num):
    """Lista todos os divisores inteiros de um número."""
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores


# --- PARTE 3: MINI-PROJETO (RECOMENDAÇÃO POR JACCARD) ---

def indice_jaccard():
    """Calcula a afinidade entre usuários baseado em interesses usando o Índice de Jaccard."""
    print("\n--- Parte 3: Sistema de Recomendação Simples (Índice de Jaccard) ---")
    
    ana = {"rock", "jazz", "cinema", "games"}
    bia = {"jazz", "cinema", "séries", "viagens"}
    caio = {"games", "tecnologia", "cinema"}
    
    def calcular(nome1, set1, nome2, set2):
        intersecao = set1.intersection(set2)
        uniao = set1.union(set2)
        jaccard = len(intersecao) / len(uniao)
        print(f"Par: {nome1} e {nome2}")
        print(f"  - Interseção: {intersecao} (Total: {len(intersecao)})")
        print(f"  - União elementos: {len(uniao)}")
        print(f"  - Índice de Jaccard: {jaccard:.2f}\n")

    calcular("Ana", ana, "Bia", bia)
    calcular("Ana", ana, "Caio", caio)
    calcular("Bia", bia, "Caio", caio)
    print("Conclusão: Para a Ana, o Caio possui maior afinidade (maior índice de Jaccard).")


# --- MENU PRINCIPAL DO PROGRAMA ---

def menu():
    while True:
        print("\n========================================")
        print("   LABORATÓRIO DE CONJUNTOS - FATEC     ")
        print("========================================")
        print("1. Executar Demonstração da Parte 1 (Teoria dos Conjuntos)")
        print("2. Executar Demonstração da Parte 2 (Classificador Numérico)")
        print("3. Executar Demonstração da Parte 3 (Mini-projeto Jaccard)")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\n--- Testando Parte 1 com Exemplo Geral ---")
            A_bruto = [1, 2, 2, 3, 4]
            B_bruto = [3, 4, 5, 6]
            U = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            
            A = remover_duplicados(A_bruto)
            B = remover_duplicados(B_bruto)
            
            print(f"Conjunto A (sem repetição): {A}")
            print(f"Conjunto B (sem repetição): {B}")
            print(f"União Manual: {uniao_manual(A, B)}")
            print(f"Interseção Manual: {intersecao_manual(A, B)}")
            print(f"Diferença A - B Manual: {diferenca_manual(A, B)}")
            print(f"Complemento de A em U: {complemento_manual(A, U)}")
            print(f"3 pertence a A? {pertinencia(3, A)}")
            print(f"Subconjunto [3, 4] em A? {subconjunto([3, 4], A)}")
            
            # Validação com solução nativa do Python (set)
            print("\n[Validação com Python Nativo (set)]")
            set_a = set(A)
            set_b = set(B)
            print(f"União nativa: {set_a.union(set_b)}")
            print(f"Interseção nativa: {set_a.intersection(set_b)}")
            
        elif opcao == "2":
            classificar_numero("7")
            classificar_numero("-3")
            classificar_numero("3/4")
            
            print(f"\nPrimos até 30 (Bônus): {crivo_eratostenes(30)}")
            print(f"Divisores de 36 (Bônus): {listar_divisores(36)}")
            
        elif opcao == "3":
            indice_jaccard()
            
        elif opcao == "0":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
