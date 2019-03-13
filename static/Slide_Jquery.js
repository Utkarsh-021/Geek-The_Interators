$(document).ready(function(){
  		var n=0;
      var login=0;
    	$(".close").on({
    mouseenter: function(){
        $(this).css("background-color", "red");
        $(this).css("color", "white");
    }, 
    mouseleave: function(){
        $(this).css("background-color", "lavender");
        $(this).css("color", "black");
    }, 
  	});
      $('#logina').click(function(){
     alert("shviam");
      $('#mymodal').modal(hide);
  // Load up a new modal...
  $('#myModal').modal('show');
    });
  	$("#logina").on({
    mouseenter: function(){
    
     
        $(this).css("color", "blue");
    }, 
    mouseleave: function(){
       
        $(this).css("color", "black");
    }, 
  	});
  	$("#tag1,#tag2,#tag3,#tag4").on({
    mouseenter: function(){
    $(this).css("color", "black");
    }, 
    mouseleave: function(){
       
        $(this).css("color", "#18191991");
    }, 
  	});
  	$("#slide-left,#slide1-left,#slide2-left,#slide3-left").on({
    mouseenter: function(){
    $(this).css("margin-left", "120px");
    }, 
    mouseleave: function(){
       
        $(this).css("margin-left", "0px");
    }, 
  	});
     $("#tag1,#tag2,#tag3,#tag4").on({
    mouseenter: function(){
    $(this).css("color", "black");
    }, 
    mouseleave: function(){
       
        $(this).css("color", "white");
    }, 
    });
  	  $("#myModal").on('show.bs.modal', function () {
  	  	
  	  	$("#pageContent").css("opacity","1");
  	  });
     $("#shivam").click(function(){
     // $(this).css("display","none");
      $("#search_doctor").toggle();

     });
     var search=0;
     $("#nav-left").click(function(){
      search=0;
      $("#transcript").attr('placeholder',"Searching The Doctor By City And Name");
      if(n==0)
      {
      $("#suggestion").modal();
n=n+1;
    }
        $("#arrow-top").css("display","block");  
        $("#arrow-top").css("left","-520px");

    });
    $("#nav-left1").click(function(){
      search=1;
      $("#transcript").attr('placeholder',"Search Remedies for treatment");
      {
      $("#suggestion").modal();
n=n+1;
    }
        $("#arrow-top").css("display","block");  
        $("#arrow-top").css("left","-590px");

    });
$("#suggestion,#suggestion1").on('hidden.bs.modal', function () {
            n=0;
             $("#arrow-top").css("display","none");  

    });
$("#mymodal,#myModal").on('hidden.bs.modal', function () {
            n=0;
             

    });
$("#log").click(function(){
  if(n==0){
  $("#mymodal").modal({backdrop:"static"});
  n=n+1;
}
});
$("#sign,#sign1,#sign2").click(function(){
  if(n==0){
  $("#myModal").modal({backdrop:"static"});
  n=n+1;
}
});

var report=0;
var appointment=0
$("#login1").click(function(){
  $("#signupandin").css("display","none");
  $("#after-sign").css("display","block");
login=1;
 if(report==1)
  {
    window.open("myReport.html","_self");
  }
   if(appointment==1)
  {
    window.open("appointment.html","_self");
  }
});
$("#logout").click(function(){

  $("#after-sign").css("display","none");
  $("#signupandin").css("display","block");
  login=0;
});
/*$("#myBtn").click(function(){
 $("#mymodal").on('hidden.bs.modal', function () {
  $("#myModal").modal({backdrop:"static"});
     });
});*/
 $("#mymodal").on('hidden.bs.modal', function () {
 report=0;
 appointment=0;
     });
$("#myReport").click(function(){
 if(login==0)
  {report=1;
 $("#mymodal").modal({backdrop:"static"});
}
 if(login==1)
  {
    window.open("templates/myReport.html","_self");
  }
});
$("#myAppointments").click(function(){
 if(login==0)
  {appointment=1
 $("#mymodal").modal({backdrop:"static"});
  }
  if(login==1)
  {
    window.open("templates/Map.html","_self");
  }
});
 $(".dropdown-toggle").dropdown();
  });
