
function revealCard(n){
    let card_to_reveal = document.getElementById(n)
    card_to_reveal.style.display = "block"
}

function hideCard(n){
    let card_to_hide = document.getElementById(n)
    card_to_hide.style.display = "none"
}