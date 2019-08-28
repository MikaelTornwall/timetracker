const confirm = (name) => window.confirm(`Do you really want to delete this ${name}?`) ? document.getElementById("delete_me").click() : null  
