document.addEventListener('DOMContentLoaded', function () {
    const formButton = document.querySelector('#form-button')
    const formDiv = document.querySelector('#form-div')
    formButton.addEventListener('click', function () {
        const newForm = document.createElement('form')
        newForm.innerHTML = {{ form }}
        formDiv.appendChild(newForm)
    })
})