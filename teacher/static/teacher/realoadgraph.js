const questionid = document
    .querySelector('[data-questionid]')
    .getAttribute('data-questionid');

function get_votes(qid) {
    const url = `http://127.0.0.1:8000/teacher/${qid}/data`;

    fetch(url)
        .then((response) => response.json())
        .then((datatxt) => {
            const data = datatxt.data;
            const total = datatxt.total;

            for (opt in data) {
                const optiondiv = document.querySelector(
                    `div[data-option="${opt}"]`
                );
                const progress = optiondiv.querySelector('.progress');
                const toast = optiondiv.querySelector('.toast');

                const num = data[opt];

                progress.style.width = `${(num / total) * 100}%`;
                toast.innerHTML = num;
            }
        });
}
