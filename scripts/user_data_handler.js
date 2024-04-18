function sendPostRequest() {
  // Create an XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  var username = document.getElementById("username").value;
  var socialUrl = document.getElementById("socialUrl").value;
  var note = document.getElementById("note").value;
  // Create an object with the user data
  var userData = {
    username: username || "test subject 10",
    socialUrl: socialUrl || "test@subject.10",
    note: note || "test subject 10 sending sth",
  };

  // Define the request parameters
  var url = "http://127.0.0.1:8000/request_handler/follow_user/";
  var data = JSON.stringify(userData); // Replace 'key' and 'value' with your data
  var method = "POST";

  // Configure the request
  xhr.open(method, url, true);
  xhr.setRequestHeader("Content-Type", "application/json");

  // Handle the response
  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        console.log("POST request successful");
        console.log("Response:", xhr.responseText);
      } else {
        console.error("Error:", xhr.statusText);
      }
    }
  };

  // Send the request
  xhr.send(data);
}
