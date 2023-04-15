async function get_vote(questionId) {
    const url = `http://127.0.0.1:8000/teacher/${questionId}/data`;

    const response = await fetch(url);
    const jsonData = await response.json();
    return jsonData.data;
    // const votes = await jsonData.get('data');
}

function plot_answer(jsondata) {
    const datax = Object.keys(jsondata);
    const datay = Object.values(jsondata);
    const maxy = Math.max(...datay);
    var data = [
        {
            x: datax,
            y: datay,
            type: 'bar',
        },
    ];

    layout = { yaxis: { tickvals: [...Array(maxy + 1).keys()] } };
    Plotly.newPlot('plot', data, layout);
}

var intervalId = window.setInterval(async function () {
    const data = await get_vote(1);
    plot_answer(data);
}, 5000);
