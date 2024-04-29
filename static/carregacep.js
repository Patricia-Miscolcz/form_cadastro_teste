//recebe o elemento botao do HTML
const botaoConsultar = document.getElementById('pesquisar') /*botão id="pesquisar"*/

//função para escrever os dados de endereço obtidos da API CEP
const setDadosForm = function(dados){
    let rua = document.getElementById('logradouro')
    let bairro = document.getElementById('bairro')
    let cidade = document.getElementById('cidade')

    rua.value = dados.logradouro
    bairro.value = dados.bairro
    cidade.value = dados.localidade

}

//função para consumir os dados de uma API de CEP
const getDadosCepAPI = async function (numeroCep){

    let url = 'https://viacep.com.br/ws/'+numeroCep+'/json/'

    /*outra forma de usar, URL da API do via CEP utilizando a concatenação reduzida de variáveis:*/
    /*let url = `https://viacep.com.br/ws/${numeroCep}/json/`*/

    //executa a url da API e aguarda (await) o retorno do servidor
    
    const response = await fetch(url) 

    //convertendo o resultado obtido em formato JSON
    const dadosCep = await response.json()

    //chama a função para colocar os dados da API no Form
    setDadosForm(dadosCep)
}

//função para pegar o cep digitado no formulário
const getCepForm = function(){

    //recebe o valor do CEP digitado pelo usuário   id="input-cep"
    let cep = document.getElementById('input-cep')
    if(cep.value == '')
        alert('Não é possível consultar o CEP em branco.')
    else
        getDadosCepAPI(cep.value)
}


//adiciona um evento de click no botao de consultar
botaoConsultar.addEventListener('click', function(){

   //chama a função que vai receber o CEP digitado
   getCepForm()
})