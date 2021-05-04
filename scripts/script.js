function verifyUser() {
    let urlBase = "http://127.0.0.1:5000/employees/"
    console.log("Hello")
    let username = document.getElementById("userInput").value
    document.getElementById("userInput").value = ""
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            let user = JSON.parse(this.response)
            console.log(user.username)
            document.getElementById("welcomeText").innerHTML = `Welcome, ${username}. Please enter your password:`
            document.getElementById("userInput").type = "password"
            document.getElementById("submitButton").setAttribute("onclick", `verifyPassword("${username}")`)
        } else {
            document.getElementById("welcomeText").innerHTML = `Username not recognized. Please try again:`
        }
    }

    xhttp.open("GET", urlBase + username, true)

    xhttp.send()
}

function verifyPassword(username) {
    let urlBase = "http://127.0.0.1:5000/employees/information/"
    let password = document.getElementById("userInput").value
    document.getElementById("userInput").value = ""
    let xhttp = new XMLHttpRequest()
    console.log("Verifying Password...")
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            let info = JSON.parse(this.response)
            if(info.username == username) {
                console.log("User authenticated! Redirecting...")
                createUserPage(password)
            } else {
                document.getElementById("welcomeText").innerHTML = `Password invalid. Please try again:`
            }
        } else {
            document.getElementById("welcomeText").innerHTML = `Password invalid. Please try again:`
        }
    }

    xhttp.open("GET", urlBase + password, true)

    xhttp.send()
}

function getUserPermissions(position_name) {
    let urlBase = "http://127.0.0.1:5000/permissions/"
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function () {
        if(this.readyState == 4 && this.status == 200) {
            let permissions = JSON.parse(this.response)
            return permissions.departmentHeadAccess, permissions.benCoAccess
        } else {
            document.getElementById("welcomeText").innerHTML = "Something is wrong with your account. Please contact HR as soon as possible."
        }
    }
    xhttp.open("GET", url + position_name, true)
    xhttp.send()
}

function getAllForms() {
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            console.log(this.response)
            console.log(JSON.parse(this.response))
            return JSON.parse(this.response)
        }
    }
    xhttp.open("GET", "http://127.0.0.1:5000/trainings/")
    xhttp.send()
}

function generateToDoList(password, permissions) {
    forms_list = getAllForms()

}

function createUserDashboard(password) {
    permissions = getUserPermissions()
}