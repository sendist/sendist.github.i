    $(document).ready(function () {

        // FETCHING DATA FROM JSON FILE
        $.getJSON("Web Scraping 1/scraping.json",
                function (data) {
            var berita = '';
            var n = 1;

            // ITERATING THROUGH OBJECTS
            $.each(data, function (key, value) {

                //CONSTRUCTION OF ROWS HAVING
                // DATA FROM JSON OBJECT
                berita += '<tr>';
                berita += '<td>' + n + '</td>'; n++;
                berita += '<td>' + value.judul + '</td>';
                berita += '<td>' + value.kategori + '</td>';
                berita += '<td>' + value.publish + '</td>';
                berita += '<td>' + value.scraping + '</td>';
                berita += '</tr>';
            });
            
            //INSERTING ROWS INTO TABLE
            $('#table').append(berita);
        });
    });

