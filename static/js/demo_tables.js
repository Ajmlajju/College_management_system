function delete_row(id,row) {
    var box = $("#mb-remove-row");
    box.addClass("open");
    box.find(".mb-control-yes").off("click").on("click", function() {
        document.getElementById("deptid").value = id;
        $.ajax({
            type: 'GET',
            url: $('#delink').val(),
            data: {
                'id': id  
            },
            dataType: 'json',
            success: function(data) {
                if (data.errormessage) {
                    alert(data.errormessage);
                    noty({ text: data.errormessage, layout: 'topRight', timeout: 1000, type: 'error' }).show();
                }

                if (data.successmessage) {
                    alert(data.successmessage);
                    noty({ text: data.successmessage, layout: 'topRight', timeout: 1000, type: 'success' }).show();
                    setTimeout(function() {
                        window.location.href = window.location.href; // Reload the page after successful deletion
                    }, 3000);
                }
                },
            error: function(data) {
                console.log(data, "error");
                // Handle error cases here
            },
            complete: function() {
                box.removeClass("open");
                $("#" + row).hide("slow", function() {
                    $(this).remove();
                });
            }
        });
    });
}


function edit_department(id){
        document.getElementById("deptid").value=id
        document.getElementById('spinner'+id).className="fa fa-spinner";
    $.ajax({ 
        type: "GET",
        url: document.getElementById('link').value,
        data: {
            'id': id
        },
        dataType: "json",
        success: function (data) {
        // Handle the successful response
            document.getElementById('edit_name').value=data.name;
            document.getElementById('edit_code').value=data.code;
            document.getElementById('edit_status').value=data.status;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+id).className="fa fa-pencil";
        },
        error: function (error) {
        // Handle errors
        console.log(error);
        }
    });

}

function update_dept()
{    
    reqest_url =document.getElementById('contacturl').value;
    updateId=document.getElementById('deptid').value;
    updateName=document.getElementById('edit_name').value;
    updateCode=document.getElementById('edit_code').value;
    updateStatus=document.getElementById('edit_status').value
    console.log(typeof(updateStatus));
    updateObject = {
        "updateId": updateId,
        "updateName": updateName,
        "updateCode": updateCode,
        "updateStatus": updateStatus
      };
    
    $.ajax({
        type:"get",
        url: reqest_url,
        data:updateObject,
        dataType: 'json',
        success: function (data) {
            $('#modal-default').modal('hide');
            if(data.errormessage){
                alert(data.errormessage)
                noty({ text: data.errormessage, layout: 'topRight', timeout: 1000, type: 'error' }).show();
                setTimeout(function () {
                    location.reload();
                }, 3000);
                }
                if(data.successmessage){
                    alert(data.successmessage)
                    noty({ text: data.successmessage, layout: 'topRight', timeout: 1000, type: 'success' }).show();
                setTimeout(function () {
                    location.reload();
                }, 3000);
    
                }
                
            },
            error: function (data) {
                console.log(data, "error");
            },
    });
}

function edit_designation(id){
    document.getElementById("deptid").value=id
    document.getElementById('spinner'+id).className="fa fa-spinner";
$.ajax({ 
    type: "GET",
    url: document.getElementById('link').value,
    data: {
        'id': id
    },
    dataType: "json",
    success: function (data) {
    // Handle the successful response
        document.getElementById('edit_name').value=data.name;
        document.getElementById('edit_code').value=data.code;
        document.getElementById('edit_status').value=data.status;
        $('#modal_basic').modal('show');
        document.getElementById('spinner'+id).className="fa fa-pencil";
    },
    error: function (error) {
    // Handle errors
    console.log(error);
    }
});

}

function update_desig() {
    var reqest_url = document.getElementById('contacturl').value;
    var updateId = document.getElementById('deptid').value;
    var updateName = document.getElementById('edit_name').value;
    var updateCode = document.getElementById('edit_code').value;
    var updateStatus = document.getElementById('edit_status').value;

    var updateObject = {
        "updateId": updateId,
        "updateName": updateName,
        "updateCode": updateCode,
        "updateStatus": updateStatus
    };

    $.ajax({
        type: "GET",
        url: reqest_url,
        data: updateObject,
        dataType: 'json',
        success: function(data) {
            $('#modal-default').modal('hide');
            if (data.errormessage) {
                alert(data.errormessage);
                noty({ text: data.errormessage, layout: 'topRight', timeout: 1000, type: 'error' }).show();
                setTimeout(function() {
                    location.reload();
                }, 3000);
            }
            if (data.successmessage) {
                alert(data.successmessage);
                noty({ text: data.successmessage, layout: 'topRight', timeout: 1000, type: 'success' }).show();
                setTimeout(function() {
                    location.reload();
                }, 3000);
            }
        },
        error: function(data) {
            console.log(data, "error");
        },
    });
}

function edit_qual(id){
    document.getElementById("deptid").value=id
    document.getElementById('spinner'+id).className="fa fa-spinner";
$.ajax({ 
    type: "GET",
    url: document.getElementById('link').value,
    data: {
        'id': id
    },
    dataType: "json",
    success: function (data) {
    // Handle the successful response
        document.getElementById('edit_name').value=data.name;
        document.getElementById('edit_status').value=data.status;
        $('#modal_basic').modal('show');
        document.getElementById('spinner'+id).className="fa fa-pencil";
    },
    error: function (error) {
    // Handle errors
    console.log(error);
    }
});

}


function update_qual()
{    
reqest_url =document.getElementById('contacturl').value
updateId=document.getElementById('deptid').value;
updateName=document.getElementById('edit_name').value;
updateStatus=document.getElementById('edit_status').value
console.log(typeof(updateStatus));

updateObject = {
    "updateId": updateId,
    "updateName": updateName,
    "updateStatus": updateStatus
  };

$.ajax({
    type:"get",
    url: reqest_url,
    data:updateObject,
    dataType: 'json',
    success: function (data) {
        $('#modal-default').modal('hide');
        if(data.errormessage){
            alert(data.errormessage)
            noty({ text: data.errormessage, layout: 'topRight', timeout: 1000, type: 'error' }).show();
            setTimeout(function () {
                location.reload();
            }, 3000);
            }
            if(data.successmessage){
                alert(data.successmessage)
                noty({ text: data.successmessage, layout: 'topRight', timeout: 1000, type: 'success' }).show();
            setTimeout(function () {
                location.reload();
            }, 3000);

            }
            
        },
        error: function (data) {
            console.log(data, "error");
        },
});
}

function edit_emp(id){
    document.getElementById("deptid").value=id
    document.getElementById('spinner'+id).className="fa fa-spinner";
    $.ajax({ 
        type: "GET",
        url: document.getElementById('link').value,
        data: {
            'id': id
    },
        dataType: "json",
        success: function (data) {
        // Handle the successful response
            document.getElementById('edit_name').value=data.name;
            document.getElementById('edit_code').value=data.area;
            document.getElementById('edit_status').value=data.status;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+id).className="fa fa-pencil";
        },
        error: function (error) {
        // Handle errors
        console.log(error);
    }
});

}

function update_emp() {
    var reqest_url = document.getElementById('contacturl').value;
    var updateId = document.getElementById('deptid').value;
    var updateName = document.getElementById('edit_name').value;
    var updateCode = document.getElementById('edit_code').value;
    var updateStatus = document.getElementById('edit_status').value;

    var updateObject = {
        "updateId": updateId,
        "updateName": updateName,
        "updateCode": updateCode,
        "updateStatus": updateStatus
    };

    $.ajax({
        type: "GET",
        url: reqest_url,
        data: updateObject,
        dataType: 'json',
        success: function(data) {
            $('#modal-default').modal('hide');
            if (data.errormessage) {
                alert(data.errormessage);
                noty({ text: data.errormessage, layout: 'topRight', timeout: 1000, type: 'error' }).show();
                setTimeout(function() {
                    location.reload();
                }, 3000);
            }
            if (data.successmessage) {
                alert(data.successmessage);
                noty({ text: data.successmessage, layout: 'topRight', timeout: 1000, type: 'success' }).show();
                setTimeout(function() {
                    location.reload();
                }, 3000);
            }
        },
        error: function(data) {
            console.log(data, "error");
        },
    });
}

function edit_sub(id){
    document.getElementById("deptid").value=id;
    document.getElementById('spinner'+id).className="fa fa-spinner";
    $.ajax({ 
        type: "GET",
        url: document.getElementById('link').value,
        data: {
            'id': id
    },
        dataType: "json",
        success: function (data) {
        // Handle the successful response
            document.getElementById('edit_name').value=data.name;
            document.getElementById('edit_status').value=data.status;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+id).className="fa fa-pencil";
        },
        error: function (error) {
        // Handle errors
        console.log(error);
    }
});

}

function update_sub() {
    var ur = document.getElementById('contacturl').value;
    var updateId = document.getElementById('deptid').value;
    var updateName = document.getElementById('edit_name').value;
    var updateStatus = document.getElementById('edit_status').value;

    var updateObject = {
        "updateId": updateId,
        "updateName": updateName,
        "updateStatus": updateStatus
    };

    $.ajax({
        type: "GET",
        url: ur,
        data: updateObject,
        dataType: 'json',
        success: function(data) {
            $('#modal-default').modal('hide');
            if (data.errormessage) {
                alert(data.errormessage);
                noty({ text: data.errormessage, layout: 'topRight', timeout: 1000, type: 'error' }).show();
                setTimeout(function() {
                    location.reload();
                }, 3000);
            }
            if (data.successmessage) {
                alert(data.successmessage);
                noty({ text: data.successmessage, layout: 'topRight', timeout: 1000, type: 'success' }).show();
                setTimeout(function() {
                    location.reload();
                }, 3000);
            }
        },
        error: function(data) {
            console.log(data, "error");
        },
    });
}

function tonly(val) {
    var v = document.getElementById('cds');
    const arr = val.split('+');
    if (arr[1] == 1) {
        v.style.display = 'block'; // Show the element
    } else {
        v.style.display = 'none'; // Hide the element
    }
}

function subc(id)
{
    $.ajax({
        url: $('#link').val(),
        data: {
            'id':id
        },
        dataType: "json",
        success: function(data){
            console.log(data)
            var subListHTML='<select>';
            for (var i=0;i<data.subjects.length;i++){
                subListHTML += '<option value="' + data.subjects[i].id +'">' + data.subjects[i].subjectname + '</option>';
            }
            subListHTML += '</select>';
            document.getElementById("subject").innerHTML=subListHTML;
        },
        error: function(error){
            console.log(error);
           
        }
    });
}

function addToTable() {
    var v = document.getElementById('recordTable');
    v.style.display = 'block';
    var classSelect = document.getElementById('class_select');
    var divisionSelect = document.getElementById('division_select');
    var subjectSelect = document.getElementById('subject');

    var selectedClass = classSelect.options[classSelect.selectedIndex].text;
    var selectedDivision = divisionSelect.options[divisionSelect.selectedIndex].text;
    var selectedSubject = subjectSelect.options[subjectSelect.selectedIndex].text;

    // Check if the combination already exists in the table
    if (isDuplicate(selectedClass, selectedDivision, selectedSubject)) {
        alert("This combination already exists in the table.");
        return;
    }

    var table = document.getElementById('tableBody');
    var newRow = table.insertRow(table.rows.length);
    var cell1 = newRow.insertCell(0);
    var cell2 = newRow.insertCell(1);
    var cell3 = newRow.insertCell(2);
    var cell4 = newRow.insertCell(3);
    var cell5 = newRow.insertCell(4);

    var text1=document.createElement("input");
    var text2=document.createElement("input");
    var text3=document.createElement("input");
    cell1.innerHTML = tableBody.rows.length;
    cell2.innerHTML = selectedClass;
    text1.type="hidden";
    text1.name="clas";
    text1.value=classSelect.options[classSelect.selectedIndex].value;
    cell2.appendChild(text1);
    cell3.innerHTML = selectedDivision;
    text2.type="hidden";
    text2.name="divi";
    text2.value=divisionSelect.options[divisionSelect.selectedIndex].value;
    cell3.appendChild(text2);
    cell4.innerHTML = selectedSubject;
    text3.type="hidden";
    text3.name="subj";
    text3.value=subjectSelect.options[subjectSelect.selectedIndex].value;
    cell4.appendChild(text3);
    cell5.innerHTML = '<button class="btn btn-delete btn-rounded btn-sm" onclick="deleteRow(this)"><span class="fa fa-trash-o"></span></button>';
}

function isDuplicate(selectedClass, selectedDivision, selectedSubject) {
    var table = document.getElementById('tableBody');
    for (var i = 0; i < table.rows.length; i++) {
        var row = table.rows[i];
        var existingClass = row.cells[1].textContent.trim();
        var existingDivision = row.cells[2].textContent.trim();
        var existingSubject = row.cells[3].textContent.trim();

        if (selectedClass === existingClass && selectedDivision === existingDivision && selectedSubject === existingSubject) {
            return true;
        }
    }
    return false;
}




function deleteRow(button) {
    var row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}
      
function clearTable() {
    // Get a reference to the table
    var table = document.getElementById("recordTable");

    // Get the table body
    var tbody = table.getElementsByTagName("tbody")[0];

    // Remove all rows from the table body
    while (tbody.firstChild) {
        tbody.removeChild(tbody.firstChild);
    }
}

function edit_empl(id){
    document.getElementById("deptid").value=id
    document.getElementById('spinner'+id).className="fa fa-spinner";
    $.ajax({ 
        type: "GET",
        url: document.getElementById('link').value,
        data: {
            'id': id
    },
        dataType: "json",
        success: function (data) {
        // Handle the successful response
            document.getElementById('edit_name').value=data.name;
            document.getElementById('edit_code').value=data.area;
            document.getElementById('edit_status').value=data.status;
            $('#modal_basic').modal('show');
            document.getElementById('spinner'+id).className="fa fa-pencil";
        },
        error: function (error) {
        // Handle errors
        console.log(error);
    }
});

}

function update_empl() {
    var reqest_url = document.getElementById('contacturl').value;
    var updateId = document.getElementById('deptid').value;
    var updateName = document.getElementById('edit_name').value;
    var updateCode = document.getElementById('edit_code').value;
    var updateStatus = document.getElementById('edit_status').value;

    var updateObject = {
        "updateId": updateId,
        "updateName": updateName,
        "updateCode": updateCode,
        "updateStatus": updateStatus
    };

    $.ajax({
        type: "GET",
        url: reqest_url,
        data: updateObject,
        dataType: 'json',
        success: function(data) {
            $('#modal-default').modal('hide');
            if (data.errormessage) {
                alert(data.errormessage);
                noty({ text: data.errormessage, layout: 'topRight', timeout: 1000, type: 'error' }).show();
                setTimeout(function() {
                    location.reload();
                }, 3000);
            }
            if (data.successmessage) {
                alert(data.successmessage);
                noty({ text: data.successmessage, layout: 'topRight', timeout: 1000, type: 'success' }).show();
                setTimeout(function() {
                    location.reload();
                }, 3000);
            }
        },
        error: function(data) {
            console.log(data, "error");
        },
    });
}