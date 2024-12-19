$(document).ready(function() {
    
    $('#get-real-processes-btn').click(function() {
        $.ajax({
            url: '/get_real_processes',
            type: 'GET',
            success: function(response) {
                $('#processes-list').html(response);
            }
        });
    });

    $('#get-simulated-processes-btn').click(function() {
        $.ajax({
            url: '/get_simulated_processes',
            type: 'GET',
            success: function(response) {
                $('#processes-list').html(response);
            }
        });
    });

    

    
    $('#add-process-btn').click(function() {
        $('#add-process-form').toggle();
    });

    // Handle the form submission
    $('#process-form').submit(function(e) {
        e.preventDefault();
        
        // Get form data
        var formData = {
            'name': $('#name').val(),
            'arrival_time': $('#arrival_time').val(),
            'service_time': $('#service_time').val(),
            'priority': $('#priority').val()
        };

        // Send data to the server
        $.ajax({
            url: '/add_process',
            type: 'POST',
            data: formData,
            success: function(response) {
                // Update the process list dynamically
                $('#processes-list').html(response);
                $('#add-process-form').hide();  // Hide form after submission
            }
        });
    });

    $('#delete-process-btn').click(function() {
        $('#delete-process-form').toggle();
    });

    $('#delete-form').submit(function(e) {
        e.preventDefault();

        var formData = {
            'pid': $('#pid').val()
        };

        $.ajax({
            url: '/delete_process',
            type: 'POST',
            data: formData,
            success: function(response) {
                $('#processes-list').html(response);
                $('#delete-process-form').hide();
            }
        });
    });
});


// Get references to the button, popup, and close button
const deleteProcessBtn = document.getElementById("delete-process-btn");
const deletePopupForm = document.getElementById("delete-popup-form");
const deleteCloseBtn = document.getElementById("delete-close-btn");

// Show the popup when the button is clicked
deleteProcessBtn.onclick = function() {
    deletePopupForm.style.display = "flex";
};

// Close the popup when the close button is clicked
deleteCloseBtn.onclick = function() {
    deletePopupForm.style.display = "none";
};

// Close the popup if the user clicks outside the form area
window.onclick = function(event) {
    if (event.target === deletePopupForm) {
        deletePopupForm.style.display = "none";
    }
};
