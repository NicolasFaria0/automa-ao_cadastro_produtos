# Automação de Cadastro de Produtos com Python e PyAutoGUI

Este script automatiza o processo de login e cadastro de produtos em um sistema web utilizando as bibliotecas `pyautogui`, `pandas` e `time`. A partir de um arquivo CSV contendo informações dos produtos, o script preenche automaticamente os campos no formulário da aplicação web.

---

## 🚀 Funcionalidades

- Abre o navegador Google Chrome.
- Acessa automaticamente a URL de login da plataforma.
- Realiza login no sistema com credenciais padrão.
- Insere informações de produtos em um formulário web, baseando-se nos dados de um arquivo CSV.
- Rola a página para garantir visibilidade de campos e botões.

---

## 📋 Pré-requisitos

Certifique-se de ter o seguinte instalado e configurado no seu sistema:

1. **Python 3.x**: [Baixe aqui](https://www.python.org/downloads/)
2. **Bibliotecas necessárias**: Execute o comando abaixo para instalar as dependências do projeto:

    ```bash
    pip install pyautogui pandas
    ```

3. **Arquivo CSV**: Um arquivo chamado `produtos.csv` contendo as colunas:
    - `codigo`
    - `marca`
    - `tipo`
    - `categoria`
    - `preco_unitario`
    - `custo`
    - `obs` (opcional)

Exemplo de estrutura do arquivo CSV:

| codigo | marca  | tipo   | categoria | preco_unitario | custo | obs            |
|--------|--------|--------|-----------|----------------|-------|----------------|
| 001    | MarcaX | TipoA  | Cat1      | 10.50          | 5.25  | Produto Novo   |
| 002    | MarcaY | TipoB  | Cat2      | 20.00          | 10.00 | Promoção       |

---

## 🛠️ Como usar

1. Clone este repositório ou copie o código fornecido.
2. Certifique-se de que o arquivo `produtos.csv` está no mesmo diretório do script.
3. Execute o script com o comando:

    ```bash
    python script.py
    ```

4. O script irá:
    - Abrir o navegador.
    - Navegar até a URL do sistema.
    - Realizar login com o usuário e senha padrão (`aluno`).
    - Inserir os dados do arquivo CSV no formulário.

---

## ⚠️ Observações importantes

- **Coordenadas do mouse**: As posições `x` e `y` nos comandos `pyautogui.click` e `pyautogui.scroll` são específicas para a resolução e layout da tela. Caso o script não funcione corretamente, ajuste as coordenadas utilizando o método `pyautogui.position()` para capturar as posições corretas.

- **Segurança**: As credenciais de login (`aluno`) estão hardcoded no script. Para maior segurança, utilize variáveis de ambiente ou arquivos de configuração.

---

## 📚 Bibliotecas utilizadas

- **pyautogui**: Para automação de cliques, teclas e navegação.
- **pandas**: Para manipulação e leitura do arquivo CSV.
- **time**: Para inserir atrasos entre comandos, garantindo a execução correta.

---

## 🖥️ Demonstração

Este script pode ser adaptado para automatizar outros sistemas ou processos repetitivos. É ideal para tarefas que envolvem inserção manual de dados em massa.

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar conforme necessário.

---

## ✉️ Contato

- **Autor**: Nicolas Fernando Sganzerla Faria  
- **E-mail**: [nicolasffaria@hotmail.com](mailto:nicolasffaria@hotmail.com)  
- **LinkedIn**: [Perfil](https://www.linkedin.com/in/nicolas-faria-4b7912320/)

