    $(document).ready(function () {

        // FETCHING DATA FROM JSON FILE
        $.getJSON("Web Scraping 2/topMovie.json", function (data) {
            var list = '';

            // ITERATING THROUGH OBJECTS
            $.each(data, function (key, value) {

                //CONSTRUCTION OF ROWS HAVING
                // DATA FROM JSON OBJECT
                list += '<tr>';
                list += '<td>' + value.No + '</td>';
                list += '<td>' + `<img src=${value.Image} alt="poster">` + '</td>';
                list += '<td>' + value.Judul + '</td>';
                list += '<td>' + value.Rilis+ '</td>';
                list += '<td>' + value.Genre+ '</td>';
                list += '<td>' + value.Durasi + '</td>';
                list += '<td>' + value.Rating + '</td>';
                list += '<td>' + value.Votes + '</td>';
                list += '<td>' + value.Direktur+ '</td>';
                list += '<td>' + value.Scraping+ '</td>';
                list += '</tr>';
            });
            
            //INSERTING ROWS INTO TABLE
            $('#table2').append(list);
        });
    });