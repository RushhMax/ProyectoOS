$(document).ready(function() {
    // Show the form when the button is clicked
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
