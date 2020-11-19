// To send mail from Contact Page

function sendMail(contactForm){
    emailjs.send("gmail", "contact_template", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value
    })
    .then (
        function (response){
            //Add message to modal
            response = $(".message-sent-text").text("We'll be in touch with you as soon as possible.");
            //Only opens modal on successful response
            $("#messageSent").modal("toggle");
            $("#btn-close-modal").click(function(){
                location.reload();
            });
        },
        function(error){
            alert("failed", error); // To block from loading a new page
        });
    return false;
}

// Scroll back to top button
// Example from w3schools.com

//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 100|| document.documentElement.scrollTop > 100) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}