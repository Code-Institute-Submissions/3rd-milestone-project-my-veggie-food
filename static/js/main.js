// Delete Modal

$('#delete').on('shown.bs.modal', function () {
    $('#delete').trigger('focus');
  });
  
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
