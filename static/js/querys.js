$(document).ready(function(){
    $("tr:even").css("background-color", "#b5ebe0");
    $("nav").mouseup(function(){
        alert("Welcome to my board have fun ^_^ ");
    });
    $("tr").on({
        mouseenter: function(){
          $(this).css("background-color", "lightgray");
        },
        mouseleave: function(){
          $(this).css("background-color", "lightblue");
        },
        click: function(){
          $(this).css("background-color", "yellow");
        }
      });
})