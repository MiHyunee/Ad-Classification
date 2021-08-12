
//check 버튼 누르면
function waitMessage(){
  $("#message").html( '<center>'+ '<h3>Getting...</h3>'+ '</center>');
}

function doneMessage() {
    $("#message").html('<center>' + '<h3>Done</h3>' + '</center>');
}

function activatePopup() {
    chrome.tabs.executeScript({
        code: `
            var url = window.location.href;
            var cookies = document.cookie.split('; ');
            var isAd = false;
            for(var i in cookies) {
                if(url==cookies[i].split('=')[0]) {
                    isAd = true;
                    break;
                }
            }
            isAd
            `
        }, function (isAd) {
          if ( isAd=='true' ) {
              $('#report').attr('disabled', true);
          } else {
              $('#report').attr('disabled', false);
          }
      });
}

function inject(data) {
    chrome.tabs.executeScript(null, {
        code: 'var newdata = "' + data + '";'
    }, function() {
        chrome.tabs.executeScript(null, {
            code: `
            var predict = newdata.split(",");
            var element = Array.from(document.getElementsByClassName("writer_info"));
            if (element.length==0) {
                element = Array.from(document.getElementsByClassName("author"));
            }
            var url = Array.from(document.getElementsByClassName('desc_inner')).map(h => h.href);
            for (var i in element) {
                if(predict[i]=="Ad") {
                    var newDiv = document.createElement('span');
                    newDiv.style.backgroundColor = 'red';
                    newDiv.style.padding = "2px 5px";
                    newDiv.style.borderRadius = "3px";
                    newDiv.style.marginLeft = "10px";
                    newDiv.style.textAlign = "center";
                    var newText = document.createTextNode(predict[i]);
                    newDiv.appendChild(newText);
                    newDiv.style.color = "white";
                    newDiv.style.fontSize = "14px";
                    newDiv.style.textAlign = "center";
                    element[i].appendChild(newDiv);
                    
                    
                    var domain = ".naver.com";
                    var today = new Date();
                    today.setTime(today.getTime() + (60*60*1000*0.5));
                    document.cookie = url[i] + '=' + i + ';path=/; expires=' + today.toGMTString() + '; domain=' + domain + ';';
                }
            }
            `
        });
    });
}

//문서가 준비되면 매개변수로 넣은 콜백함수를 실행
$(document).ready(function(){
    activatePopup();

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
                url: 'http://127.0.0.1:5000/concurrent',
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

  $("#report").click(function () {
      chrome.tabs.executeScript({
          code: `var url = window.location.href;
              url`
          }, function(url) {
                var data = {'url': url};
                $.ajax({
                url: 'http://127.0.0.1:5000/report',
                type: 'post',
                dataType: 'json',
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(url),
                success: function (data) {
                    alert("done");
                },
                error: function (error) {
                    console.log("error");
                }
                })
          }
      )
  });

});
