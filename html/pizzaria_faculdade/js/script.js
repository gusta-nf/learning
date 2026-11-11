/*
PRIMEIRA FUNCIONALIDADE: Enviar um alerta ao usuário de que a reserva foi realizada ao apertar o botão
SEGUNDA FUNCIONALIDADE: Validador de formulário
*/
const name = document.getElementById("nome")
const mail = document.getElementById("email")
const phone = document.getElementById("telefone")
const button = document.getElementById("botao")
button.addEventListener("click", enviar)

function enviar(){
    // Alerta de quando o formulário foi preenchido corretamente ou errado.
if (validar(name.value) == false){
    alert("O nome foi preenchido incorretamente. Por favor, corrigir para prosseguir!")
    return
}
if (validar(mail.value) == false){
    alert("O e-mail foi preenchido incorretamente. Por favor, corrigir para prosseguir!")
    return
}
if (validar(phone.value) == false){
    alert("O telefone foi preenchido incorretamente. Por favor, corrigir para prosseguir!")
    return
}
alert("A reserva foi feita!")
}

function validar(texto){
    // Validador de campos do formulário
if (typeof texto != "string" || texto.trim() == "" ){
    return false
}
return true
}