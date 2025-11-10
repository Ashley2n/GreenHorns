// https://www.html-code-generator.com/javascript/countdown-timer

//import {handleImageUpload} from "./imageHandler.js";

function getTime(prep_time, cook_time){
    let prep_minutes = prep_time * 60;
    let cook_minutes = cook_time * 60;
    return prep_minutes + cook_minutes
}

function handleImageUpload()
{

const image = document.getElementById("upload").files[0];

    const reader = new FileReader();

    reader.onload = function(e) {
      document.getElementById("display-image").src = e.target.result;
    }

    reader.readAsDataURL(image);

}

let initialTime = getTime(.1, .1)

const TIMER_INTERVAL_MS = 1000;
let countdownInterval;
let timeLeft = initialTime;
let isRunning = false;

const timerDisplay = document.getElementById("timer");
const startPauseBtn = document.getElementById("start-button");
const timeInput = document.getElementById("time-input");


const formatTime = seconds => {
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return [mins, secs].map(unit => String(unit).padStart(2, '0')).join(':');
};

const updateDisplay = seconds => {
    const formatted = formatTime(seconds);
    timerDisplay.textContent = formatted;
    document.title = `Timer: ${formatted}`;
};

// where we will ask for the picture of the food at the end
const onTimeEnd = () => {
    isRunning = false;
    startPauseBtn.textContent = 'Start';
    startPauseBtn.disabled = true;

    const paragraph = document.getElementById("update-user")
    paragraph.innerHTML = `Please take a picture of the food you've created! :D`
};

const startCountdown = () => {
    isRunning = true;
    startPauseBtn.textContent = 'Pause';
    startPauseBtn.disabled = false;
    countdownInterval = setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            updateDisplay(timeLeft);
        } else {
            clearInterval(countdownInterval);
            onTimeEnd();
        }
    }, TIMER_INTERVAL_MS);
};

const pauseCountdown = () => {
    clearInterval(countdownInterval);
    isRunning = false;
    startPauseBtn.textContent = 'Resume';
};

const handleStartPause = () => {
    if (isRunning) {
        pauseCountdown();
    } else {
        if (timeInput?.value) {
            const newTime = parseInt(timeInput.value, 10);
            if (isNaN(newTime) || newTime <= 0) {
                alert("Please enter a valid time in seconds.");
                return;
            }
            initialTime = newTime;
            if (timeLeft === 0 || timeLeft === DEFAULT_TIME) {
                timeLeft = initialTime;
                updateDisplay(timeLeft);
            }
        }
        startCountdown();
    }
};


updateDisplay(timeLeft);

startPauseBtn.addEventListener("click", handleStartPause);