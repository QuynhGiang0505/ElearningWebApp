console.log(' world quiz')
const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const scoreBox = document.getElementById('score-box')
const resultBox = document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')
const header = document.getElementById('col1')
var a = false
console.log(a)
const activateTimer = (time) => {
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(() => {
        seconds--
        if (seconds < 0) {
            seconds = 59
            minutes--
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0' + minutes
        } else {
            displayMinutes = minutes
        }
        if (seconds.toString().length < 2) {
            displaySeconds = '0' + seconds
        } else {
            displaySeconds = seconds
        }
        if (a == true) {
            setTimeout(() => {
                clearInterval(timer)
            }, 500)
        }
        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(() => {
                clearInterval(timer)
                alert('Đã hết thời gian, bài làm của bạn sẽ được tự động nộp')
                sendData()
            }, 500)
        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000)
}

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function(response) {

        const data = response.data
        data.forEach(el => {

            for (const [question, answers] of Object.entries(el)) {
                q = question.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;")

                quizBox.innerHTML += `
                    <hr>
                    <div style="color:white;" class="mb-2">
                        <b >${q}</b>
                    </div>
                `
                answers.forEach(answer => {
                    a = answer.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#039;")
                    quizBox.innerHTML += `
                        <div >
                            <input type="radio" class="ans" id="${q}-${a}" name="${q}" value="${a}">
                            <label for="${q}">${a}</label>
                        </div>
                    `
                })
            }
        });
        activateTimer(response.time)

    },
    error: function(error) {
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response) {
            const results = response.results
            quizForm.classList.add('not-visible')
            scoreBox.innerHTML = `Điểm số của bạn là: ${response.score}%`

            results.forEach(res => {
                const resDiv = document.createElement("div")
                for (const [question, resp] of Object.entries(res)) {

                    resDiv.innerHTML += question
                    const cls = ['container', 'p-3', 'text-light', 'h6']
                    resDiv.classList.add(...cls)

                    if (resp == 'not answered') {
                        resDiv.innerHTML += '- not answered'
                        resDiv.classList.add('bg-danger')
                    } else {
                        const answer = resp['answered']
                        const correct = resp['correct_answer']

                        if (answer == correct) {
                            resDiv.classList.add('bg-success')
                            resDiv.innerHTML += ` answered: ${answer}`
                        } else {
                            resDiv.classList.add('bg-danger')
                            resDiv.innerHTML += ` | correct answer: ${correct}`
                            resDiv.innerHTML += ` | answered: ${answer}`
                        }
                    }
                }
                resultBox.append(resDiv)
            })
        },
        error: function(error) {
            console.log(error)
        }
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    a = true
    console.log(a)
    sendData()
})
quizForm.addEventListener('reset', e => {
    e.preventDefault()
    window.location.href = url
})