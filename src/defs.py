'''
    EN:
    Module responsible to center all the functions needed to run the program.

    PT:
    Módulo responsável por centralizar todas as funções necessárias para rodar o programa.
'''

from email.mime.multipart import MIMEMultipart # Class responsible to gather different contents in a E-mail
from email.mime.text import MIMEText # Class responsible for the text in body
from email.mime.application import MIMEApplication # Class responsible for the attachments
import smtplib # Main module to deal with E-mails SMTP
import os # Module that allow us to use the OS functionalities
import pandas as pd # Module responsible to read the data


from docs.EmailPatterns.patterns import realizacao_primeira_etapa # Function to send the first email pattern
from docs.EmailPatterns.patterns import lembrete_primeira_etapa # Function to send the second email pattern
from docs.EmailPatterns.patterns import aprovacao_primeira_etapa # Function to send the third email pattern
from docs.EmailPatterns.patterns import reprovacao_primeira_etapa # Function to send the fourth email pattern

list_emails_sent_1a_etapa = [] # Global variable to create a csv file of the already sent "1a etapa" emails
list_emails_sent_aprovados = [] # Global variable to create a csv file of the already sent "Aprovados" emails

def create_and_format_pattern(path: str) -> list:
    '''
    EN:
    Function responsible to format the needed lists to send the first pattern of e-mail

    PT:
    Função responsável por formatar as listas necessárias para enviar o primeiro padrão de e-mail
    '''
    dataframe = pd.read_csv(path)
    formated_dataframe = dataframe.drop(columns=['Carimbo de data/hora','Endereço de e-mail',
                                                '📞 Qual é o seu WhatsApp? (Contato de emergência)',
                                                '💡 Qual é o seu curso?',
                                                '🤔 É a sua primeira vez participando do processo seletivo?',
                                                '📄 Qual é o link do seu LinkedIn? (opcional)',
                                                '👁️ Como você ficou sabendo do PS?'])
            
    full_name_list = formated_dataframe.iloc[:, 0].tolist()
    nickname_list = formated_dataframe.iloc[:, 1].tolist()
    email_list = formated_dataframe.iloc[:, 2].tolist()
    
    return [full_name_list, nickname_list, email_list]

def create_and_format_pattern2(path: str) -> list:
    '''
    EN:
    Function responsible to format the needed lists to send the fourth pattern of e-mail

    PT:
    Função responsável por formatar as listas necessárias para enviar o quarto padrão de e-mail
    '''
    dataframe = pd.read_csv(path)
    formated_dataframe = dataframe.loc[:,['Endereço de e-mail', 'Nome']]

    full_name_list = formated_dataframe.iloc[:, 0].tolist()
    email_list = formated_dataframe.iloc[:, 1].tolist()

    return [full_name_list, email_list]

def select_reasons(dataframe: pd.DataFrame) -> list:
    '''
    EN:
    Function that fit together the reasons why the candidate was eliminated
    PT:
    Função que junta os motivos do porquê o candidato foi eliminado
    '''

    formated_dataframe = dataframe.drop(['Endereço de e-mail','Nome'], axis=1)  # Remover as colunas 'E-mail' e 'Nome'

    list_reasons = []

    for _, row in formated_dataframe.iterrows():
        reasons = []  # Inicializar uma lista vazia para armazenar os motivos desta linha
        for content in row:
            if not pd.isnull(content):
                reasons.append(content)
        list_reasons.append(reasons)  # Adicionar a lista de motivos desta linha à lista principal
    
    return list_reasons
    
def connect(email_login: str, password: str, adressee: str, message: MIMEMultipart) -> None:
    '''
    EN:
    Function responsible for creating the connection and allowing the send of a e-mail message
    PT:
    Função responsável por criar a conexão e permitir o envio de uma mensagem de e-mail
    '''

    # Stablishing the connection
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()

    # Logging in
    connection.login(email_login, password)

    # Sending the e-mail
    connection.sendmail(email_login, adressee, message.as_string())
                
    # Reseting the instance
    del(message)

    # Finishing the session
    connection.quit()

def send_email(your_email:str, app_key: str, discord_link:str) -> None:
    '''
    EN:
    Function responsible to send, in fact, the e-mail

    PT:
    Função responsável por enviar, de fato, o e-mail
    '''

    flag = 1

    while flag:
        print("\n\t -=-=-=-=-=-=-=-=-=- Pattern Selection -=-=-=-=-=-=-=-=-=-\n\n")
        option = input("\tDigite a opção de email a qual deseja enviar: \n"
                       + "[1] - E-mail para etapa 1 (pós-inscrição no PS);\n"
                       + "[2] - E-mail de lembrete etapa 1;\n"
                       + "[3] - E-mail de APROVAÇÃO etapa 1;\n"
                       + "[4] - E-mail de REPROVAÇÃO etapa 1;\n"
                       + "[0] - Sair\n\n>>> ")
        
        try:
            int_option = int(option)


        except ValueError: # If the user insert a str value, but it can't be converted to int
            os.system('cls')
            print('\n\tInsira um valor válido!\n\n')
            continue

        except Exception: # It's a bad choice, but for a own code, it's valid
            os.system('cls')
            print(f'\n\tErro desconhecido: {type(Exception).__name__} -> {Exception}.\n\n Por favor, reinicie o programa.\n\n')

        if int_option == 0:
            os.system('cls')
            print('\n\tPrograma encerrado com sucesso!\n\n')
            flag = 0
            
        elif int_option == 1:
            os.system('cls')

            # Receiving the needed values
            [fullname_list,
            nickname_list,
            email_list # this one will be changed
            ] = create_and_format_pattern('./docs/spreadsheets/inscricoes.csv')

            # -=-=-=-=-=-=-=- Creating the message and sending it! -=-=-=-=-=-=-=-
            your_password = f'{app_key}' # App-Key here

            for i, email in enumerate(email_list):
                message = MIMEMultipart() # Creation of an instance of MIMEMultipart Class
                message['From'] = f'{your_email}' # Putting the email that you're working with
                message['To'] = email # As we're iterating in a email list, the current one is the addressee
                message['Subject'] = "Processo Seletivo 24.1" # Just put the subject here

                # -=-=-=-=-=-=-=- Creating the body_message -=-=-=-=-=-=-=-

                # Checking if the candidate has or not a nickname

                if not pd.isnull(nickname_list[i]):
                    body_message = realizacao_primeira_etapa(nickname_list[i])
                else:
                    body_message = realizacao_primeira_etapa(fullname_list[i])
                        
                # Specifying the kind of message content
                message.attach(MIMEText(body_message, 'html'))

                # Creating a MIMEApplication to attach an external document

                file = r'./docs/Apresentacao.pdf'
                with open(file, 'rb') as f:
                    attachment = MIMEApplication(f.read(), _subtype='pdf')
                        
                # Attaching the file
                attachment.add_header('content_disposition', 'attachment', filename='Apresentação da liga.pdf')
                message.attach(attachment)

                # Making the connection
                connect(your_email, your_password, message['To'], message)

                print(f'Email enviado com sucesso para {email}')
            

        elif int_option == 2:
            os.system('cls')
            print('\n\tOpção selecionada: Lembrete para etapa 1\n\n')

            # Receiving the needed values
            [fullname_list,
             nickname_list,
             email_list
            ] = create_and_format_pattern('./docs/spreadsheets/inscricoes.csv')

            # -=-=-=-=-=-=-=- Creating the message and sending it! -=-=-=-=-=-=-=-
            your_password = f'{app_key}' # App-Key here

            for i, email in enumerate(email_list):
                message = MIMEMultipart() # Creation of an instance of MIMEMultipart Class
                message['From'] = f'{your_email}' # Putting the email that you're working with
                message['To'] = email # As we're iterating in a email list, the current one is the addressee
                message['Subject'] = "Processo Seletivo 24.1 - Etapa 1" # Just put the subject here

                # -=-=-=-=-=-=-=- Creating the body_message -=-=-=-=-=-=-=-

                body_message = lembrete_primeira_etapa()

                # Specifying the kind of message content
                message.attach(MIMEText(body_message, 'html'))

                # Creating a MIMEApplication to attach an external document

                file = r'./docs/Apresentacao.pdf'
                with open(file, 'rb') as f:
                    attachment = MIMEApplication(f.read(), _subtype='pdf')
                
                # Attaching the file
                attachment.add_header('content_disposition', 'attachment', filename='Apresentação.pdf')
                message.attach(attachment)

                # Making the connection
                connect(your_email, your_password, message['To'], message)

                print(f'Email enviado com sucesso para {email}')
        
        elif int_option == 3:
            os.system('cls')
            print('\n\tOpção selecionada: APROVAÇÃO na etapa 1\n\n')

            # Receiving the needed values
            [fullname_list,
            nickname_list,
            email_list # this one will be changed
            ] = create_and_format_pattern('./docs/spreadsheets/aprovados.csv')

            # -=-=-=-=-=-=-=- Creating the message and sending it! -=-=-=-=-=-=-=-
            your_password = f'{app_key}' # App-Key here

            for i, email in enumerate(email_list):
                message = MIMEMultipart() # Creation of an instance of MIMEMultipart Class
                message['From'] = f'{your_email}' # Putting the email that you're working with
                message['To'] = email # As we're iterating in a email list, the current one is the addressee
                message['Subject'] = "PS for_code - Resultado da 1a etapa" # Just put the subject here
                    
            # -=-=-=-=-=-=-=- Creating the body_message -=-=-=-=-=-=-=-

                # Checking if the candidate has or not a nickname

                if not pd.isnull(nickname_list[i]):
                    body_message = aprovacao_primeira_etapa(nickname_list[i], f'{discord_link}')
                else:
                    body_message = aprovacao_primeira_etapa(fullname_list[i], f'{discord_link}')

                # Specifying the kind of message content
                message.attach(MIMEText(body_message, 'html'))

                # Making the connection
                connect(your_email, your_password, message['To'], message)

                print(f'Email enviado com sucesso para {email}')
            
        elif int_option == 4:

            os.system('cls')
            print('\n\tOpção selecionada: REPROVAÇÃO na etapa 1\n\n')

            file_exists = os.path.isfile('./docs/spreadsheets/EmailsJaEnviados3.csv')

            if file_exists:
                # Receiving the needed values
                [email_list, # this one will be changed
                fullname_list
                ] = create_and_format_pattern2('./docs/spreadsheets/Feedbacks.csv') # arquivo

                # -=-=-=-=-=-=-=- Creating the message and sending it! -=-=-=-=-=-=-=-
                your_password = f'{app_key}' # App-Key here

                for i, email in enumerate(email_list):
                    message = MIMEMultipart() # Creation of an instance of MIMEMultipart Class
                    message['From'] = f'{your_email}' # Putting the email that you're working with
                    message['To'] = email # As we're iterating in a email list, the current one is the addressee
                    message['Subject'] = "PS for_code - Resultado da 1a etapa" # Just put the subject here
                    
                # -=-=-=-=-=-=-=- Creating the body_message -=-=-=-=-=-=-=-

                    lista_feedback = select_reasons(pd.read_csv('./docs/spreadsheets/Feedbacks.csv'))
                    body_message = reprovacao_primeira_etapa(fullname_list[i], lista_feedback[i])

                    # Specifying the kind of message content
                    message.attach(MIMEText(body_message, 'html'))

                    # Making the connection
                    connect(your_email, your_password, message['To'], message)

                    print(f'Email enviado com sucesso para {email}')
        
        else:
            os.system('cls')
            print('\n\tSelecione uma das opções acima!!')
