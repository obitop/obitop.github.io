const num = document.getElementById("number")
const fahr = document.getElementById("fahr")
const cele = document.getElementById("cele")
result = document.getElementById("result")

fahr.textContent = "celesius -> fahr"
cele.textContent = "fahr -> celesius"

function convert() {
    if (fahr.checked) {
        temp = Number(num.value)
        temp = temp * 9 / 5 + 32
        result.textContent = temp + " fahrenheit"
    }
    else if (cele.checked) {
        temp = Number(num.value)
        temp = temp - 32 * 5 / 9
        result.textContent = temp + " celesius"
    }
}
