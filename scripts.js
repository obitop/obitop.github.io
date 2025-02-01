const num = document.getElementById("number")
fahr = document.getElementById("fahr")
cele = document.getElementById("cele")
result = document.getElementById("result")


function convert() {
    if (fahr.checked) {
        temp = Number(num.value)
        temp = temp * 9 / 5 + 32
        result.textContent = parseFloat(temp.toFixed(3)) + " fahrenheit"
    }
    else if (cele.checked) {
        temp = Number(num.value)
        temp = (temp - 32) * (5 / 9)
        result.textContent = parseFloat(temp.toFixed(3)) + " celesius"
    }
}
