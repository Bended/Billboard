$( document ).ready(function() {

    $("#plus_id").click(function() {
    $("#new_msg").slideDown();
    $(".add_msg").hide();
    });

    $("#validate").click(function() {
        $("#new_msg").hide(300);
        $(".add_msg").show();
    });

    $("#cancel").click(function() {
    $("#new_msg").hide(300);
    $(".add_msg").show();
    });
});