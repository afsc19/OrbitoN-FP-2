# Projeto 2 FP 2024/2025
# Criado por André Cadete
# Aluno 114254 - ist1114254
# email: andre.cadete@tecnico.ulisboa.pt


def cria_posicao(col, lin):
    """
    cria_posicao: str × int → posicao

    Recebe um carácter correspondente uma coluna
    e um inteiro correspondente uma linha.

    Devolve a posição correspondente à coluna e linha especificadas.

    Caso os argumentos sejam inválidos, gera um erro.
    """
    if not (eh_coluna(col) and eh_linha(lin)):
        raise ValueError("cria_posicao: argumentos invalidos")
    # Representação interna: tuplo
    return (col, lin)


# Função Auxiliar
def eh_coluna(arg):
    """
    eh_coluna: arg → booleano

    Recebe um argumento e devolve True se o argumento corresponder
    a uma coluna possível de um tabuleiro com 2 <= n <= 5.
    """
    return isinstance(arg, str) and len(arg) == 1 and 'a' <= arg <= 'j'


# Função Auxiliar
def eh_linha(arg):
    """
    eh_linha: arg → booleano

    Recebe um argumento.

    Devolve True se o argumento corresponder a uma
    linha possível de um tabuleiro com 2 <= n <= 5.
    """
    return type(arg) == int and 1 <= arg <= 10


# Função Auxiliar
def eh_n(arg):
    """
    eh_n: universal → booleano

    Recebe um argumento.

    Devolve True se o argumento recebido for um n do jogo Orbito-n.
    Caso contrário, devolve False.
    """
    return type(arg) == int and 2 <= arg <= 5


def obtem_pos_col(p):
    """
    obtem_pos_col: posicao → str

    Recebe uma posição.

    Devolve a sua coluna.
    """
    return p[0]


def obtem_pos_lin(p):
    """
    obtem_pos_lin: posicao → int

    Recebe uma posição.

    Devolve a sua linha.
    """
    return p[1]


def eh_posicao(arg):
    """
    eh_posicao: universal → booleano

    Recebe um argumento.

    Devolve True se o argumento corresponder a uma posição (TAD).
    Caso contrário, devolve False.
    """
    return (isinstance(arg, tuple) and len(arg) == 2
            and eh_coluna(obtem_pos_col(arg))
            and eh_linha(obtem_pos_lin(arg)))


def posicoes_iguais(p1, p2):
    """
    posicoes_iguais: posicao × posicao → booleano

    Recebe dois argumentos.

    Devolve True se os argumentos forem posições e iguais
    (se tiverem a mesma linha e coluna).
    Caso contrário, devolve False.
    """
    return (eh_posicao(p1) and eh_posicao(p2)
            and obtem_pos_col(p1) == obtem_pos_col(p2)
            and obtem_pos_lin(p1) == obtem_pos_lin(p2))


def posicao_para_str(p):
    """
    posicao_para_str: posicao → str

    Recebe uma posição.

    Devolve a cadeia de caracteres que representa o seu argumento.
    """
    return obtem_pos_col(p) + str(obtem_pos_lin(p))


def str_para_posicao(s):
    """
    str_para_posicao: str → posicao

    Recebe uma cadeia de caracteres.

    Devolve a posição representada pela mesma.
    """
    return cria_posicao(s[0], int(s[1:]))


def eh_posicao_valida(p, n):
    """
    eh_posicao_valida: posicao × inteiro → booleano

    Recebe uma posição e um inteiro n que representa o nº de orbitais.

    Devolve True se p é uma posição válida dentro do tabuleiro de Orbito-n com n orbitais.
    Caso contrário, devolve False.
    """
    return (eh_posicao(p) and eh_n(n)
            and ord('a') <= ord(obtem_pos_col(p)) < ord('a') + n * 2
            and 1 <= obtem_pos_lin(p) <= n * 2)


def obtem_posicoes_adjacentes(p, n, d):
    """
    obtem_posicoes_adjacentes: posicao × inteiro × booleano → tuplo

    Recebe uma posição, um inteiro n que representa o nº de orbitais
    e um booleano d.

    Se d for True, a função devolve um tuplo com as posições do tabuleiro Orbito-n
    adjacentes à posição p (horizontal, vertical e diagonalmente).
    Caso contrário, devolve as posições adjacentes ortogonais.
    """
    lin, col = obtem_pos_lin(p), obtem_pos_col(p)
    adjacentes = []
    # Deslocamentos das posições adjacentes.
    if d:
        deslocamentos = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                         (1, 0), (1, -1), (0, -1), (-1, -1)]
    else:
        deslocamentos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for d_lin, d_col in deslocamentos:
        nova_lin = lin + d_lin
        nova_col = chr(ord(col) + d_col)

        if eh_coluna(nova_col) and eh_linha(nova_lin):
            p_adj = cria_posicao(nova_col, nova_lin)
            if eh_posicao_valida(p_adj, n):
                adjacentes.append(p_adj)
    return tuple(adjacentes)


def ordena_posicoes(t, n):
    """
    ordena_posicoes: tuplo × inteiro → tuplo

    Recebe um tuplo com posições e um inteiro n que representa o nº de orbitais.

    Devolve um tuplo com as posições do tuplo recebido,
    ordenado conforme a ordem de leitura do tabuleiro de Orbito-n.
    """
    return sorted(t, key=lambda p: (obtem_orbita(p, n), obtem_pos_lin(p), obtem_pos_col(p)))


# Função Auxiliar
def obtem_orbita(p, n):
    """
    obtem_orbita: posicao → int

    Recebe uma posição.

    Devolve um inteiro que representa a orbital onde a posição recebida está contida.
    """
    centro = n + 0.5  # Centro fictício.
    distancia_horizontal = abs(obtem_pos_lin(p) - centro)
    i_col = ord(obtem_pos_col(p)) - (ord('a') - 1)
    distancia_vertical = abs(i_col - centro)

    # A maior distância + 0.5 dará sempre a órbita.
    return int(max(distancia_vertical, distancia_horizontal) + 0.5)


def cria_pedra_branca():
    """
    cria_pedra_branca: {} → pedra

    Devolve uma pedra pertencente ao jogador branco.
    """
    return -1


def cria_pedra_preta():
    """
    cria_pedra_preta: {} → pedra

    Devolve uma pedra pertencente ao jogador preto.
    """
    return 1


def cria_pedra_neutra():
    """
    cria_pedra_neutra: {} → pedra

    Devolve uma pedra neutra.
    """
    return 0


def eh_pedra(arg):
    """
    eh_pedra: universal → booleano

    Recebe um argumento.

    Devolve True se o argumento corresponder a um TAD pedra.
    Caso contrário, devolve False.
    """
    return (type(arg) == int and arg in (-1, 0, 1))


def eh_pedra_branca(p):
    """
    eh_pedra_branca: pedra → booleano

    Recebe uma pedra.

    Devolve true se a pedra recebida for do jogador branco.
    Caso contrário, devolve False.
    """
    return p == cria_pedra_branca()


def eh_pedra_preta(p):
    """
    eh_pedra_preta: pedra → booleano

    Recebe uma pedra.

    Devolve true se a pedra recebida for do jogador preto.
    Caso contrário, devolve False.
    """
    return p == cria_pedra_preta()


def pedras_iguais(p1, p2):
    """
    pedras_iguais: universal × universal → booleano

    Recebe duas pedras.

    Devolve True se as pedras forem iguais.
    Caso contrário, devolve false.
    """
    return eh_pedra(p1) and eh_pedra(p2) and p1 == p2


def pedra_para_str(p):
    """
    pedra_para_str: pedra → str

    Recebe uma pedra.

    Devolve a cadeia de caracteres que representa o jogador dono da pedra.
    Isto é, devolverá 'O', 'X' ou ' ', para as pedras
    do jogador branco, preto ou neutra respetivamente.
    """
    if eh_pedra_branca(p):
        return 'O'
    elif eh_pedra_preta(p):
        return 'X'
    else:
        return ' '


def eh_pedra_jogador(p):
    """
    eh_pedra_jogador: pedra → booleano

    Recebe uma pedra.

    Devolve True se a pedra recebida seja de um jogador.
    Caso contrário, devolve False.
    """
    return eh_pedra_preta(p) or eh_pedra_branca(p)


def pedra_para_int(p):
    """
    pedra_para_int: pedra → int

    Recebe uma pedra.

    Devolve um inteiro 1, -1 ou 0, dependendo se a pedra
    é do jogador preto, branco ou neutra, respetivamente.
    """
    if eh_pedra_branca(p):
        return -1
    elif eh_pedra_preta(p):
        return 1
    else:
        return 0


def cria_tabuleiro_vazio(n):
    """
    cria_tabuleiro_vazio: int → tabuleiro

    Recebe um inteiro n que representa o nº de orbitais.

    Devolve um TAD tabuleiro de Orbito com n órbitas, sem posições ocupadas.

    Caso os argumentos sejam inválidos, gera um erro.
    """
    if not eh_n(n):
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")

    return [[cria_pedra_neutra() for i_col in range(n * 2)] for lin in range(n * 2)]


# Função auxiliar
def col_para_indice(col):
    """
    col_para_indice: str → int

    Recebe um caracter que representa uma coluna do tabuleiro.

    Devolve um inteiro que corresponde ao índice da coluna recebida.
    """
    return ord(col) - ord('a')


# Função auxiliar
def indice_para_col(i_col):
    """
    indice_para_col: int → str

    Recebe um inteiro que representa o índice duma coluna do tabuleiro.

    Devolve um caracter que corresponde à coluna do índice recebido.
    """
    return chr(ord('a') + i_col)


def cria_tabuleiro(n, tp, tb):
    """
    cria_tabuleiro: int × tuplo × tuplo → tabuleiro

    Recebe um inteiro n que representa o nº de orbitais.

    Devolve um TAD tabuleiro de Orbito com n órbitas,
    com as posições do tuplo tp e tb ocupadas por posições de pedras pretas e brancas, respetivamente.

    Caso os argumentos sejam inválidos, gera um erro.
    """
    if not (eh_n(n) and isinstance(tp, tuple) and isinstance(tb, tuple)):
        raise ValueError("cria_tabuleiro: argumentos invalidos")
    tabuleiro = cria_tabuleiro_vazio(n)
    # Percorre cada tuplo para verificar e colocar a pedra respetiva na posição
    for tup, pedra in ((tb, cria_pedra_branca()), (tp, cria_pedra_preta())):
        for pos in tup:
            # Verifica se cada posição é válida e se não é repetida.
            if not eh_posicao_valida(pos, n) or eh_pedra_jogador(obtem_pedra(tabuleiro, pos)):
                raise ValueError("cria_tabuleiro: argumentos invalidos")
            coloca_pedra(tabuleiro, pos, pedra)
    return tabuleiro


def cria_copia_tabuleiro(t):
    """
    cria_copia_tabuleiro: tabuleiro → tabuleiro

    Recebe um tabuleiro.

    Devolve uma cópia do tabuleiro recebido.
    """
    return [linha.copy() for linha in t]


def obtem_numero_orbitas(t):
    """
    obtem_numero_orbitas: tabuleiro → int

    Recebe um tabuleiro.

    Devolve o número de órbitas do tabuleiro recebido.
    """
    return len(t) // 2


def obtem_pedra(t, p):
    """
    obtem_pedra: tabuleiro × posicao → pedra

    Recebe um tabuleiro e uma posição desse tabuleiro.

    Devolve a pedra na posição p do tabuleiro t.
    Se a posição não estiver ocupada, devolve uma pedra neutra.
    """
    i_lin = obtem_pos_lin(p) - 1
    i_col = col_para_indice(obtem_pos_col(p))
    return t[i_lin][i_col]


def obtem_linha_horizontal(t, p):
    """
    obtem_linha_horizontal: tabuleiro × posicao → tuplo

    Recebe um tabuleiro e uma posição.

    Devolve um tuplo formado por tuplos de dois elementos correspondentes à posição
    e o valor de todas as posições da linha horizontal pela posição p,
    ordenadas da esquerda para a direita.
    """
    n = obtem_numero_orbitas(t)
    lin = obtem_pos_lin(p)
    # Percorre o índice da coluna.
    return tuple((cria_posicao(indice_para_col(i_col), lin), t[lin - 1][i_col])
                 for i_col in range(n * 2))


def obtem_linha_vertical(t, p):
    """
    obtem_linha_vertical: tabuleiro × posicao → tuplo

    Recebe um tabuleiro e uma posição.

    Devolve um tuplo formado por tuplos de dois elementos correspondentes à posição
    e o valor de todas as posições da linha horizontal pela posição p,
    ordenadas da esquerda para a direita.
    """
    n = obtem_numero_orbitas(t)
    col = obtem_pos_col(p)
    i_col = col_para_indice(col)
    # Percorre o índice da linha.
    return tuple((cria_posicao(col, i_lin + 1), t[i_lin][i_col])
                 for i_lin in range(n * 2))


def obtem_linhas_diagonais(t, p):
    """
    obtem_linhas_diagonais: tabuleiro × posicao → tuplo × tuplo

    Recebe um tabuleiro e uma posição desse tabuleiro.

    Devolve dois tuplos formados cada um deles por tuplos de dois elementos
    correspondentes à posição e o valor de todas as posições que formam
    a diagonal e a antidiagonal, que passam pela posição p, respetivamente.
    """
    n = obtem_numero_orbitas(t)
    # Calcula a linha e o índice da coluna da posição recebida.
    i_lin = obtem_pos_lin(p) - 1
    i_col = col_para_indice(obtem_pos_col(p))

    diagonais = [[], []]
    # O sinal é +1 para a diagonal e -1 para a antidiagonal
    for sinal in (-1, +1):
        if sinal == +1:
            # Calcula os índices da primeira posição da diagonal.
            if i_lin >= i_col:
                i_col_d, i_lin_d = 0, i_lin - i_col
            else:
                i_lin_d, i_col_d = 0, i_col - i_lin
        else:
            # Calcula os índices da primeira posição da antidiagonal.
            if (n * 2 - 1) - i_lin >= i_col:
                i_col_d, i_lin_d = 0, i_lin + i_col
            else:
                i_lin_d, i_col_d = n * 2 - 1, i_col - (n * 2 - 1 - i_lin)

        # Enquanto estiver dentro dos limites do tabuleiro.
        while 0 <= i_col_d < n * 2 and 0 <= i_lin_d < n * 2:
            p = cria_posicao(indice_para_col(i_col_d), i_lin_d + 1)
            diagonais[0 if sinal == -1 else 1].append((p, obtem_pedra(t, p)))
            i_col_d += 1
            i_lin_d += 1 * sinal

    return (tuple(diagonais[1]), tuple(diagonais[0]))


# Função Auxiliar
def obtem_todas_posicoes(n):
    """
    obtem_todas_posicoes: inteiro → tuplo

    Recebe um inteiro n.

    Devolve um tuplo formado por todas as posições do tabuleiro.
    """
    return [cria_posicao(indice_para_col(i_col), i_lin + 1)
            for i_col in range(n * 2)
            for i_lin in range(n * 2)]


def obtem_posicoes_pedra(t, j):
    """
    obtem_posicoes_pedra: tabuleiro × pedra → tuplo

    Recebe um tabuleiro e uma pedra.

    Devolve o tuplo formado por todas as posições do tabuleiro
    ocupadas por pedras j (brancas, pretas ou neutras),
    ordenadas em ordem de leitura do tabuleiro.
    """
    n = obtem_numero_orbitas(t)
    todas_posicoes = obtem_todas_posicoes(n)
    # Filtra as posições com pedras iguais e ordena esse tuplo.
    return ordena_posicoes(tuple(filter(lambda x: pedras_iguais(obtem_pedra(t, x), j), todas_posicoes)), n)


def coloca_pedra(t, p, j):
    """
    coloca_pedra: tabuleiro × posicao × pedra → tabuleiro

    Recebe um tabuleiro, uma posição do tabuleiro e uma pedra.

    Modifica destrutivamente o tabuleiro t colocando a pedra j na posição p.

    Devolve o próprio tabuleiro.
    """
    i_lin = obtem_pos_lin(p) - 1
    i_col = col_para_indice(obtem_pos_col(p))
    t[i_lin][i_col] = j
    return t


def remove_pedra(t, p):
    """
    remove_pedra: tabuleiro × posicao → tabuleiro

    Recebe um tabuleiro e uma posicao do tabuleiro.

    Modifica destrutivamente o tabuleiro t removendo a pedra da posição p.

    Devolve o próprio tabuleiro.
    """
    i_lin = obtem_pos_lin(p) - 1
    i_col = col_para_indice(obtem_pos_col(p))
    t[i_lin][i_col] = cria_pedra_neutra()
    return t


def eh_tabuleiro(arg):
    """
    eh_tabuleiro: universal → booleano

    Recebe um argumento.

    Devolve True se o argumento for um TAD tabuleiro.
    Caso contrário, devolve False.
    """
    if not isinstance(arg, list):
        return False
    n_linhas = len(arg)
    # Nº de linhas tem de ser múltiplo de dois (n*2).
    if not (4 <= n_linhas <= 10 and n_linhas % 2 == 0):
        return False
    for linha in arg:
        # O filter é utilizado para verificar se todas as colunas contêm pedras válidas.
        if not (isinstance(linha, list) and len(linha) == n_linhas) \
                or tuple(filter(lambda x: not eh_pedra(x), linha)):
            return False
    return True


def tabuleiros_iguais(t1, t2):
    """
    tabuleiros_iguais: universal × universal → booleano

    Recebe dois argumentos.

    Devolve True se t1 e t2 forem tabuleiros e forem iguais.
    Caso contrário, devolve False.
    """
    if not (eh_tabuleiro(t1) and eh_tabuleiro(t2)
            and obtem_numero_orbitas(t1) == obtem_numero_orbitas(t2)):  # Verifica também se as órbitas são iguais.
        return False
    branca, preta, neutra = cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra()
    return obtem_posicoes_pedra(t1, branca) == obtem_posicoes_pedra(t2, branca) \
        and obtem_posicoes_pedra(t1, preta) == obtem_posicoes_pedra(t2, preta) \
        and obtem_posicoes_pedra(t1, neutra) == obtem_posicoes_pedra(t2, neutra)


def tabuleiro_para_str(t):
    """
    tabuleiro_para_str: tabuleiro → str

    Recebe um tabuleiro.

    Devolve a cadeia de caracteres que representa o tabuleiro.
    """
    n = obtem_numero_orbitas(t)
    # O split com um for serve para adicionar as colunas dependendo do n.
    texto = (" " +
             ''.join("   " + chr(ord('a') + i_col)
                     for i_col in range(n * 2))
             + '\n')

    for i_lin in range(n * 2):
        lin = i_lin + 1
        # Formatação com dois dígitos
        texto += f"{lin:02} "
        for i_col in range(n * 2):
            # Separador entre colunas
            if texto[-1] != ' ':
                texto += '-'
            # Pedra entre []
            p = pedra_para_str(obtem_pedra(t, cria_posicao(indice_para_col(i_col), lin)))
            texto += f"[{p}]"
        # Separador entre linhas
        if lin < n * 2:
            texto += '\n ' + '   |' * n * 2 + '\n'
    return texto


def move_pedra(t, p1, p2):
    """
    move_pedra: tabuleiro × posicao × posicao → tabuleiro

    Recebe um tabuleiro e duas posições.

    Modifica destrutivamente o tabuleiro t movendo a pedra
    da posição p1 para a posição p2.

    Devolve o próprio tabuleiro.
    """
    t = coloca_pedra(t, p2, obtem_pedra(t, p1))
    t = coloca_pedra(t, p1, cria_pedra_neutra())
    return t


def obtem_posicao_seguinte(t, p, s):
    """
    obtem_posicao_seguinte: tabuleiro × posicao × booleano → posicao

    Recebe um tabuleiro, uma posição e um booleano
    que corresponde ao sentido de rotação do tabuleiro.

    Devolve a posição da mesma órbita que p se encontra a seguir no tabuleiro t
    em sentido horário se s for True ou anti-horário se for False.
    """
    n = obtem_numero_orbitas(t)
    orbita = obtem_orbita(p, n)
    i_lin, i_col = obtem_pos_lin(p) - 1, col_para_indice(obtem_pos_col(p))
    # Calcula o índice da primeira coluna/linha da órbita.
    i1 = n - orbita

    # Prepara as duas posições adjacentes da mesma órbita numa lista.
    possiveis = [adj
                 for adj in obtem_posicoes_adjacentes(p, n, False)
                 if obtem_orbita(adj, n) == orbita]

    # A posição da lista dependerá se a posição está na primeira coluna/linha da órbita,
    # bem como dependerá do sentido.
    if i_lin == i1 or i_col == i1:
        return possiveis[0] if s else possiveis[1]
    else:
        return possiveis[1] if s else possiveis[0]


def roda_tabuleiro(t):
    """
    roda_tabuleiro: tabuleiro → tabuleiro

    Recebe um tabuleiro.

    Modifica destrutivamente o tabuleiro t rodando todas
    as pedras uma posição em sentido anti-horário.

    Devolve o próprio tabuleiro.
    """
    tab_antigo = cria_copia_tabuleiro(t)
    for pos in obtem_todas_posicoes(obtem_numero_orbitas(t)):
        coloca_pedra(t, obtem_posicao_seguinte(t, pos, False), obtem_pedra(tab_antigo, pos))
    return t


def verifica_linha_pedras(t, p, j, k):
    """
    verifica_linha_pedras: tabuleiro × posicao × pedra × int → booleano

    Recebe um tabuleiro, uma posição do tabuleiro, uma pedra e um inteiro k.

    Devolve True se existe pelo menos uma linha (horizontal, vertical ou diagonal)
    que contenha a posição p com k ou mais pedras consecutivas do jogador com pedras j.
    Caso contrário, devolve False.
    """

    linhas = [obtem_linha_vertical(t, p), obtem_linha_horizontal(t, p)]
    linhas.extend(obtem_linhas_diagonais(t, p))

    # Percorre todas as linhas anteriormente guardadas.
    for linha in linhas:
        # É escusado verificar linhas (as diagonais) que não tenham pelo menos k pedras.
        if len(linha) < k:
            continue
        cont = 0
        p_contabilizada = False
        for pos, pedra in linha:
            if posicoes_iguais(p, pos):
                p_contabilizada = True
            if pedras_iguais(pedra, j):
                cont += 1
            else:
                cont = 0
                if p_contabilizada:
                    # Desnecessário verificar o resto da linha.
                    break
            if cont >= k and p_contabilizada:
                return True
    return False


def eh_vencedor(t, j):
    """
    eh_vencedor: tabuleiro × pedra → booleano

    Recebe um tabuleiro e uma pedra de jogador.

    Devolve True se existe uma linha completa
    do tabuleiro de pedras do jogador.
    Caso contrário, devolve False.
    """
    n = obtem_numero_orbitas(t)

    # Verifica se existem n*2 pedras seguidas do jogador
    for pos in obtem_posicoes_pedra(t, j):
        if verifica_linha_pedras(t, pos, j, n * 2):
            return True
    return False


def eh_fim_jogo(t):
    """
    eh_fim_jogo: tabuleiro → booleano

    Recebe um tabuleiro.

    Devolve True se o jogo já terminou.
    Caso contrário, devolve False.
    """
    livres = obtem_posicoes_pedra(t, cria_pedra_neutra())
    return not livres or eh_vencedor(t, cria_pedra_preta()) or eh_vencedor(t, cria_pedra_branca())


def escolhe_movimento_manual(t):
    """
    escolhe_movimento_manual: tabuleiro → posicao

    Recebe um tabuleiro t.

    Permite escolher uma posição livre do tabuleiro onde colocar uma pedra.
    A função não modifica o tabuleiro t.

    Devolve a posição escolhida.
    """
    n = obtem_numero_orbitas(t)
    pos = None
    # While => Pede ao utilizador uma posição até esta ser válida.
    while not (eh_posicao_valida(pos, n) and not eh_pedra_jogador(obtem_pedra(t, pos))):
        texto = input("Escolha uma posicao livre:")
        # Verifica se o texto inserido é composto por uma letra e um inteiro até 10.
        if (((len(texto) > 2 and texto[1:] == '10') or (len(texto) == 2))
                and texto[0].isalpha() and texto[1:].isdigit()):
            col = texto[0]
            lin = int(texto[1:])
            if eh_coluna(col) and eh_linha(lin):
                # Posição que vai ser verificada na condição do while.
                pos = cria_posicao(texto[0], int(texto[1:]))
    return pos


def escolhe_movimento_auto(t, j, lvl):
    """
    escolhe_movimento_auto: tabuleiro × pedra × str → posicao

    Recebe um tabuleiro t (em que o jogo não terminou ainda),
    uma pedra j, e a cadeia de carateres lvl correspondente à estratégia.
    As estratégias podem ser: 'facil' ou 'normal'.

    Devolve a posição escolhida automaticamente conforme a estratégia
    selecionada para o jogador com pedras j.
    A função não modifica nenhum dos seus argumentos.
    """
    n = obtem_numero_orbitas(t)
    apos_rotacao = roda_tabuleiro(cria_copia_tabuleiro(t))
    adv = cria_pedra_preta() if eh_pedra_branca(j) else cria_pedra_branca()
    if lvl == 'facil':
        livres = obtem_posicoes_pedra(t, cria_pedra_neutra())
        for livre in livres:
            livre_rodada = obtem_posicao_seguinte(t, livre, False)
            for adj in obtem_posicoes_adjacentes(livre_rodada, n, True):
                if pedras_iguais(obtem_pedra(apos_rotacao, adj), j):
                    # Como a lista já foi ordenada, basta devolver o primeiro.
                    return livre
        return livres[0]
    else:
        maior_l_jog = 0
        possiveis_jog = []
        maior_l_adv = 0
        possiveis_adv = []
        for livre in obtem_posicoes_pedra(apos_rotacao, cria_pedra_neutra()):
            # Cria duas cópias com para simular a jogada de cada jogador na posição livre.
            possibilidade_jog = coloca_pedra(cria_copia_tabuleiro(apos_rotacao), livre, j)
            # No caso do adversário, este só poderá verificar o l após rodar ainda mais uma vez.
            possibilidade_adv = roda_tabuleiro(coloca_pedra(cria_copia_tabuleiro(apos_rotacao), livre, adv))
            # Percorre os l's, em ordem decrescente, de k até ao maior l encontrado.
            for l in range(n * 2, max(maior_l_jog, maior_l_adv) - 1, -1):
                if verifica_linha_pedras(possibilidade_jog, livre, j, l) and l >= maior_l_jog:
                    if l > maior_l_jog:
                        maior_l_jog = l
                        possiveis_jog.clear()
                    # Como o tabuleiro rodou em antihorário, a posição a jogar será a seguinte em sentido horário.
                    possiveis_jog.append(obtem_posicao_seguinte(t, livre, True))

                # Utiliza também a posição seguinte da livre para verificação.
                if verifica_linha_pedras(possibilidade_adv, obtem_posicao_seguinte(t, livre, False), adv,
                                         l) and l >= maior_l_adv:
                    if l > maior_l_adv:
                        maior_l_adv = l
                        possiveis_adv.clear()
                    # Como o tabuleiro rodou em antihorário, a posição a jogar será a seguinte em sentido horário.
                    possiveis_adv.append(obtem_posicao_seguinte(t, livre, True))

                # Assim que se encontra um l maior, é escusado verificar os l's seguintes (mais pequenos).
                if max(maior_l_jog, maior_l_adv) >= l:
                    break

        return ordena_posicoes(tuple(possiveis_jog), n)[0] if maior_l_jog >= maior_l_adv else \
            ordena_posicoes(tuple(possiveis_adv), n)[0]


def orbito(n, modo, jog):
    """
    orbito: int × str × str → int

    Função principal que permite jogar um jogo completo de Orbito-n.

    Recebe o número de órbitas do tabuleiro,
    uma cadeia de carateres que representa o modo de jogo,
    e a representação externa de uma pedra (preta ou branca).

    Devolve um inteiro identificando o jogador vencedor
    (1 para preto ou -1 para branco), ou 0 em caso de empate.
    O jogo começa sempre com pedras pretas.

    Caso os argumentos sejam inválidos, gera um erro.

    Modos de jogo:

    'facil': Jogo de um jogador contra o computador que utiliza a estratégia fácil (sec. 1.3).
    O jogador joga com as pedras com representação externa jog.
    No fim do jogo a função mostra o resultado obtido pelo jogador:
    VITORIA, DERROTA ou EMPATE.

    'normal': Jogo de um jogador contra o computador que utiliza a estratégia normal (sec. 1.3).
    O jogador joga com as pedras com representação externa jog.
    No fim do jogo a função mostra o resultado obtido pelo jogador:
    VITORIA, DERROTA ou EMPATE.

    '2jogadores': Jogo de dois jogadores.
    No fim do jogo a função mostra o resultado do jogo:
    VITORIA DO JOGADOR 'X', VITORIA DO JOGADOR 'O' ou EMPATE.
    """
    # Converte as pedras dos jogadores para símbolos.
    simbolos = (pedra_para_str(cria_pedra_preta()), pedra_para_str(cria_pedra_branca()))
    if not (eh_n(n) and modo in ('facil', 'normal', '2jogadores') and jog in simbolos):
        raise ValueError("orbito: argumentos invalidos")

    # Converte o simbolo recebido para pedra.
    j = cria_pedra_preta() if jog == simbolos[0] else cria_pedra_branca()
    tabuleiro = cria_tabuleiro_vazio(n)
    jogador_atual = cria_pedra_preta()
    # Mensagens de entrada.
    print(f'Bem-vindo ao ORBITO-{n}.')
    print(f"Jogo contra o computador ({modo}).\nO jogador joga com '{jog}'."
          if modo != '2jogadores' else
          "Jogo para dois jogadores.")
    print(tabuleiro_para_str(tabuleiro))
    # Ciclo do jogo
    while not eh_fim_jogo(tabuleiro):
        if modo != '2jogadores' and not pedras_iguais(jogador_atual, j):
            print(f"Turno do computador ({modo}):")
            pos = escolhe_movimento_auto(tabuleiro, jogador_atual, modo)
        else:
            print("Turno do jogador."
                  if modo != '2jogadores' else
                  f"Turno do jogador '{pedra_para_str(jogador_atual)}'.")
            pos = escolhe_movimento_manual(tabuleiro)

        coloca_pedra(tabuleiro, pos, jogador_atual)
        roda_tabuleiro(tabuleiro)
        print(tabuleiro_para_str(tabuleiro))

        # Verifica se os jogadores são vencedores.
        vpreta = eh_vencedor(tabuleiro, cria_pedra_preta())
        vbranca = eh_vencedor(tabuleiro, cria_pedra_branca())
        if vpreta or vbranca:
            # Caso de empate.
            if vpreta and vbranca:
                break
            p_vencedora = cria_pedra_preta() if vpreta else cria_pedra_branca()
            if modo != '2jogadores':
                print('VITORIA' if pedras_iguais(j, p_vencedora) else 'DERROTA')
            else:
                print(F"VITORIA DO JOGADOR '{pedra_para_str(p_vencedora)}'")
            return pedra_para_int(p_vencedora)

        # Troca o turno.
        jogador_atual = cria_pedra_branca() if eh_pedra_preta(jogador_atual) else cria_pedra_preta()

    # Nenhum ganha.
    print("EMPATE")
    return pedra_para_int(cria_pedra_neutra())
