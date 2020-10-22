
$(document).ready(function() {

    $Divs = $("div.card-body");
  
    $Divs.click(function() {
      $Divs.removeClass("highlight");
      $(this).addClass("highlight");
  
    });
  });