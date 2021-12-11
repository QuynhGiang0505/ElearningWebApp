console.log('hello world quizaasssssssa')
const url = window.location.href
const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    const user = modalBtn.getAttribute('data-user')
    const course = modalBtn.getAttribute('data-course')
    modalBody.innerHTML = `
    <div class="h5 mb-3 paymentt">Bạn có muốn thanh toán giỏ hàng này? 
    <form>
        <div class="form-group">
            <label for="name">Tên của bạn là</label>
            <input type="text" class="form-control" id="InputName" >
        </div>
        <div class="form-group">
            <label for="bank">Thẻ ngân hàng</label>
            <input type="text" class="form-control" id="InputBank" >
        </div>
        <button type="submit" class="btn btn-primary"id="btnSubmit">Submit</button>
    </form>
    </div>
    `
    const url1 = url + "payment/"
    console.log(url1)
    console.log("r")
    const startBtn = document.getElementById("btnSubmit")
    startBtn.addEventListener('click', () => {
        $.ajax({
            type: 'POST',
            url: `${url}payment/`,
            user: user,
            course: course,
            success: function() {
                console.log("mmmmmmmmmmmmmmmmmmmmmmmmm")
            },
            error: function(error) {
                console.log(error)
            }
        });

    })
}))