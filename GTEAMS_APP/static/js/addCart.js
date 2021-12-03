console.log('hello')
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById("start-button")
const url = window.location.href
console.log(url)
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    const id = modalBtn.getAttribute('data-id')
    const title = modalBtn.getAttribute('data-title')
    const subject = modalBtn.getAttribute('data-subject')
    const cost = modalBtn.getAttribute('data-cost')

    modalBody.innerHTML = `
    <div class="h5 mb-3 cart">Bạn có muốn thêm vào giỏ hàng khóa học: "<b>${title}</b>"
    <div class="text-muted">
        <ul>
            <li>Thuộc khóa học: <b>${subject}</b></li>
            <li>phí mua khóa học là: <b>${cost}</b></li>
        </ul>
    </div>
    `

    startBtn.addEventListener('click', () => {
        addCart(id)
        console.log("success")
        window.location.href = url
    })
}))