 $("#print_url").click(function () {
      chrome.tabs.executeScript({
          code: `var url = window.location.href;
              url`
          }, function(url) {
                var data = {'url': url};
                $.ajax({
                url: 'http://127.0.0.1:5000/admin_report',
                type: 'get', //전송 타입
                dataType: 'json', //받는 형식
                success: function (res) {
                    alert("done");

                    // 서버단에서 HTML을 반환해서 페이지를 깜빡임없이 새로고침
                    document.querySelector("#appendHtml").innerHTML = res;
                },
                error: function (error) {
                    console.log("error");
                }
                })
          }
      )
  });