'''
    EN:
    Module created to define the E-mail Patterns that will be imported to the functions 
    that send, in fact, the e-mails.

    PT:
    Módulo criado para definir os Padrões de E-mail que serão importados para as funções
    que enviam, de fato, os e-mails
'''
LINK_STAGE01 = 'https://forms.gle/AWaCYXJK44j2z55AA' # Change the link when you need
data_limite = 'XX/XX/XXXX' # Put the correct date here

# Texto da primeira etapa
def realizacao_primeira_etapa(nome_candidato: str) -> None:
    '''
    EN: Function to be pulled and insert the name of a candidate
    PT: Função para ser puxada e inserir o nome de um candidato
    '''
    f'''
    <p align="center">
        <img aling="center" src="../imgs/Banner.png">
    </p>

    <br>

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

    <p> <b>Link para a etapa 1:</b> <a>{LINK_STAGE01}</a></p>
    '''
