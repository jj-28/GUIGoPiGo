//first make a function that adds and removes waypoint names from the map
var x =0;
var cmdqueue= Array();
function addWaypoint(id) {
//        for (var i = 0; i < cmdqueue.length; i++) {
    if (cmdqueue.length == 0) {
        cmdqueue.push(id);
        // document.getElementById("print").innerHTML = cmdqueue.length;
        window.alert(cmdqueue.toString());
        // cmdqueue[x] = document.getElementById(id).value;
        // alert("Element: " + cmdqueue[x] + " Added at index " + x);
        // x++;
    } else {
        if (cmdqueue[cmdqueue.length - 1] != id) {
            // cmdqueue[x] = document.getElementById(id).value;
            // alert("Element: " + cmdqueue[x] + " Added at index " + x);
            // x++;
            cmdqueue.push(id);
            // document.getElementById("print").innerHTML = cmdqueue.length;
            window.alert(cmdqueue.toString());

        } else {
            window.alert("You can't add the same waypoint 2 times in a row. Ex:No N1-N1-N@");
        }
    }
}

function setup2()
{
    var $txt = $("#data");      			// assigns the data(hostname/ip address) entered in the text box
    name = $txt.val();          			// Variable name contains the string(hostname/ip address) entered in the text box
    var host =  "ws://"+name+":9093/ws"; 	// combines the three string and creates a new string
    var socket = new WebSocket(host);
    var $txt = $("#data");
    var $btnSend = $("#sendtext");
    $txt.focus();

    // event handlers for UI
    $btnSend.on('click',function()
    {
        var text = $txt.val();
        if(text == "")
        {
            return;
        }
        $txt.val("");
    });
    $txt
        .keypress(function(evt)
        {
            if(evt.which == 13)
            {
                $btnSend.click();
            }
        });

    // event handlers for websocket
    if(socket)
    {
        var count =1;
        socket.onopen = function()
        {
            count = 0;
            send();    // function for detecting the button press on webpage
        }
        //Send the button pressed backed to the Raspberry Pi
        function send()
        {
            var json = JSON.stringify(cmdqueue.toString());
                socket.send();
        }
        socket.onmessage = function(msg)
        {
            showServerResponse(msg.data);
        }
        socket.onclose = function()
        {
            //alert("connection closed....");
            showServerResponse("The connection has been closed.");
        }
    }
    else
    {
        console.log("invalid socket");
    }
    function showServerResponse(txt)
    {
        var p = document.createElement('p');
        p.innerHTML = txt;
        document.getElementById('output').appendChild(p);
    }
}




//then send those values as a python array, to the pathfinder


//
