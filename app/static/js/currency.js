const create_auditing = async card_id => {
    let bank_currency = document.querySelector("#bank_currency").innerText,
        market_currency = document.getElementById("#market_currency").innerText,
        value = document.querySelector("#value").innerText,

    await $.ajax({
        method: "POST",
        url: "/home/sub_cards/",
        headers: {"X-CSRFToken": CSRF},
        data: {
            "type": "create",
            "bank_currency": bank_currency,
            "market_currency": market_currency,
            "tel_number": value,

        }
    })
    .then(res => res.success == 1 ? alert("Created successfully") : alert("Oops, something went wrong..."))
}