
//check 버튼 누르면
function waitMessage(){
  $("#message").html( '<center>'+ '<h3>Getting...</h3>'+ '</center>');
}

function doneMessage() {
    $("#message").html('<center>' + '<h3>Done</h3>' + '</center>');
}

function inject(data) {
    chrome.tabs.executeScript(null, {
        code: 'var newdata = "' + data + '";'
    }, function() {
        chrome.tabs.executeScript(null, {
            code: `
            var predict = newdata.split(",");
            var element = Array.from(document.getElementsByClassName("writer_info"));
            for (var i in element) {
                if(predict[i]=="Ad") {
                    var newDiv = document.createElement('span');
                    newDiv.style.backgroundColor = 'red';
                    newDiv.style.height = "20px";
                    newDiv.style.width = "40px";
                    newDiv.style.borderRadius = "3px"
                    newDiv.style.marginLeft = "10px"
                    var newText = document.createTextNode(predict[i]);
                    newDiv.appendChild(newText);
                    newDiv.style.color = "white";
                    newDiv.style.fontSize = "14px";
                    newDiv.style.textAlign = "center";
                    element[i].appendChild(newDiv);
                }
            }
            `
        });
    });
}

//문서가 준비되면 매개변수로 넣은 콜백함수를 실행
$(document).ready(function(){

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
                    inject(data.results);
                    doneMessage();
                },
                error: function (error) {
                    console.log("error");
                }
                })
          }
      )
  });
});
