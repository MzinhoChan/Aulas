const idade= parseInt("Digite a sua idade: ");
const elementoH2 = document.getElementById("nomeUsuario");

if (idade > 18) {
    elementoH2.insertText = "Você é maior de idade."
} else {
    elementoH2.innerText = "Você é menor de idade."
}
