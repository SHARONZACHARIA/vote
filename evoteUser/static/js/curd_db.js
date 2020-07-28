$(function () {

  $("#addcandidates-div").hide();

  $("#add_candidates").click(function () {
      console.log("clicked")
      cname = $("#cname").val()
      desc = $("#description").val()
      caseid=$("#vid").val()
      // img=$("#img").val()

      payload={
          "cname":cname,
          "description":desc,
          "caseid":caseid
      }       
      var token = '{{csrf_token}}';
    $.ajax({

      headers: { "X-CSRFToken": token },
      url: 'http://127.0.0.1:8000/add_candidate/',
       type: 'POST',
      dataType: 'json',
      data:payload,
      success: function (data) {
         console.log(data)

      }
    });
  });



  $("#createcase").click(function () {
    console.log("first data")

    vcname = $("#name").val()
    vid = $("#vid").val()
    controller = $("#controller").val()
    desc = $("#desc").val()

    payload = {
      "name": vcname,
      "vid": vid,
      "controller": controller,
      "desc": desc
    }

    console.log(payload)

    var token = '{{csrf_token}}';
    $.ajax({

      headers: { "X-CSRFToken": token },
      url: 'http://127.0.0.1:8000/add_votecase/',
      type: 'POST',
      dataType: 'json',
      data: payload,
      success: function (data) {
        $("#addcandidates-div").show();
        $("#votecase-div").hide();
      }
    });
  });


  $("#done").click(function () {
    console.log("hello") 
    window.location.replace('http://127.0.0.1:8000/login_intro');

  });

});


