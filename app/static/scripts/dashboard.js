$(document).ready(function(){


    /* OPENING AND CLOSING OF COLLECTIONS */
    $("#category").click(function(e){
        e.preventDefault();

        $("#collection").toggleClass("collection-close");
    })
    /* */


    /* menscollection-link  */
    $(".collection-link").click(function(e){
        e.preventDefault();
        $(".collection-classes").empty();
        $(".collection-header").empty();

        let link_text = $(this).text();
        collection_header = $(".collection-header");
        let h2 = $("<h2></h2>").text(link_text)
        collection_header.append(h2);

        $.ajax({
            url:"/get_men_relationships",
            method:"post",
            success:function(response){
                for (const key in response) {
                    let div = $("<div class='collection-classes-child'></div>");
                    let link = $("<p></p>").text(response[key]);
                    div.append(link);
                    $(".collection-classes").append(div);
                }
                let first = $(".collection-classes-child").first();
                first.addClass("active");
                $(".add-data-btn").find("p").remove();
                let collection_name = first.text();
                let para = $("<p></p>").text(collection_name);
                $(".add-data-btn").append(para);
                $(".add-collection-data").css("display","flex");

                let data = { name: collection_name};
                
                // RETRIVING TABLE NAMES OF THE FIRST SELECTED COLLECTION NAME
                $.ajax({
                    url:"/field_names",
                    type:"POST",
                    data:JSON.stringify(data),
                    contentType:"application/json",
                    success:function(response){
                        $(".table-header").empty();
                        for (const key in response) {
                            let td = $("<td></td").text(response[key]);
                            $(".table-header").append(td);

                        }
                    }
                    

                })
                // END OF RETRIVING TABLE NAMES
            }       
        }) 

    })

    // When user clicks on the links -> add and active  class and creating add button

    $(".collection-classes").on("click", ".collection-classes-child", function(e){
        // let collection = $(this).children();

        $(".collection-classes-child").removeClass("active")
        $(this).addClass("active");

        let collection_name = $(this).text();

        $(".add-data-btn").find("p").remove();

        let para = $("<p></p>").text(collection_name);
        $(".add-data-btn").append(para);  

        $(".add-collection-data").hide();
        
        $(".add-collection-data").css('display','flex');
    })

    // When add tshirt button is clicked bring out form

    $(".add-data-btn").click(function(e){
        

        $(".add-collection-form").css("display","flex");
        let add_text = $(".add-data-btn").find("p").text();
        $("form").submit(function(e){
            e.preventDefault();
            console.log(add_text);
        })

        
        
    })
    // Cancel button to close form
    $("#cancel").click(function(e){
        $("#add-form").hide();
    })
    







    
})