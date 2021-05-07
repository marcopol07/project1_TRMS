function verifyUser() {
    let urlBase = "http://127.0.0.1:5000/employees/"
    let username = document.getElementById("userInput").value
    document.getElementById("userInput").value = ""
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            let user = JSON.parse(this.response)
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
            userInfo = JSON.parse(this.response)
            // console.log(userInfo)
            if(userInfo.username == username) {
                console.log("User authenticated! Redirecting...")
                getUserPermissions(username, password, userInfo)
            } else {
                console.log("Password Invalid. Try again.")
                document.getElementById("welcomeText").innerHTML = `Password invalid. Please try again:`
            }
        } else {
            document.getElementById("welcomeText").innerHTML = `Password invalid. Please try again:`
        }
    }

    xhttp.open("GET", urlBase + password, true)

    xhttp.send()
}

function getUserPermissions(username, password, userInfo) {
    document.title = `${userInfo.firstName} Dashboard`
    let urlBase = "http://127.0.0.1:5000/permissions/"
    let positionName = userInfo.positionName
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function () {
        if(this.readyState == 4){
            if(this.status == 200) {
                permissions = JSON.parse(this.response)
                getAllForms(username, password, userInfo, permissions)
            } else {
                document.getElementById("welcomeText").innerHTML = "Something is wrong with your account. Please contact HR as soon as possible."
            } 
        }
    }
    xhttp.open("GET", urlBase + positionName, true)
    xhttp.send()
}

function getAllForms(username, password, userInfo, permissions) {
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            formList = JSON.parse(this.response)
            generateToDoList(username, password, userInfo, permissions, formList)
        }
    }
    xhttp.open("GET", "http://127.0.0.1:5000/trainings", true)
    xhttp.send()
}

function generateToDoList(username, password, userInfo, permissions, formList) {
    toDoList = []
    pendingList = []
    for(index in formList) {
        let element = formList[index]
        if(permissions.benCoAccess && !element.bencoApproval && element.dhApproval) {
            toDoList.push(element)
        } else if(element.departmentHead == username && !element.dhApproval && element.dsApproval) {
            toDoList.push(element)
        } else if(element.directSupervisor == username && !element.dsApproval) {
            toDoList.push(element)
        } else if(element.queryWhom == username) {
            toDoList.push(element)
        }
        if(element.employeeUser == username ) {
            pendingList.push(element)
        }
    }
    createUserDashboard(username, password, userInfo, permissions, toDoList, pendingList)
}

function createUserDashboard(username, password, userInfo, permissions, toDoList, pendingList) {
    document.getElementById("welcome").innerHTML = `Welcome to your dashboard, ${userInfo.firstName}.`
    document.getElementById("userInput").remove()
    document.getElementById("submitButton").innerHTML = "Sign Out"
    document.getElementById("submitButton").setAttribute("onclick", "reloadPage()")
    let toDoTable = document.getElementById("toDoTable")
    let pendingTable = document.getElementById("pendingTable")
    document.getElementById("toDoHeader").innerHTML = "Forms requiring your attention:"
    generateToDoTableBody(toDoTable, toDoList, permissions)
    generateToDoTableHead(toDoTable, permissions)
    document.getElementById("pendingHeader").innerHTML = "Forms submitted:"
    generatePendingTableBody(pendingTable, pendingList)
    generatePendingTableHead(pendingTable)
    generateFormSubmission(userInfo)
}

function generateToDoTableBody(table, toDoList, permissions) {
    i = 0;
    for(let element of toDoList) {
        i = i + 1
        row = table.insertRow()
        let cell1 = row.insertCell()
        let t1 = document.createTextNode(element.employeeUser)
        cell1.appendChild(t1)
        let cell2 = row.insertCell()
        let t2 = document.createTextNode(element.tuitionType)
        cell2.appendChild(t2)
        let cell3 = row.insertCell()
        let t3 = document.createTextNode(element.trainingDate)
        cell3.appendChild(t3)
        let cell4 = row.insertCell()
        let t4 = document.createTextNode(element.directSupervisor)
        cell4.appendChild(t4)
        let cell5 = row.insertCell()
        let t5 = document.createTextNode(element.departmentHead)
        cell5.appendChild(t5)
        let cell6 = row.insertCell()
        let t6 = document.createTextNode(`$${element.reimbursementAmount}`)
        cell6.appendChild(t6)
        let cell7 = row.insertCell()
        let t7 = document.createTextNode(element.justification)
        cell7.appendChild(t7)
        let cell8 = row.insertCell()
        let s = document.createElement("select")
        let o1 = document.createElement("option")
        o1.value = "approve"
        o1.innerHTML = "Approve"
        s.appendChild(o1)
        let o2 = document.createElement("option")
        o2.value = "deny"
        o2.innerHTML = "Deny"
        s.appendChild(o2)
        s.id = "approveDeny" + i
        cell8.appendChild(s)
        let t8 = document.createElement("button")
        t8.setAttribute("onclick",`sendSelection(${element.caseId},[${permissions.benCoAccess},${permissions.departmentHeadAccess}],${i},0)`)
        t8.id = "approveDenyButton" + i
        t8.innerHTML = "Submit"
        cell8.appendChild(t8)
        if(permissions.benCoAccess) {
            cell9 = row.insertCell()
            t9 = document.createElement("input")
            t9.id = "queryBody" + i
            cell9.appendChild(t9)
            cell10 = row.insertCell()
            t10 = document.createElement("button")
            t10.id = "queryButton" + i
            t10.setAttribute("onclick", `sendQuery(${element.caseId}, ${i})`)
            t10.innerHTML = "Send"
            cell10.appendChild(t10)
        }

    }

}

function sendQuery (case_id, i) {
    document.getElementById("approveDenyButton" + i).disabled = "disabled"
    document.getElementById("queryButton" + i).disabled = "disabled"
    let url = `http://127.0.0.1:5000/trainings/query/${case_id}`
    let query = document.getElementById("queryBody" + i).value
    let requestBody = {
        "query": query
    }
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.response == 200){
            console.log("Query submitted!")
        }
    }
    xhttp.open("PUT", url, true)
    xhttp.setRequestHeader('Content-Type', 'application/json')
    xhttp.send(JSON.stringify(requestBody))
}

function generateToDoTableHead(table, permissions) {
    let thead = table.createTHead()
    let row = thead.insertRow()
    let headers = ["Employee", "Training Type", "Training Date", "Supervisor", "Department Head", 
                    "Reimbursement Amount", "Justification", "Approve"]
    if(permissions.benCoAccess) {
        headers.push("Request More Info", "Send")
    }
    
    for(item of headers) {
        let th = document.createElement("th")
        let text = document.createTextNode(item)
        th.appendChild(text)
        row.appendChild(th)
    }
}

function generatePendingTableBody(table, pendingList){
    i = 0;
    for(let element of pendingList) {
        i = i + 1
        row = table.insertRow()
        let cell1 = row.insertCell()
        let t1 = document.createTextNode(element.dateSubmitted)
        cell1.appendChild(t1)
        let cell2 = row.insertCell()
        let t2 = document.createTextNode(element.tuitionType)
        cell2.appendChild(t2)
        let cell3 = row.insertCell()
        let t3 = document.createTextNode(element.trainingDate)
        cell3.appendChild(t3)
        let cell4 = row.insertCell()
        let t4 = document.createTextNode(element.justification)
        cell4.appendChild(t4)
        let cell5 = row.insertCell()
        let t5 = document.createTextNode(`$${element.reimbursementAmount}`)
        cell5.appendChild(t5)
        let cell6 = row.insertCell()
        let t6 = document.createTextNode(element.query)
        cell6.appendChild(t6)
        cell7 = row.insertCell()
        if(element.bencoApproval){
            t7 = document.createTextNode("Approved")
        } else {
            t7 = document.createTextNode("Pending...")
        }
        cell7.appendChild(t7)
    }
}

function generatePendingTableHead(table) {
    let thead = table.createTHead()
    let row = thead.insertRow()
    let headers = ["Date Submitted", "Training Type", "Training Date", "Justification", "Projected Reimbursement Amount", "Alerts", "Status"]

    for(item of headers){
        let th = document.createElement("th")
        let text = document.createTextNode(item)
        th.appendChild(text)
        row.appendChild(th)
    }
}

function generateFormSubmission(userInfo) {
    let url = "http://127.0.0.1:5000/tuitions"
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            types = JSON.parse(this.response)
            createForm(userInfo, types)
        }
    }
    xhttp.open("GET", url, true)
    xhttp.send()
}

function createForm(userInfo, types) {
    let form = document.getElementById("form")
    let head = document.getElementById("formHeader")
    head.innerHTML = "Reimbursement Form:"
    let selectHead = document.createElement("h5")
    selectHead.innerHTML = "Select the training type:"
    let selectDiv = document.createElement("div")
    let selector = document.createElement("select")
    selector.id = "typeSelector"
    for(type of types) {
        let option = document.createElement("option")
        option.value = type.tuitionName
        option.innerHTML = type.tuitionName
        selector.appendChild(option)
    }
    selectDiv.appendChild(selectHead)
    selectDiv.appendChild(selector)
    form.appendChild(selectDiv)
    form.appendChild(document.createElement("br"))
    let dateHead = document.createElement("h5")
    dateHead.innerHTML = "Select the date of the training:"
    form.appendChild(dateHead)
    let date = document.createElement('input')
    date.type = "date"
    date.id = "date"
    form.appendChild(date)
    form.appendChild(document.createElement("br"))
    let costHead = document.createElement("h5")
    costHead.innerHTML = "Please input the cost of the training:"
    form.appendChild(costHead)
    let costInput = document.createElement("input")
    costInput.id = "costInput"
    costInput.type = "number"
    form.appendChild(costInput)
    let justifyHead = document.createElement("h5")
    justifyHead.innerHTML = "Please enter your reason for taking this training:"
    form.appendChild(justifyHead)
    let justifyInput = document.createElement("input")
    justifyInput.id = "justifyInput"
    form.appendChild(justifyInput)
    let formButton = document.createElement("button")
    formButton.id = "formButton"
    formButton.innerHTML = "Submit Form"
    formButton.setAttribute("onclick", `sendPostRequest(${userInfo.reimbursementFundsRemaining}, "${userInfo.username}", "${userInfo.department}")`)
    form.appendChild(formButton)
}

function sendPostRequest(remainingFunds, username, department) {
    let type = document.getElementById("typeSelector").value
    let date = document.getElementById("date").value
    let cost = document.getElementById("costInput").value
    let justification = document.getElementById("justifyInput").value
    if(!type || !date || !cost || !justification) {
        alert("Please fill out all the parameters!")
    } else {
        let url = "http://127.0.0.1:5000/tuitions/"
        let xhttp = new XMLHttpRequest()
        xhttp.onreadystatechange = function() {
            if(this.readyState == 4 && this.status == 200) {
                let r = JSON.parse(this.response)
                reimbursement = cost * r.reimbursementPercent
                if (reimbursement > remainingFunds) {
                    reimbursement = remainingFunds
                }
                let button = document.getElementById("formButton")
                button.disabled = "disabled"
                button.innerHTML = `Submitted! Your projected reimbursement amount is $${reimbursement}.`
                let dateNow = new Date()
                requestBody = {
                    "dateSubmitted": dateNow,
                    "trainingDate": date,
                    "employeeUser": username,
                    "justification": justification,
                    "reimbursementAmount": reimbursement,
                    "tuitionType": type,
                    "department": department
                }
                post(requestBody)
            }
        }
        xhttp.open("GET", url + type, true)
        xhttp.send()
    }
}

function post(requestBody) {
    let url = "http://127.0.0.1:5000/trainings"
    let xhttp = new XMLHttpRequest()
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.response == 201){
            console.log("Form submitted!")
        }
    }
    xhttp.open("POST", url, true)
    xhttp.setRequestHeader('Content-Type', 'application/json')
    xhttp.send(JSON.stringify(requestBody))
}

function sendSelection(caseId, permissions, i) {
    choice = document.getElementById("approveDeny" + i).value
    if(permissions[0]) {
        document.getElementById("queryButton" + i).disabled = "disabled"
    }
    document.getElementById("approveDeny" + i).remove()
    document.getElementById("approveDenyButton" + i).remove()
    if(choice == "approve") {
        sendApproval(caseId, permissions)
    }
    if(choice == "deny") {
        sendDenial(caseId)
    }
}

function sendApproval(caseId, permissions) {
    if(permissions[0]) {
        approve(caseId, "ds_approval")
        approve(caseId, "ds_approval")
        approve(caseId, "benco_approval")
    } else if(permissions[1]) {
        approve(caseId, "ds_approval")
        approve(caseId, "dh_approval")
    } else {
        approve(caseId, "ds_approval")
    }
}

function approve(caseId, permissionLevel) {
    let url = "http://127.0.0.1:5000/trainings/" + caseId + "/" + permissionLevel
    let xhttp = new XMLHttpRequest()
    
    xhttp.open("PUT", url, true)
    xhttp.setRequestHeader('Content-Type', 'application/json')
    xhttp.send()
}

function sendDenial(caseId) {
    let url = "http://127.0.0.1:5000/trainings/" + caseId
    let xhttp = new XMLHttpRequest()
    
    xhttp.open("DELETE", url, true)
    xhttp.setRequestHeader('Content-Type', 'application/json')
    xhttp.send()
}
