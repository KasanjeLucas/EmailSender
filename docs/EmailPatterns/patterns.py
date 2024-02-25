'''
    EN:
    Module created to define the E-mail Patterns that will be imported to the functions 
    that send, in fact, the e-mails.

    PT:
    Módulo criado para definir os Padrões de E-mail que serão importados para as funções
    que enviam, de fato, os e-mails
'''


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

    <p> Olá {nome_candidato}


    '''
