const votes = document.querySelectorAll('#votes>button');

votes.forEach((option) => {
    const questionId = option.getAttribute('data-questionId');
    const optionId = option.getAttribute('data-optionId');
    option.addEventListener('click', (e) => {
        send_vote(questionId, optionId);
        votes.forEach((b) => {
            b.removeAttribute('data-clicked');
        });
        e.target.setAttribute('data-clicked', true);
    });
});

function send_vote(questionId, optionId) {
    const url = `http://127.0.0.1:8000/sendvotes/${questionId}/${optionId}/register`;

    fetch(url).then((res) => {
        console.log(res);
        document.getElementById('alert').innerText = res.vote;
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + '=') {
                cookieValue = decodeURIComponent(
                    cookie.substring(name.length + 1)
                );
                break;
            }
        }
    }
    return cookieValue;
}
