const searchForm = document.getElementById("searchForm");
const searchInput = document.getElementById("searchInput");

searchForm.addEventListener("submit", function (event) {

    event.preventDefault();

    const pesquisa = searchInput.value
        .trim()
        .toLowerCase();

    if (!pesquisa) {
        return;
    }

    const secoes = document.querySelectorAll("main section");

    let encontrou = false;

    secoes.forEach(function (secao) {

        const texto = secao.innerText.toLowerCase();

        if (!encontrou && texto.includes(pesquisa)) {

            secao.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

            encontrou = true;
        }
    });

    if (!encontrou) {
        alert("Não encontramos nenhum conteúdo relacionado à sua pesquisa.");
    }
});