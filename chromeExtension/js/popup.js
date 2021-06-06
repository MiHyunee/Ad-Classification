
//check 버튼 누르면
function waitMessage(){
  $("#message").html( '<center>'+
                      '<h3>Getting...</h3>'+
                      '</center>'
                    );
}


//문서가 준비되면 매개변수로 넣은 콜백함수를 실행
$(document).ready(function(){

  //checking whether spam or not spam
  $("#getData").click(function () {
      //waitMessage출력
      waitMessage();

      //데이터 가져오기
      chrome.tabs.executeScript({
          code: `var result = Array.from(document.getElementsByClassName("desc_inner")).map(h => h.href);
              result`
          }, function(result) {
                var data = {'url': result};
                $.ajax({
                url: 'http://127.0.0.1:5000/search',
                type: 'post',
                dataType: 'json',
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(result),
                success: function (data) {
                    var response = data;
                    output = data['response'] + 'is_ad' + data['isAd'] + 'index' + data['index'];
                    chrome.runtime.sendMessage({type: "isStatus", count: data});
                    data = null;
                    }
                })
          }
      )
  });
});
