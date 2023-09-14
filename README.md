# It-is-not-Illegal
LinkedIn Bot for easy apply!! adjusted code from https://github.com/nicolomantini/LinkedIn-Easy-Apply-Bot

Adapted the code from nicolomantini to complete openended questions using Hugging Face models with my curriculum as context. It is important to initialize a colab server to process the API call on a separate machine!! To keep the Colab server running, just imput this command on the JS commandline in the browser:

function ClickConnect(){
console.log("Working");
document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click();
}
setInterval(ClickConnect,60000)
