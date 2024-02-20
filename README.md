# zomato_project

Bem-vindo ao meu primeiro projeto de análise de dados como estudante de ciência de dados! Neste projeto, tive a oportunidade de mergulhar em dados do mundo real da "No Hunger", um marketplace de restaurantes, para descobrir insights valiosos acerca dos dados.

Como um aspirante a cientista de dados, este projeto marcou um marco significativo em minha jornada de aprendizado e aplicação de técnicas de ciência de dados para resolver problemas práticos de negócio. Com orientação, embarquei neste projeto com entusiasmo e sede de conhecimento, ansiosa para colocar as habilidades aprendidas durante minha jornada no curso de Formação em Data Science à prova e fazer contribuições significativas.

Os objetivos deste projeto foram: primeiro, obter experiência prática na condução de análises de dados de ponta a ponta, desde a limpeza de dados até a análise exploratória de dados e visualização; e segundo, fornecer insights acionáveis que pudessem ajudar na tomada de decisões e impulsionar o crescimento do negócio para a "No Hunger".

Ao longo deste projeto, encontrei vários desafios e oportunidades de aprendizado, desde o tratamento de dados até a descoberta de padrões e tendências ocultas. Cada obstáculo me impulsionou a expandir meu arsenal analítico e aprimorar minhas habilidades de resolução de problemas.

Neste relatório, vou guiá-lo pelo processo da minha análise, destacando insights derivados dos dados. Desde entender a distribuição de restaurantes entre países e cidades até explorar as relações entre tipos de culinária e avaliações de clientes. Vamos lá:

A. Problema de negócio

A empresa “No Hunger” é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da “No Hunger”, disponibilizando informações como endereço, tipo de culinária servida, disponibilidade de reservas e entregas, além de uma avaliação dos serviços e produtos oferecidos. 

O recém-contratado CEO, Guerra, busca compreender profundamente o negócio para tomar decisões estratégicas assertivas e impulsionar o crescimento da empresa. Para isso, é necessária uma análise nos dados da empresa e a criação de dashboards para melhor entendimento da empresa, de modo que ele seja capaz de tomar decisões mais assertivas. O objetivo do projeto é:

1. Identificar a amplitude do mercado atendido pela empresa e a distribuição geográfica dos restaurantes cadastrados, fornecendo uma visão inicial do panorama global da plataforma.
2. Avaliar o engajamento dos usuários com a plataforma, analisando a quantidade e o teor das avaliações recebidas pelos restaurantes.
3. Entender a diversidade de opções gastronômicas oferecidas, destacando os diferentes estilos de culinária disponíveis para os usuários.
4. Identificar padrões e tendências geográficas, como a receptividade em diferentes países e regiões, para orientar futuras estratégias de expansão.
5. Analisar a densidade e popularidade dos restaurantes em áreas urbanas específicas, além da qualidade dos estabelecimentos com base em avaliações de clientes.
6. Avaliar o desempenho individual dos restaurantes em métricas como quantidade de avaliações, média de avaliação e preços, permitindo a identificação de áreas de melhoria.
7. Investigar as preferências gastronômicas dos usuários, identificando as culinárias mais populares e a qualidade dos restaurantes em cada categoria

Essa análise abrangente permitirá que o CEO Guerra compreenda melhor o desempenho e a diversidade da plataforma "No Hunger", fornecendo insights valiosos para decisões estratégicas e melhorias contínuas. 

B. Premissas de negócio

a.	A análise foi realizada com dados de outubro de 2019.
b.	O modelo assumido foi um marketplace de restaurantes.
c.	As visões de negócio incluíram: Visão de cidades, Visão de países e Visão de culinárias

C. Estratégia de solução

Para abordar o problema em questão, realizei a limpeza e a preparação dos dados, incluindo a padronização dos nomes das colunas para seguir uma padronização, a remoção de valores ausentes e a atribuição dos nomes dos países com base nos códigos correspondentes.

Posteriormente, desenvolvi um painel estratégico que se baseia em métricas chave para proporcionar uma compreensão abrangente do modelo de negócio da empresa. Este painel se concentra em três principais visões:

a. Visão de Distribuição por País: Nesta análise, focamos na visualização dos dados por país, permitindo uma seleção flexível de países específicos através de um filtro lateral. Isso nos permite entender a distribuição geográfica dos restaurantes e identificar padrões ou discrepâncias entre diferentes regiões.

b. Visão de Distribuição por Cidade: Aqui, o foco está na distribuição dos registros por cidade. Mais uma vez, fornecemos a capacidade de filtrar os resultados por país, permitindo uma análise mais detalhada da presença e popularidade dos restaurantes em diferentes áreas urbanas.

c. Visão de Distribuição por Tipo de Culinária: Esta visão nos permite analisar a distribuição dos registros com base nos tipos de culinária oferecidos pelos restaurantes. Com a capacidade de filtrar por país e tipo de culinária, podemos identificar tendências gastronômicas e avaliar a popularidade de diferentes estilos culinários em diferentes regiões.

Ao adotar essa estratégia de solução, buscamos fornecer insights valiosos que possam orientar as decisões estratégicas da empresa e impulsionar seu crescimento contínuo.

D. Top 3 insights

1. Embora a Índia tenha o maior número de cidades e restaurantes registrados, incluindo estabelecimentos com as mais altas avaliações, a culinária indiana não se destaca como uma das melhores em termos de média geral de avaliações em comparação com outras cozinhas do mundo.

Ao perceber que a culinária indiana, apesar de sua abundância, não está entre as mais bem avaliadas globalmente, o CEO pode decidir explorar estratégias para diversificar o catálogo de restaurantes, promovendo outras cozinhas que possam atrair mais clientes ou melhorar a qualidade dos restaurantes indianos

2. A Índia abriga tanto os restaurantes mais bem avaliados quanto os menos bem avaliados, refletindo uma variação significativa na qualidade da comida.

O CEO pode, dessa forma, investir em programas de qualidade sou revisar critérios de seleção de estabelecimentos para melhorar a consistência e qualidade do serviço oferecido ao cliente.

4. Apesar da Indonésia ter uma das menores contagens de restaurantes registrados, ela se destaca por ter a maior quantidade de avaliações, sugerindo um alto nível de engajamento dos usuários. Além disso, os restaurantes na Indonésia tendem a ter um preço médio por refeição para dois superior, indicando uma disposição para gastar mais em experiências gastronômicas.

Isso pode indicar uma oportunidade de aumentar os esforços de marketing nesse país ou de expandir parcerias estratégicas com restaurantes premium para impulsionar o crescimento das receitas.

E. O produto final do projeto

O produto final do projeto é um painel online, hospedado em Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através do link: https://zomatoproject-jessicanadalete.streamlit.app/

F. Conclusão

A análise métrica realizada neste projeto forneceu insights valiosos sobre diversos aspectos das operações da empresa e do cenário de mercado. 

Em primeiro lugar, é evidente que o mercado indiano conta com um número substancial de cidades e restaurantes registrados. No entanto, apesar dessa abundância, a culinária indiana não figura consistentemente entre as mais bem avaliadas globalmente. Isso sugere uma oportunidade potencial para diversificação nas ofertas de restaurantes para atender a uma gama mais ampla de preferências dos consumidores.

Em segundo lugar, a variabilidade nas avaliações de restaurantes dentro da Índia destaca a importância de iniciativas de gestão de qualidade e aprimoramento da experiência do cliente. Abordar essa variabilidade pode contribuir para uma percepção mais consistente e favorável dos serviços da empresa entre os consumidores.

Por último, os altos níveis de engajamento e disposição para gastar mais em experiências gastronômicas na Indonésia destacam a importância desse mercado no impulsionamento do crescimento da receita. A expansão dos esforços de marketing e a formação de parcerias estratégicas com restaurantes na Indonésia poderiam capitalizar ainda mais essas tendências.

Em conclusão, os insights obtidos a partir da análise métrica destacam a importância da tomada de decisões orientada por dados, promovendo iniciativas estratégicas e no fomento à expansão do negócio. Ao aproveitar essas descobertas, a empresa pode refinar suas estratégias, aprimorar a eficiência operacional e, em última análise, impulsionar um crescimento sustentável no mercado competitivo.

G. Próximos passos

Como próximos passos para melhoria da solução:

a. Adicionar "Estratégia do Negócio" como nova visão de negócio por meio da analise da popularidade dos restaurantes e das avaliações dos clientes;
b. Adicionar novas métricas para melhor compreensão dos dados, como por exemplo, análise de insights dos textos das avaliações fazendo um paralelo com as notas de avaliação, além da incorporação de métricas relacionadas ao intervalo de preços dos restaurantes, como por exemplo a comparação dos preços com a concorrência.
