$(document).ready( function() {

		function hide_elements() {
			document.getElementById("matches").style.visibility = 'hidden';
			document.getElementById("match_title").style.display = 'none'; 
		}
		
		function readURL(input) {
		    if (input.files && input.files[0]) {
		        var reader = new FileReader();
		        file1 = input.files[0]

		        reader.onload = function (e) {
		            $('#main_picture').attr('src', e.target.result);
		        } 
		        reader.readAsDataURL(input.files[0]);
		    }
		}

		hide_elements()

		$("#image_input").click(function(){
			hide_elements()
		});

		$("#image_input").change(function(){
			// hide_elements()
		    readURL(this);
		});

		$("#upload").click(function () {
			//file_name = $("#vid-name").text();
			var file = document.getElementById('image_input').files[0];
			var formData = new FormData();
			formData.append("image", file);

        $.ajax({
            type: 'POST',
            url: "/processImage",
            // enctype: 'multipart/form-data',
            data: formData,
            processData: false,
            contentType: false,
            success: function (data) {
                data = JSON.parse(data)
                // alert(data)
                ctr = 0
                for (var image_path in data){
			        var celeb_name = data[image_path];
			        // alert(image_path)
			        // alert(celeb_name)
			        // alert('/static/'+image_path)
			        document.getElementById("picture_"+String(ctr)).src = '/static/'+image_path
			        document.getElementById("name_"+String(ctr)).innerHTML = celeb_name
			        ctr += 1
			    }

			    document.getElementById("match_title").style.display = 'block';
			    document.getElementById("matches").style.visibility = 'visible';

            }
        });
    });

	});



