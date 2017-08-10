/**
 * Created by ryan on 09/08/17.
 */
function connectionStatus() {
	var connectionStatus = 1
	var div = document.createElement("div");
	document.getElementById("Server Status").style.textAlign = "center";
	document.getElementById("Server Status").appendChild(div);
	if (connectionStatus == 1){
		div.setAttribute('class', 'alert alert-success');
		div.innerHTML = "<strong>Connected</strong> </a>";
	}else
	{
		div.setAttribute('class', 'alert alert-danger');
		div.innerHTML = "<strong>Disconnected</strong> </a>";
	}
}