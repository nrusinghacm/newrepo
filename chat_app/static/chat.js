$('#chat-form').on('submit', function(event){
  event.preventDefault();
  $.ajax({
    url : '/post/',
    type : 'POST',
    data : {msgbox:$('#chat-msg').val()},

    success:function(json){
      $('#chat-msg').val('');
      $('#msg-list').append('<li class="text-right list-group-item">'+json.msg+'</li>');
      var chatlist = document.getElementsById('msg-list-div');
      chatlist.scrollTop = chatlist.scrollHeight;
    }
  });
});
function getMessage(){
  if (!scrolling){
    $.get('/messages', function(messages)){
      $('#msg-list').html(messages);
      var chatlist = document.getElementsById('msg-list-div');
      chatlist.scrollTop = chatlist.scrollHeight;
    });
  }
  scrolling = false;
}
var scrolling = false;
$(function(){
  $('#msg-list-div').on('scroll', function(){
    scrolling = true;
  });
  refreshTimer = setInterval(getMessages, 2500);
});

$(document).ready(function(){
  $('#send').attr('disabled', 'disabled');
  $('#chat-msg').keyup(function(){
    if($(this).val() != ''){
      $('#send').removeAttr('disabled')
    }
    else{
    $('#send').attr('disabled','disabled');
    }
  });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
