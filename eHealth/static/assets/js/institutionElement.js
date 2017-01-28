//JQuery para pasar la informacion al views de eliminar el elemento de una institución

$(function(){
    $("#deleteButton_institutionElement").click(function(){
        $("#myModal_institutionElement").hide();

        var value = $("#deleteButton_institutionElement").val().split(" ");
        console.log(value);
        var id = value[0];
        var int_id = value[1];
        console.log(id);
        console.log(int_id);
        
        $.ajax({
          type: 'POST',
          url: '/delete_institutionElement',
          data: JSON.stringify([id,int_id]),
          contentType:'application/json; charset=utf-8',

          success: function(response) {
              console.log(response);
              //window.location.reload(true);
              $('#show-institutions').load(document.URL +  ' #show-institutions');
          },
          error: function(error) {
              console.log(error);
          }
      });
    });
});


// Funciones para controlar la aparicion del modal
// Get the modal
var modal_institutionElement = document.getElementById('myModal_institutionElement');
// Get the button that closes the modal
var cancel_institutionElement = document.getElementById("cancel_institutionElement");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, close the modal 
cancel_institutionElement.onclick = function() {
    modal_institutionElement.style.display = "none";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal_institutionElement.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal_institutionElement) {
        modal_institutionElement.style.display = "none";
    }
}
// When the user clicks on the button, open the modal 
function openModal_institutionElement(id,int_id) {
    console.log(id);
    console.log(int_id);
    modal_institutionElement.style.display = "block";
    document.getElementById('deleteButton_institutionElement').value =  id + " " + int_id;

}