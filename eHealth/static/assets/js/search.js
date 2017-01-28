$(document).ready(function() {
    $('#search_result').DataTable( {
        "pagingType": "full_numbers"
    } );

        $("#search-button").click(function(){
    	var data = $('input').val();
        $.ajax({
          type: 'POST',
          url: '/search',
          data: JSON.stringify(data),
          contentType:'application/json; charset=utf-8',

          success: function(response) {
          	response = $.parseJSON(response);
              console.log(response["tabla"]);
              //window.location.reload(true);
              //$('#show-institutions').load(document.URL +  ' #show-institutions');
              $('tbody').html(response["tabla"]);
          },
          error: function(error) {
              console.log(error);
          }
      });
    });

   // });

} );

$(document).ready(function(){
        
    })