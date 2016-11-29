# Web 7 Challenge

## Topics Covered

This is a Javascript challenge that also tests reversing a XOR encryption, or the use of the Javascript debugger. Whichever one finds easier.

## Tools

* Developer console in any web browser (Typically available using F12)

## Method

First thing to do is to check the source code of the website (right click, view source). In there you should notice a line that reads 

```
<input type="submit" value="Submit" onClick="checkCode(this.form)">
```

This adds a callback for the submit button, it calls the function 'checkCode' but this doesn't appear to be in our source-code anywhere.

However at the top of the page you can see I've included the 'Bootstrap.js' file. Since this is the only other javascript source on this page we should check it out.

```
<script type="text/javascript" src="/js/bootstrap.js"></script>
```

Looking at this file and searching for 'checkCode' we come across the callback function.

```
function checkCode (form) {
    var result = "http://ctf.sigint.mx:8000/web5?code="


    var enteredCode = form.code.value;

    var enc = [0x14,0x5c,0x13,0x32,0x0c,0x40];
    var key = "llamas";
    var flag = "";

    for(i = 0; i < enc.length; i++){
        flag = flag + String.fromCharCode(enc[i] ^ key.charCodeAt(i));
    }

    if (enteredCode == flag){

        alert("Well played")

	}else{

		alert("Wrong code! Please try again");
	}
}
```

What this function does is a simple XOR encryption to make finding the input a little harder. In the for loop this line

```
      flag = flag + String.fromCharCode(enc[i] ^ key.charCodeAt(i));
```

Uses the XOR bitwise operator '^' to xor the binary values of enc and key together and appends the ascii character that value represents to flag.

At this point you can manually decrypt the encrypted array using the key, or you can set a javascript breakpoint in the debugger just after and read the value. Doing either of these reveals the correct input which is "x0r_m3". Submitting this to the code entry box gives you the correct flag.
