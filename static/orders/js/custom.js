var clkBtn
var customer_id
var customer_name
var products
var quantity
var discount_percentage

$(document).ready(function() {

$(document).on("change", 'td select.product', function () {
  $this = $(this)
  $.ajax({
            data: {'ajax_type':'choose_price', 'product_id':this.value},
            type: "GET",
            dataType: "html",
            url: this.url,
            success: function(response) {
                     a = $this.closest('tr').find('td.price input').val(response);
            },
            error: function(e, x, r) {
               alert("error");
            }
    });

});

    $('#id_customer').select2({
    }).on("change", function (e) {
          $("#edit_customer").prop('hidden', false)
          customer_id = $(this).val();
    });

    $("#edit_customer").click(function(evt) {
            $.ajax({
            data: {'ajax_type':'get_user_data', 'customer_id':customer_id},
            type: "GET",
            dataType: "html",
            url: this.url,
            success: function(response) {
                    $("#customer_details").html(response)
                     $("#customer_edit").modal({
                      backdrop: 'static',
                      keyboard: false,
                      show: true });

            },
            error: function(e, x, r) {
               alert("error");
            }
    });

    });

    $("#save_edit").on('click', function(){
                    $.ajax({
                    data: {'ajax_type':'save_user_data', 'customer_id':customer_id, 'phone_number':$('#phone_number').val(), 'address':$('#address').val()},
                    type: "GET",
                    dataType: "html",
                    url: this.url,
                    success: function(response) {
                              $('#customer_edit').modal('toggle');
                    },
                    error: function(e, x, r) {
                       alert("error");
                    }
                });



    })

    $("#button").click(function () {
        $('#customer_edit').modal('toggle');
    });

    $("#model_button").click(function () {
        $('#myModal').modal('toggle');
    });

    $('.submit_btn').click(function(evt) {
        clkBtn = this.id
        });

    $("#order_form").submit(function(event){
        if (clkBtn == 'confirm_order'){
               event.preventDefault();
               products = [];
               quantity = [];
               $('td select.product').each(function(i){
                        products.push($(this).val());
                    })

               $('td input.product').each(function(i){
                        quantity.push($(this).val());
                    })
               var amount = 0
               discount_percentage = $("#id_discount_percentage").val()

               $("#product_table").find('tr:not(:first-child)').each(function (i, el) {
                var $tds = $(this).find('td .product'),
                    product = $tds.eq(0).find("option:selected").html(),
                    price = parseInt($tds.eq(1).val()),
                    Quantity = parseInt($tds.eq(2).val()),
                    value =price*Quantity
                    amount = amount+value
                    html_text = '<tr><td>'+product+'</td><td>'+price+'</td><td>*</td><td>'+Quantity+'</td><td>'+value+'</td></tr>'
                    $("#order_summary_table").append(html_text)
                 });

                 var discount_amount = amount *(discount_percentage/100)
                 var total = amount - discount_amount
                 console.log(discount_amount)
                 var amount_details = '<p>amount = '+amount+' </p><p> Discount = '+discount_amount+'( '+discount_percentage+'% )</p><p>Total = '+total+' </p>'
                 $("#amount_data").html(amount_details)
                 $("#customer_name").text($("#select2-id_customer-container").text())

                $("#myModal").modal({
                      backdrop: 'static',
                      keyboard: false,
                      show: true });




        }
    })




    function removethis(elem){
            swal({
              title: "Are you sure?",
              text: "Once deleted, you will not be not able to recover this entry",
              icon: "warning",
              buttons: true,
              dangerMode: true,
            })
            .then((willDelete) => {
              if (willDelete) {
                      $(elem).closest("tr").remove();
              }
            })
    }



});
