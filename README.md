<p align="center">
  <img src="https://i.imgur.com/TsoLODG.png" height="120">
  <h2 align="center">Email Sender - for_code</h2>
<p align="center">Local application to send e-mails with SMTP Protocol (specifically through the Gmail port)<p>
  <p align="center">
    <a href="https://github.com/KasanjeLucas/EmailSender/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />
    </a>
</p>

<p align = "center">EmailSender arised from a problem that I had to solve on the academic league that I participate.</p>

## Problem
<p>Given a database obtained through form responses from a Selection Process, how could we automate the process of sending emails to participants?</p>

## Libraries
<p>In this project, we'll use, in the most part, native Python libs and some external libs. These are:</p>
<ul>
    <li><kbd>email</kbd> package: A package for parsing, handling, and generating email messages;</li>
    <li><kbd>smtp</kbd>: Allow us to send emails with the SMTP protocol;</li>
    <li><kbd>os</kbd>: Allow us to use the current OS functionalities</li>
    <li><kbd>pandas</kbd>: Responsible for data manipulation and analysis</li>
</ul>

## Installing dependencies
<p>The project has a requirement file, allowing us to install the project dependencies. To do it, clone the project code, open your terminal on the correct path and write:</p>

```sh
python -m venv venv
```

Then, it'll start automatically your virtual enviroment (which one i highly recommend you to build).

To install the libs needed, you'll need to do (on the terminal too):

```sh
pip install -r requirements.txt
```

<p>By running it, the libs will be installed on your virtual enviroment and, then, you'll have all setup to run the program on the <kbd>main</kbd> module</p>

## How does it work?
<p>When executing this program, the user must first enter their sender credentials¹ and the invite link of their Discord server². Then, he/she will see the following menu:</p>
<ul>
    <li>Digite a opção de email a qual deseja enviar:</li>
    <li>[1] - E-mail para etapa 1 (pós-inscrição no PS);</li>
    <li>[2] - E-mail de lembrete etapa 1;</li>
    <li>[3] - E-mail de APROVAÇÃO etapa 1;</li>
    <li>[4] - E-mail de REPROVAÇÃO etapa 1;</li>
    <li>[0] - Sair</li>
</ul>

<p>By filling the input, the program will verify if the input is correct by analyzing the kind of data and if it's available on menu, trough the lines of code, respectively:</p>

```sh
try:
  int_option = int(option)


except ValueError: # If the user insert a str value, but it can't be converted to int
  os.system('cls')
  print('\n\tInsira um valor válido!\n\n')
  continue

except Exception: # It's a bad choice, but for a own code, it's valid
  os.system('cls')
  print(f'\n\tErro desconhecido: {type(Exception).__name__} -> {Exception}.\n\n Por favor, reinicie o programa.\n\n')
```

```sh
if int_option == 0:
  os.system('cls')
  print('\n\tPrograma encerrado com sucesso!\n\n')
  flag = 0

#   .
#   .    (Other options included here)
#   .

else:
  os.system('cls')
  print('\n\tSelecione uma das opções acima!!')
```

<p>If the input matches with any of options, then the code will run the respective code block.</p>

<h4>PS¹: The sender credentials need the User Login E-mail and an App-Key, which one can be made on the configurations of Gmail. If you have any question on how to create this, I recommend this video: https://www.youtube.com/watch?v=lSURGX0JHbA</h4>
<h4>Obs: Credits to MailsDaddy Software Channel</h4>
<h4>PS²: The requirement of the Discord link was associated with the context that I was inserted in.</h4>

## Features
<p>This project has the malleability to add other body_texts and options on the menu. To understand it, check the <kbd>patterns.py</kbd> module</p>


## Conclusion
<p>This project is soooo specific to [@for_code](https://github.com/forcodeufrj) league, but the idea of the project can be used by anyone. So, if you want, fork the project and handle it to your own way.</p>
<p>Furthermore, I'm so grateful to for_code by granting me these kind of challenges and tasks that can improve my knowledge.</p>
