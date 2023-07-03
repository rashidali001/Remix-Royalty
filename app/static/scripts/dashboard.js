$(document).ready(function(){


    /* OPENING AND CLOSING OF COLLECTIONS */
    $("#category").click(function(e){
        e.preventDefault();

        $("#collection").toggleClass("collection-close");
    })
    /* */

    /* menscollection-link  */
    $("#menscollection-link").click((e)=>{
        e.preventDefault();

        $.ajax({
            url:"/get_men_relationships",
            method:"post",
            success:function(response){
                alert(response);

            }
        })




    })
    
})