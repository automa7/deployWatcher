# Deploy Watcher

API Flask RESTFul que pode ser integrada ao seu pipeline de deployment para monitorar tempos de deployment.

## Instalação e Uso

### Local
Para executar localmente em seu computador, é necessário ter instalados os seguintes requisitos:
1. Python versão 3.6+
2. Pacotes listados em requirements.txt
3. Git (para clonar o repositório)

Se esses requisitos estão atendidos, para iniciar a api em execução manual, abra sua command line e execute os seguintes comandos:
#### Windows cmd/Powershell
    git clone https://github.com/automa7/deployWatcher.git
    cd deployWatcher
    flask run
    
#### Linux shell
    git clone https://github.com/automa7/deployWatcher.git 
    cd deployWatcher
    flask run

### Docker
#### Dev
TBD.
#### Prod
TBD.
### Lambda
TBD.

## Considerações
As seguintes suposições são consideradas para execução desse aplicativo:
* O sistema miolo deve permanecer agnóstico a provedores de nuvem e bancos de dados, permitindo assim flexibilidade na sua integração.
* O Padrão RESTful será respeitado.
* O tratamento de inputs se dará por parte do sistema originário. Isso é assumido para que haja flexibilidade na tradução dos dados para a API.
* Os ambientes Local e Dev não levam em consideração a persistência dos dados, e foram criados apenas para fornecer um ambiente de desenvolvimento fácil.

