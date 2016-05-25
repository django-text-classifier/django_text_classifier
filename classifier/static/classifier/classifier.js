var $addDataForm = $('#addDataForm');
var $body = $('#body');
var $target = $('#target');
var $classifier = $('#classifier');

$addDataForm.submit(function() {
  console.log('Form submitted!');

  $.ajax({
      method: 'POST',
      url: '/../../api/texts/',
      beforeSend: function(request) {
          var token = document.cookie.replace('csrftoken=', '')
          request.setRequestHeader('X-CSRFToken', token)
      },
      data: {
        body: $body.val(),
        target: $target.val(),
        classifier: $classifier.val(),
      },
      success: function(newQuestion) {
        console.log('test');
        document.getElementById("addDataForm").reset();
      },
    });

    return false;
  });
