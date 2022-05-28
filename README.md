# NET-4U (HACKATHON SECOMP 2022)
Este repositório refere-se ao desenvolvimento de um web-app para a participação do Hackathon da semana de computação (SECOMP) do Instituto Nacional de Telecomunicações - [INATEL](https://inatel.br/home/), patrocinado pela empresa [VIASAT](https://www.viasat.com/pt-br/).

<img src="App/static/styles/assets/logo_azul.png" align="right" width="330">

# NET-4U
Projeto desenvolvido para ajudar pessoas a encontrarem os serviços de provedores de internet mais próximos.

<h4 align="left"> 
	Autores :pencil2:
</h4>

<p align="left">
 <a href="https://github.com/jvoliveirag">João Victor de Oliveira Gomes Ribeiro<br></a> 
 <a href="https://github.com/MaycolTeles">Maycol Teles Costa Dionisio Pereira</a>
</p>

#

## Sumário
* [A ideia](#A-ideia)
* [Funcionamento](#Funcionamento)
* [Pré-Requisitos](#Pré-requisitos)
* [Como executar](#Como-executar)

#

## A ideia :pencil: <a name="A-ideia"></a> 

Ajudar pessoas a encontrarem os serviços de provedores de internet mais próximos de modo prático, rápido e eficaz.

* Hipótese:

	O app NET-4U tem como principal proposta conectar clientes procurando um provedor de internet em sua região com as empresas/instaladores mais próximos, facilitando a comunicação, otimizando tempo e garantindo um serviço de qualidade, partindo do princípio de que o cliente pode avaliar e verificar as avaliações dos trabalhos já prestados, bem como os instaladores podem fazer o mesmo para os clientes antes de aceitar a oferta.

* Premissas:

	1. Buscar um serviço:
		O primeiro e principal recurso do app é o de buscar por um serviço próximo, seja esse serviço um instalador ou um determinado plano de internet.

    2. Verificar planos e condições disponíveis:
		A próxima funcionalidade a ser implementada é a de verificar os planos e condições possíveis naquela respectiva região na qual o cliente se encontra/fez a busca

	3. Agendar/contratar um serviço encontrado:  
		Após buscar e conferir o que há disponível ao seu redor, o cliente pode então agendar/contratar uma instalação no seu local registrado.

		OBS.: Uma funcionalidade para efetuar o pagamento pelo app após a instalação também já foi planejada e em breve pode ser implementada, criando uma experiência ainda mais completa para ambas as partes.

    4. Contactar a empresa/o instalador e vice-versa:
		Por fim, para sanar eventuais dúvidas ou demais assuntos as partes envolvidas podem entrar em contato entre si a fim de evitar conflitos e facilitar a comunicação.

#

## Funcionamento :gear: <a name="Funcionamento"></a>

1. Buscando um serviço:
	A busca por serviços, neste caso, ocorre através do consumo dos dados de uma [API](https://cookie-submarine-e90.notion.site/Rotas-da-API-e790b9219bb44a33a7ec07b5d2cbb613) disponibilizada para o evento que, basicamente, entrega informações pertinentes aos instaladores e planos de internet de acordo o estado. A busca é feita indicando a localização como filtro.
	
2. Verificando planos e condições disponíveis:
	Para verificar então os planos e serviços/instaladores disponíveis a consulta de acordo com o filtro da localização indicada retorna as informações dos respectivos grupos e exibe-as na tela.

3. Agendando um serviço encontrado:
	Após validar as informações e identificar um serviço que o atenda, o cliente pode selecioná-lo e então confirmar para agendar/contrar esse serviço. (Uma mensagem será exibida na tela indicando que o serviço foi agendado - caso o instalador resposável confirme, o cliente receberá uma notificação de que o serviço foi confirmado)

4. Contactando a empresa/o instalador e vice-versa:
	Futuramente será possível gerenciar os serviços contratados (cliente) e prestados (instalador) e também entrar em contato diretamente com o responsável pelo próprio app.
#

## Pré-requitos :white_check_mark: <a name="Pré-requisitos"></a>
* Listar pré-requisitos

#

## Como executar :rocket: <a name="Como-executar"></a>
* Clone este repositório na sua máquina;

#
