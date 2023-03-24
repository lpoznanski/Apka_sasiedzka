document.addEventListener('DOMContentLoaded', function () {
    const formButton = document.querySelector('#form-button')
    const formDiv = document.querySelector('#form-div')
    const form = document.querySelector('#form')
    formButton.addEventListener('click', function () {
        if (form.hasAttribute('style')) {
            form.removeAttribute('style')
            formDiv.setAttribute('style', 'background-color: #E8D33F')
        }
        else {
            form.setAttribute('style', 'display: none')
            formDiv.removeAttribute('style')
        }
    })
})