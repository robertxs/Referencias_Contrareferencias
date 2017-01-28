//JQuery para pasar la informacion al views de eliminar especialización.

$(function(){
    $("#deleteButton_specialization").click(function(){
        $("#myModal_specialization").hide();

        var id = $("#deleteButton_specialization").val();
        console.log(id);
        
        $.ajax({
          type: 'POST',
          url: '/delete_specialization',
          data: JSON.stringify(id),
          contentType:'application/json; charset=utf-8',

          success: function(response) {
              console.log(response);
              //window.location.reload(true);
              $('#show-specializations').load(document.URL +  ' #show-specializations');
          },
          error: function(error) {
              console.log(error);
          }
      });
    });
});


// Funciones para controlar la aparicion del modal
// Get the modal
var modal_specialization = document.getElementById('myModal_specialization');
// Get the button that closes the modal
var cancel_specialization = document.getElementById("cancel_specialization");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, close the modal 
cancel_specialization.onclick = function() {
    modal_specialization.style.display = "none";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal_specialization.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal_specialization) {
        modal_specialization.style.display = "none";
    }
}
// When the user clicks on the button, open the modal 
function openModal_specialization(id) {
    console.log(id);
    modal_specialization.style.display = "block";
    document.getElementById('deleteButton_specialization').value =  id;
}
