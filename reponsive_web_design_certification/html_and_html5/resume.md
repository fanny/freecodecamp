`<!-- -->`
- Uso:
    Definem os comentários em um arquivo html.

`<h1>, <h2>, <h3>, <h4>, <h5>, <h6> de header n`
- Uso:
    Definem cabeçalhos no nosso html, quanto maior o numero, menor o tamanho da fonte. O h1, é usado como cabeçalho principal, enquanto os outros são os subcabeçalhos ou subtitulos.

- Características:


`<p> de paragraph`
- Uso:
    Definem o paragrafo de um texto.

- Características

`<header>`
- Uso:
- Características:

`<footer>`

- Uso:
- Características:

`<nav>`

- Uso:
- Características:

`<article>`

- Uso:
- Características:

`<section>`

- Uso:
- Características:

`<aside>`

- Uso:
- Características:

`<main>`
- Uso:
    Define o conteúdo principal do html.
- Características:

`<img> de image`
- Uso:
    Definem imagens no nosso html.
- Atributos:

    `alt`: define uma breve descrição acerca da imagem, caso o browser tenha problemas ao carregá-la.

    `src`: define o local onde a imagem se encontra.
- Características:
    São **self-closing**

`<a> de anchor`
- Uso:
    Definem links em nossa página, podemos definir tanto links externos quanto links internos, para os externos basta colocarmos a URL, para os internos, a sintaxe é `#id_elemento`.
- Atributos:

    `href`: Define o alvo do  link.

    `target`: define se o link será carregado em uma nova página, caso seu valor seja `_blank`, ou na mesma página caso esse atributo não seja definido.
- Características:

`<ol> de ordered list`:
- Uso:
    Define uma lista ordenada no nosso html
- Características

`<ul> de unordered list`
- Uso:
    Definem uma lista não ordenada. `<li> de list item` define um item ou elemento dessa lista.
- Características


`<input>`
- Uso: 
    Definem um campo para receber entradas do usuário.
- Atributos:
    `type`: define o tipo do input, caso definido como `text` define um campo de texto, quando definido
    como:
        - `radio`: dão uma opção de resposta em relação a várias. Todos os botões devem ter o mesmo atributio `name`, selecionando um deles automaticamente irá desmarcar os outros. É sempre uma boa prática colocar os inputs envolvidos por uma label, de modo que o `for` dela aponte para o `id` do elemento, isso permite a algumas tecnologias criarem uma relação associativa, entre o `input` e a `label`.        
        - `checkbox`: Funciona de modo semelhante ao radio, no entanto,  podem ter mais de uma resposta em relações as opções. Permanecem as configurações do `name` e da `label`. 
        *É possível definir uma opção default com o atributo `checked`.*
        
    `placeholding`: define o texto exibido no plano de fundo do input, antes do usuário digitar alguma coisa. 
    
    `required`: define o campo como obrigatório.
- Características:
    São **self-closing**

`<form>`
- Uso:
    Definem como enviar os dados para um servidor.
- Atributos:
    `action`: define a url onde o form será submetido.
- Características

`<button>`
- Uso:
    Definem botões.
- Atributos:
    `click`: define a ação do botão.
- Características:


