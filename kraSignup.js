document.querySelector('#cancelbtn').addEventListener('click', exit);
function exit(){
    let question;
    question = alert('Are you sure you want to Quit?');
    let answer = 'ok';
    let page = 'modalSignup.html';
    if(answer == 'ok'){
        document.location='kra_start.html'
    }
}


