$(document).ready(function(){
    $(function() {
      $('input[name="daterange"]').daterangepicker({
        "startDate": "2022.01.01",
        "endDate": "2022.08.19",
        opens: 'center',
        locale: {
          format: 'YYYY.MM.DD'
        }
        
      });
    });
  });





