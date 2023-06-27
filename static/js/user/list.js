$(document).ready(function (){
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'searchdata'
        },
    }).done(function(data){
        console.log(data)
        let data_table = $('#tableData').DataTable({
            autoWidth: false,
            destroy: true,
            scrollX: true,
            deferRender: true,
            sAjaxDataProp: "",
            data: data,
            columns: [
                {"data": "id"},
                {"data": "full_name"},
                {"data": "username"},
                {"data": "dni"},
                {"data": "phone_user"},
                {"data": "date_joined"},
                {"data": "groups"},
                {"data": "id"},
            ],
            columnDefs:[
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var html = '';
                        $.each(row.groups, function (key, value) {
                            html += '<span class="badge badge-success">' + value.name + '</span> ';
                        });
                        return html;
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/user/update/' + row.id + '/" class="btn btn-secondary btn-xs"><i class="fas fa-edit"></i></a> ';
                        buttons += '<a href="/user/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs"><i class="fas fa-trash-alt"></i></a>';
                        return buttons;
                    }
                },
            ]
        });
    })
})
