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

def send_email(your_email:str, app_key: str) -> None:
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
                       + "[2] - E-mail  de lembrete etapa 1;\n"
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
            
        if int_option == 1:
            os.system('cls')
            print('\n\tOpção selecionada: E-mail para a etapa 1\n\n')

            dataframe = pd.read_csv('./docs/inscricoes.csv')
            formated_dataframe = dataframe.drop(columns=['Carimbo de data/hora','Endereço de e-mail',
                                                         '📞 Qual é o seu WhatsApp? (Contato de emergência)',
                                                         '💡 Qual é o seu curso?',
                                                         '🤔 É a sua primeira vez participando do processo seletivo?',
                                                         '📄 Qual é o link do seu LinkedIn? (opcional)',
                                                         '👁️ Como você ficou sabendo do PS?'])
            
            full_name_list = []
            nickname_list = []
            email_list = []

            for value in formated_dataframe.values:
                for i, needed_value in enumerate(value):
                    if i == 0:
                        full_name_list.append(needed_value)
                    
                    if i == 1:
                        nickname_list.append(needed_value)
                    
                    if i == 2:
                        email_list.append(needed_value)

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
                    body_message = realizacao_primeira_etapa(full_name_list[i])
                
                # Specifying the kind of message content
                message.attach(MIMEText(body_message, 'html'))

                # Creating a MIMEApplication to attach an external document

                file = r'./docs/Apresentacao.pdf'
                with open(file, 'rb') as f:
                    attachment = MIMEApplication(f.read(), _subtype='pdf')
                
                # Attaching the file
                attachment.add_header('content_disposition', 'attachment', filename='Apresentação.pdf')
                message.attach(attachment)

                # Stablishing the connection
                connection = smtplib.SMTP('smtp.gmail.com', 587)
                connection.starttls()

                # Logging in
                connection.login(message['From'], your_password)

                # Sending the e-mail
                connection.sendmail(message['From'], message['To'], message.as_string())
                
                # Reseting the instance
                del(message)

                # Finishing the session
                connection.quit()

                print(f'Email enviado com sucesso para {email}')
