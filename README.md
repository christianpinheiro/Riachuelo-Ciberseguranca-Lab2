# 🔐 Simulação de Malware com Python (Ransomware e Keylogger)

Projeto desenvolvido como laboratório educacional para estudo de **malwares simulados** utilizando **Python**.
O objetivo é compreender, em um ambiente controlado, como ameaças como **Ransomware** e **Keylogger** funcionam e quais estratégias podem ser utilizadas para prevenção e mitigação.

⚠️ **Aviso importante:**
Este projeto foi desenvolvido **exclusivamente para fins educacionais** em um ambiente de laboratório isolado.
Não deve ser utilizado para atividades maliciosas ou em sistemas reais.

---

# 🎯 Objetivos do Projeto

Este laboratório tem como objetivo:

* Demonstrar o funcionamento básico de um **Ransomware**
* Simular a captura de teclas utilizando um **Keylogger**
* Aplicar criptografia em arquivos de teste
* Registrar eventos do teclado em um arquivo de log
* Demonstrar como dados podem ser coletados por malwares
* Documentar o aprendizado em um repositório técnico

---

# 📂 Estrutura do Projeto

```
Riachuelo-Ciberseguranca-Lab2/
│
├── ransomware/
│   ├── encrypt.py
│   ├── decrypt.py
│   └── test_files/
│       └── exemplo.txt
│
├── keylogger/
│   └── keylogger.py
│
├── requisitosPython.txt
└── README.md
```

---

# 🔐 Ransomware Simulado

Ransomware é um tipo de malware que **criptografa os arquivos da vítima**, impedindo o acesso aos dados até que um pagamento seja realizado.

Neste laboratório foi criado um script que simula esse comportamento através das seguintes etapas:

1. Geração de uma chave de criptografia
2. Criptografia de arquivos de teste
3. Descriptografia posterior utilizando a mesma chave

### Arquivos

**encrypt.py**

Responsável por:

* gerar chave de criptografia
* criptografar arquivos da pasta `test_files`

**decrypt.py**

Responsável por:

* utilizar a chave gerada
* restaurar os arquivos criptografados

### Biblioteca utilizada

```
cryptography
```

Instalação:

```
pip install cryptography
```

---

# ⌨️ Keylogger Simulado

Keyloggers são programas maliciosos que registram tudo que o usuário digita no teclado.

Esses dados podem incluir:

* senhas
* mensagens
* informações confidenciais

Neste laboratório foi implementado um script que:

1. Captura eventos do teclado
2. Registra as teclas pressionadas
3. Salva os dados em um arquivo de log

### Biblioteca utilizada

```
pynput
```

Instalação:

```
pip install pynput
```

### Saída do script

```
log.txt
```

Exemplo de conteúdo registrado:

```
usuario123
senha123
[Key.space]
```

---

# 📧 Simulação de Exfiltração de Dados

Em ataques reais, keyloggers frequentemente enviam as informações capturadas para servidores remotos ou e-mails controlados por atacantes.

Neste laboratório foi demonstrado, de forma educacional, como logs poderiam ser enviados utilizando **SMTP**.

Essa funcionalidade foi utilizada apenas para demonstrar **como a exfiltração de dados pode ocorrer**.

---

# 🛡️ Estratégias de Defesa Contra Malware

Durante o estudo foram analisadas práticas importantes de segurança para prevenir ataques.

## Defesa contra Ransomware

* manter **backups frequentes**
* utilizar **antivírus atualizado**
* aplicar **patches de segurança**
* restringir permissões de usuário
* implementar detecção comportamental
* utilizar soluções de **EDR/XDR**

## Defesa contra Keyloggers

* antivírus com proteção em tempo real
* monitoramento de processos suspeitos
* autenticação multifator (**MFA**)
* evitar instalação de softwares desconhecidos
* treinamento e conscientização de usuários

---

# 🧪 Ambiente de Testes

Este laboratório foi executado em ambiente seguro utilizando:

* máquina virtual
* arquivos de teste
* ambiente isolado

Nenhum dado real foi utilizado.

---

# 📚 Aprendizados Obtidos

Durante o desenvolvimento deste projeto foi possível compreender:

* como ransomwares utilizam **criptografia para sequestrar arquivos**
* como keyloggers capturam **eventos do teclado**
* como malwares podem realizar **exfiltração de dados**
* a importância da **segurança em camadas (Defense in Depth)**

---

# 🚀 Possíveis Melhorias

Algumas melhorias que podem ser implementadas futuramente:

* monitoramento de processos maliciosos
* criação de um painel de análise de logs
* simulação de comunicação com servidor C2
* implementação de técnicas de detecção de comportamento suspeito

---

# ⚙️ Instalação do Projeto

Clone o repositório:

```
git clone https://github.com/christianpinheiro/Riachuelo-Ciberseguranca-Lab2.git
```

Acesse a pasta:

```
cd Riachuelo-Ciberseguranca-Lab2
```

Instale as dependências:

```
pip install -r requisitosPython.txt
```

---

⭐ Projeto educacional voltado ao estudo de **cibersegurança e análise de malware**.
