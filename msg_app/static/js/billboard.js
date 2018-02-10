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

    $(".trash").click(function(){
        msg_id = $(this).attr("id");
        console.log (msg_id);
        $(this).parent('.msg_box').remove();
        $.ajax({
            url: 'trash',
            type: 'DELETE',
            data: {msg_id : msg_id},
            success: function(result) {
                alert("Message deleted !")
                $(this).parent('.msg_box').remove();
                }
        });
    });
});
