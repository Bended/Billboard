$("#plus_id").click(function() {
  $("#new_msg").slideDown();
});

$("#validate").click(function() {
    $("#new_msg").hide(300);
    var submittedForm = $(this);
    console.log(submittedForm.serialize());
    $.post("/new_msg",submittedForm.serialize(),function(result){
        if (result["STATUS"] == "ERROR"){
            alert(result["MSG"]);
        }else{
            alert("Message créé");
        }
    },"json");
    return false;
  });

$("#cancel").click(function() {
$("#new_msg").hide(300);
});