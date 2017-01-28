//JQuery para pasar la informacion al views de eliminar usuario

$(function(){
    $("#deleteButton_user").click(function(){
        $("#myModal_user").hide();

        var ci = $("#deleteButton_user").val();
        console.log(ci);
        
        $.ajax({
          type: 'POST',
          url: '/delete_user',
          data: JSON.stringify(ci),
          contentType:'application/json; charset=utf-8',

          success: function(response) {
              console.log(response);
              //window.location.reload(true);
              $('#show-users').load(document.URL +  ' #show-users');
          },
          error: function(error) {
              console.log(error);
          }
      });
    });
});


// Funciones para controlar la aparicion del modal
// Get the modal
var modal_user = document.getElementById('myModal_user');
// Get the button that closes the modal
var cancel_user = document.getElementById("cancel_user");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, close the modal 
cancel_user.onclick = function() {
    modal_user.style.display = "none";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal_user.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal_user) {
        modal_user.style.display = "none";
    }
}
// When the user clicks on the button, open the modal 
function openModal_user(ci) {
    console.log(ci);
    modal_user.style.display = "block";
    document.getElementById('deleteButton_user').value =  ci;
}
