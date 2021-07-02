

##################################                                                 
#  Goncalo Nunes - 99074
#  Projeto 2 - Jogo do Moinho                                                  
##################################




###################################
# TAD - posicao
#
# Representacao Interna: string de dois elementos, 
# o primeiro a coluna e o segundo a linha da posicao
###################################


# CONSTRUTORES 
# cria_posicao: str x str -> posicao
# cria_copia_posicao: posicao -> posicao

# SELETORES 
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str

# RECONHECEDOR
# eh_posicao: universal -> bool

# TESTE
# posicoes_iguais: posicao x posicao -> bool

# TRANSFORMADOR 
# posicao_para_str: posicao -> str



# eh_coluna: str -> bool
def eh_coluna(coluna):
    """
    Verifica se eh uma coluna valida

    :param coluna: string
    :return: bool

    Recebe um string e verifica se eh uma coluna valida. Se for, devolve True, caso contrario devolve False
    """
    return coluna >= 'a' and coluna <= 'c'


# eh_coluna: str -> bool
def eh_linha(linha):
    """
    Verifica se eh uma linha valida

    :param linha: string
    :return: bool

    Recebe um string e verifica se eh uma linha valida. Se for, devolve True, caso contrario devolve False
    """
    return linha >= '1' and linha <= '3'


# cria_posicao: str x str -> posicao
def cria_posicao(coluna, linha):
    """
    Devolve uma posicao valida.

    :param coluna: string
    :param linha: string
    :return: string

    Recebe duas strings, a coluna deve ser um caracter entre 'a' e 'c' e a linha deve ser um caracter entre '1' e '3'. 
    Devolve uma string de dois caracteres onde o primeiro eh a coluna e o segundo a linha da posicao.
    Se algum dos argumentos dados for invalido, a funcao gera um erro.
    """

    if type(coluna) != str or len(coluna) != 1 or not eh_coluna(coluna) or \
        type(linha) != str or len(linha) != 1 or not eh_linha(linha):
        raise ValueError("cria_posicao: argumentos invalidos")

    return coluna + linha


# cria_copia_posicao: posicao -> posicao
def cria_copia_posicao(pos):
    """
    Devolve uma copia da posicao inserida.

    :param pos: posicao
    :return: posicao
    """
    return pos.lower()


# obter_pos_c: posicao -> str
def obter_pos_c(pos):
    """
    Devolve a coluna da posicao.

    :param pos: posicao
    :return: string
    """
    return pos[0]


# obter_pos_l: posicao -> str
def obter_pos_l(pos):
    """
    Devolve a linha da posicao.

    :param pos: posicao
    :return: string
    """
    return pos[1]

# eh_posicao: universal -> bool
def eh_posicao(posicao):
    """
    Reconhece posicao.

    :param pos: universal
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma posicao
    e False caso contrario.
    """
    return type(posicao) == str and len(posicao) == 2 and \
        eh_coluna(obter_pos_c(posicao)) and eh_linha(obter_pos_l(posicao))


# posicoes_iguais: posicao x posicao -> bool
def posicoes_iguais(pos1, pos2):
    """
    Avalia se duas posicoes sao iguais.

    :param pos1: posicao 
    :param pos2: posicao 
    :return: bool

    Recebe duas posicoes e retorna True se forem duas posicoes validas iguais e False caso contrario.
    """
    return eh_posicao(pos1) and eh_posicao(pos2) and pos1 == pos2


# posicao_para_str: posicao -> str
def posicao_para_str(pos):
    """
    Devolve a posicao em string

    :param pos: posicao 
    :return: string

    Recebe uma posicao e devolve a string e representa a posicao fornecida.
    """
    return obter_pos_c(pos) + obter_pos_l(pos)


# obter_posicoes: {} -> tuplo de posicoes
def obter_posicoes():
    """
    Retorna um tuplo com todas as posicoes do tabuleiro

    :return: tuplo
    """
    linhas = ("1", "2", "3")
    colunas = ("a", "b", "c")
    posicoes_tab = ()
    for linha in linhas:
        for coluna in colunas:
            posicoes_tab += (cria_posicao(coluna, linha),)
    return posicoes_tab


# obter_posicoes_adjacentes: posicao -> tuplo de posicoes
def obter_posicoes_adjacentes(pos):
    """
    Devolve as posicoes adjacentes ah posicao inserida

    :param pos: posicao 
    :return: tuplo

    Recebe uma posicao e devolve um tuplo com as posicoes adjacentes ah posicao inserida.
    """
    posicoes = obter_posicoes()
    pos_nao_diagonais = tuple(cria_posicao(x[0], x[1]) for x in ("b1", "a2", "c2", "b3"))
    coluna = obter_pos_c(pos)
    linha = obter_pos_l(pos)
    pos_adjacentes = ()
    for e in posicoes:
        diff_colunas = abs(ord(obter_pos_c(e)) - ord(coluna))
        diff_linhas = abs(ord(obter_pos_l(e)) - ord(linha))
        if pos in pos_nao_diagonais:
            if diff_colunas <= 1 and diff_linhas <= 1 and (diff_linhas != diff_colunas):
                pos_adjacentes += (e,)
        else:
             if diff_colunas <= 1 and diff_linhas <= 1 and not posicoes_iguais(pos, e):
                pos_adjacentes += (e,)

    return pos_adjacentes





###################################
# TAD - peca
#
# Representacao Interna: String de um unico elemento 
# ex: ("X", "O", " ")
###################################

# CONSTRUTORES 
# cria_peca: str x str -> peca
# cria_copia_peca: peca -> peca

# RECONHECEDOR
# eh_peca: universal -> bool

# TESTE
# pecas_iguais: peca x peca -> bool

# TRANSFORMADOR 
# peca_para_str: peca -> str



# cria_peca: str x str -> peca
def cria_peca(char):
    """
    Devolve a peca correspondente ah string inserida

    :param char: string
    :return: peca

    Recebe uma string e devolve a peca correspondente a essa string. 
    Caso o argumento seja invalido e nao corresponda a nenhum peca, a funcao gera um erro
    """
    if char not in ("X", "O", " "):
        raise ValueError("cria_peca: argumento invalido")
    return char


# cria_copia_peca: peca -> peca
def cria_copia_peca(peca):
    """
    Devolve uma copia da peca inserida.

    :param peca: peca
    :return: peca
    """
    return peca.upper()


# eh_peca: universal -> bool
def eh_peca(peca):
    """
    Reconhece peca.

    :param peca: universal
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma peca
    e False caso contrario.
    """
    return peca in ("X", "O", " ")


# pecas_iguais: peca x peca -> bool
def pecas_iguais(peca1, peca2):
    """
    Avalia se duas pecas sao iguais.

    :param pos1: peca 
    :param pos2: peca 
    :return: bool

    Recebe duas pecas e retorna True se forem duas pecas validas iguais, caso contrario retorna False.
    """
    return eh_peca(peca1) and eh_peca(peca2) and peca1 == peca2


# peca_para_str: peca -> str
def peca_para_str(peca):
    """
    Devolve a peca em string

    :param pos: peca
    :return: string

    Recebe uma peca e devolve a string e representa a peca fornecida.
    """
    return "[{}]".format(peca)


# peca_para_inteiro: peca -> inteiro (-1, 0 ou 1)
def peca_para_inteiro(peca):
    """
    Converte uma peca para inteiro

    :param pos: peca
    :return: int

    Recebe uma peca e devolve o inteiro que representa essa peca.
    """
    peca_str = peca_para_str(peca)
    return 1 if peca_str == "[X]" else (-1 if peca_str == "[O]" else 0)





###################################
# TAD - tabuleiro
#
# Representacao Interna: Dicionario de 9 elementos,
# as chaves correspondem ah representacao externa das posicoes e 
# os valores correspondem as pecas que ocupam as posicoes do tabueiro
###################################

# CONSTRUTORES 
# cria_tabuleiro: {} -> tabuleiro
# cria_copia_tabuleiro: tabuleiro -> tabuleiro

# SELETORES 
# obter_peca: tabuleiro x posicao -> peca
# obter_vetor: tabuleiro x str -> tuplo de pecas

# MODIFICADORES
# coloca_peca: tabuleiro x peca x posicao -> tabulerio
# remove_peca: tabuleiro x posicao -> tabulerio
# move_peca: tabuleiro x posicao x posicao -> tabuleiro

# RECONHECEDOR
# eh_tabuleiro: universal -> bool
# eh_posicao_livre: tabulerio x posicao -> bool

# TESTE
# posicoes_iguais: tabuleiro x tabuleiro -> bool

# TRANSFORMADOR 
# tabuleiro_para_str: tabuleiro -> str
# tuplo_para_tabuleiro: tuplo -> tabuleiro




# cria_tabuleiro: {} -> tabuleiro
def cria_tabuleiro():
    """
    Devolve um tabuleiro

    :return: tabuleiro

    Devolve um tabuleiro sem posicoes ocupadas por pecas dos jogadores.
    """
    tabuleiro = {}
    for pos in obter_posicoes():
        tabuleiro[posicao_para_str(pos)] = cria_peca(" ")
    return tabuleiro


# cria_copia_tabuleiro: tabuleiro -> tabuleiro
def cria_copia_tabuleiro(tab):
    """
    Devolve uma copia do tabuleiro inserido.

    :param tab: tabuleiro
    :return: tabuleiro
    """
    return dict(tab)


# obter_peca: tabuleiro x posicao -> peca
def obter_peca(tab, pos):
    """
    Devolve uma copia do tabuleiro inserido.

    :param tab: tabuleiro
    :return: tabuleiro
    """
    return tab[posicao_para_str(pos)]


# inverter_elementos: tuplo -> tuplo
def inverter_elementos(iteravel):
    """
    Inverte os elementos dentro de um tuplo.

    :param iteravel: tuplo
    :return: tuplo 

    Exemplo:
    >>> tpl = ("a1", "b3")
    >>> inverter_elementos(tpl)
    ("1a", "3b")
    """
    res = ()
    for e in iteravel:
        res += (e[::-1],)
    return res


# obter_vetor: tabuleiro x str -> tuplo de pecas
def obter_vetor(tab, char):
    """
    Devolve pecas na linha ou coluna

    :param tab: tabuleiro
    :param char: string
    :return: tuplo

    Recebe um tabuleiro e uma linha ou coluna e devolve um tuplo com todas as pecas
    na linha ou coluna especificada pelo seu argumento.
    """
    sorted_keys = inverter_elementos(sorted(inverter_elementos(tab.keys())))
        
    vetor = ()
    for key in sorted_keys:
        if char in key:
            vetor += (tab[key],)
    return vetor


# coloca_peca: tabuleiro x peca x posicao -> tabulerio
def coloca_peca(tab, peca, pos):
    """
    Coloca uma peca no tabuleiro

    :param tab: tabuleiro
    :param peca: peca
    :param pos: posicao
    :return: tabuleiro

    Recebe um tabuleiro, uma peca e uma posicao. 
    Modifica destrutivamente o tabuleiro alterando a peca na posicao inserida pela peca inserida.
    """
    tab[posicao_para_str(pos)] = peca
    return tab


# remove_peca: tabuleiro x posicao -> tabulerio
def remove_peca(tab, pos):
    """
    Remove uma peca no tabuleiro

    :param tab: tabuleiro
    :param pos: posicao
    :return: tabuleiro

    Recebe um tabuleiro e uma posicao.
    Modifica destrutivamente o tabuleiro removendo a peca na posicao inserida.
    """
    tab[posicao_para_str(pos)] = cria_peca(" ")
    return tab


# move_peca: tabuleiro x posicao x posicao -> tabuleiro
def move_peca(tab, pos1, pos2):
    """
    Coloca uma peca no tabuleiro

    :param tab: tabuleiro
    :param pos1: posicao
    :param pos2: posicao
    :return: tabuleiro

    Recebe um tabuleiro, e duas posicoes.
    Modifica destrutivamente o tabuleiro movendo a peca 
    que se encontra na primeira posicao para a segunda posicao inserida.
    """
    peca_pos1 = tab[posicao_para_str(pos1)]
    return coloca_peca(remove_peca(tab, pos1), peca_pos1, pos2)


# obter_ganhadores: tabuleiro -> tuplo 
def obter_ganhadores(tab):
    """
    Obtem os jogadores que fizeram 3 em linha.

    :param tab: tabuleiro
    :return: tuplo

    Recebe um tabuleiro e retorna um tuplo com as pecas dos jogador(es) que ganharam o jogo.
    Caso nao haja nenhum jogador ganhador, a funcao retorna um tuplo com uma peca vazia.
    """
    colunas = ("a", "b", "c")
    linhas = ("1", "2", "3")
    pecas = tuple((cria_peca("X"), cria_peca("O")))

    ganhadores = ()
    for peca in pecas:
        if any(all(pecas_iguais(peca, e) for e in obter_vetor(tab, i)) for i in colunas + linhas):
            ganhadores += (peca,)

    return ganhadores if ganhadores != () else tuple(cria_peca(" "))


# eh_tabuleiro: universal -> bool
def eh_tabuleiro(tab):
    """
    Reconhece tabuleiro.

    :param tab: universal
    :return: bool

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a um tabuleiro
    valido e False caso contrario.
    """

    values = tuple(tab.values()) if type(tab) == dict else ()
    return type(tab) == dict and len(tab) == 9 and \
            all(type(x) == str and len(x) == 2 and \
            eh_coluna(x[0]) and eh_linha(x[1]) for x in tab) and \
            values.count(cria_peca("X")) <= 3 and \
            values.count(cria_peca("O")) <= 3 and \
            abs(values.count(cria_peca("O")) - values.count(cria_peca("X"))) <= 1 and \
            all(eh_peca(x) for x in values) and \
            len(obter_ganhadores(tab)) < 2



# eh_posicao_livre: tabulerio x posicao -> bool
def eh_posicao_livre(tab, pos):
    """
    Verifica se a posicao esta livre.

    :param tab: tabuleiro
    :param pos: posicao
    :return: bool

    Recebe um tabuleiro e uma posicao e devolve True se a posicao correspondente no tabuleiro
    estiver livre, caso contrario devolve False.
    """
    return pecas_iguais(tab[posicao_para_str(pos)], cria_peca(' '))


# tabuleiros_iguais: tabuleiro x tabuleiro -> bool
def tabuleiros_iguais(tab1, tab2):
    """
    Avalia se dois tabuleiros sao iguais.

    :param tab1: tabuleiro 
    :param tab2: tabuleiro
    :return: bool

    Recebe dois tabuleiros e retorna True se forem dois tabuleiros validas iguais, caso contrario retorna False.
    """
    return eh_tabuleiro(tab1) and eh_tabuleiro(tab2) and tab1 == tab2


# tabuleiro_para_str: tabuleiro -> str
def tabuleiro_para_str(tab):
    """
    Devolve a representacao do tabuleiro em string

    :param tab: tabuleiro
    :return: string

    Recebe um tabuleiro e devolve a sua representacao em string. Exemplo:
       a   b   c
    1 [O]-[ ]-[O]
       | \ | / |
    2 [ ]-[X]-[ ]
       | / | \ |
    3 [ ]-[ ]-[ ]
    """
    pecas = ()
    for i in range(3):
        pecas += obter_vetor(tab, str(i + 1))

    pecas_str = ()
    for peca in pecas:
        pecas_str += (peca_para_str(peca),)

    uniao = "| \\ | / |"
    return ('   a   b   c\n1 {}-{}-{}\n   ' + uniao  + '\n2 {}-{}-{}\n   ' + \
         uniao[::-1] + '\n3 {}-{}-{}').format(*pecas_str)


# tuplo_para_tabuleiro: tuplo -> tabuleiro    
def tuplo_para_tabuleiro(tuplo):
    """
    Converte um tuplo de 3 tuplos para tabuleiro.

    :param tuplo: tuplo
    :return: tabuleiro

    Recebe um tuplo de 3 tuplos, contendo valores inteiros entre -1 e 1,
     e devolve o tabuleiro que o representa.
    """
    tab = cria_tabuleiro()
    posicoes = obter_posicoes()
    int_para_str = {1: "X", -1: "O", 0: " "}

    i = 0
    for linha in tuplo:
        for e in linha:
            tab = coloca_peca(tab, cria_peca(int_para_str[e]), posicoes[i])
            i += 1
    return tab


# obter_ganhador: tabuleiro -> peca
def obter_ganhador(tab):
    """
    Devolve o jogador ganhador.

    :param tab: tabuleiro
    :return: peca

    Recebe um tabuleiro, e devolve a peca correspondente ao jogador que ganhou a partida. 
    Caso nao haja jogador ganhador a funcao devolve uma peca livre. 
    """
    return obter_ganhadores(tab)[0]


# obter_posicoes_livres: tabuleiro -> tuplo de posicoes
def obter_posicoes_livres(tab):
    """
    Devolve as posicoes livres do tabuleiro.

    :param tab: tabuleiro
    :return: tuplo

    Recebe um tabuleiro, e devolve um tuplo com todas as posicoes livres do tabuleiro inserido. 
    """
    return tuple(pos for pos in obter_posicoes() if eh_posicao_livre(tab, pos))
        

# obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
def obter_posicoes_jogador(tab, peca):
    """
    Devolve as posicoes ocupadas pelo jogador.

    :param tab: tabuleiro
    :return: tuplo

    Recebe um tabuleiro, e devolve um tuplo com todas as posicoes ocupadas pelo jogador no tabuleiro inserido. 
    """
    return tuple(pos for pos in obter_posicoes() if pecas_iguais(obter_peca(tab, pos), peca))


# obter_posicoes_adjacentes_livres: tabuleiro x posicao -> tuplo de posicoes
def obter_posicoes_adjacentes_livres(tab, pos):
    """
    Devolve as posicoes livres adjacentes ah posicao.

    :param tab: tabuleiro
    :param pos: posicao
    :return: tuplo

    Recebe um tabuleiro, e devolve um tuplo com todas as posicoes livres adjacentes ah posicao inserida. 
    """
    res = ()
    for e in obter_posicoes_adjacentes(pos):
        if eh_posicao_livre(tab, e):
            res += (e,)
    return res





###################################
# Funcoes Adicionais
###################################


# obter_movimento_manual: tabuleiro x peca -> tuplo de posicoes
def obter_movimento_manual(tab, peca):
    """
    Devolve a posicao ou movimento escolhido pelo utilizador.

    :param tab: tabuleiro
    :param peca: peca
    :return: tuplo

    Recebe um tabuleiro e uma peca e devolve um tuplo com a posicao escolhida pela utilizador
    se o jogo estiver na fase de colocacao de pecas. Caso o jogo esteja na fase de movimentacao, 
    a funcao devolve um tuplo de duas posicoes, que representam o movimento da peca do jogador, 
    onde o primeiro elemento eh a posicao original da peca e o segundo eh a posicao de destino da peca.
    """
    
    pos_livres = obter_posicoes_livres(tab)
    pos_jogador = obter_posicoes_jogador(tab, peca)
    if len(pos_livres) > 3:
        escolha = input("Turno do jogador. Escolha uma posicao: ")
        if all(escolha != posicao_para_str(pos) for pos in obter_posicoes_livres(tab)):
            raise ValueError("obter_movimento_manual: escolha invalida")
        return (cria_posicao(escolha[0], escolha[1]),)
    else:
        movimento =  input("Turno do jogador. Escolha um movimento: ")
        pos_partida = movimento[:len(movimento)//2]
        pos_chegada = movimento[len(movimento)//2:]

        if (all(obter_posicoes_adjacentes_livres(tab, e) == () for e in pos_jogador) \
        and pos_partida == pos_chegada) or \
        (any(pos_partida == posicao_para_str(pos) for pos in pos_jogador) and \
        any(pos_chegada == posicao_para_str(pos) for pos in pos_livres) and \
        any(pos_chegada == posicao_para_str(pos) for pos in  
        obter_posicoes_adjacentes(cria_posicao(pos_partida[0], pos_partida[1])))):
            
            return (cria_posicao(pos_partida[0], pos_partida[1]), \
                 cria_posicao(pos_chegada[0], pos_chegada[1]))

        raise ValueError("obter_movimento_manual: escolha invalida")


# minimax: tabuleiro x peca x int x tuplo -> tuplo
def minimax(tab, peca, profundidade, seq_mov=()):
    """
    Funcao recursiva que obtem a melhor sequencia de movimentos para o jogador.

    :param tab: tabuleiro
    :param peca: peca
    :param profundidade: int
    :return: tuplo

    Recebe um tabuleiro, a peca do jogador com o turno atual, 
    a profundidade da recursao e uma sequencia de movimentos.
    A funcao explora todos os movimentos legais do jogador chamando-se a si propria 
    com um tabuleiro modificado com um dos movimentos e o jogador adversario como parametros.

    Quando se atinge o nivel maximo de profundidade de recusao ou se obtem um ganhador,
    a funcao devolve um tuplo com o melhor resultado que eh possivel alcancar e a sequencia de movimentos
    que mais beneficia o jogador escolhido.
    """
    melhor_seq_mov = ()
    if not pecas_iguais(obter_ganhador(tab), cria_peca(" ")) or profundidade == 0: 
        return peca_para_inteiro(obter_ganhador(tab)), seq_mov

    melhor_res = -peca_para_inteiro(peca)
    for pos_jog in obter_posicoes_jogador(tab, peca):
        for pos_adj in obter_posicoes_adjacentes(pos_jog):
            if eh_posicao_livre(tab, pos_adj):
                tab_copia = cria_copia_tabuleiro(tab)
                tab_copia = move_peca(tab_copia, pos_jog, pos_adj)
                
                adversario = "O" if peca_para_inteiro(peca) == 1 else "X"
                novo_res, nova_seq_mov = minimax(tab_copia, cria_peca(adversario), \
                    profundidade-1, seq_mov + tuple((pos_jog, pos_adj)))

                if (melhor_seq_mov == ()) or (peca_para_inteiro(peca) == 1 \
                    and novo_res > melhor_res) or \
                    (peca_para_inteiro(peca) == -1 and novo_res < melhor_res):
                        melhor_res, melhor_seq_mov = novo_res, nova_seq_mov

    return melhor_res, melhor_seq_mov
                

# obter_movimento_auto: tabuleiro x peca x str -> tuplo de posicoes
def obter_movimento_auto(tab, peca, dificuldade):
    """
    Devolve uma posicao ou movimento escolhido pelo computador

    :param tab: tabuleiro
    :param peca: peca
    :param dificuldade: string 
    :return: tuplo

    Recebe um tabuleiro, uma peca e uma string que indica a dificuldade do jogo.
    Devolve um tuplo com a posicao escolhida caso o jogo esteja na fase de colocacao de pecas.
    Caso o jogo esteja na fase de movimentacao das pecas, a funcao devolve um movimento de acordo
    com a dificuldade escolhida.
    Na dificuldade 'normal' e 'dificil' a funcao recorre ao algoritmo minimax 
    para obter o melhor movimento possivel.
    """
    # Obtem, se existir, a posicao que leva ah vitoria do jogador na proxima jogada
    def vitoria(tab, peca): 
        pos_livres = obter_posicoes_livres(tab)
        for pos in pos_livres:
            copia_tab = cria_copia_tabuleiro(tab)
            if not pecas_iguais(obter_ganhador(coloca_peca(copia_tab, peca, pos)), cria_peca(" ")):
                return pos

    # Obtem, se existir, a posicao que bloqueia a vitoria do adversario
    def bloqueio(tab, peca):
        # basta inverter a peca e chamar a funcao 'vitoria'
        peca = cria_peca("X") if pecas_iguais(peca, cria_peca("O")) else cria_peca("O")
        return vitoria(tab, peca)

    # Devolve, se estiver livre, a posicao central do tabulerio
    def centro(tab, peca):
        centro = cria_posicao("b", "2") 
        return centro if eh_posicao_livre(tab, centro) else ()

    # Devolve o primeiro canto livre
    def canto(tab, peca):
        cantos_str = ("a1", "c1", "a3", "c3")
        cantos = tuple(cria_posicao(x[0], x[1]) for x in cantos_str)
        for canto in cantos:
            copia_tab = cria_copia_tabuleiro(tab)
            if eh_posicao_livre(copia_tab, canto):
                return canto
    
    # Devolve a primeira posicao lateral livre
    def lateral(tab, peca):
        laterais_str = ("b1", "a2", "c2", "b3")
        laterias = tuple(cria_posicao(x[0], x[1]) for x in laterais_str)
        for lateral in laterias:
            copia_tab = cria_copia_tabuleiro(tab)
            if eh_posicao_livre(copia_tab, lateral):
                return lateral

    # Fase de colocacao das pecas
    if len(obter_posicoes_livres(tab)) > 3:
        criterios = (vitoria, bloqueio, centro, canto, lateral)
        for criterio in criterios:
            pos = criterio(tab, peca)
            if eh_posicao(pos):
                return (pos,)

    # Fase de movimentacao das pecas
    pos_jog = obter_posicoes_jogador(tab, peca)
    if (all(obter_posicoes_adjacentes_livres(tab, e) == () for e in pos_jog)): # verificar se todas as pecas do jogador estao bloqueadas
        return tuple((pos_jog[0], pos_jog[0]))

    if dificuldade == "facil":
        for pos in pos_jog:
            pos_partida = pos
            pos_adjacentes = obter_posicoes_adjacentes(pos_partida)
            pos_chegada = tuple(pos for pos in pos_adjacentes if eh_posicao_livre(tab, pos))
            if len(pos_chegada) > 0:
                  return tuple((pos_partida, pos_chegada[0]))

    elif dificuldade == "normal":
        escolha = minimax(tab, peca, 1)[1]
        return tuple((escolha[0], escolha[1]))

    elif dificuldade == "dificil":
        escolha = minimax(tab, peca, 5)[1]
        return tuple((escolha[0], escolha[1]))
  


# moinho: str x str -> str
def moinho(humano, dificuldade):
    """
    Funcao principal do jogo do moinho

    :param humano: string
    :param dificuldade: string
    :return: string

    Funcao principal que permite jogar um jogo completo do Jogo do Moinho de um jogador contra o computador.
    Recebe duas strings e devolve a representacao do jogador ganhador ('[X] ou [O]')
    O primeiro argumento corresponde ah peca que o jogador deseja utilizar,
    e o segundo argumento correspondeah dificuldade do computador. Se algum dos argumentos forem
    invalidos, eh gerado um erro.
    """

    if dificuldade not in ("facil", "normal", "dificil") or humano not in ("[X]", "[O]"):
        raise ValueError("moinho: argumentos invalidos")

    print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.".format(dificuldade))
    tab = cria_tabuleiro()
    print(tabuleiro_para_str(tab))
    peca_humano = cria_peca(humano[1])
    peca_computador = cria_peca("X") if not pecas_iguais(cria_peca("X"), peca_humano) \
         else cria_peca("O")
    jogador_atual = peca_para_inteiro(cria_peca("X"))
    humano_int = peca_para_inteiro(peca_humano) 


    while pecas_iguais(obter_ganhador(tab), cria_peca(" ")):
        if jogador_atual == humano_int:
            peca = peca_humano
            escolha = obter_movimento_manual(tab, peca_humano)
        else: 
            print("Turno do computador ({}):".format(dificuldade))
            peca = peca_computador
            escolha = obter_movimento_auto(tab, peca_computador, dificuldade)

        if len(obter_posicoes_livres(tab)) > 3:
            tab = coloca_peca(tab, peca, escolha[0])
        else:
            tab = move_peca(tab, escolha[0], escolha[1])

        print(tabuleiro_para_str(tab))
        jogador_atual = -jogador_atual
    
    return peca_para_str(obter_ganhador(tab))


