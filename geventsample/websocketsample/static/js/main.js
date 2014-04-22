(function(){
    var socket = io.connect();
    socket.on('message', function(recvData){
        recvData = JSON.parse(recvData)
        if(recvData.message){
            var $li = $("<li>").text(recvData.message);
            $(".income-list").prepend($li);
        }
    });
    socket.send(JSON.stringify({'action':'subscribe'}));
})();