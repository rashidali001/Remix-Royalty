let DB_COLLECTION;
let SPECIFIC_COLLECTION;

/* When the document is ready, do the following functions: */

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

        DB_COLLECTION = $(this).data("value");
        let link_text = $(this).text();
        collection_header = $(".collection-header");
        let h2 = $("<h2></h2>").text(link_text);
        collection_header.append(h2);
        data = { collection_name : DB_COLLECTION };

        $.ajax({
            url:"/get_relationships",
            method:"post",
            data: JSON.stringify(data),
            contentType:"application/json",
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
                let category_name = first.text();
                let para = $("<p></p>").text(category_name);
                para.attr("data-value",category_name.toLowerCase());
                $(".add-data-btn").append(para);
                $(".add-collection-data").css("display","flex");

                let data = { name: category_name };
                
                // RETRIVING TABLE NAMES OF THE FIRST SELECTED COLLECTION NAME (category_name)
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

        let category_name = $(this).text();

        $(".add-data-btn").find("p").remove();

        let para = $("<p></p>").text(category_name);
        para.attr("data-value", category_name.toLowerCase());
        $(".add-data-btn").append(para);  
        
        $(".add-collection-data").css('display','flex');

        let data = { name: category_name };
                
        // RETRIVING TABLE NAMES OF THE FIRST SELECTED COLLECTION NAME (category_name)
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
    })

    // When add button is clicked bring out form

    $(".add-data-btn").click(function(e){       
        let category = $(this).find("p").data("value");
        $(".add-collection-form").css("display","flex");
       
       
        
    })
    // Cancel button to close form
    $("#cancel").click(function(e){
        $("#add-form").hide();
    })

    // when size no is clicked
    $("#size-no-wrapper").click(function(e){
        e.preventDefault();
        $(this).find("input").prop("disabled", false);
        $("#size").attr("disabled","disabled");
    
    })

    // when select element is clicked
    $("#size").click(function(e){
        e.preventDefault();
        $(this).prop("disabled", false);
        $("#size-no-wrapper").find("input").prop("disabled", true);
    })
    
            // On submit send data to the database 
            $("#form-data").submit(function(e){
                e.preventDefault();

                let category = $(".add-data-btn").find("p").data("value")

                let formData = new FormData(this);

                formData.append("category", category);
                formData.append("db_collection", DB_COLLECTION)

               
                $.ajax({
                    url:"/add_collection",
                    type:"post",
                    data: formData,
                    contentType:false,
                    processData:false,
                    success: function(){
                        
                    }
                })
    
    
    
                
        
            })



    



    
})