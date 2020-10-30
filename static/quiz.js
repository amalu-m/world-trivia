
$(function(){
    $("#id_input").autocomplete({
      source: '/autocomplete/',
      minLength: 2,
      select: function (event, ui) {
                // event.preventDefault()
                $("#id_input").val(ui.item.label);
                location.href="/questions?&item=" + ui.item.label;
                return false;
        }
    });
  });

$(function(){
  $('#myselection input').on('click',function(){
              $.ajax({
            type: 'GET',
            url: '/questions/',
            data: { clicked :$('#myselection input:checked').val()},
            success:function(response,data){
                $("#myselection input[type=radio]").attr('disabled',true);
                var elements = document.querySelectorAll("#myselection input[type=radio]")
                for (var i = 0, element; element = elements[i++];) {
                    if ((element.checked && element.value === response.answerKey)||(element.value === response.answerKey)){
                      element.labels[0].style["color"] = "#36eb69";
                    } else if (element.checked) {
                      element.labels[0].style["color"] = "red";
                    } else {
                      // reset color to black
                      element.labels[0].style["color"] = "black";
                    }
                }
                }
              })

                  });
  });
