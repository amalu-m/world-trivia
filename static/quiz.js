

$(function(){
    $("#id_input").autocomplete({
      source: '/autocomplete/',
      minLength: 2,
      select: function (event, ui) {
                event.preventDefault()
                $("#id_input").val(ui.item.label);
                location.href="/questions?&search_item=" + ui.item.label + "&item="+ui.item.value;
                $("#hidden_input").val(ui.item.value);
                return false;
        }
    });
  });
