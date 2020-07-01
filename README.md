OBS: Para versão em portugues, [clique aqui](README_ptBR.md)
# Deploy Watcher

A Flask RESTful API that can be integrated by deployment pipelines in order to keep track of deployment times.

## Installation and Usage

### Local
To run locally on your computer, you must have the following installed:
1. Python version 3.6+
2. Packages listed in requirements.txt
3. Git (to clone the repository)

If these requirements are met, you can start the api in manual execution by opening your command line and run the following commands:
#### Windows cmd/Powershell
    git clone https://github.com/automa7/deployWatcher.git
    cd deployWatcher
    flask run
    
#### Linux shell
    git clone https://github.com/automa7/deployWatcher.git 
    cd deployWatcher
    flask run
### Docker
TBD.
### Lambda
TBD.

## Considerations
The following assumptions are made for this application:
* The core system must remain agnostic to cloud providers and databases, thus allowing integration flexibility.
* The REST Standard must be respected.
* The inputs will be handled by the originating system. This is assumed so that there is flexibility in translating the data to the API.
* The Local and Dev environments do not take into account data persistence, and are designed only to provide an easy environment for development.