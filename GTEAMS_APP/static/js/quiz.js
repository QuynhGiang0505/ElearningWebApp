console.log('hello')
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById("start-button")
const url = window.location.href
modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    const topic = modalBtn.getAttribute('data-topic')
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-question')
    const scoreToPass = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = `
    <div class="h5 mb-3">Bạn có muốn bắt đầu ngay bây giờ "<b>${name}</b>"
    <div class="text-muted">
        <ul>
            <li>Number of question: <b>${numQuestions}</b></li>
            <li>Thời gian làm bài: <b>${time} phút </b></li> 
            <li>Điểm để hoàn thành bài kiểm tra: <b>${scoreToPass}</b></li>
        </ul>
    </div>
    `

    startBtn.addEventListener('click', () => {
        window.location.href = url + topic
    })
}))