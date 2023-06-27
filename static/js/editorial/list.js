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
            {"data": "codigo_editorial"},
            {"data": "nombre_editorial"},
            {"data": "pagina_web"},
            {"data": "pais_origen"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = `<a href="/app/editorial/update/${row.id}/" class="btn btn-secondary btn-xs"><i class="fas fa-edit"></i></a>
                                    <a href="/app/editorial/delete/${row.id}/" class="btn btn-danger btn-xs"><i class="fas fa-trash"></i></a>`
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});