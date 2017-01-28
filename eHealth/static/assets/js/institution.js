//JQuery para pasar la informacion al views de eliminar institución

$(function(){
    $("#deleteButton_institution").click(function(){
        $("#myModal_institution").hide();

        var id = $("#deleteButton_institution").val();
        console.log(id);
        
        $.ajax({
          type: 'POST',
          url: '/delete_institution',
          data: JSON.stringify(id),
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
var modal_institution = document.getElementById('myModal_institution');
// Get the button that closes the modal
var cancel_institution = document.getElementById("cancel_institution");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, close the modal 
cancel_institution.onclick = function() {
    modal_institution.style.display = "none";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal_institution.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal_institution) {
        modal_institution.style.display = "none";
    }
}
// When the user clicks on the button, open the modal 
function openModal_institution(id) {
    console.log(id);
    modal_institution.style.display = "block";
    document.getElementById('deleteButton_institution').value =  id;
}

//Al darle click a la institucion, mostrar su informacion
$("#show-institutions td").click(function(){
  var id = $(this).siblings().first().text();
  $.ajax({
          type: 'POST',
          url: '/show_institution_data',
          data: JSON.stringify(id),
          contentType:'application/json; charset=utf-8',

          success: function(response) {
              var d = $.parseJSON(response);
              console.log(response);
              $("p.name").html(d.name);
              $("p.address").html(d.address);
              $(".modal-info-institution").modal('show');
              $(".modal-backdrop.in").hide(); 
              $("a.close-modal-button").click(function(){
                alert("HOLA");
                $("button.modal-info-institution").modal('hide');
                $("button.modal-info-institution").css('display','none');
              });

              //window.location.reload(true);
              //$('#show-institutions').load(document.URL +  ' #show-institutions');
          },
          error: function(error) {
              console.log(error);
          }
      });
  });
