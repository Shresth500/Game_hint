let question_el=document.getElementById("Question-el")
let clues_el = document.getElementById("Clues-el")
let dead = document.getElementById("dead-ends-el")
let solution = document.getElementById("solution-el")
let hint = document.getElementById("hint-el")
let ans = document.getElementById("ans-el")
let inp = document.getElementById("input-el")
let warn = document.getElementById("warning-id")
let btn1,btn2,btn3
var image_url = "{{ image_url }}";

score = 0

let flag=false

btn1 = document.createElement("button")
btn1.innerHTML = "Clues for the question"
btn2 = document.createElement("button")
btn2.innerHTML = "Click here for answer"

count=0;

var questions = [0]
var clues = [["Short cut always lead to failure",
                "Red sign is a sign of failure",
            "Blue Sign is a sign of success"]]

console.log(clues[0])

var answer = ["Right"]
var images =["River.png"]

i = 0

let dead_ends=2, clues_number = 5
let answer_number=1

function start_game(){
    flag=true
    warn.textContent = ""
    document.body.appendChild(btn1);
    document.body.appendChild(btn2);
    btn1.onclick = function(){
        if(count < clues.length && clues_number > 0 ){
            if(i < clues[count].length && clues_number > 0){
                score -= 1
                hint.textContent += "\n HINT - " + String(i+1) + " " + clues[count][i];
                i+=1 ;
                clues_number-=1
                clues_el.textContent = "NUMBER OF CLUES - " + String(clues_number)
            }
            else{
                hint.textContent += "No more clues to give"
            }
        }
    }
    btn2.onclick = function(){
        if(answer_number > 0){
            score-=5
            ans.textContent = answer[count]
            answer_number-=1
            solution.textContent = "SOLUTION - " + String(answer_number)
        }
        else{
            ans.textContent+="No more attempts\n"
        }
    }
    document.getElementById("images-el").textContent = "In the Image what will be the path you will take";
    document.getElementById("para").style.height = "500px"
    document.getElementById("para").style.width = "500px"
    document.getElementById("para").src = "http://127.0.0.1:8000/Images/Images/River.png";
}
function submit(){
    if(!flag){
        warn.textContent = "First Click on start button"
    }
    else{
        if(inp.value === ""){
            warn.textContent = "Write Something here"
        }
        else{
            if(dead_ends === 0 || count === questions.length){
                document.getElementById("para").src = ""
                document.getElementById("para").style.height = "0px"
                document.getElementById("para").style.widtg = "0px"
                document.querySelector('#sub-el').addEventListener('click', function(event) {
                    event.preventDefault(); // prevent default behavior
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', '/start_game/', true);
                    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                    xhr.onreadystatechange = function() {
                        if (xhr.readyState === 4 && xhr.status === 200) {
                            console.log(xhr.responseText); // log response from Django view
                        }
                    };
                    var data = 'score=' + encodeURIComponent(score); // set score data in request body
                    xhr.send(data); // send AJAX request
                });
                window.location.href = '/ends/';

            }
            if(inp.value != answer[count]){
                score-=2
                dead_ends-=1
                dead.textContent = "NUMBER OF DEAD ENDS - " + String(dead_ends)
            }
            else{
                warn.textContent = "Your Answer is Correct"
                document.getElementById("para").src = ""
                document.getElementById("para").style.height = "0px"
                document.getElementById("para").style.widtg = "0px"
                count+=1
                document.body.removeChild(btn1);
                document.body.removeChild(btn2);
            }
            if(dead_ends === 0 || count === questions.length-1){
                document.getElementById("para").src = ""
                document.getElementById("para").style.height = "0px"
                document.getElementById("para").style.widtg = "0px"
                document.querySelector('#sub-el').addEventListener('click', function(event) {
                    event.preventDefault(); // prevent default behavior
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', '/start_game/', true);
                    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
                    xhr.onreadystatechange = function() {
                        if (xhr.readyState === 4 && xhr.status === 200) {
                            console.log(xhr.responseText); // log response from Django view
                        }
                    };
                    var data = 'score=' + encodeURIComponent(score); // set score data in request body
                    xhr.send(data); // send AJAX request
                });
                window.location.href = '/ends/';
            }
        }
    }
}