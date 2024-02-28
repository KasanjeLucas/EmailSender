'''
    EN:
    Module created to define the E-mail Patterns that will be imported to the functions 
    that send, in fact, the e-mails.

    PT:
    Módulo criado para definir os Padrões de E-mail que serão importados para as funções
    que enviam, de fato, os e-mails
'''
LINK_STAGE01 = 'https://forms.gle/AWaCYXJK44j2z55AA' # Change the link when you need
data_limite = '23/03/2024' # Put the correct date here

def create_unordered_list(quantity: int, content: list) -> str:
    '''
    EN:
    Function made to create an unordered list according to the quantity of bullet points specified
    PT:
    Função feita para criar uma lista não-ordenada de acordo com a quantidade de bullet points especificada
    '''
    items = []  # Initializes an empty list to store the unordered list items
    for i in range(quantity):
        items.append(f'<li>{content[i]}</li>')  # Adds each item to the list

    # Joins all items in the unordered list into a single string
    unordered_list = '<ul>' + ''.join(items) + '</ul>'
    
    return unordered_list  # Returns the complete unordered list as a string


# Texto da primeira etapa
def realizacao_primeira_etapa(nome_candidato: str) -> str:
    '''
    EN: Function to be pulled and insert the name of a candidate
    PT: Função para ser puxada e inserir o nome de um candidato
    '''
    return (
    f'''
    <p>Olá {nome_candidato}!! Esperamos que você esteja bem. </p>
    <p>Estamos muito felizes com o entusiasmo que você demonstrou em relação à oportunidade de participar 
    do nosso processo seletivo.</p>

    <p>Como parte desse processo, gostaríamos de compartilhar o link para o formulário da primeira etapa, 
    que ficará disponível até o dia {data_limite}. Reserve um momento para preenchê-lo assim que possível.</p>

    <p>Além disso, para que você possa conhecer melhor a for_code, anexamos um documento informativo que 
    detalha nossa missão, valores e realizações. Acreditamos que isso o ajudará a entender melhor nossa liga 
    e como você poderá contribuir para o nosso sucesso conjunto. Sugerimos também que o documento seja lido 
    antes da realização da primeira etapa.</p>

    <p> Estamos torcendo pelo seu sucesso e estamos à disposição para esclarecer qualquer dúvida que possa 
    surgir. Boa sorte &#128521; &#128640;</p>

    <p> <b>Link para a etapa 1:</b> <a href="{LINK_STAGE01}">{LINK_STAGE01}</a></p>
    '''
    )

# Texto de lembrete da primeira etapa
def lembrete_primeira_etapa() -> str:
    '''
    EN: Function that returns the body-text relative to the text reminder
    PT: Função que retorna o body-text relativo ao texto de lembrete
    '''
    return (
        f'''
        <p>Olá! Tudo bem? </p>
        <p> Percebemos que muitas pessoas ainda não responderam à etapa 1 &#129402;. 
        Gostaríamos de lembrar apenas da importância de respondê-lo e ressaltar que ele ficará aberto 
        até o dia {data_limite}.</p>
        <br>
        <p>Obs.: Caso você já tenha respondido, apenas desconsidere este e-mail.</p>

        Estamos ansiosos pelas respostas &#128521;.

        <p> <b>Link para a etapa 1:</b> <a href="{LINK_STAGE01}">{LINK_STAGE01}</a></p>
        '''
    )

# Texto de aprovação na primeira etapa
def aprovacao_primeira_etapa(nome_candidato: str, discord_link: str) -> str:
    '''
    EN: Function that returns the body-text relative to the approvement text
    PT: Função que retorna o body-text relativo ao texto de aprovação na primeira etapa
    '''
    return (f'''
    <p>Olá, {nome_candidato}!! Esperamos que você esteja bem.</p>

    <p>A primeira etapa do nosso processo seletivo acabou e gostaríamos de falar que você foi aprovado!!! &#129395;</p> 

    <p>Estamos muito felizes com o entusiasmo que você demonstrou em relação à oportunidade de participar 
    do nosso processo seletivo.</p>

    <p>Agora, para as próximas etapas, precisamos que você entre no seguinte <b>servidor do discord: 
    <a href = "{discord_link}">{discord_link}</a></b></p>

    <p>Lembrando que <b>quem não entrar será desclassificado...</b></p>

    <p>A partir de agora, você está cada vez mais perto de se tornar um for_coder!</p>

    <p>Estamos ansiosos para as próximas etapas e para poder conhecer um pouquinho mais de você! &#128156;&#128156;</p>

''')

# Texto de reprovação na primeira etapa
def reprovacao_primeira_etapa(nome_candidato: str, lista_feedback:list) -> str:
    '''
    EN: Function that returns the body-text relative to the reprobation text
    PT: Função que retorna o body-text relativo ao texto de reprovação na primeira etapa
    '''
    feedback = create_unordered_list(len(lista_feedback), lista_feedback)
    
    return (f'''
    <p>Olá, {nome_candidato}!! Esperamos que você esteja bem.</p>
    <p>A primeira etapa do nosso processo seletivo acabou e gostaríamos de falar que, infelizmente, não foi dessa vez... &#128546;</p>
    <p>Estamos mandando um feedback desse PS para que você possa ver seus pontos mais fracos e melhorá-los da próxima vez.</p>
    {feedback}
    <p>Agradecemos a sua participação no nosso processo seletivo e estaremos te aguardando para o próximo! &#128156;</p> 
''')