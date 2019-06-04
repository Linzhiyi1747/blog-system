function register(){
	var funame = document.getElementById("uname");
	var fpword = document.getElementById("pword");
	var fpword2 = document.getElementById("pword2");
	if (funame.value.length<6||uname.value.length>12){
		document.getElementById("uerror").innerHTML = "用户名长度不合法!";
		return false;
		}else if(fpword.value.length<6||fpword.value.length>20){
			document.getElementById("perror").innerHTML = "密码长度不合法!";
			return false;
			}else if(fpword.value!=fpword2.value){
				document.getElementById("perror2").innerHTML  = "密码输入不一致!";
				return false;
				}
	return true;
}