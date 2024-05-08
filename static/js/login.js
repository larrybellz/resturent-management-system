//to implement the password toggle

const passwordField=document.querySelector('#passwordField');
const showPasswordbtn=document.querySelector('#showbtn')



showPasswordbtn.addEventListener('click',()=>{
    console.log('test')
    if (showPasswordbtn.innerHTML==='SHOW'){
        showPasswordbtn.innerHTML='HIDE'
        passwordField.setAttribute('type','text')

    }
    else{
        showPasswordbtn.innerHTML='SHOW'
        passwordField.setAttribute('type','password')
    }


})