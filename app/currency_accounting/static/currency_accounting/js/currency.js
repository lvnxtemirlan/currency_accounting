const create_auditing = async () => {
    let bank_currency = document.querySelector("#bank_currency").value,
        market_currency = document.querySelector("#market_currency").value,
        value = document.querySelector("#value").value;

    console.log(bank_currency);
    console.log(market_currency);
    console.log(value);

    await $.ajax({
        method: "POST",
        url: "/currency/table/",
        headers: {},
        data: {
            "type": "create",
            "bank_currency": bank_currency,
            "market_currency": market_currency,
            "value": value,
        }
    })
//    .then(res => res.success == 1 ? alert("Created successfully") : alert("Oops, something went wrong..."))
    .catch(err => console.error(err))
}
