"use strict";

const start_btn = document.querySelector(".start_btn button");
const info_box = document.querySelector(".info_box");
const exit_btn = info_box.querySelector(".buttons .quit");
const continue_btn = info_box.querySelector(".buttons .restart");
const quiz_box = document.querySelector(".quiz_box");
const option_list = document.querySelectorAll(".option_list");
const options = document.querySelectorAll(".option_list .option")
const timeText = document.querySelector(".timer .time_left_txt");
const timeCount = document.querySelector(".timer .timer_sec");
const total_que = document.querySelector("footer .total_que");



start_btn.onclick = () => {
    info_box.classList.add("activeInfo"); 
    console.log(options.length)
}


exit_btn.onclick = () => {
    info_box.classList.remove("activeInfo"); 
}


continue_btn.onclick = () => {
    info_box.classList.remove("activeInfo"); 
    let seconds = option_list.length * 60
    time(seconds)
    quiz_box.classList.add("activeQuiz"); 
    total_que.textContent = `${option_list.length} سوال`

}


for (let i = 0; i < options.length; i++) {
    options[i].setAttribute("onclick", "optionSelected(this)");
}

function optionSelected(answer) {
    console.log(answer)
    let radioButton = answer.querySelector('#radios');
    radioButton.checked = true;
}

function time(second) {
    const counter = setInterval(timer, 1000)

    function timer() {
        timeCount.textContent = second;
        second--;
        let addText = timeCount.textContent;
        timeCount.textContent = "ثانیه" + addText; 
        if (second < 0) { 
            clearInterval(counter); 
            timeText.textContent = 'وقتت تموم شد سید'
            for (let i = 0; i < options.length; i++) {
                options[i].classList.add('disabled'); 
            }
        }
    }
}
