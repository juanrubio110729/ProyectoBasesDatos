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
            {"data": "usuario"},
            {"data": "libro"},
            {"data": "fecha"},
            {"data": "direccion_ip"},
        ],
        initComplete: function (settings, json) {
        }
    });
});
