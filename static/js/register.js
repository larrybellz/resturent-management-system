const usernameField=document.querySelector('#usernameField')
const emailField=document.querySelector('#emailField')
const submitbtn=document.querySelector(".submit-btn")
const feedbackArea=document.querySelector('.invalid_feedback')
const emailfeedbackArea=document.querySelector('.emailfeedback')



usernameField.addEventListener('keyup',(e)=>{
    console.log('click')
    const usernameVal=e.target.value;
    usernameField.classList.remove("is-invalid");
    feedbackArea.style.display="none";
    if (usernameVal.length>0){
        fetch("/authentication/validate-username/",{
            body:JSON.stringify({username:usernameVal}),
            method:"post"

        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("data",data)
            if (data.username_error){
                submitbtn.disabled=true;
                usernameField.classList.add('is-invalid')
                feedbackArea.style.display='block'
                feedbackArea.innerHTML=`<p>${data.username_error}</p>`
                


            }

            else{
                submitbtn.disabled=false;}
        })
    }

})


emailField.addEventListener("keyup",(e)=>{
   const emailVal= e.target.value
   emailField.classList.remove("is-invalid");
   emailfeedbackArea.style.display="none";
   if (emailVal.length){
       fetch("/authentication/validate-email/",{
           body:JSON.stringify({email:emailVal}),
           method:"POST"
       })
       .then((res)=>res.json())
       .then((data)=>{
           console.log(data)
           if (data.email_error){
                submitbtn.disabled=true;
                emailField.classList.add('is-invalid')
                emailfeedbackArea.style.display='block'
                emailfeedbackArea.innerHTML=`<p>${data.email_error}</p>`

           }
           else{
                submitbtn.disabled=false;}

           
       })
       
   }
})
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