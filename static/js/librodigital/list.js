$(function () {
    $('#tableData').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "position"},
            {"data": "datalibro.titulo"},
            {"data": "datalibro.isbn"},
            {"data": "formato"},
            {"data": "url"},
            {"data": "tamanio"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = `<a href="/app/librodigital/update/${row.id}/" class="btn btn-secondary btn-xs"><i class="fas fa-edit"></i></a>
                                   <a href="/app/librodigital/delete/${row.id}/" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>
                                   <button onClick="descargar(${row.id})" class="btn btn-primary btn-xs"><i class="fa-solid fa-download"></i></button>`
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});

function descargar(id){
    console.log(id)
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'download',
            'parameters': id
        },
    }).done(function() {
        Swal.fire({
            icon: 'success',
            title: 'Se descargo el libro',
            showConfirmButton: false,
            timer: 1000
        });              
    }).fail(function (textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
    });
}