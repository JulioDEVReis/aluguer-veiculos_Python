# aluguer-veiculos_Python

Projeto de final de curso Python, com o seguinte contexto, passado pela Tokyo School:
A Luxury Wheels, é uma empresa de aluguer de carros que deseja desenvolver um site, onde os clientes deverão conseguir registar-se e alugar um veículo, e uma app para a gestão da frota, a partir do qual a empresa consiga gerir todos os seus veículos.

Foram dadas 3 propostas para criação desse projeto final:
Proposta A: Assumir a responsabilidade do desenvolvimento do site, onde os clientes da Luxury Wheels deverão conseguir registar-se e alugar um veículo. 
OU
Proposta B: Assumir a responsabilidade do desenvolvimento de uma app, pela qual a Luxury Wheels consiga gerir a sua frota de veículos.
OU
Proposta C: Assumir a responsabilidade de desenvolvimento do site e também da app, tendo em conta que és um profissional completo e  queres demonstrar isso como reflexo da proatividade no trabalho.

De forma a melhor aplicar o conhecimento e continuar o aprendizado, escolhi a PROPOSTA C, por justamente ser a mais completa e mais desafiadora.

Alguns requisitos foram determinados para a elaboração do projeto:

Desenvolvimento do site:
1. Vai ser necessário a criação de uma aplicação web (site) como forma do utilizador alugar o veículo.
2. Vamos ter de organizar toda a informação necessária para o projeto em bases de dados em SQL (os veículos da empresa e clientes).
3. Através do site, os clientes terão categorias (gold, silver e económico) e deveremos ter uma forma de autenticar o cliente, que consoante a sua categoria (podes definir por filtro de valores em que o cliente está disposto a pagar), terá acesso aos veículos correspondentes ao mesmo. 
4. A ideia é que o cliente consiga realizar uma transação do início ao fim dentro do teu site, inclusive que seja finalizado o pagamento e agendamento de recolha do veículo.

Desenvolvimento do App Desktop:
1. Através da app, os gestores devem conseguir aceder a todos os veículos que podem ser alugados pelos clientes, e visualizar se estão disponíveis ou alugados, e a que categoria correspondem.
2. Vamos ter de organizar toda a informação necessária para o projeto em bases de dados em SQL.
3. Os veículos desgastam-se. A empresa deve receber um alerta da necessidade de manutenção, para cada veículo (podes colocar uma data de última revisão e próxima revisão na base de dados). Deverá haver uma opção de manutenção que ao ser acionada, o veículo fica indisponível por 30 dias (e durante esta fase, não pode ser alugado pelo cliente).
4. É necessário legalizar os veículos. Cada veículo deverá ter associado a data na qual foi feita a sua última legalização e a próxima data para a sua legalização, na qual um valor de 250€ para carros e 150€ para motas, terá de ser pago pela empresa. No caso da data se aproximar, deverá ser apresentado um alerta. Podes ter em consideração, neste ponto, que é necessário anualmente a legalização do veículo.
5. Teremos de ter atenção ao estoque. É esperado que o cliente da Luxury Wheels tenha sempre 5 veículos disponíveis para escolher.

## Minha Solução:

### APP WEB:
1. Tecnologias utilizadas:
	- Flask (Framework usado para o desenvolvimento do site)
	- SQLAlchemy (acesso e manipulação do banco de dados SQL com o Flask)
	- FlaskForm e WTForms (customização de formulario de cadastro de usuario e integração com o Flask)
	- Flask Bcrypt (para criptografia das senhas do usuário - Hash - entre o banco de dados e a aplicação)
	- Flask Migrate (para lidar com migrações de banco de dados SQLAlchemy para aplicativos Flask usando alembic)
	- Flask_Login (Para a autenticação e gestão do usuário)
	- Bootstrap (Livraria de componentes gráficos e paginador de desenho)
	- Jinja (Motor de renderização de páginas web).
	- Bootstrap (Estilização da minha página Web)

![Captura de tela 2023-12-01 191404](https://github.com/JulioDEVReis/aluguer-veiculos_Python/assets/142347463/9c125d32-4d0f-477f-876d-3a7ce4306092)

2. Passo a passo como eu desenvolvi o projeto:
	- Precisei desenvolver separadamente os projetos, Web e Desktop, mas de forma que pudesse integrar o Banco de Dados entre os dois aplicativos. Todos os desenvolvimentos e estudos sempre levaram em conta isso. Então, para melhor organização e clareza do projeto, já criei os diretórios que precisarei durante a elaboração desse projeto:
		- database: Diretório para inclusão do meu Banco de dados.
		- static: Para criação e armazenamento do meu arquivo de estilos, .css
		- templates: Para a criação dos meus arquivos HTML necessários a esse projeto
	- A escolha do Flask foi em razão da Tokio School concentrar o ensino para esse Framewok. Apesar de conhecer e poder usar o Django, escolhi o Flask apenas por esse motivo. 
	- Iniciamos então nosso servidor web Flask, com o código padrão já para termos nosso roteamento e abertura do site em http://127.0.0.1:5000 durante o desenvolvimento do site.
	- Como precisamos ter um banco de dados, para autenticação dos usuários, inicializei também nosso banco de dados SQLAlchemy, posicionando o cursor para acesso e gestão.
	- Nesse momento, usei o SQLite para criar meu banco de dados dentro da pasta database, através do console da propria IDE, e então voltei ao meu código para indicar o caminho e nome do meu banco de dados para que o SQLAlchemy possa acessá-lo.
	- O planejamento do meu projeto web contava com a criação de páginas HTML usando os estilos do Bootstrap, para o design de cada página. Abaixo descrevo cada página criada, em ordem de criação, em função do planejamento feito para elaboração do projeto:
		- Página principal (index.html): Essa já seria a página de Login do usuário. Como a definição e idéia do projeto é que o usuário pudesse ver os veículos disponíveis de acordo com a categoria cadastrada, minha página principal então não foi uma página contendo os veículos, mas sim a página de login.
		- Página de Registo de usuário (registo.html): Página onde os usuários podem registar-se e escolher a categoria de carros que preferir. A categoria de veículo escolhida irá interferir em quais carros irão aparecer para seleção e reserva para aluguer.
		- Página com os veículos disponíveis, para seleção e aluguer (aluguer.html): Nessa página o usuário poderá escolher o veículo para aluguer. Aparecerão na tela apenas os veículos disponíveis, de acordo com a categoria a qual se registou. O usuário então, já logado, poderá selecionar a data de retirada e devolução do veículo e então clicar no botão para reservar o veículo.
		- Página para pagamento da reserva (pagamento.html): Página voltada para a realização do pagamento pelo usuário, via cartão de crédito ou débito. Inclui a descrição do veículo, data selecionada para retirada e devolução, e valor total a ser pago.
		- Página de confirmação da reserva do veículo (comprovante.html): Página final, para o usuário comprovar a reserva e agendamento e retirar o veículo. Deve incluir as mesmas informações que apareceram no ato do pagamento.
	
![Captura de tela 2023-12-01 191858](https://github.com/JulioDEVReis/aluguer-veiculos_Python/assets/142347463/33ff3035-ed5d-4962-8e92-20fc237310ac)

![Captura de tela 2023-12-01 191916](https://github.com/JulioDEVReis/aluguer-veiculos_Python/assets/142347463/b00ffa69-e80c-456d-847e-36ed99fbaa76)
 
  - Em nosso arquivo Python, criaremos uma função para cada rota que precisaremos. login( ) - '/', register( ) - '/registo, aluguer( ) - '/aluguer/<categoria>', pagamento( ) - '/pagamento/<int:veiculo_id>'  e comprovante( ) - '/comprovante/<int:veiculo_id>'. Cada função então tratará das ações realizadas em cada rota especificada no decorador da função.
	- Como temos também nosso banco de dados já criado, precisamos criar as classes para identificar os dados que estarão nas nossas tabelas, também identificadas. Como nosso banco de dados será compartilhado, entre o aplicativo Web e o aplicativo Desktop, já incluiremos os dados que vamos usar na  gestão da frota, no aplicativo desktop.  As classes então criadas foram:
		- User: Os dados dessa classe são para registo e autenticação do usuário, e estão no banco de dados, na tabela 'users'. Inclui: nome, id, username, email, password e categoria.
		- Veiculo: Os dados dessa classe são para gestão e disponibilidade dos veículos, e estão no banco de dados, na tabela 'veiculos'. Inclui: id, nome, categoria, preço, imagem, quilometragem, manutenção, data inicio manutenção, data final manutenção , licenciamento e disponibilidade.
		- RegistrationForm: Os dados dessa classe são para personalização do nosso registo e posterior inclusão no banco de dados. Tem os mesmos campos presentes no banco de dados User, justamente para que, ao realizar o cadastro, esses dados sejam imputados no banco de dados.
		- LoginForm: São os dados necessários para login do usuário, que serão confrontados com o banco de dados, para dar acesso ao usuário.
		- PaymentForm: São os dados necessários para realizar o pagamento da reserva do veículo escolhido. Em nosso projeto apenas exemplifiquei o processo. Num projeto real utilizaria um dos métodos de pagamento seguros aqui nessa classe.
	- Cada rota então possui uma função e um arquivo HTML para tratar das ações daquele site.
		- index / login: A pagina HTML de login inclui o formulário de login, que busca, utilizando JINJA, os processos de LoginForm( ) da minha função login, para verificar se o username e o password são os registrados no meu banco de dados. Se o login for bem sucedido, redirecionei a pagina para a rota aluguer, para o usuário entrar e ver os veículos de acordo com sua categoria cadastrada.
		- registo: A pagina HTML de registo possui então os campos do formulário de registo que usam RegistrationForm( ) da nossa função register( ). Inclui condições na minha função, justamente para verificar se os campos foram preenchidos e verificar se o email ou o usuário já existem. Os dados são então colocados no banco de dados, na tabela users, e fiz o redirecionamento para a tela de login, assim que completar com sucesso o registo.
                -Aluguer: Nosso arquivo HTML, aluguer.html, inclui um loop for para iterar sobre os veículos disponíveis com a imagem do veículo, categoria, valor diário do aluguer, data para selecionar a retirada e data para selecionar a devolução. Ao final, criei o botão reservar, para cada veículo. Já a função aluguer( ) inicia com a definição de veiculo sendo aquele que estiver na categoria do usuário, e com disponibilidade, justamente para exibir apenas esses veículos na pagina HTML.  Coloquei as condicionais para tratamento e retorno ao usuário em caso das datas selecionadas para retirada e devolução serem menores que a data atual, ou que a data de devolução seja anterior a data da retirada.  Caso tudo estiver selecionado então, e o usuário clique no botão reservar, redireciono ele para a pagina de pagamento.
                - Pagamento: A minha pagina HTML não inclui um método seguro de pagamento por tratar-se de um projeto de final de curso, que não será utilizada de fato, e portanto, fiz um processo simples de pagamento, incluindo as informações sobre o veiculo alugado, as datas de retirada e devolução e o valor total a ser pago. Na minha função pagamento, os campos de preenchimento são então geridos pelo PaymentForm(request.form). Como não trata-se de um sistema real de pagamento, fiz o redirecionamento de qualquer forma para a pagina do comprovante.
               - Comprovante: A pagina do comprovante é também simples, já que, da mesma forma, é apenas para mostrar o resultado final do projeto, não sendo usado por clientes reais. Sendo assim, foi montado algo simples, com as informações da reserva contendo nome do veiculo,  data da retirada e devolução, valor total pago, nome  e email do cliente.

![Captura de tela 2023-12-01 191949](https://github.com/JulioDEVReis/aluguer-veiculos_Python/assets/142347463/6129074b-90ef-4f0d-ba00-3ce66cd1a76b)
![Captura de tela 2023-12-01 192035](https://github.com/JulioDEVReis/aluguer-veiculos_Python/assets/142347463/9c4a6d98-93b8-4bde-b681-8010af6b51d8)

### APP DESKTOP:
1. Tecnologias utilizadas:
	- tkinter (Framework que usamos para desenvolver o app desktop, usado pela Tokio School nos projetos das aulas)
	- sqlite3 (usado para nossa conexão com o bando de dados SQL)
	- pandas (Usamos para gerar relatorios de gestão de usuários e da frota de veículos, em formato Excel).

![Captura de tela 2023-12-01 221453](https://github.com/JulioDEVReis/aluguer-veiculos_Python/assets/142347463/41f50d89-755f-4a3a-8fe6-7a788e0cd218)

2. Passo a passo como eu desenvolvi o projeto:
	- Nosso primeiro passo foi criar o Aplicativo, com o código mínimo, tkinter.
	- Criei então nossa classe Applicattion, com nosso construtor para inicializar nossa janela e executar as funções necessárias para execução do aplicativo.
	-  Criei uma função só para tratar da configuração da janela, com as propriedades utilizadas.
        - A próxima função criada foi para configurar um menu, para sair do aplicativo quando quisermos.
        - Criei então uma função para o Frame de Login, para que apenas o usuário gestor possa entrar e usar o aplicativo. Uma função interna, verificar_login( ), executa ações para verificar se o usuário e a senha digitados no campo são as cadastradas no app, e então concede acesso executando a próxima função, mostra_dashboard( ). Caso contrário, uma janela de erro exibe a mensagem na tela.
        - Após logado, a próxima função é o Dashboard. Assim que logado, a primeira ação é eliminar todos os widgets da janela, para que fique vazia para a inclusão dos widgets nessa função mostra_dashboard( ). Para o Dashboard, planejei a inclusão de informações na tela para o gestor acompanhar, além dos botões para redirecionar para as janelas de gestão de usuários ou gestão de veículos.
Uma das propriedades que aparece no Dashboard para o gestor acompanhar é a indicação do próximo veículo a entrar em manutenção.  Para conseguir fazer isso eu busquei as informações que precisava no banco de dados, principalmente a coluna quilometragem e manutenção na tabela veiculos, e então  iterei sobre cada veículo para calcular a diferença entre a manutenção (Km que fará a manutenção) e a quilometragem atual do veículo. Na iteração eu também inclui uma condição IF para verificar, em relação ao veiculo com menor diferença entre as quilometragens, se o veiculo que esta sendo iterado no momento possui ou não menor quilometragem que o registrado na iteração anterior. Aquele que tem menor diferença de quilometragem fica então registrado em menor_diferenca_manut, guardando o  nome do veiculo e seu ID na variavel veiculo_mais_proximo. Por fim, se há então o veiculo mais proximo ele é colocado na tela do Dashboard. Caso contrário, uma mensagem dizendo que não há veiculos para fazer manutenção fica na tela no lugar.
Outra propriedade que aparece na tela Dashboard é qual o veículo mais próximo a fazer o licenciamento. A função verifica_proximo_licenciamento( ) verifica então, dentre todos os carros, qual aquele que está com data  mais proxima para fazer o licenciamento e coloca no Dashboard para o gestor acompanhar. A lógica é muito similar à de verificar a proxima manutenção, só que agora, ao invés de quilometragem, estamos falando em datas, em relação a data atual.
Por fim, a ultima propriedade que aparece no Dashboard são os veículos que estão disponíveis, por categoria, justamente para o gestor acompanhar a quantidade de veículos disponíveis para os clientes reservarem. Para isso, fui até o banco de dados e extrai todos os veiculos e suas informações para aqueles que possuem disponibilidade, ou seja, sua coluna disponibilidade na tabela veiculos esteja com valor 'sim'. Armazeno todos os veiculos então em uma variavel e faço a iteração com FOR para , em cada veiculo iterado eu verifique sua categoria com IF/ELIF/ELSE, e inclua no label correto os dados do carro, no Dashboard.

![Captura de tela 2023-12-01 221543](https://github.com/JulioDEVReis/aluguer-veiculos_Python/assets/142347463/f1a64282-727e-4e0a-b8e5-184b0bc3e548)

          - A tela Gerir usuários é separada em 2 partes. A primeira parte inclui os campos para inclusão de novos usuários ou pesquisa por usuários existentes no banco de dados, com os botões para limpar os campos do formulário, apagar cliente, alterar o cliente (caso eu modifique alguma informação), buscar cliente, ou ainda voltar para o Dashboard.
Todos esses botões acionam ações sobre o formulário ou então sobre o banco de dados, e para deixar o código mais limpo, incluimos todas essas ações em funções separadas, numa classe criada, chamada Funcs, que passa então a ser uma subclasse da classe Applicattion.
Na segunda parte da janela é nossa tabela com os dados extraídos do banco de dados, da tabela 'users'. Nessa segunda janela, para facilitar os comandos pelo usuário, criamos uma função, na classe Funcs, para implementar a funcionalidade de duplo clique na tabela, e então colocar os dados selecionados nos campos (entrys) da parte superior da janela, facilitando as funcionalidades de apagar ou alterar usuários. funciona muito bem após a pesquisa também. O gestor pode pesquisar, por exemplo, o nome de um usuário e então dar duplo clique no resultado da busca, na segunda parte da janela, para autopreencher os dados todos nos demais campos (entrys) da parte superior, e então poder apagar ou alterar esses dados, clicando no botão correspondente.
Por fim, criei um menu para incluir a funcionalidade de podermos exportar a tabela em formato Excel. 
OBS: Para a inclusão de novos usuários, somente os usuários podem fazer através do Aplicativo Web, em Registo de usuário.

![Captura de tela 2023-12-01 221749](https://github.com/JulioDEVReis/aluguer-veiculos_Python/assets/142347463/8d5a84d9-681b-4f67-8bb5-19d72cbc1aff)

         - A tela Gerir Veículos é muito similar a tela de gestão de usuários, com as mudanças para as propriedades existentes na tabela veículos, do banco de dados SQL.
A lógica para todos as funcionalidades é a mesma, tendo apenas como particularidade a possibilidade de inclusão de veículos novos
A diferença nas funções da classe Funcs, além da mudança das propriedades existentes na coluna veiculos do banco de dados, é a inclusão de 2 funções que não existem para a gestão de usuários, que é a inclusão de veiculos no banco de dados e a atualização da disponibilidade do veiculo (UPDATE veiculos SET disponibilidade = 'nao' WHERE quilometragem = manutencao OR ? BETWEEN data_inicio_manut AND data_final_manut), ou seja, muda a coluna disponibilidade para 'não', caso o veiculo esteja com a mesma quilometragem da quilometragem registrada na manutenção ou então esteja dentro do periodo de data de inicio e final da manutenção.

![Captura de tela 2023-12-01 221715](https://github.com/JulioDEVReis/aluguer-veiculos_Python/assets/142347463/04544338-73e9-47de-ac5f-81b27624866d)
